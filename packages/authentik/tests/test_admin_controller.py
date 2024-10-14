# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.app import App
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.login_metrics import LoginMetrics
from authentik_openapi.models.patched_settings_request import PatchedSettingsRequest
from authentik_openapi.models.settings import Settings
from authentik_openapi.models.settings_request import SettingsRequest
from authentik_openapi.models.system_info import SystemInfo
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi.models.version import Version
from authentik_openapi.models.workers import Workers


pytestmark = pytest.mark.asyncio

async def test_admin_apps_list(client):
    """Test case for admin_apps_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/apps/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_metrics_retrieve(client):
    """Test case for admin_metrics_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/metrics/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_models_list(client):
    """Test case for admin_models_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/models/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_settings_partial_update(client):
    """Test case for admin_settings_partial_update

    
    """
    body = {"default_user_change_email":True,"default_user_change_name":True,"impersonation":True,"default_token_duration":"default_token_duration","default_user_change_username":True,"default_token_length":171976545,"event_retention":"event_retention","footer_links":"","gdpr_compliance":True,"avatars":"avatars"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/admin/settings/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_settings_retrieve(client):
    """Test case for admin_settings_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/settings/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_settings_update(client):
    """Test case for admin_settings_update

    
    """
    body = {"default_user_change_email":True,"default_user_change_name":True,"impersonation":True,"default_token_duration":"default_token_duration","default_user_change_username":True,"default_token_length":171976545,"event_retention":"event_retention","footer_links":"","gdpr_compliance":True,"avatars":"avatars"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/admin/settings/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_system_create(client):
    """Test case for admin_system_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/admin/system/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_system_retrieve(client):
    """Test case for admin_system_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/system/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_version_retrieve(client):
    """Test case for admin_version_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/version/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_workers_retrieve(client):
    """Test case for admin_workers_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/admin/workers/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

