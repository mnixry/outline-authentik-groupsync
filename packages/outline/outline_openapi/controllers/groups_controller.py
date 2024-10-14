from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.collections_remove_user_post_request import CollectionsRemoveUserPostRequest
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.groups_add_user_post200_response import GroupsAddUserPost200Response
from outline_openapi.models.groups_add_user_post_request import GroupsAddUserPostRequest
from outline_openapi.models.groups_create_post200_response import GroupsCreatePost200Response
from outline_openapi.models.groups_create_post_request import GroupsCreatePostRequest
from outline_openapi.models.groups_info_post200_response import GroupsInfoPost200Response
from outline_openapi.models.groups_info_post_request import GroupsInfoPostRequest
from outline_openapi.models.groups_list_post200_response import GroupsListPost200Response
from outline_openapi.models.groups_memberships_post200_response import GroupsMembershipsPost200Response
from outline_openapi.models.groups_memberships_post_request import GroupsMembershipsPostRequest
from outline_openapi.models.groups_remove_user_post200_response import GroupsRemoveUserPost200Response
from outline_openapi.models.groups_update_post_request import GroupsUpdatePostRequest
from outline_openapi import util


async def groups_add_user_post(request: web.Request, body=None) -> web.Response:
    """Add a group member

    This method allows you to add a user to the specified group.

    :param body: 
    :type body: dict | bytes

    """
    body = GroupsAddUserPostRequest.from_dict(body)
    return web.Response(status=200)


async def groups_create_post(request: web.Request, body=None) -> web.Response:
    """Create a group

    

    :param body: 
    :type body: dict | bytes

    """
    body = GroupsCreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def groups_delete_post(request: web.Request, body=None) -> web.Response:
    """Delete a group

    Deleting a group will cause all of its members to lose access to any collections the group has previously been added to. This action can’t be undone so please be careful.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsDeletePostRequest.from_dict(body)
    return web.Response(status=200)


async def groups_info_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a group

    

    :param body: 
    :type body: dict | bytes

    """
    body = GroupsInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def groups_list_post(request: web.Request, body=None) -> web.Response:
    """List all groups

    

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsViewedPostRequest.from_dict(body)
    return web.Response(status=200)


async def groups_memberships_post(request: web.Request, body=None) -> web.Response:
    """List all group members

    List and filter all the members in a group.

    :param body: 
    :type body: dict | bytes

    """
    body = GroupsMembershipsPostRequest.from_dict(body)
    return web.Response(status=200)


async def groups_remove_user_post(request: web.Request, body=None) -> web.Response:
    """Remove a group member

    This method allows you to remove a user from the group.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsRemoveUserPostRequest.from_dict(body)
    return web.Response(status=200)


async def groups_update_post(request: web.Request, body=None) -> web.Response:
    """Update a group

    

    :param body: 
    :type body: dict | bytes

    """
    body = GroupsUpdatePostRequest.from_dict(body)
    return web.Response(status=200)
