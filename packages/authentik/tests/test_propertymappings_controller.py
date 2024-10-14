# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_openapi.models.google_workspace_provider_mapping_request import GoogleWorkspaceProviderMappingRequest
from authentik_openapi.models.ldap_source_property_mapping import LDAPSourcePropertyMapping
from authentik_openapi.models.ldap_source_property_mapping_request import LDAPSourcePropertyMappingRequest
from authentik_openapi.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_openapi.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest
from authentik_openapi.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_openapi.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest
from authentik_openapi.models.o_auth_source_property_mapping import OAuthSourcePropertyMapping
from authentik_openapi.models.o_auth_source_property_mapping_request import OAuthSourcePropertyMappingRequest
from authentik_openapi.models.paginated_google_workspace_provider_mapping_list import PaginatedGoogleWorkspaceProviderMappingList
from authentik_openapi.models.paginated_ldap_source_property_mapping_list import PaginatedLDAPSourcePropertyMappingList
from authentik_openapi.models.paginated_microsoft_entra_provider_mapping_list import PaginatedMicrosoftEntraProviderMappingList
from authentik_openapi.models.paginated_notification_webhook_mapping_list import PaginatedNotificationWebhookMappingList
from authentik_openapi.models.paginated_o_auth_source_property_mapping_list import PaginatedOAuthSourcePropertyMappingList
from authentik_openapi.models.paginated_plex_source_property_mapping_list import PaginatedPlexSourcePropertyMappingList
from authentik_openapi.models.paginated_property_mapping_list import PaginatedPropertyMappingList
from authentik_openapi.models.paginated_rac_property_mapping_list import PaginatedRACPropertyMappingList
from authentik_openapi.models.paginated_radius_provider_property_mapping_list import PaginatedRadiusProviderPropertyMappingList
from authentik_openapi.models.paginated_saml_property_mapping_list import PaginatedSAMLPropertyMappingList
from authentik_openapi.models.paginated_saml_source_property_mapping_list import PaginatedSAMLSourcePropertyMappingList
from authentik_openapi.models.paginated_scim_mapping_list import PaginatedSCIMMappingList
from authentik_openapi.models.paginated_scim_source_property_mapping_list import PaginatedSCIMSourcePropertyMappingList
from authentik_openapi.models.paginated_scope_mapping_list import PaginatedScopeMappingList
from authentik_openapi.models.patched_google_workspace_provider_mapping_request import PatchedGoogleWorkspaceProviderMappingRequest
from authentik_openapi.models.patched_ldap_source_property_mapping_request import PatchedLDAPSourcePropertyMappingRequest
from authentik_openapi.models.patched_microsoft_entra_provider_mapping_request import PatchedMicrosoftEntraProviderMappingRequest
from authentik_openapi.models.patched_notification_webhook_mapping_request import PatchedNotificationWebhookMappingRequest
from authentik_openapi.models.patched_o_auth_source_property_mapping_request import PatchedOAuthSourcePropertyMappingRequest
from authentik_openapi.models.patched_plex_source_property_mapping_request import PatchedPlexSourcePropertyMappingRequest
from authentik_openapi.models.patched_rac_property_mapping_request import PatchedRACPropertyMappingRequest
from authentik_openapi.models.patched_radius_provider_property_mapping_request import PatchedRadiusProviderPropertyMappingRequest
from authentik_openapi.models.patched_saml_property_mapping_request import PatchedSAMLPropertyMappingRequest
from authentik_openapi.models.patched_saml_source_property_mapping_request import PatchedSAMLSourcePropertyMappingRequest
from authentik_openapi.models.patched_scim_mapping_request import PatchedSCIMMappingRequest
from authentik_openapi.models.patched_scim_source_property_mapping_request import PatchedSCIMSourcePropertyMappingRequest
from authentik_openapi.models.patched_scope_mapping_request import PatchedScopeMappingRequest
from authentik_openapi.models.plex_source_property_mapping import PlexSourcePropertyMapping
from authentik_openapi.models.plex_source_property_mapping_request import PlexSourcePropertyMappingRequest
from authentik_openapi.models.property_mapping import PropertyMapping
from authentik_openapi.models.property_mapping_test_request import PropertyMappingTestRequest
from authentik_openapi.models.property_mapping_test_result import PropertyMappingTestResult
from authentik_openapi.models.rac_property_mapping import RACPropertyMapping
from authentik_openapi.models.rac_property_mapping_request import RACPropertyMappingRequest
from authentik_openapi.models.radius_provider_property_mapping import RadiusProviderPropertyMapping
from authentik_openapi.models.radius_provider_property_mapping_request import RadiusProviderPropertyMappingRequest
from authentik_openapi.models.saml_property_mapping import SAMLPropertyMapping
from authentik_openapi.models.saml_property_mapping_request import SAMLPropertyMappingRequest
from authentik_openapi.models.saml_source_property_mapping import SAMLSourcePropertyMapping
from authentik_openapi.models.saml_source_property_mapping_request import SAMLSourcePropertyMappingRequest
from authentik_openapi.models.scim_mapping import SCIMMapping
from authentik_openapi.models.scim_mapping_request import SCIMMappingRequest
from authentik_openapi.models.scim_source_property_mapping import SCIMSourcePropertyMapping
from authentik_openapi.models.scim_source_property_mapping_request import SCIMSourcePropertyMappingRequest
from authentik_openapi.models.scope_mapping import ScopeMapping
from authentik_openapi.models.scope_mapping_request import ScopeMappingRequest
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_propertymappings_all_destroy(client):
    """Test case for propertymappings_all_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/all/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_all_list(client):
    """Test case for propertymappings_all_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/all/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_all_retrieve(client):
    """Test case for propertymappings_all_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/all/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_all_test_create(client):
    """Test case for propertymappings_all_test_create

    
    """
    body = {"context":{"key":""},"user":0,"group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    params = [('format_result', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/all/{pm_uuid}/test'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_all_types_list(client):
    """Test case for propertymappings_all_types_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/all/types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_all_used_by_list(client):
    """Test case for propertymappings_all_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/all/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_notification_create(client):
    """Test case for propertymappings_notification_create

    
    """
    body = {"expression":"expression","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/notification/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_notification_destroy(client):
    """Test case for propertymappings_notification_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/notification/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_notification_list(client):
    """Test case for propertymappings_notification_list

    
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
        path='/api/v3/propertymappings/notification/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_notification_partial_update(client):
    """Test case for propertymappings_notification_partial_update

    
    """
    body = {"expression":"expression","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/notification/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_notification_retrieve(client):
    """Test case for propertymappings_notification_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/notification/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_notification_update(client):
    """Test case for propertymappings_notification_update

    
    """
    body = {"expression":"expression","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/notification/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_notification_used_by_list(client):
    """Test case for propertymappings_notification_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/notification/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_google_workspace_create(client):
    """Test case for propertymappings_provider_google_workspace_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/provider/google_workspace/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_google_workspace_destroy(client):
    """Test case for propertymappings_provider_google_workspace_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/provider/google_workspace/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_google_workspace_list(client):
    """Test case for propertymappings_provider_google_workspace_list

    
    """
    params = [('expression', 'expression_example'),
                    ('managed', ['managed_example']),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('pm_uuid', 'pm_uuid_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/google_workspace/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_google_workspace_partial_update(client):
    """Test case for propertymappings_provider_google_workspace_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/provider/google_workspace/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_google_workspace_retrieve(client):
    """Test case for propertymappings_provider_google_workspace_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/google_workspace/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_google_workspace_update(client):
    """Test case for propertymappings_provider_google_workspace_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/provider/google_workspace/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_google_workspace_used_by_list(client):
    """Test case for propertymappings_provider_google_workspace_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/google_workspace/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_microsoft_entra_create(client):
    """Test case for propertymappings_provider_microsoft_entra_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/provider/microsoft_entra/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_microsoft_entra_destroy(client):
    """Test case for propertymappings_provider_microsoft_entra_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/provider/microsoft_entra/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_microsoft_entra_list(client):
    """Test case for propertymappings_provider_microsoft_entra_list

    
    """
    params = [('expression', 'expression_example'),
                    ('managed', ['managed_example']),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('pm_uuid', 'pm_uuid_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/microsoft_entra/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_microsoft_entra_partial_update(client):
    """Test case for propertymappings_provider_microsoft_entra_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/provider/microsoft_entra/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_microsoft_entra_retrieve(client):
    """Test case for propertymappings_provider_microsoft_entra_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/microsoft_entra/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_microsoft_entra_update(client):
    """Test case for propertymappings_provider_microsoft_entra_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/provider/microsoft_entra/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_microsoft_entra_used_by_list(client):
    """Test case for propertymappings_provider_microsoft_entra_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/microsoft_entra/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_rac_create(client):
    """Test case for propertymappings_provider_rac_create

    
    """
    body = {"expression":"expression","static_settings":{"key":""},"managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/provider/rac/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_rac_destroy(client):
    """Test case for propertymappings_provider_rac_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/provider/rac/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_rac_list(client):
    """Test case for propertymappings_provider_rac_list

    
    """
    params = [('managed', ['managed_example']),
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
        path='/api/v3/propertymappings/provider/rac/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_rac_partial_update(client):
    """Test case for propertymappings_provider_rac_partial_update

    
    """
    body = {"expression":"expression","static_settings":{"key":""},"managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/provider/rac/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_rac_retrieve(client):
    """Test case for propertymappings_provider_rac_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/rac/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_rac_update(client):
    """Test case for propertymappings_provider_rac_update

    
    """
    body = {"expression":"expression","static_settings":{"key":""},"managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/provider/rac/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_rac_used_by_list(client):
    """Test case for propertymappings_provider_rac_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/rac/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_radius_create(client):
    """Test case for propertymappings_provider_radius_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/provider/radius/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_radius_destroy(client):
    """Test case for propertymappings_provider_radius_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/provider/radius/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_radius_list(client):
    """Test case for propertymappings_provider_radius_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/provider/radius/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_radius_partial_update(client):
    """Test case for propertymappings_provider_radius_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/provider/radius/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_radius_retrieve(client):
    """Test case for propertymappings_provider_radius_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/radius/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_radius_update(client):
    """Test case for propertymappings_provider_radius_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/provider/radius/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_radius_used_by_list(client):
    """Test case for propertymappings_provider_radius_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/radius/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_saml_create(client):
    """Test case for propertymappings_provider_saml_create

    
    """
    body = {"friendly_name":"friendly_name","expression":"expression","managed":"managed","name":"name","saml_name":"saml_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/provider/saml/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_saml_destroy(client):
    """Test case for propertymappings_provider_saml_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/provider/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_saml_list(client):
    """Test case for propertymappings_provider_saml_list

    
    """
    params = [('friendly_name', 'friendly_name_example'),
                    ('managed', ['managed_example']),
                    ('managed__isnull', True),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('saml_name', 'saml_name_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/saml/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_saml_partial_update(client):
    """Test case for propertymappings_provider_saml_partial_update

    
    """
    body = {"friendly_name":"friendly_name","expression":"expression","managed":"managed","name":"name","saml_name":"saml_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/provider/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_saml_retrieve(client):
    """Test case for propertymappings_provider_saml_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_saml_update(client):
    """Test case for propertymappings_provider_saml_update

    
    """
    body = {"friendly_name":"friendly_name","expression":"expression","managed":"managed","name":"name","saml_name":"saml_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/provider/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_saml_used_by_list(client):
    """Test case for propertymappings_provider_saml_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/saml/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scim_create(client):
    """Test case for propertymappings_provider_scim_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/provider/scim/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scim_destroy(client):
    """Test case for propertymappings_provider_scim_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/provider/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scim_list(client):
    """Test case for propertymappings_provider_scim_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/provider/scim/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scim_partial_update(client):
    """Test case for propertymappings_provider_scim_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/provider/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scim_retrieve(client):
    """Test case for propertymappings_provider_scim_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scim_update(client):
    """Test case for propertymappings_provider_scim_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/provider/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scim_used_by_list(client):
    """Test case for propertymappings_provider_scim_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/scim/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scope_create(client):
    """Test case for propertymappings_provider_scope_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name","description":"description","scope_name":"scope_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/provider/scope/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scope_destroy(client):
    """Test case for propertymappings_provider_scope_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/provider/scope/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scope_list(client):
    """Test case for propertymappings_provider_scope_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('scope_name', 'scope_name_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/scope/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scope_partial_update(client):
    """Test case for propertymappings_provider_scope_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name","description":"description","scope_name":"scope_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/provider/scope/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scope_retrieve(client):
    """Test case for propertymappings_provider_scope_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/scope/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scope_update(client):
    """Test case for propertymappings_provider_scope_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name","description":"description","scope_name":"scope_name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/provider/scope/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_provider_scope_used_by_list(client):
    """Test case for propertymappings_provider_scope_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/provider/scope/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_ldap_create(client):
    """Test case for propertymappings_source_ldap_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/source/ldap/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_ldap_destroy(client):
    """Test case for propertymappings_source_ldap_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/source/ldap/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_ldap_list(client):
    """Test case for propertymappings_source_ldap_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/source/ldap/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_ldap_partial_update(client):
    """Test case for propertymappings_source_ldap_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/source/ldap/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_ldap_retrieve(client):
    """Test case for propertymappings_source_ldap_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/ldap/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_ldap_update(client):
    """Test case for propertymappings_source_ldap_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/source/ldap/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_ldap_used_by_list(client):
    """Test case for propertymappings_source_ldap_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/ldap/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_oauth_create(client):
    """Test case for propertymappings_source_oauth_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/source/oauth/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_oauth_destroy(client):
    """Test case for propertymappings_source_oauth_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/source/oauth/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_oauth_list(client):
    """Test case for propertymappings_source_oauth_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/source/oauth/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_oauth_partial_update(client):
    """Test case for propertymappings_source_oauth_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/source/oauth/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_oauth_retrieve(client):
    """Test case for propertymappings_source_oauth_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/oauth/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_oauth_update(client):
    """Test case for propertymappings_source_oauth_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/source/oauth/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_oauth_used_by_list(client):
    """Test case for propertymappings_source_oauth_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/oauth/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_plex_create(client):
    """Test case for propertymappings_source_plex_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/source/plex/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_plex_destroy(client):
    """Test case for propertymappings_source_plex_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/source/plex/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_plex_list(client):
    """Test case for propertymappings_source_plex_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/source/plex/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_plex_partial_update(client):
    """Test case for propertymappings_source_plex_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/source/plex/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_plex_retrieve(client):
    """Test case for propertymappings_source_plex_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/plex/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_plex_update(client):
    """Test case for propertymappings_source_plex_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/source/plex/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_plex_used_by_list(client):
    """Test case for propertymappings_source_plex_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/plex/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_saml_create(client):
    """Test case for propertymappings_source_saml_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/source/saml/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_saml_destroy(client):
    """Test case for propertymappings_source_saml_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/source/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_saml_list(client):
    """Test case for propertymappings_source_saml_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/source/saml/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_saml_partial_update(client):
    """Test case for propertymappings_source_saml_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/source/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_saml_retrieve(client):
    """Test case for propertymappings_source_saml_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_saml_update(client):
    """Test case for propertymappings_source_saml_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/source/saml/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_saml_used_by_list(client):
    """Test case for propertymappings_source_saml_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/saml/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_scim_create(client):
    """Test case for propertymappings_source_scim_create

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/propertymappings/source/scim/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_scim_destroy(client):
    """Test case for propertymappings_source_scim_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/propertymappings/source/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_scim_list(client):
    """Test case for propertymappings_source_scim_list

    
    """
    params = [('managed', ['managed_example']),
                    ('managed__isnull', True),
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
        path='/api/v3/propertymappings/source/scim/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_scim_partial_update(client):
    """Test case for propertymappings_source_scim_partial_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/propertymappings/source/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_scim_retrieve(client):
    """Test case for propertymappings_source_scim_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_scim_update(client):
    """Test case for propertymappings_source_scim_update

    
    """
    body = {"expression":"expression","managed":"managed","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/propertymappings/source/scim/{pm_uuid}'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_propertymappings_source_scim_used_by_list(client):
    """Test case for propertymappings_source_scim_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/propertymappings/source/scim/{pm_uuid}/used_by'.format(pm_uuid='pm_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

