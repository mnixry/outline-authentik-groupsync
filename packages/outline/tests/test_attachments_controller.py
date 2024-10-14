# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.attachments_create_post200_response import AttachmentsCreatePost200Response
from outline_openapi.models.attachments_create_post_request import AttachmentsCreatePostRequest
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.attachments_redirect_post_request import AttachmentsRedirectPostRequest
from outline_openapi.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_attachments_create_post(client):
    """Test case for attachments_create_post

    Create an attachment
    """
    body = outline_openapi.AttachmentsCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/attachments.create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attachments_delete_post(client):
    """Test case for attachments_delete_post

    Delete an attachment
    """
    body = outline_openapi.AttachmentsRedirectPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/attachments.delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attachments_redirect_post(client):
    """Test case for attachments_redirect_post

    Retrieve an attachment
    """
    body = outline_openapi.AttachmentsRedirectPostRequest()
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/attachments.redirect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

