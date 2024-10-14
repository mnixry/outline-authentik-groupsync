from typing import List, Dict
from aiohttp import web

from outline_openapi.models.error import Error
from outline_openapi.models.events_list_post200_response import EventsListPost200Response
from outline_openapi.models.events_list_post_request import EventsListPostRequest
from outline_openapi import util


async def events_list_post(request: web.Request, body=None) -> web.Response:
    """List all events

    Events are an audit trail of important events that happen in the knowledge base.

    :param body: 
    :type body: dict | bytes

    """
    body = EventsListPostRequest.from_dict(body)
    return web.Response(status=200)
