import datetime
import uuid
from typing import Generic, Literal, TypeVar

from pydantic import (
    AliasPath,
    BaseModel,
    ConfigDict,
    Field,
    alias_generators,
)


class OutlineBaseModel(BaseModel):
    model_config = ConfigDict(alias_generator=alias_generators.to_camel)


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
