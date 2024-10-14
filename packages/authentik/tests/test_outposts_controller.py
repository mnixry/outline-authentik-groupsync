# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.docker_service_connection import DockerServiceConnection
from authentik_openapi.models.docker_service_connection_request import DockerServiceConnectionRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.kubernetes_service_connection import KubernetesServiceConnection
from authentik_openapi.models.kubernetes_service_connection_request import KubernetesServiceConnectionRequest
from authentik_openapi.models.ldap_check_access import LDAPCheckAccess
from authentik_openapi.models.outpost import Outpost
from authentik_openapi.models.outpost_default_config import OutpostDefaultConfig
from authentik_openapi.models.outpost_health import OutpostHealth
from authentik_openapi.models.outpost_request import OutpostRequest
from authentik_openapi.models.paginated_docker_service_connection_list import PaginatedDockerServiceConnectionList
from authentik_openapi.models.paginated_kubernetes_service_connection_list import PaginatedKubernetesServiceConnectionList
from authentik_openapi.models.paginated_ldap_outpost_config_list import PaginatedLDAPOutpostConfigList
from authentik_openapi.models.paginated_outpost_list import PaginatedOutpostList
from authentik_openapi.models.paginated_proxy_outpost_config_list import PaginatedProxyOutpostConfigList
from authentik_openapi.models.paginated_radius_outpost_config_list import PaginatedRadiusOutpostConfigList
from authentik_openapi.models.paginated_service_connection_list import PaginatedServiceConnectionList
from authentik_openapi.models.patched_docker_service_connection_request import PatchedDockerServiceConnectionRequest
from authentik_openapi.models.patched_kubernetes_service_connection_request import PatchedKubernetesServiceConnectionRequest
from authentik_openapi.models.patched_outpost_request import PatchedOutpostRequest
from authentik_openapi.models.radius_check_access import RadiusCheckAccess
from authentik_openapi.models.service_connection import ServiceConnection
from authentik_openapi.models.service_connection_state import ServiceConnectionState
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_create(client):
    """Test case for outposts_instances_create

    
    """
    body = {"managed":"managed","name":"name","service_connection":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"proxy","config":{"key":""},"providers":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/outposts/instances/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_default_settings_retrieve(client):
    """Test case for outposts_instances_default_settings_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/instances/default_settings/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_destroy(client):
    """Test case for outposts_instances_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/outposts/instances/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_health_list(client):
    """Test case for outposts_instances_health_list

    
    """
    params = [('managed__icontains', 'managed__icontains_example'),
                    ('managed__iexact', 'managed__iexact_example'),
                    ('name__icontains', 'name__icontains_example'),
                    ('name__iexact', 'name__iexact_example'),
                    ('ordering', 'ordering_example'),
                    ('providers__isnull', True),
                    ('providers_by_pk', [56]),
                    ('search', 'search_example'),
                    ('service_connection__name__icontains', 'service_connection__name__icontains_example'),
                    ('service_connection__name__iexact', 'service_connection__name__iexact_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/instances/{uuid}/health'.format(uuid='uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_list(client):
    """Test case for outposts_instances_list

    
    """
    params = [('managed__icontains', 'managed__icontains_example'),
                    ('managed__iexact', 'managed__iexact_example'),
                    ('name__icontains', 'name__icontains_example'),
                    ('name__iexact', 'name__iexact_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('providers__isnull', True),
                    ('providers_by_pk', [56]),
                    ('search', 'search_example'),
                    ('service_connection__name__icontains', 'service_connection__name__icontains_example'),
                    ('service_connection__name__iexact', 'service_connection__name__iexact_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/instances/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_partial_update(client):
    """Test case for outposts_instances_partial_update

    
    """
    body = {"managed":"managed","name":"name","service_connection":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"proxy","config":{"key":""},"providers":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/outposts/instances/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_retrieve(client):
    """Test case for outposts_instances_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/instances/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_update(client):
    """Test case for outposts_instances_update

    
    """
    body = {"managed":"managed","name":"name","service_connection":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","type":"proxy","config":{"key":""},"providers":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/outposts/instances/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_instances_used_by_list(client):
    """Test case for outposts_instances_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/instances/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_ldap_access_check(client):
    """Test case for outposts_ldap_access_check

    
    """
    params = [('app_slug', 'app_slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/ldap/{id}/check_access'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_ldap_list(client):
    """Test case for outposts_ldap_list

    
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
        path='/api/v3/outposts/ldap/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_proxy_list(client):
    """Test case for outposts_proxy_list

    
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
        path='/api/v3/outposts/proxy/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_radius_access_check(client):
    """Test case for outposts_radius_access_check

    
    """
    params = [('app_slug', 'app_slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/radius/{id}/check_access'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_radius_list(client):
    """Test case for outposts_radius_list

    
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
        path='/api/v3/outposts/radius/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_all_destroy(client):
    """Test case for outposts_service_connections_all_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/outposts/service_connections/all/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_all_list(client):
    """Test case for outposts_service_connections_all_list

    
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
        path='/api/v3/outposts/service_connections/all/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_all_retrieve(client):
    """Test case for outposts_service_connections_all_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/all/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_all_state_retrieve(client):
    """Test case for outposts_service_connections_all_state_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/all/{uuid}/state'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_all_types_list(client):
    """Test case for outposts_service_connections_all_types_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/all/types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_all_used_by_list(client):
    """Test case for outposts_service_connections_all_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/all/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_docker_create(client):
    """Test case for outposts_service_connections_docker_create

    
    """
    body = {"tls_authentication":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","local":True,"url":"url","tls_verification":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/outposts/service_connections/docker/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_docker_destroy(client):
    """Test case for outposts_service_connections_docker_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/outposts/service_connections/docker/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_docker_list(client):
    """Test case for outposts_service_connections_docker_list

    
    """
    params = [('local', True),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('tls_authentication', 'tls_authentication_example'),
                    ('tls_verification', 'tls_verification_example'),
                    ('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/docker/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_docker_partial_update(client):
    """Test case for outposts_service_connections_docker_partial_update

    
    """
    body = {"tls_authentication":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","local":True,"url":"url","tls_verification":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/outposts/service_connections/docker/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_docker_retrieve(client):
    """Test case for outposts_service_connections_docker_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/docker/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_docker_update(client):
    """Test case for outposts_service_connections_docker_update

    
    """
    body = {"tls_authentication":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","local":True,"url":"url","tls_verification":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/outposts/service_connections/docker/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_docker_used_by_list(client):
    """Test case for outposts_service_connections_docker_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/docker/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_kubernetes_create(client):
    """Test case for outposts_service_connections_kubernetes_create

    
    """
    body = {"verify_ssl":True,"name":"name","local":True,"kubeconfig":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/outposts/service_connections/kubernetes/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_kubernetes_destroy(client):
    """Test case for outposts_service_connections_kubernetes_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/outposts/service_connections/kubernetes/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_kubernetes_list(client):
    """Test case for outposts_service_connections_kubernetes_list

    
    """
    params = [('local', True),
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
        path='/api/v3/outposts/service_connections/kubernetes/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_kubernetes_partial_update(client):
    """Test case for outposts_service_connections_kubernetes_partial_update

    
    """
    body = {"verify_ssl":True,"name":"name","local":True,"kubeconfig":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/outposts/service_connections/kubernetes/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_kubernetes_retrieve(client):
    """Test case for outposts_service_connections_kubernetes_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/kubernetes/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_kubernetes_update(client):
    """Test case for outposts_service_connections_kubernetes_update

    
    """
    body = {"verify_ssl":True,"name":"name","local":True,"kubeconfig":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/outposts/service_connections/kubernetes/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_outposts_service_connections_kubernetes_used_by_list(client):
    """Test case for outposts_service_connections_kubernetes_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/outposts/service_connections/kubernetes/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

