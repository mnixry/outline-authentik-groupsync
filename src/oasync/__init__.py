import datetime
from enum import StrEnum
import hashlib
import hmac
import re
import time
from urllib.parse import urljoin
import uuid
from typing import Annotated, Any, Generic, Literal, TypeVar

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import HTTPException
from httpx import AsyncClient
from pydantic import AliasPath, BaseModel, ConfigDict, Field, HttpUrl, alias_generators

from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.status import HTTP_400_BAD_REQUEST

app = FastAPI()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="OASYNC_")

    timedelta_seconds: int = 60

    outline_host: HttpUrl
    outline_api_key: str
    outline_webhook_secret: bytes

    ak_host: HttpUrl
    ak_api_key: str
    ak_group_attribute: str = "app.getoutline.com/group_id"


settings = Settings()  # type: ignore


async def check_webhook_signature(request: Request):
    signature = request.headers.get("outline-signature")
    if not signature:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Missing signature"
        )
    matched = re.match(r"^t=([0-9]+),s=([0-9a-f]+)$", signature)
    if not matched:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Invalid signature format"
        )
    timestamp, signature = matched.groups()
    if abs(time.time() * 1000 - int(timestamp)) > settings.timedelta_seconds:
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Expired signature"
        )
    request_body_digest = hmac.new(
        settings.outline_webhook_secret,
        f"{timestamp}.".encode() + await request.body(),
        hashlib.sha256,
    ).hexdigest()
    if not hmac.compare_digest(
        request_body_digest.casefold(),
        signature.casefold(),
    ):
        raise HTTPException(
            status_code=HTTP_400_BAD_REQUEST, detail="Invalid signature digest"
        )
    return


class OutlineBaseModel(BaseModel):
    model_config = ConfigDict(alias_generator=alias_generators.to_snake)


class UserSignInPayload(OutlineBaseModel):
    id: uuid.UUID
    name: str
    avatar_url: str | None
    color: str
    role: str
    is_suspended: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_active_at: datetime.datetime


_OPT = TypeVar("_OPT", bound=OutlineBaseModel)


# TODO: use PEP-695 format generic
# see: https://github.com/pydantic/pydantic/issues/9782
class OutlineEventBase(OutlineBaseModel, Generic[_OPT]):
    id: uuid.UUID
    actor_id: uuid.UUID
    webhook_subscription_id: uuid.UUID
    created_at: datetime.datetime
    payload_id: uuid.UUID = Field(validation_alias=AliasPath("payload", "id"))
    payload: _OPT = Field(validation_alias=AliasPath("payload", "model"))


class OutlineSignInEvent(OutlineEventBase[UserSignInPayload]):
    event: Literal["users.signin"]


async def httpx_async_client():
    async with AsyncClient() as client:
        yield client


AsyncClientDepends = Annotated[
    AsyncClient,
    Depends(httpx_async_client),
]

"""
{
  "data": {
    "id": "123e4567-e89b-12d3-a456-426614174000",
    "name": "Jane Doe",
    "avatarUrl": "https://example.com",
    "email": "hello@example.com",
    "role": "admin",
    "isSuspended": true,
    "lastActiveAt": "2024-10-13T14:33:09.462Z",
    "createdAt": "2024-10-13T14:33:09.462Z"
  }
}
"""


class OutlineUserInfo(OutlineBaseModel):
    id: uuid.UUID
    name: str
    avatar_url: str | None
    email: str
    role: str
    is_suspended: bool
    last_active_at: datetime.datetime
    created_at: datetime.datetime


async def outline_user_info(user_id: uuid.UUID, client: AsyncClientDepends):
    response = await client.post(
        urljoin(str(settings.outline_host), "api/users.info"),
        headers={
            # TODO: replace this with httpx.Auth based implementation
            "Authorization": f"Bearer {settings.outline_api_key}",
        },
        json={"id": str(user_id)},
    )
    data: dict[str, Any] = response.json()
    if not data.get("ok", True):
        raise RuntimeError("Failed to fetch user info", data.get("message", data))
    return OutlineUserInfo.model_validate(data["data"])


"""
{
  "data": {
    "groups": [
      {
        "id": "123e4567-e89b-12d3-a456-426614174000",
        "name": "Engineering",
        "memberCount": 11,
        "createdAt": "2024-10-13T14:33:09.462Z",
        "updatedAt": "2024-10-13T14:33:09.462Z"
      }
    ],
    "groupMemberships": [
      {
        "id": "…",
        "groupId": "123e4567-e89b-12d3-a456-426614174000",
        "userId": "123e4567-e89b-12d3-a456-426614174000",
        "user": {
          "id": "123e4567-e89b-12d3-a456-426614174000",
          "name": "Jane Doe",
          "avatarUrl": "https://example.com",
          "email": "hello@example.com",
          "role": "admin",
          "isSuspended": true,
          "lastActiveAt": "2024-10-13T14:33:09.462Z",
          "createdAt": "2024-10-13T14:33:09.462Z"
        }
      }
    ]
  },
  "pagination": {
    "offset": 1,
    "limit": 25
  }
}
"""


class OutlinePaginatedInfo(OutlineBaseModel):
    offset: int
    limit: int


class OutlineGroupInfo(OutlineBaseModel):
    id: uuid.UUID
    name: str
    member_count: int
    created_at: datetime.datetime
    updated_at: datetime.datetime


class OutlineGroupMembershipInfo(OutlineBaseModel):
    id: uuid.UUID
    group_id: uuid.UUID
    user_id: uuid.UUID
    user: OutlineUserInfo


class OutlineListGroupsData(OutlineBaseModel):
    groups: list[OutlineGroupInfo]
    group_memberships: list[OutlineGroupMembershipInfo]


class OutlinePaginatedResponse(OutlineBaseModel, Generic[_OPT]):
    data: _OPT
    pagination: OutlinePaginatedInfo


class OutlinePaginationSort(StrEnum):
    ASC = "ASC"
    DESC = "DESC"


async def outline_all_groups(
    client: AsyncClientDepends,
    offset: int = 0,
    limit: int = 25,
    sort: str | None = None,
    direction: OutlinePaginationSort | None = None,
):
    request_body: dict[str, Any] = {"offset": offset, "limit": limit}
    if sort is not None:
        request_body["sort"] = sort
    if direction is not None:
        request_body["direction"] = direction
    response = await client.post(
        urljoin(str(settings.outline_host), "api/groups.list"),
        headers={
            "Authorization": f"Bearer {settings.outline_api_key}",
        },
        json=request_body,
    )
    data: dict[str, Any] = response.json()
    if not data.get("ok", True):
        raise RuntimeError("Failed to fetch group info", data.get("message", data))
    return OutlinePaginatedResponse[OutlineListGroupsData].model_validate(data)


"""
{
  "pagination": {
    "next": 0,
    "previous": 0,
    "count": 1,
    "current": 1,
    "total_pages": 1,
    "start_index": 1,
    "end_index": 1
  },
  "results": [
    {
      "pk": 6,
      "username": "akadmin",
      "name": "authentik Default Admin",
      "is_active": false,
      "last_login": "2024-09-30T16:48:57.792647Z",
      "is_superuser": true,
      "groups": [
        "423b66ef-18c0-4e8c-9464-73b0fa1bfa56"
      ],
      "groups_obj": [
        {
          "pk": "423b66ef-18c0-4e8c-9464-73b0fa1bfa56",
          "num_pk": 88037,
          "name": "authentik Admins",
          "is_superuser": true,
          "parent": null,
          "parent_name": null,
          "attributes": {}
        }
      ],
      "email": "admin@buptmerak.cn",
      "avatar": "data:image/svg+xml;base64,PHN2ZyB4bWxucz0iaHR0cDovL3d3dy53My5vcmcvMjAwMC9zdmciIHdpZHRoPSI2NHB4IiBoZWlnaHQ9IjY0cHgiIHZpZXdCb3g9IjAgMCA2NCA2NCIgdmVyc2lvbj0iMS4xIj48cmVjdCBmaWxsPSIjMzc3YjM3IiBjeD0iMzIiIGN5PSIzMiIgd2lkdGg9IjY0IiBoZWlnaHQ9IjY0IiByPSIzMiIvPjx0ZXh0IHg9IjUwJSIgeT0iNTAlIiBzdHlsZT0iY29sb3I6ICNmZmY7IGxpbmUtaGVpZ2h0OiAxOyBmb250LWZhbWlseTogJ1JlZEhhdFRleHQnLCdPdmVycGFzcycsb3ZlcnBhc3MsaGVsdmV0aWNhLGFyaWFsLHNhbnMtc2VyaWY7ICIgZmlsbD0iI2ZmZiIgYWxpZ25tZW50LWJhc2VsaW5lPSJtaWRkbGUiIGRvbWluYW50LWJhc2VsaW5lPSJtaWRkbGUiIHRleHQtYW5jaG9yPSJtaWRkbGUiIGZvbnQtc2l6ZT0iMjgiIGZvbnQtd2VpZ2h0PSI0MDAiIGR5PSIuMWVtIj5BQTwvdGV4dD48L3N2Zz4=",
      "attributes": {
        "last_email_sent": 1727616838
      },
      "uid": "49cc2fed21db230ba6f7bfd4b9094ee3900a3a89469538bf869a14f75b73426b",
      "path": "users",
      "type": "internal",
      "uuid": "c4869ca8-9647-4473-8da9-6767ce864798"
    }
  ]
}
"""


class AkUserInfoGroupObj(OutlineBaseModel):
    pk: uuid.UUID
    num_pk: int
    name: str
    is_superuser: bool
    parent: uuid.UUID | None
    parent_name: str | None
    attributes: dict[str, Any]


class AkUserType(StrEnum):
    external = "external"
    internal = "internal"
    internal_service_account = "internal_service_account"
    service_account = "service_account"


class AKUserInfo(BaseModel):
    pk: int
    username: str
    name: str
    is_active: bool
    last_login: datetime.datetime
    is_superuser: bool
    groups: list[uuid.UUID]
    groups_obj: list[AkUserInfoGroupObj]
    email: str
    avatar: str
    attributes: dict[str, Any]
    uid: str
    path: str
    type: AkUserType
    uuid: uuid.UUID


_AT = TypeVar("_AT", bound=BaseModel)


class AkPaginatedInfo(BaseModel):
    next: int
    previous: int
    count: int
    current: int
    total_pages: int
    start_index: int
    end_index: int


class AkPaginatedResponse(BaseModel, Generic[_AT]):
    pagination: AkPaginatedInfo
    results: list[_AT]


async def ak_query_user(email: str, client: AsyncClientDepends):
    response = await client.get(
        urljoin(str(settings.ak_host), "core/users/"),
        params={"email": email},
        headers={
            "Authorization": f"Bearer {settings.ak_api_key}",
        },
    )
    data: dict[str, Any] = response.json()
    if error_code := data.get("code"):
        raise RuntimeError("Failed to query user", error_code, data)
    return AkPaginatedResponse[AKUserInfo].model_validate(data)


@app.post("/webhook", dependencies=[Depends(check_webhook_signature)])
async def webhook(event: OutlineSignInEvent, client: AsyncClientDepends):
    pass
