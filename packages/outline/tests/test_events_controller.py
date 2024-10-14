# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.error import Error
from outline_openapi.models.events_list_post200_response import EventsListPost200Response
from outline_openapi.models.events_list_post_request import EventsListPostRequest


pytestmark = pytest.mark.asyncio

async def test_events_list_post(client):
    """Test case for events_list_post

    List all events
    """
    body = outline_openapi.EventsListPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/events.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

