from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_add_group_post200_response import CollectionsAddGroupPost200Response
from outline_openapi.models.collections_add_group_post_request import CollectionsAddGroupPostRequest
from outline_openapi.models.collections_add_user_post200_response import CollectionsAddUserPost200Response
from outline_openapi.models.collections_add_user_post_request import CollectionsAddUserPostRequest
from outline_openapi.models.collections_create_post200_response import CollectionsCreatePost200Response
from outline_openapi.models.collections_create_post_request import CollectionsCreatePostRequest
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.collections_documents_post200_response import CollectionsDocumentsPost200Response
from outline_openapi.models.collections_export_all_post_request import CollectionsExportAllPostRequest
from outline_openapi.models.collections_export_post200_response import CollectionsExportPost200Response
from outline_openapi.models.collections_export_post_request import CollectionsExportPostRequest
from outline_openapi.models.collections_group_memberships_post200_response import CollectionsGroupMembershipsPost200Response
from outline_openapi.models.collections_group_memberships_post_request import CollectionsGroupMembershipsPostRequest
from outline_openapi.models.collections_info_post200_response import CollectionsInfoPost200Response
from outline_openapi.models.collections_info_post_request import CollectionsInfoPostRequest
from outline_openapi.models.collections_list_post200_response import CollectionsListPost200Response
from outline_openapi.models.collections_memberships_post200_response import CollectionsMembershipsPost200Response
from outline_openapi.models.collections_memberships_post_request import CollectionsMembershipsPostRequest
from outline_openapi.models.collections_remove_group_post_request import CollectionsRemoveGroupPostRequest
from outline_openapi.models.collections_remove_user_post_request import CollectionsRemoveUserPostRequest
from outline_openapi.models.collections_update_post_request import CollectionsUpdatePostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.pagination import Pagination
from outline_openapi import util


async def collections_add_group_post(request: web.Request, body=None) -> web.Response:
    """Add a group to a collection

    This method allows you to give all members in a group access to a collection.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsAddGroupPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_add_user_post(request: web.Request, body=None) -> web.Response:
    """Add a collection user

    This method allows you to add a user membership to the specified collection.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsAddUserPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_create_post(request: web.Request, body=None) -> web.Response:
    """Create a collection

    

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsCreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_delete_post(request: web.Request, body=None) -> web.Response:
    """Delete a collection

    Delete a collection and all of its documents. This action can’t be undone so please be careful.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsDeletePostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_documents_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a collections document structure

    

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_export_all_post(request: web.Request, body=None) -> web.Response:
    """Export all collections

    Triggers a bulk export of all documents in and their attachments. The endpoint returns a &#x60;FileOperation&#x60; that can be queried through the fileOperations endpoint to track the progress of the export and get the url for the final file.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsExportAllPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_export_post(request: web.Request, body=None) -> web.Response:
    """Export a collection

    Triggers a bulk export of the collection in markdown format and their attachments. If documents are nested then they will be nested in folders inside the zip file. The endpoint returns a &#x60;FileOperation&#x60; that can be queried to track the progress of the export and get the url for the final file.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsExportPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_group_memberships_post(request: web.Request, body=None) -> web.Response:
    """List all collection group members

    This method allows you to list a collections group memberships. This is the list of groups that have been given access to the collection.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsGroupMembershipsPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_info_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a collection

    

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_list_post(request: web.Request, body=None) -> web.Response:
    """List all collections

    

    :param body: 
    :type body: dict | bytes

    """
    body = Pagination.from_dict(body)
    return web.Response(status=200)


async def collections_memberships_post(request: web.Request, body=None) -> web.Response:
    """List all collection memberships

    This method allows you to list a collections individual memberships. It&#39;s important to note that memberships returned from this endpoint do not include group memberships.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsMembershipsPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_remove_group_post(request: web.Request, body=None) -> web.Response:
    """Remove a collection group

    This method allows you to revoke all members in a group access to a collection. Note that members of the group may still retain access through other groups or individual memberships.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsRemoveGroupPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_remove_user_post(request: web.Request, body=None) -> web.Response:
    """Remove a collection user

    This method allows you to remove a user from the specified collection.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsRemoveUserPostRequest.from_dict(body)
    return web.Response(status=200)


async def collections_update_post(request: web.Request, body=None) -> web.Response:
    """Update a collection

    

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsUpdatePostRequest.from_dict(body)
    return web.Response(status=200)
