# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_add_group_post200_response import CollectionsAddGroupPost200Response
from outline_openapi.models.collections_add_group_post_request import CollectionsAddGroupPostRequest
from outline_openapi.models.collections_add_user_post200_response import CollectionsAddUserPost200Response
from outline_openapi.models.collections_add_user_post_request import CollectionsAddUserPostRequest
from outline_openapi.models.collections_create_post200_response import CollectionsCreatePost200Response
from outline_openapi.models.collections_create_post_request import CollectionsCreatePostRequest
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.collections_documents_post200_response import CollectionsDocumentsPost200Response
from outline_openapi.models.collections_export_all_post_request import CollectionsExportAllPostRequest
from outline_openapi.models.collections_export_post200_response import CollectionsExportPost200Response
from outline_openapi.models.collections_export_post_request import CollectionsExportPostRequest
from outline_openapi.models.collections_group_memberships_post200_response import CollectionsGroupMembershipsPost200Response
from outline_openapi.models.collections_group_memberships_post_request import CollectionsGroupMembershipsPostRequest
from outline_openapi.models.collections_info_post200_response import CollectionsInfoPost200Response
from outline_openapi.models.collections_info_post_request import CollectionsInfoPostRequest
from outline_openapi.models.collections_list_post200_response import CollectionsListPost200Response
from outline_openapi.models.collections_memberships_post200_response import CollectionsMembershipsPost200Response
from outline_openapi.models.collections_memberships_post_request import CollectionsMembershipsPostRequest
from outline_openapi.models.collections_remove_group_post_request import CollectionsRemoveGroupPostRequest
from outline_openapi.models.collections_remove_user_post_request import CollectionsRemoveUserPostRequest
from outline_openapi.models.collections_update_post_request import CollectionsUpdatePostRequest
from outline_openapi.models.error import Error
from outline_openapi.models.pagination import Pagination


pytestmark = pytest.mark.asyncio

async def test_collections_add_group_post(client):
    """Test case for collections_add_group_post

    Add a group to a collection
    """
    body = outline_openapi.CollectionsAddGroupPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.add_group',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_add_user_post(client):
    """Test case for collections_add_user_post

    Add a collection user
    """
    body = outline_openapi.CollectionsAddUserPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.add_user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_create_post(client):
    """Test case for collections_create_post

    Create a collection
    """
    body = outline_openapi.CollectionsCreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_delete_post(client):
    """Test case for collections_delete_post

    Delete a collection
    """
    body = outline_openapi.CollectionsDeletePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.delete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_documents_post(client):
    """Test case for collections_documents_post

    Retrieve a collections document structure
    """
    body = outline_openapi.CollectionsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_export_all_post(client):
    """Test case for collections_export_all_post

    Export all collections
    """
    body = outline_openapi.CollectionsExportAllPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.export_all',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_export_post(client):
    """Test case for collections_export_post

    Export a collection
    """
    body = outline_openapi.CollectionsExportPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.export',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_group_memberships_post(client):
    """Test case for collections_group_memberships_post

    List all collection group members
    """
    body = outline_openapi.CollectionsGroupMembershipsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.group_memberships',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_info_post(client):
    """Test case for collections_info_post

    Retrieve a collection
    """
    body = outline_openapi.CollectionsInfoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.info',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_list_post(client):
    """Test case for collections_list_post

    List all collections
    """
    body = {"offset":0.8008281904610115,"limit":25}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.list',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_memberships_post(client):
    """Test case for collections_memberships_post

    List all collection memberships
    """
    body = outline_openapi.CollectionsMembershipsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.memberships',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_remove_group_post(client):
    """Test case for collections_remove_group_post

    Remove a collection group
    """
    body = outline_openapi.CollectionsRemoveGroupPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.remove_group',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_remove_user_post(client):
    """Test case for collections_remove_user_post

    Remove a collection user
    """
    body = outline_openapi.CollectionsRemoveUserPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.remove_user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_update_post(client):
    """Test case for collections_update_post

    Update a collection
    """
    body = outline_openapi.CollectionsUpdatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/collections.update',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

