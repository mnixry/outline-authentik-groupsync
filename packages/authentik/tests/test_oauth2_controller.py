# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.expiring_base_grant_model import ExpiringBaseGrantModel
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_expiring_base_grant_model_list import PaginatedExpiringBaseGrantModelList
from authentik_openapi.models.paginated_token_model_list import PaginatedTokenModelList
from authentik_openapi.models.token_model import TokenModel
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_oauth2_access_tokens_destroy(client):
    """Test case for oauth2_access_tokens_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/oauth2/access_tokens/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_access_tokens_list(client):
    """Test case for oauth2_access_tokens_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider', 56),
                    ('search', 'search_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/access_tokens/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_access_tokens_retrieve(client):
    """Test case for oauth2_access_tokens_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/access_tokens/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_access_tokens_used_by_list(client):
    """Test case for oauth2_access_tokens_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/access_tokens/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_authorization_codes_destroy(client):
    """Test case for oauth2_authorization_codes_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/oauth2/authorization_codes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_authorization_codes_list(client):
    """Test case for oauth2_authorization_codes_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider', 56),
                    ('search', 'search_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/authorization_codes/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_authorization_codes_retrieve(client):
    """Test case for oauth2_authorization_codes_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/authorization_codes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_authorization_codes_used_by_list(client):
    """Test case for oauth2_authorization_codes_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/authorization_codes/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_refresh_tokens_destroy(client):
    """Test case for oauth2_refresh_tokens_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/oauth2/refresh_tokens/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_refresh_tokens_list(client):
    """Test case for oauth2_refresh_tokens_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider', 56),
                    ('search', 'search_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/refresh_tokens/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_refresh_tokens_retrieve(client):
    """Test case for oauth2_refresh_tokens_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/refresh_tokens/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_oauth2_refresh_tokens_used_by_list(client):
    """Test case for oauth2_refresh_tokens_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/oauth2/refresh_tokens/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

