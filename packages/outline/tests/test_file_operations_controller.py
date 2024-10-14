# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.error import Error
from outline_openapi.models.file_operations_info_post200_response import FileOperationsInfoPost200Response
from outline_openapi.models.file_operations_info_post_request import FileOperationsInfoPostRequest
from outline_openapi.models.file_operations_list_post200_response import FileOperationsListPost200Response
from outline_openapi.models.file_operations_list_post_request import FileOperationsListPostRequest


pytestmark = pytest.mark.asyncio

async def test_file_operations_delete_post(client):
    """Test case for file_operations_delete_post

    Delete a file operation
    """
    body = outline_openapi.FileOperationsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/fileOperations.delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_operations_info_post(client):
    """Test case for file_operations_info_post

    Retrieve a file operation
    """
    body = outline_openapi.FileOperationsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/fileOperations.info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_operations_list_post(client):
    """Test case for file_operations_list_post

    List all file operations
    """
    body = outline_openapi.FileOperationsListPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/fileOperations.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_file_operations_redirect_post(client):
    """Test case for file_operations_redirect_post

    Retrieve the file
    """
    body = outline_openapi.FileOperationsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/fileOperations.redirect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

