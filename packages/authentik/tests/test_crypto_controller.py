# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.certificate_data import CertificateData
from authentik_openapi.models.certificate_generation_request import CertificateGenerationRequest
from authentik_openapi.models.certificate_key_pair import CertificateKeyPair
from authentik_openapi.models.certificate_key_pair_request import CertificateKeyPairRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_certificate_key_pair_list import PaginatedCertificateKeyPairList
from authentik_openapi.models.patched_certificate_key_pair_request import PatchedCertificateKeyPairRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_create(client):
    """Test case for crypto_certificatekeypairs_create

    
    """
    body = {"certificate_data":"certificate_data","name":"name","key_data":"key_data"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/crypto/certificatekeypairs/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_destroy(client):
    """Test case for crypto_certificatekeypairs_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/crypto/certificatekeypairs/{kp_uuid}'.format(kp_uuid='kp_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_generate_create(client):
    """Test case for crypto_certificatekeypairs_generate_create

    
    """
    body = {"subject_alt_name":"subject_alt_name","validity_days":0,"common_name":"common_name","alg":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/crypto/certificatekeypairs/generate/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_list(client):
    """Test case for crypto_certificatekeypairs_list

    
    """
    params = [('has_key', True),
                    ('include_details', True),
                    ('managed', 'managed_example'),
                    ('name', 'name_example'),
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
        path='/api/v3/crypto/certificatekeypairs/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_partial_update(client):
    """Test case for crypto_certificatekeypairs_partial_update

    
    """
    body = {"certificate_data":"certificate_data","name":"name","key_data":"key_data"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/crypto/certificatekeypairs/{kp_uuid}'.format(kp_uuid='kp_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_retrieve(client):
    """Test case for crypto_certificatekeypairs_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/crypto/certificatekeypairs/{kp_uuid}'.format(kp_uuid='kp_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_update(client):
    """Test case for crypto_certificatekeypairs_update

    
    """
    body = {"certificate_data":"certificate_data","name":"name","key_data":"key_data"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/crypto/certificatekeypairs/{kp_uuid}'.format(kp_uuid='kp_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_used_by_list(client):
    """Test case for crypto_certificatekeypairs_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/crypto/certificatekeypairs/{kp_uuid}/used_by'.format(kp_uuid='kp_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_view_certificate_retrieve(client):
    """Test case for crypto_certificatekeypairs_view_certificate_retrieve

    
    """
    params = [('download', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/crypto/certificatekeypairs/{kp_uuid}/view_certificate'.format(kp_uuid='kp_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_crypto_certificatekeypairs_view_private_key_retrieve(client):
    """Test case for crypto_certificatekeypairs_view_private_key_retrieve

    
    """
    params = [('download', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/crypto/certificatekeypairs/{kp_uuid}/view_private_key'.format(kp_uuid='kp_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

