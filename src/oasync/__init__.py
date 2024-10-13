import datetime
import hashlib
import hmac
import re
import time
import uuid
from typing import Generic, Literal, TypeVar

from fastapi import Depends, FastAPI, Request
from fastapi.exceptions import HTTPException
from pydantic import AliasPath, BaseModel, ConfigDict, Field, HttpUrl, alias_generators
from pydantic_settings import BaseSettings, SettingsConfigDict
from starlette.status import HTTP_400_BAD_REQUEST

app = FastAPI()


class Settings(BaseSettings):
    model_config = SettingsConfigDict(env_prefix="OASYNC_")

    timedelta_seconds: int = 60

    outline_secret: bytes
    outline_host: HttpUrl
    ak_host: HttpUrl


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
        settings.outline_secret,
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


class OutlinePayloadBase(BaseModel):
    pass


class UserSignInPayload(OutlinePayloadBase):
    id: uuid.UUID
    name: str
    avatar_url: str | None
    color: str
    role: str
    is_suspended: bool
    created_at: datetime.datetime
    updated_at: datetime.datetime
    last_active_at: datetime.datetime


_PT = TypeVar("_PT", bound=OutlinePayloadBase)


# TODO: use PEP-695 format generic
# see: https://github.com/pydantic/pydantic/issues/9782
class OutlineEventBase(BaseModel, Generic[_PT]):
    model_config = ConfigDict(alias_generator=alias_generators.to_snake)
    id: uuid.UUID
    actor_id: uuid.UUID
    webhook_subscription_id: uuid.UUID
    created_at: datetime.datetime
    payload_id: uuid.UUID = Field(validation_alias=AliasPath("payload", "id"))
    payload: _PT = Field(validation_alias=AliasPath("payload", "model"))


class OutlineSignInEvent(OutlineEventBase[UserSignInPayload]):
    event: Literal["users.signin"]


@app.post("/webhook", dependencies=[Depends(check_webhook_signature)])
async def webhook(event: OutlineSignInEvent):
    pass
