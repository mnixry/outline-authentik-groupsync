# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.blueprint_file import BlueprintFile
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.models.blueprint_instance_request import BlueprintInstanceRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_blueprint_instance_list import PaginatedBlueprintInstanceList
from authentik_openapi.models.patched_blueprint_instance_request import PatchedBlueprintInstanceRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_apply_create(client):
    """Test case for managed_blueprints_apply_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/managed/blueprints/{instance_uuid}/apply'.format(instance_uuid='instance_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_available_list(client):
    """Test case for managed_blueprints_available_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/managed/blueprints/available/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_create(client):
    """Test case for managed_blueprints_create

    
    """
    body = {"path":"","name":"name","context":"","enabled":True,"content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/managed/blueprints/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_destroy(client):
    """Test case for managed_blueprints_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/managed/blueprints/{instance_uuid}'.format(instance_uuid='instance_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_list(client):
    """Test case for managed_blueprints_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('path', 'path_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/managed/blueprints/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_partial_update(client):
    """Test case for managed_blueprints_partial_update

    
    """
    body = {"path":"","name":"name","context":"","enabled":True,"content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/managed/blueprints/{instance_uuid}'.format(instance_uuid='instance_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_retrieve(client):
    """Test case for managed_blueprints_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/managed/blueprints/{instance_uuid}'.format(instance_uuid='instance_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_update(client):
    """Test case for managed_blueprints_update

    
    """
    body = {"path":"","name":"name","context":"","enabled":True,"content":"content"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/managed/blueprints/{instance_uuid}'.format(instance_uuid='instance_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_managed_blueprints_used_by_list(client):
    """Test case for managed_blueprints_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/managed/blueprints/{instance_uuid}/used_by'.format(instance_uuid='instance_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

