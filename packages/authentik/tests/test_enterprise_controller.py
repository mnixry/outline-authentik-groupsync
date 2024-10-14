# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.install_id import InstallID
from authentik_openapi.models.license import License
from authentik_openapi.models.license_forecast import LicenseForecast
from authentik_openapi.models.license_request import LicenseRequest
from authentik_openapi.models.license_summary import LicenseSummary
from authentik_openapi.models.paginated_license_list import PaginatedLicenseList
from authentik_openapi.models.patched_license_request import PatchedLicenseRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_create(client):
    """Test case for enterprise_license_create

    
    """
    body = {"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/enterprise/license/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_destroy(client):
    """Test case for enterprise_license_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/enterprise/license/{license_uuid}'.format(license_uuid='license_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_forecast_retrieve(client):
    """Test case for enterprise_license_forecast_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/license/forecast/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_install_id_retrieve(client):
    """Test case for enterprise_license_install_id_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/license/install_id/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_list(client):
    """Test case for enterprise_license_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/license/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_partial_update(client):
    """Test case for enterprise_license_partial_update

    
    """
    body = {"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/enterprise/license/{license_uuid}'.format(license_uuid='license_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_retrieve(client):
    """Test case for enterprise_license_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/license/{license_uuid}'.format(license_uuid='license_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_summary_retrieve(client):
    """Test case for enterprise_license_summary_retrieve

    
    """
    params = [('cached', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/license/summary/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_update(client):
    """Test case for enterprise_license_update

    
    """
    body = {"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/enterprise/license/{license_uuid}'.format(license_uuid='license_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enterprise_license_used_by_list(client):
    """Test case for enterprise_license_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/enterprise/license/{license_uuid}/used_by'.format(license_uuid='license_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

