from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.error import Error
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest
from outline_openapi.models.users_invite_post200_response import UsersInvitePost200Response
from outline_openapi.models.users_invite_post_request import UsersInvitePostRequest
from outline_openapi.models.users_list_post200_response import UsersListPost200Response
from outline_openapi.models.users_list_post_request import UsersListPostRequest
from outline_openapi.models.users_update_post_request import UsersUpdatePostRequest
from outline_openapi.models.users_update_role_post_request import UsersUpdateRolePostRequest
from outline_openapi import util


async def users_activate_post(request: web.Request, body=None) -> web.Response:
    """Activate a user

    Activating a previously suspended user allows them to signin again. Users that are activated will cause billing totals to be re-calculated in the hosted version.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def users_delete_post(request: web.Request, body=None) -> web.Response:
    """Delete a user

    Deleting a user removes the object entirely. In almost every circumstance it is preferable to suspend a user, as a deleted user can be recreated by signing in with SSO again.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def users_info_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a user

    

    :param body: 
    :type body: dict | bytes

    """
    body = UsersInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def users_invite_post(request: web.Request, body=None) -> web.Response:
    """Invite users

    

    :param body: 
    :type body: dict | bytes

    """
    body = UsersInvitePostRequest.from_dict(body)
    return web.Response(status=200)


async def users_list_post(request: web.Request, body=None) -> web.Response:
    """List all users

    List and filter all the users in the team

    :param body: 
    :type body: dict | bytes

    """
    body = UsersListPostRequest.from_dict(body)
    return web.Response(status=200)


async def users_suspend_post(request: web.Request, body=None) -> web.Response:
    """Suspend a user

    Suspending a user prevents the user from signing in. Users that are suspended are also not counted against billing totals in the hosted version.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def users_update_post(request: web.Request, body=None) -> web.Response:
    """Update a user

    Update a users name or avatar. If no &#x60;id&#x60; is passed then the user associated with the authentication will be updated by default.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersUpdatePostRequest.from_dict(body)
    return web.Response(status=200)


async def users_update_role_post(request: web.Request, body=None) -> web.Response:
    """Change a users role

    Change the role of a user, only available to admin authorization.

    :param body: 
    :type body: dict | bytes

    """
    body = UsersUpdateRolePostRequest.from_dict(body)
    return web.Response(status=200)
