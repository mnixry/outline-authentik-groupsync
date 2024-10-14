# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.revisions_info_post200_response import RevisionsInfoPost200Response
from outline_openapi.models.revisions_info_post_request import RevisionsInfoPostRequest
from outline_openapi.models.revisions_list_post200_response import RevisionsListPost200Response


pytestmark = pytest.mark.asyncio

async def test_revisions_info_post(client):
    """Test case for revisions_info_post

    Retrieve a revision
    """
    body = outline_openapi.RevisionsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/revisions.info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revisions_list_post(client):
    """Test case for revisions_list_post

    List all revisions
    """
    body = outline_openapi.DocumentsViewedPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/revisions.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

