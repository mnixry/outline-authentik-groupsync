# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.connection_token import ConnectionToken
from authentik_openapi.models.connection_token_request import ConnectionTokenRequest
from authentik_openapi.models.endpoint import Endpoint
from authentik_openapi.models.endpoint_request import EndpointRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_connection_token_list import PaginatedConnectionTokenList
from authentik_openapi.models.paginated_endpoint_list import PaginatedEndpointList
from authentik_openapi.models.patched_connection_token_request import PatchedConnectionTokenRequest
from authentik_openapi.models.patched_endpoint_request import PatchedEndpointRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_rac_connection_tokens_destroy(client):
    """Test case for rac_connection_tokens_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/rac/connection_tokens/{connection_token_uuid}'.format(connection_token_uuid='connection_token_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_connection_tokens_list(client):
    """Test case for rac_connection_tokens_list

    
    """
    params = [('endpoint', 'endpoint_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider', 56),
                    ('search', 'search_example'),
                    ('session__user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rac/connection_tokens/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_connection_tokens_partial_update(client):
    """Test case for rac_connection_tokens_partial_update

    
    """
    body = {"endpoint":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","provider":0,"pk":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/rac/connection_tokens/{connection_token_uuid}'.format(connection_token_uuid='connection_token_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_connection_tokens_retrieve(client):
    """Test case for rac_connection_tokens_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rac/connection_tokens/{connection_token_uuid}'.format(connection_token_uuid='connection_token_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_connection_tokens_update(client):
    """Test case for rac_connection_tokens_update

    
    """
    body = {"endpoint":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","provider":0,"pk":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/rac/connection_tokens/{connection_token_uuid}'.format(connection_token_uuid='connection_token_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_connection_tokens_used_by_list(client):
    """Test case for rac_connection_tokens_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rac/connection_tokens/{connection_token_uuid}/used_by'.format(connection_token_uuid='connection_token_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_endpoints_create(client):
    """Test case for rac_endpoints_create

    
    """
    body = {"settings":"","protocol":"rdp","provider":0,"maximum_connections":441289069,"name":"name","host":"host","auth_mode":"static","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/rac/endpoints/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_endpoints_destroy(client):
    """Test case for rac_endpoints_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/rac/endpoints/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_endpoints_list(client):
    """Test case for rac_endpoints_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider', 56),
                    ('search', 'search_example'),
                    ('superuser_full_list', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rac/endpoints/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_endpoints_partial_update(client):
    """Test case for rac_endpoints_partial_update

    
    """
    body = {"settings":"","protocol":"rdp","provider":0,"maximum_connections":441289069,"name":"name","host":"host","auth_mode":"static","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/rac/endpoints/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_endpoints_retrieve(client):
    """Test case for rac_endpoints_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rac/endpoints/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_endpoints_update(client):
    """Test case for rac_endpoints_update

    
    """
    body = {"settings":"","protocol":"rdp","provider":0,"maximum_connections":441289069,"name":"name","host":"host","auth_mode":"static","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/rac/endpoints/{pbm_uuid}'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rac_endpoints_used_by_list(client):
    """Test case for rac_endpoints_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rac/endpoints/{pbm_uuid}/used_by'.format(pbm_uuid='pbm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

