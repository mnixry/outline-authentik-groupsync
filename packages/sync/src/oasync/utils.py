from functools import lru_cache
from typing import Annotated
from urllib.parse import urljoin

import authentik_openapi
import outline_openapi
from fastapi import Depends
from pydantic import HttpUrl
from pydantic_settings import BaseSettings, SettingsConfigDict


class Settings(BaseSettings):
    model_config = SettingsConfigDict(
        env_prefix="OASYNC_", env_file=".env", env_file_encoding="utf-8"
    )

    timedelta_seconds: int = 60
    skip_signature_check: bool = False

    outline_host: HttpUrl
    outline_api_key: str
    outline_webhook_secret: bytes
    outline_default_role: outline_openapi.UserRole = outline_openapi.UserRole.MEMBER
    outline_pagination_limit: int = 100

    ak_host: HttpUrl
    ak_api_key: str
    ak_group_attribute: str | None = "app.getoutline.com/group_id"
    ak_admin_group: str | None = None


@lru_cache
def settings_dependency():
    return Settings()  # type: ignore


SettingsDepend = Annotated[
    Settings,
    Depends(settings_dependency),
]


async def outline_client_dependency(settings: SettingsDepend):
    configuration = outline_openapi.Configuration(
        host=urljoin(str(settings.outline_host), "api"),
        access_token=settings.outline_api_key,
    )
    async with outline_openapi.ApiClient(
        configuration=configuration,
    ) as client:
        yield client


OutlineClientDepend = Annotated[
    outline_openapi.ApiClient,
    Depends(outline_client_dependency),
]


async def ak_client_dependency(settings: SettingsDepend):
    configuration = authentik_openapi.Configuration(
        host=urljoin(str(settings.ak_host), "api/v3"),
        access_token=settings.ak_api_key,
    )
    async with authentik_openapi.ApiClient(
        configuration=configuration,
    ) as client:
        yield client


AkClientDepend = Annotated[
    authentik_openapi.ApiClient,
    Depends(ak_client_dependency),
]
