# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.config import Config
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_root_config_retrieve(client):
    """Test case for root_config_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/root/config/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

