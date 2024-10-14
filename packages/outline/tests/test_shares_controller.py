# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_shares_create_post(client):
    """Test case for shares_create_post

    Create a share
    """
    body = outline_openapi.SharesCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/shares.create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_info_post(client):
    """Test case for shares_info_post

    Retrieve a share object
    """
    body = outline_openapi.SharesInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/shares.info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_list_post(client):
    """Test case for shares_list_post

    List all shares
    """
    body = outline_openapi.DocumentsViewedPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/shares.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_revoke_post(client):
    """Test case for shares_revoke_post

    Revoke a share
    """
    body = outline_openapi.CollectionsDeletePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/shares.revoke',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shares_update_post(client):
    """Test case for shares_update_post

    Update a share
    """
    body = outline_openapi.SharesUpdatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/shares.update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

