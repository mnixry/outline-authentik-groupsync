from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.shares_create_post_request import SharesCreatePostRequest
from outline_openapi.models.shares_info_post200_response import SharesInfoPost200Response
from outline_openapi.models.shares_info_post_request import SharesInfoPostRequest
from outline_openapi.models.shares_list_post200_response import SharesListPost200Response
from outline_openapi.models.shares_update_post_request import SharesUpdatePostRequest
from outline_openapi import util


async def shares_create_post(request: web.Request, body=None) -> web.Response:
    """Create a share

    Creates a new share link that can be used by to access a document. If you request multiple shares for the same document with the same API key, the same share object will be returned. By default all shares are unpublished.

    :param body: 
    :type body: dict | bytes

    """
    body = SharesCreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def shares_info_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a share object

    

    :param body: 
    :type body: dict | bytes

    """
    body = SharesInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def shares_list_post(request: web.Request, body=None) -> web.Response:
    """List all shares

    

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsViewedPostRequest.from_dict(body)
    return web.Response(status=200)


async def shares_revoke_post(request: web.Request, body=None) -> web.Response:
    """Revoke a share

    Makes the share link inactive so that it can no longer be used to access the document.

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsDeletePostRequest.from_dict(body)
    return web.Response(status=200)


async def shares_update_post(request: web.Request, body=None) -> web.Response:
    """Update a share

    Allows changing an existing shares published status, which removes authentication and makes it available to anyone with the link.

    :param body: 
    :type body: dict | bytes

    """
    body = SharesUpdatePostRequest.from_dict(body)
    return web.Response(status=200)
