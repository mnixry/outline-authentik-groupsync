from typing import List, Dict
from aiohttp import web

from outline_openapi.models.error import Error
from outline_openapi.models.shares_create_post_request import SharesCreatePostRequest
from outline_openapi.models.views_create_post200_response import ViewsCreatePost200Response
from outline_openapi.models.views_list_post200_response import ViewsListPost200Response
from outline_openapi import util


async def views_create_post(request: web.Request, body=None) -> web.Response:
    """Create a view

    Creates a new view for a document. This is documented in the interests of thoroughness however it is recommended that views are not created from outside of the Outline UI.

    :param body: 
    :type body: dict | bytes

    """
    body = SharesCreatePostRequest.from_dict(body)
    return web.Response(status=200)


async def views_list_post(request: web.Request, body=None) -> web.Response:
    """List all views

    List all users that have viewed a document and the overall view count.

    :param body: 
    :type body: dict | bytes

    """
    body = SharesCreatePostRequest.from_dict(body)
    return web.Response(status=200)
