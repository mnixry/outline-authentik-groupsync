from typing import List, Dict
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.comments_create_post200_response import CommentsCreatePost200Response
from outline_openapi.models.comments_create_post_request import CommentsCreatePostRequest
from outline_openapi.models.comments_list_post200_response import CommentsListPost200Response
from outline_openapi.models.comments_list_post_request import CommentsListPostRequest
from outline_openapi.models.comments_update_post_request import CommentsUpdatePostRequest
from outline_openapi.models.error import Error
from outline_openapi import util


async def comments_create_post(request: web.Request, body=None) -> web.Response:
    """Create a comment

    Create a comment

    :param body: 
    :type body: dict | bytes

    """
    body = CommentsCreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def comments_delete_post(request: web.Request, body=None) -> web.Response:
    """Delete a comment

    Delete a comment

    :param body: 
    :type body: dict | bytes

    """
    body = CollectionsDeletePostRequest.from_dict(body)
    return web.Response(status=200)


async def comments_list_post(request: web.Request, body=None) -> web.Response:
    """List all comments

    This method will list all comments matching the given properties.

    :param body: 
    :type body: dict | bytes

    """
    body = CommentsListPostRequest.from_dict(body)
    return web.Response(status=200)


async def comments_update_post(request: web.Request, body=None) -> web.Response:
    """Update a comment

    Update a comment

    :param body: 
    :type body: dict | bytes

    """
    body = CommentsUpdatePostRequest.from_dict(body)
    return web.Response(status=200)
