# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.error import Error
from outline_openapi.models.shares_create_post_request import SharesCreatePostRequest
from outline_openapi.models.views_create_post200_response import ViewsCreatePost200Response
from outline_openapi.models.views_list_post200_response import ViewsListPost200Response


pytestmark = pytest.mark.asyncio

async def test_views_create_post(client):
    """Test case for views_create_post

    Create a view
    """
    body = outline_openapi.SharesCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/views.create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_views_list_post(client):
    """Test case for views_list_post

    List all views
    """
    body = outline_openapi.SharesCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/views.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

