import datetime
import hashlib
import hmac
import re
import time
import uuid
from typing import Generic, Literal, TypeVar

import authentik_openapi
import outline_openapi
from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import HTTPException
import outline_openapi.api
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


async def outline_client_dependency():
    configuration = outline_openapi.Configuration(
        host=settings.outline_host,
        access_token=settings.outline_api_key,
    )
    async with outline_openapi.ApiClient(
        configuration=configuration,
    ) as client:
        yield client


async def ak_client_dependency():
    configuration = authentik_openapi.Configuration(
        host=settings.ak_host,
        access_token=settings.ak_api_key,
    )
    async with authentik_openapi.ApiClient(
        configuration=configuration,
    ) as client:
        yield client


@app.post("/webhook", dependencies=[Depends(check_webhook_signature)])
async def webhook(event: OutlineSignInEvent):
    pass
