# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.comments_create_post200_response import CommentsCreatePost200Response
from outline_openapi.models.comments_create_post_request import CommentsCreatePostRequest
from outline_openapi.models.comments_list_post200_response import CommentsListPost200Response
from outline_openapi.models.comments_list_post_request import CommentsListPostRequest
from outline_openapi.models.comments_update_post_request import CommentsUpdatePostRequest
from outline_openapi.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_comments_create_post(client):
    """Test case for comments_create_post

    Create a comment
    """
    body = outline_openapi.CommentsCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/comments.create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_delete_post(client):
    """Test case for comments_delete_post

    Delete a comment
    """
    body = outline_openapi.CollectionsDeletePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/comments.delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_list_post(client):
    """Test case for comments_list_post

    List all comments
    """
    body = outline_openapi.CommentsListPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/comments.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_comments_update_post(client):
    """Test case for comments_update_post

    Update a comment
    """
    body = outline_openapi.CommentsUpdatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/comments.update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

