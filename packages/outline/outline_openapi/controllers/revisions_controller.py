from typing import List, Dict
from aiohttp import web

from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.revisions_info_post200_response import RevisionsInfoPost200Response
from outline_openapi.models.revisions_info_post_request import RevisionsInfoPostRequest
from outline_openapi.models.revisions_list_post200_response import RevisionsListPost200Response
from outline_openapi import util


async def revisions_info_post(request: web.Request, body=None) -> web.Response:
    """Retrieve a revision

    

    :param body: 
    :type body: dict | bytes

    """
    body = RevisionsInfoPostRequest.from_dict(body)
    return web.Response(status=200)


async def revisions_list_post(request: web.Request, body=None) -> web.Response:
    """List all revisions

    

    :param body: 
    :type body: dict | bytes

    """
    body = DocumentsViewedPostRequest.from_dict(body)
    return web.Response(status=200)
