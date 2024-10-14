# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.error import Error
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest
from outline_openapi.models.users_invite_post200_response import UsersInvitePost200Response
from outline_openapi.models.users_invite_post_request import UsersInvitePostRequest
from outline_openapi.models.users_list_post200_response import UsersListPost200Response
from outline_openapi.models.users_list_post_request import UsersListPostRequest
from outline_openapi.models.users_update_post_request import UsersUpdatePostRequest
from outline_openapi.models.users_update_role_post_request import UsersUpdateRolePostRequest


pytestmark = pytest.mark.asyncio

async def test_users_activate_post(client):
    """Test case for users_activate_post

    Activate a user
    """
    body = outline_openapi.UsersInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.activate',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_delete_post(client):
    """Test case for users_delete_post

    Delete a user
    """
    body = outline_openapi.UsersInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_info_post(client):
    """Test case for users_info_post

    Retrieve a user
    """
    body = outline_openapi.UsersInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_invite_post(client):
    """Test case for users_invite_post

    Invite users
    """
    body = outline_openapi.UsersInvitePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.invite',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_list_post(client):
    """Test case for users_list_post

    List all users
    """
    body = outline_openapi.UsersListPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_suspend_post(client):
    """Test case for users_suspend_post

    Suspend a user
    """
    body = outline_openapi.UsersInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.suspend',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_post(client):
    """Test case for users_update_post

    Update a user
    """
    body = outline_openapi.UsersUpdatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_users_update_role_post(client):
    """Test case for users_update_role_post

    Change a users role
    """
    body = outline_openapi.UsersUpdateRolePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/users.update_role',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

