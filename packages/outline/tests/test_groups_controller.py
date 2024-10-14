# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.collections_remove_user_post_request import CollectionsRemoveUserPostRequest
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.groups_add_user_post200_response import GroupsAddUserPost200Response
from outline_openapi.models.groups_add_user_post_request import GroupsAddUserPostRequest
from outline_openapi.models.groups_create_post200_response import GroupsCreatePost200Response
from outline_openapi.models.groups_create_post_request import GroupsCreatePostRequest
from outline_openapi.models.groups_info_post200_response import GroupsInfoPost200Response
from outline_openapi.models.groups_info_post_request import GroupsInfoPostRequest
from outline_openapi.models.groups_list_post200_response import GroupsListPost200Response
from outline_openapi.models.groups_memberships_post200_response import GroupsMembershipsPost200Response
from outline_openapi.models.groups_memberships_post_request import GroupsMembershipsPostRequest
from outline_openapi.models.groups_remove_user_post200_response import GroupsRemoveUserPost200Response
from outline_openapi.models.groups_update_post_request import GroupsUpdatePostRequest


pytestmark = pytest.mark.asyncio

async def test_groups_add_user_post(client):
    """Test case for groups_add_user_post

    Add a group member
    """
    body = outline_openapi.GroupsAddUserPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.add_user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_create_post(client):
    """Test case for groups_create_post

    Create a group
    """
    body = outline_openapi.GroupsCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_delete_post(client):
    """Test case for groups_delete_post

    Delete a group
    """
    body = outline_openapi.CollectionsDeletePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_info_post(client):
    """Test case for groups_info_post

    Retrieve a group
    """
    body = outline_openapi.GroupsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_list_post(client):
    """Test case for groups_list_post

    List all groups
    """
    body = outline_openapi.DocumentsViewedPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_memberships_post(client):
    """Test case for groups_memberships_post

    List all group members
    """
    body = outline_openapi.GroupsMembershipsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.memberships',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_remove_user_post(client):
    """Test case for groups_remove_user_post

    Remove a group member
    """
    body = outline_openapi.CollectionsRemoveUserPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.remove_user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_groups_update_post(client):
    """Test case for groups_update_post

    Update a group
    """
    body = outline_openapi.GroupsUpdatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/groups.update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

