# coding: utf-8

import pytest
import json
from aiohttp import web

from outline_openapi.models.auth_config_post200_response import AuthConfigPost200Response
from outline_openapi.models.auth_info_post200_response import AuthInfoPost200Response
from outline_openapi.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_auth_config_post(client):
    """Test case for auth_config_post

    Retrieve auth config
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/auth.config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_auth_info_post(client):
    """Test case for auth_info_post

    Retrieve auth
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/auth.info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

