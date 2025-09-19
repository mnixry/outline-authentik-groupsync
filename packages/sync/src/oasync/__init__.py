import asyncio
import hashlib
import hmac
import logging
import re
import time
from contextlib import asynccontextmanager
from itertools import count

import authentik_openapi
import outline_openapi
from fastapi import Depends, FastAPI, Request
from fastapi.exception_handlers import (
    http_exception_handler as fastapi_http_exception_handler,
)
from fastapi.exception_handlers import (
    request_validation_exception_handler as fastapi_request_validation_exception_handler,  # noqa
)
from fastapi.exceptions import HTTPException, RequestValidationError
from starlette.status import HTTP_400_BAD_REQUEST

from .models import OutlineSignInEvent
from .utils import (
    AkClientDepend,
    OutlineClientDepend,
    SettingsDepend,
    settings_dependency,
)

logger = logging.getLogger(__name__)


@asynccontextmanager
async def lifespan(app: FastAPI):
    settings_dependency()
    logger.debug("Outline sync service started")
    yield


app = FastAPI(lifespan=lifespan)


@app.exception_handler(HTTPException)
async def http_exception_handler(request, exc):
    logger.warning("captured http exception raised: %s", exc)
    return await fastapi_http_exception_handler(request, exc)


@app.exception_handler(RequestValidationError)
async def request_validation_exception_handler(request, exc):
    logger.warning("captured validation exception raised: %s", exc)
    return await fastapi_request_validation_exception_handler(request, exc)


async def check_webhook_signature(request: Request, settings: SettingsDepend):
    if settings.skip_signature_check:
        logger.warning("Signature check will be skipped")
        return
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
    if abs(time.time() * 1000 - int(timestamp)) > settings.timedelta_seconds * 1000:
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


@app.get("/ping")
async def ping():
    return "pong"


@app.post("/webhook", dependencies=[Depends(check_webhook_signature)])
async def webhook(  # noqa: C901
    event: OutlineSignInEvent,
    settings: SettingsDepend,
    outline_client: OutlineClientDepend,
    ak_client: AkClientDepend,
):
    logger.info("Received event: %s, start processing", event)

    users_api = outline_openapi.UsersApi(outline_client)
    user_info = await users_api.users_info(
        outline_openapi.UsersInfoRequest(id=str(event.payload.id))
    )
    assert user_info.data

    ak_core_api = authentik_openapi.CoreApi(ak_client)
    user_search_result = await ak_core_api.core_users_list(email=user_info.data.email)
    match user_search_result.results:
        case [ak_user_info]:
            pass
        case _:
            raise HTTPException(
                status_code=HTTP_400_BAD_REQUEST, detail="User not found or ambiguous"
            )

    # step1. update user role if mismatch
    should_be_admin = next(
        (
            group
            for group in (ak_user_info.groups_obj or [])
            if group.name == settings.ak_admin_group
        ),
        None,
    )
    if (
        settings.ak_admin_group is not None
        and (
            # User is not an admin in Outline but assigned to admin group in Authentik
            should_be_admin
            and user_info.data.role is not outline_openapi.UserRole.ADMIN
        )
    ) or (
        # User is an admin in Outline but not assigned to admin group in Authentik
        user_info.data.role is outline_openapi.UserRole.ADMIN and not should_be_admin
    ):
        updated_role = (
            outline_openapi.UserRole.ADMIN
            if should_be_admin
            else settings.outline_default_role
        )
        result = await users_api.users_update_role(
            outline_openapi.UsersUpdateRoleRequest(
                id=str(user_info.data.id), role=updated_role
            )
        )
        assert result.data
        assert result.data.role is updated_role

    # step2.1. fetch all groups from Outline
    groups_api = outline_openapi.GroupsApi(outline_client)
    all_outline_groups: list[outline_openapi.Group] = []
    for offset in count(0, settings.outline_pagination_limit):
        result = await groups_api.groups_list(
            outline_openapi.GroupsListRequest(
                limit=settings.outline_pagination_limit, offset=offset
            )
        )
        assert result.data is not None
        if not result.data.groups:
            break
        all_outline_groups.extend(result.data.groups)

    # step2.2. check groups existed in Authentik for current user but not in Outline
    group_mapping: dict[str, str] = {}  # {outline_group_id: authentik_group_id}
    not_exist_groups: list[authentik_openapi.UserGroup] = []
    need_attribute_groups: list[authentik_openapi.UserGroup] = []
    for group in ak_user_info.groups_obj or []:
        if (settings.ak_group_attribute and group.attributes) and (
            group_id := group.attributes.get(settings.ak_group_attribute)
        ):
            group_mapping[group_id] = group.pk
        elif same_name_group := next(
            (
                outline_group
                for outline_group in all_outline_groups
                if outline_group.name == group.name
            ),
            None,
        ):
            assert same_name_group.id
            group_mapping[same_name_group.id] = group.pk
            need_attribute_groups.append(group)
        else:
            not_exist_groups.append(group)

    # step2.3. create groups in Outline if not exist
    if not_exist_groups:
        created_groups = await asyncio.gather(
            *(
                groups_api.groups_create(
                    outline_openapi.GroupsCreateRequest(name=group.name)
                )
                for group in not_exist_groups
            )
        )
        assert all(result.data for result in created_groups)
        for group, result in zip(not_exist_groups, created_groups, strict=True):
            assert result.data
            assert result.data.id
            group_mapping[result.data.id] = group.pk
            need_attribute_groups.append(group)

    # step2.4. update group attributes in Authentik if needed
    if settings.ak_group_attribute and need_attribute_groups:
        async with asyncio.TaskGroup() as tg:
            for group in need_attribute_groups:
                outline_group_id = next(
                    k for k, v in group_mapping.items() if v == group.pk
                )

                coro = ak_core_api.core_groups_partial_update(
                    group.pk,
                    authentik_openapi.PatchedGroupRequest(
                        attributes={
                            **(group.attributes or {}),
                            settings.ak_group_attribute: outline_group_id,
                        }
                    ),
                )
                tg.create_task(coro)

    # step3. update user group membership in Outline
    assert user_info.data.id
    async with asyncio.TaskGroup() as tg:
        for outline_group in all_outline_groups:
            assert outline_group.id
            if outline_group.id in group_mapping:
                # user in group that should be in, add user to group
                coro = groups_api.groups_add_user(
                    outline_openapi.GroupsAddUserRequest(
                        id=outline_group.id, userId=user_info.data.id
                    )
                )
            else:
                # user in group that should not be in, remove user from group
                coro = groups_api.groups_remove_user(
                    outline_openapi.CollectionsRemoveUserRequest(
                        id=outline_group.id, userId=user_info.data.id
                    )
                )
            tg.create_task(coro)
    pass
