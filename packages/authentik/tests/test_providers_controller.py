# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.google_workspace_provider import GoogleWorkspaceProvider
from authentik_openapi.models.google_workspace_provider_group import GoogleWorkspaceProviderGroup
from authentik_openapi.models.google_workspace_provider_group_request import GoogleWorkspaceProviderGroupRequest
from authentik_openapi.models.google_workspace_provider_request import GoogleWorkspaceProviderRequest
from authentik_openapi.models.google_workspace_provider_user import GoogleWorkspaceProviderUser
from authentik_openapi.models.google_workspace_provider_user_request import GoogleWorkspaceProviderUserRequest
from authentik_openapi.models.ldap_provider import LDAPProvider
from authentik_openapi.models.ldap_provider_request import LDAPProviderRequest
from authentik_openapi.models.microsoft_entra_provider import MicrosoftEntraProvider
from authentik_openapi.models.microsoft_entra_provider_group import MicrosoftEntraProviderGroup
from authentik_openapi.models.microsoft_entra_provider_group_request import MicrosoftEntraProviderGroupRequest
from authentik_openapi.models.microsoft_entra_provider_request import MicrosoftEntraProviderRequest
from authentik_openapi.models.microsoft_entra_provider_user import MicrosoftEntraProviderUser
from authentik_openapi.models.microsoft_entra_provider_user_request import MicrosoftEntraProviderUserRequest
from authentik_openapi.models.o_auth2_provider import OAuth2Provider
from authentik_openapi.models.o_auth2_provider_request import OAuth2ProviderRequest
from authentik_openapi.models.o_auth2_provider_setup_urls import OAuth2ProviderSetupURLs
from authentik_openapi.models.paginated_google_workspace_provider_group_list import PaginatedGoogleWorkspaceProviderGroupList
from authentik_openapi.models.paginated_google_workspace_provider_list import PaginatedGoogleWorkspaceProviderList
from authentik_openapi.models.paginated_google_workspace_provider_user_list import PaginatedGoogleWorkspaceProviderUserList
from authentik_openapi.models.paginated_ldap_provider_list import PaginatedLDAPProviderList
from authentik_openapi.models.paginated_microsoft_entra_provider_group_list import PaginatedMicrosoftEntraProviderGroupList
from authentik_openapi.models.paginated_microsoft_entra_provider_list import PaginatedMicrosoftEntraProviderList
from authentik_openapi.models.paginated_microsoft_entra_provider_user_list import PaginatedMicrosoftEntraProviderUserList
from authentik_openapi.models.paginated_o_auth2_provider_list import PaginatedOAuth2ProviderList
from authentik_openapi.models.paginated_provider_list import PaginatedProviderList
from authentik_openapi.models.paginated_proxy_provider_list import PaginatedProxyProviderList
from authentik_openapi.models.paginated_rac_provider_list import PaginatedRACProviderList
from authentik_openapi.models.paginated_radius_provider_list import PaginatedRadiusProviderList
from authentik_openapi.models.paginated_saml_provider_list import PaginatedSAMLProviderList
from authentik_openapi.models.paginated_scim_provider_group_list import PaginatedSCIMProviderGroupList
from authentik_openapi.models.paginated_scim_provider_list import PaginatedSCIMProviderList
from authentik_openapi.models.paginated_scim_provider_user_list import PaginatedSCIMProviderUserList
from authentik_openapi.models.patched_google_workspace_provider_request import PatchedGoogleWorkspaceProviderRequest
from authentik_openapi.models.patched_ldap_provider_request import PatchedLDAPProviderRequest
from authentik_openapi.models.patched_microsoft_entra_provider_request import PatchedMicrosoftEntraProviderRequest
from authentik_openapi.models.patched_o_auth2_provider_request import PatchedOAuth2ProviderRequest
from authentik_openapi.models.patched_proxy_provider_request import PatchedProxyProviderRequest
from authentik_openapi.models.patched_rac_provider_request import PatchedRACProviderRequest
from authentik_openapi.models.patched_radius_provider_request import PatchedRadiusProviderRequest
from authentik_openapi.models.patched_saml_provider_request import PatchedSAMLProviderRequest
from authentik_openapi.models.patched_scim_provider_request import PatchedSCIMProviderRequest
from authentik_openapi.models.property_mapping_preview import PropertyMappingPreview
from authentik_openapi.models.provider import Provider
from authentik_openapi.models.proxy_provider import ProxyProvider
from authentik_openapi.models.proxy_provider_request import ProxyProviderRequest
from authentik_openapi.models.rac_provider import RACProvider
from authentik_openapi.models.rac_provider_request import RACProviderRequest
from authentik_openapi.models.radius_provider import RadiusProvider
from authentik_openapi.models.radius_provider_request import RadiusProviderRequest
from authentik_openapi.models.saml_metadata import SAMLMetadata
from authentik_openapi.models.saml_provider import SAMLProvider
from authentik_openapi.models.saml_provider_request import SAMLProviderRequest
from authentik_openapi.models.scim_provider import SCIMProvider
from authentik_openapi.models.scim_provider_group import SCIMProviderGroup
from authentik_openapi.models.scim_provider_group_request import SCIMProviderGroupRequest
from authentik_openapi.models.scim_provider_request import SCIMProviderRequest
from authentik_openapi.models.scim_provider_user import SCIMProviderUser
from authentik_openapi.models.scim_provider_user_request import SCIMProviderUserRequest
from authentik_openapi.models.sync_object_request import SyncObjectRequest
from authentik_openapi.models.sync_object_result import SyncObjectResult
from authentik_openapi.models.sync_status import SyncStatus
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_providers_all_destroy(client):
    """Test case for providers_all_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/all/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_all_list(client):
    """Test case for providers_all_list

    
    """
    params = [('application__isnull', True),
                    ('backchannel', True),
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
        path='/api/v3/providers/all/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_all_retrieve(client):
    """Test case for providers_all_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/all/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_all_types_list(client):
    """Test case for providers_all_types_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/all/types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_all_used_by_list(client):
    """Test case for providers_all_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/all/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_create(client):
    """Test case for providers_google_workspace_create

    
    """
    body = {"default_group_email_domain":"default_group_email_domain","delegated_subject":"delegated_subject","property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"credentials":"","filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","scopes":"scopes","user_delete_action":"do_nothing","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/google_workspace/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_destroy(client):
    """Test case for providers_google_workspace_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/google_workspace/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_groups_create(client):
    """Test case for providers_google_workspace_groups_create

    
    """
    body = {"google_id":"google_id","provider":0,"group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/google_workspace_groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_groups_destroy(client):
    """Test case for providers_google_workspace_groups_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/google_workspace_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_groups_list(client):
    """Test case for providers_google_workspace_groups_list

    
    """
    params = [('group__group_uuid', 'group__group_uuid_example'),
                    ('group__name', 'group__name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider__id', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace_groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_groups_retrieve(client):
    """Test case for providers_google_workspace_groups_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_groups_used_by_list(client):
    """Test case for providers_google_workspace_groups_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace_groups/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_list(client):
    """Test case for providers_google_workspace_list

    
    """
    params = [('delegated_subject', 'delegated_subject_example'),
                    ('exclude_users_service_account', True),
                    ('filter_group', 'filter_group_example'),
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
        path='/api/v3/providers/google_workspace/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_partial_update(client):
    """Test case for providers_google_workspace_partial_update

    
    """
    body = {"default_group_email_domain":"default_group_email_domain","delegated_subject":"delegated_subject","property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"credentials":"","filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","scopes":"scopes","user_delete_action":"do_nothing","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/google_workspace/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_retrieve(client):
    """Test case for providers_google_workspace_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_sync_object_create(client):
    """Test case for providers_google_workspace_sync_object_create

    
    """
    body = {"sync_object_model":"authentik.core.models.User","sync_object_id":"sync_object_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/google_workspace/{id}/sync/object'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_sync_status_retrieve(client):
    """Test case for providers_google_workspace_sync_status_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace/{id}/sync/status'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_update(client):
    """Test case for providers_google_workspace_update

    
    """
    body = {"default_group_email_domain":"default_group_email_domain","delegated_subject":"delegated_subject","property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"credentials":"","filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","scopes":"scopes","user_delete_action":"do_nothing","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/google_workspace/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_used_by_list(client):
    """Test case for providers_google_workspace_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_users_create(client):
    """Test case for providers_google_workspace_users_create

    
    """
    body = {"google_id":"google_id","provider":6,"user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/google_workspace_users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_users_destroy(client):
    """Test case for providers_google_workspace_users_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/google_workspace_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_users_list(client):
    """Test case for providers_google_workspace_users_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider__id', 56),
                    ('search', 'search_example'),
                    ('user__id', 56),
                    ('user__username', 'user__username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace_users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_users_retrieve(client):
    """Test case for providers_google_workspace_users_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_google_workspace_users_used_by_list(client):
    """Test case for providers_google_workspace_users_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/google_workspace_users/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_ldap_create(client):
    """Test case for providers_ldap_create

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","uid_start_number":-1803530559,"search_mode":"direct","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","base_dn":"base_dn","name":"name","certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","tls_server_name":"tls_server_name","mfa_support":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"gid_start_number":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/ldap/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_ldap_destroy(client):
    """Test case for providers_ldap_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/ldap/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_ldap_list(client):
    """Test case for providers_ldap_list

    
    """
    params = [('application__isnull', True),
                    ('authorization_flow__slug__iexact', 'authorization_flow__slug__iexact_example'),
                    ('base_dn__iexact', 'base_dn__iexact_example'),
                    ('certificate__kp_uuid__iexact', 'certificate__kp_uuid__iexact_example'),
                    ('certificate__name__iexact', 'certificate__name__iexact_example'),
                    ('gid_start_number__iexact', 56),
                    ('name__iexact', 'name__iexact_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('tls_server_name__iexact', 'tls_server_name__iexact_example'),
                    ('uid_start_number__iexact', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/ldap/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_ldap_partial_update(client):
    """Test case for providers_ldap_partial_update

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","uid_start_number":-1803530559,"search_mode":"direct","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","base_dn":"base_dn","name":"name","certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","tls_server_name":"tls_server_name","mfa_support":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"gid_start_number":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/ldap/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_ldap_retrieve(client):
    """Test case for providers_ldap_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/ldap/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_ldap_update(client):
    """Test case for providers_ldap_update

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","uid_start_number":-1803530559,"search_mode":"direct","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","base_dn":"base_dn","name":"name","certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","tls_server_name":"tls_server_name","mfa_support":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"gid_start_number":441289069}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/ldap/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_ldap_used_by_list(client):
    """Test case for providers_ldap_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/ldap/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_create(client):
    """Test case for providers_microsoft_entra_create

    
    """
    body = {"tenant_id":"tenant_id","property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","client_secret":"client_secret","user_delete_action":"do_nothing","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"client_id":"client_id","exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/microsoft_entra/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_destroy(client):
    """Test case for providers_microsoft_entra_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/microsoft_entra/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_groups_create(client):
    """Test case for providers_microsoft_entra_groups_create

    
    """
    body = {"microsoft_id":"microsoft_id","provider":0,"group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/microsoft_entra_groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_groups_destroy(client):
    """Test case for providers_microsoft_entra_groups_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/microsoft_entra_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_groups_list(client):
    """Test case for providers_microsoft_entra_groups_list

    
    """
    params = [('group__group_uuid', 'group__group_uuid_example'),
                    ('group__name', 'group__name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider__id', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra_groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_groups_retrieve(client):
    """Test case for providers_microsoft_entra_groups_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_groups_used_by_list(client):
    """Test case for providers_microsoft_entra_groups_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra_groups/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_list(client):
    """Test case for providers_microsoft_entra_list

    
    """
    params = [('exclude_users_service_account', True),
                    ('filter_group', 'filter_group_example'),
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
        path='/api/v3/providers/microsoft_entra/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_partial_update(client):
    """Test case for providers_microsoft_entra_partial_update

    
    """
    body = {"tenant_id":"tenant_id","property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","client_secret":"client_secret","user_delete_action":"do_nothing","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"client_id":"client_id","exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/microsoft_entra/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_retrieve(client):
    """Test case for providers_microsoft_entra_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_sync_object_create(client):
    """Test case for providers_microsoft_entra_sync_object_create

    
    """
    body = {"sync_object_model":"authentik.core.models.User","sync_object_id":"sync_object_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/microsoft_entra/{id}/sync/object'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_sync_status_retrieve(client):
    """Test case for providers_microsoft_entra_sync_status_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra/{id}/sync/status'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_update(client):
    """Test case for providers_microsoft_entra_update

    
    """
    body = {"tenant_id":"tenant_id","property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","client_secret":"client_secret","user_delete_action":"do_nothing","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"client_id":"client_id","exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/microsoft_entra/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_used_by_list(client):
    """Test case for providers_microsoft_entra_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_users_create(client):
    """Test case for providers_microsoft_entra_users_create

    
    """
    body = {"microsoft_id":"microsoft_id","provider":6,"user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/microsoft_entra_users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_users_destroy(client):
    """Test case for providers_microsoft_entra_users_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/microsoft_entra_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_users_list(client):
    """Test case for providers_microsoft_entra_users_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider__id', 56),
                    ('search', 'search_example'),
                    ('user__id', 56),
                    ('user__username', 'user__username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra_users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_users_retrieve(client):
    """Test case for providers_microsoft_entra_users_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_microsoft_entra_users_used_by_list(client):
    """Test case for providers_microsoft_entra_users_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/microsoft_entra_users/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_create(client):
    """Test case for providers_oauth2_create

    
    """
    body = {"signing_key":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","client_type":"","redirect_uris":"redirect_uris","sub_mode":"","client_id":"client_id","refresh_token_validity":"refresh_token_validity","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","access_code_validity":"access_code_validity","include_claims_in_id_token":True,"access_token_validity":"access_token_validity","issuer_mode":"","jwks_sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","client_secret":"client_secret","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/oauth2/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_destroy(client):
    """Test case for providers_oauth2_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/oauth2/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_list(client):
    """Test case for providers_oauth2_list

    
    """
    params = [('access_code_validity', 'access_code_validity_example'),
                    ('access_token_validity', 'access_token_validity_example'),
                    ('application', 'application_example'),
                    ('authorization_flow', 'authorization_flow_example'),
                    ('client_id', 'client_id_example'),
                    ('client_type', 'client_type_example'),
                    ('include_claims_in_id_token', True),
                    ('issuer_mode', 'issuer_mode_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('property_mappings', ['property_mappings_example']),
                    ('redirect_uris', 'redirect_uris_example'),
                    ('refresh_token_validity', 'refresh_token_validity_example'),
                    ('search', 'search_example'),
                    ('signing_key', 'signing_key_example'),
                    ('sub_mode', 'sub_mode_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/oauth2/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_partial_update(client):
    """Test case for providers_oauth2_partial_update

    
    """
    body = {"signing_key":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","client_type":"","redirect_uris":"redirect_uris","sub_mode":"","client_id":"client_id","refresh_token_validity":"refresh_token_validity","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","access_code_validity":"access_code_validity","include_claims_in_id_token":True,"access_token_validity":"access_token_validity","issuer_mode":"","jwks_sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","client_secret":"client_secret","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/oauth2/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_preview_user_retrieve(client):
    """Test case for providers_oauth2_preview_user_retrieve

    
    """
    params = [('for_user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/oauth2/{id}/preview_user'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_retrieve(client):
    """Test case for providers_oauth2_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/oauth2/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_setup_urls_retrieve(client):
    """Test case for providers_oauth2_setup_urls_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/oauth2/{id}/setup_urls'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_update(client):
    """Test case for providers_oauth2_update

    
    """
    body = {"signing_key":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","client_type":"","redirect_uris":"redirect_uris","sub_mode":"","client_id":"client_id","refresh_token_validity":"refresh_token_validity","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","access_code_validity":"access_code_validity","include_claims_in_id_token":True,"access_token_validity":"access_token_validity","issuer_mode":"","jwks_sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","client_secret":"client_secret","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/oauth2/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_oauth2_used_by_list(client):
    """Test case for providers_oauth2_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/oauth2/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_proxy_create(client):
    """Test case for providers_proxy_create

    
    """
    body = {"external_host":"https://openapi-generator.tech","cookie_domain":"cookie_domain","skip_path_regex":"skip_path_regex","certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","basic_auth_password_attribute":"basic_auth_password_attribute","refresh_token_validity":"refresh_token_validity","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","mode":"","internal_host":"https://openapi-generator.tech","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","basic_auth_enabled":True,"basic_auth_user_attribute":"basic_auth_user_attribute","access_token_validity":"access_token_validity","jwks_sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","intercept_header_auth":True,"internal_host_ssl_validation":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/proxy/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_proxy_destroy(client):
    """Test case for providers_proxy_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/proxy/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_proxy_list(client):
    """Test case for providers_proxy_list

    
    """
    params = [('application__isnull', True),
                    ('authorization_flow__slug__iexact', 'authorization_flow__slug__iexact_example'),
                    ('basic_auth_enabled__iexact', True),
                    ('basic_auth_password_attribute__iexact', 'basic_auth_password_attribute__iexact_example'),
                    ('basic_auth_user_attribute__iexact', 'basic_auth_user_attribute__iexact_example'),
                    ('certificate__kp_uuid__iexact', 'certificate__kp_uuid__iexact_example'),
                    ('certificate__name__iexact', 'certificate__name__iexact_example'),
                    ('cookie_domain__iexact', 'cookie_domain__iexact_example'),
                    ('external_host__iexact', 'external_host__iexact_example'),
                    ('internal_host__iexact', 'internal_host__iexact_example'),
                    ('internal_host_ssl_validation__iexact', True),
                    ('mode__iexact', 'mode__iexact_example'),
                    ('name__iexact', 'name__iexact_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('property_mappings__iexact', ['property_mappings__iexact_example']),
                    ('redirect_uris__iexact', 'redirect_uris__iexact_example'),
                    ('search', 'search_example'),
                    ('skip_path_regex__iexact', 'skip_path_regex__iexact_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/proxy/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_proxy_partial_update(client):
    """Test case for providers_proxy_partial_update

    
    """
    body = {"external_host":"https://openapi-generator.tech","cookie_domain":"cookie_domain","skip_path_regex":"skip_path_regex","certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","basic_auth_password_attribute":"basic_auth_password_attribute","refresh_token_validity":"refresh_token_validity","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","mode":"","internal_host":"https://openapi-generator.tech","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","basic_auth_enabled":True,"basic_auth_user_attribute":"basic_auth_user_attribute","access_token_validity":"access_token_validity","jwks_sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","intercept_header_auth":True,"internal_host_ssl_validation":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/proxy/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_proxy_retrieve(client):
    """Test case for providers_proxy_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/proxy/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_proxy_update(client):
    """Test case for providers_proxy_update

    
    """
    body = {"external_host":"https://openapi-generator.tech","cookie_domain":"cookie_domain","skip_path_regex":"skip_path_regex","certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","basic_auth_password_attribute":"basic_auth_password_attribute","refresh_token_validity":"refresh_token_validity","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","mode":"","internal_host":"https://openapi-generator.tech","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","basic_auth_enabled":True,"basic_auth_user_attribute":"basic_auth_user_attribute","access_token_validity":"access_token_validity","jwks_sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","intercept_header_auth":True,"internal_host_ssl_validation":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/proxy/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_proxy_used_by_list(client):
    """Test case for providers_proxy_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/proxy/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_rac_create(client):
    """Test case for providers_rac_create

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","settings":"","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","delete_token_on_disconnect":True,"name":"name","connection_expiry":"connection_expiry","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/rac/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_rac_destroy(client):
    """Test case for providers_rac_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/rac/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_rac_list(client):
    """Test case for providers_rac_list

    
    """
    params = [('application__isnull', True),
                    ('name__iexact', 'name__iexact_example'),
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
        path='/api/v3/providers/rac/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_rac_partial_update(client):
    """Test case for providers_rac_partial_update

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","settings":"","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","delete_token_on_disconnect":True,"name":"name","connection_expiry":"connection_expiry","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/rac/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_rac_retrieve(client):
    """Test case for providers_rac_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/rac/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_rac_update(client):
    """Test case for providers_rac_update

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","settings":"","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","delete_token_on_disconnect":True,"name":"name","connection_expiry":"connection_expiry","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/rac/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_rac_used_by_list(client):
    """Test case for providers_rac_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/rac/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_radius_create(client):
    """Test case for providers_radius_create

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","client_networks":"client_networks","name":"name","shared_secret":"shared_secret","mfa_support":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/radius/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_radius_destroy(client):
    """Test case for providers_radius_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/radius/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_radius_list(client):
    """Test case for providers_radius_list

    
    """
    params = [('application__isnull', True),
                    ('authorization_flow__slug__iexact', 'authorization_flow__slug__iexact_example'),
                    ('client_networks__iexact', 'client_networks__iexact_example'),
                    ('name__iexact', 'name__iexact_example'),
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
        path='/api/v3/providers/radius/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_radius_partial_update(client):
    """Test case for providers_radius_partial_update

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","client_networks":"client_networks","name":"name","shared_secret":"shared_secret","mfa_support":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/radius/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_radius_retrieve(client):
    """Test case for providers_radius_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/radius/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_radius_update(client):
    """Test case for providers_radius_update

    
    """
    body = {"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","client_networks":"client_networks","name":"name","shared_secret":"shared_secret","mfa_support":True,"property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/radius/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_radius_used_by_list(client):
    """Test case for providers_radius_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/radius/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_create(client):
    """Test case for providers_saml_create

    
    """
    body = {"audience":"audience","sign_response":True,"session_valid_not_on_or_after":"session_valid_not_on_or_after","sp_binding":"","default_relay_state":"default_relay_state","acs_url":"https://openapi-generator.tech","issuer":"issuer","assertion_valid_not_before":"assertion_valid_not_before","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","digest_algorithm":"http://www.w3.org/2000/09/xmldsig#sha1","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","encryption_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sign_assertion":True,"name":"name","assertion_valid_not_on_or_after":"assertion_valid_not_on_or_after","signature_algorithm":"http://www.w3.org/2000/09/xmldsig#rsa-sha1","verification_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name_id_mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"signing_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/saml/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_destroy(client):
    """Test case for providers_saml_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_providers_saml_import_metadata_create(client):
    """Test case for providers_saml_import_metadata_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('name', 'name_example')
    data.add_field('authorization_flow', 'authorization_flow_example')
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v3/providers/saml/import_metadata/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_list(client):
    """Test case for providers_saml_list

    
    """
    params = [('acs_url', 'acs_url_example'),
                    ('assertion_valid_not_before', 'assertion_valid_not_before_example'),
                    ('assertion_valid_not_on_or_after', 'assertion_valid_not_on_or_after_example'),
                    ('audience', 'audience_example'),
                    ('authentication_flow', 'authentication_flow_example'),
                    ('authorization_flow', 'authorization_flow_example'),
                    ('backchannel_application', 'backchannel_application_example'),
                    ('default_relay_state', 'default_relay_state_example'),
                    ('digest_algorithm', 'digest_algorithm_example'),
                    ('encryption_kp', 'encryption_kp_example'),
                    ('is_backchannel', True),
                    ('issuer', 'issuer_example'),
                    ('name', 'name_example'),
                    ('name_id_mapping', 'name_id_mapping_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('property_mappings', ['property_mappings_example']),
                    ('search', 'search_example'),
                    ('session_valid_not_on_or_after', 'session_valid_not_on_or_after_example'),
                    ('sign_assertion', True),
                    ('sign_response', True),
                    ('signature_algorithm', 'signature_algorithm_example'),
                    ('signing_kp', 'signing_kp_example'),
                    ('sp_binding', 'sp_binding_example'),
                    ('verification_kp', 'verification_kp_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/saml/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_metadata_retrieve(client):
    """Test case for providers_saml_metadata_retrieve

    
    """
    params = [('download', True),
                    ('force_binding', 'force_binding_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/saml/{id}/metadata'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_partial_update(client):
    """Test case for providers_saml_partial_update

    
    """
    body = {"audience":"audience","sign_response":True,"session_valid_not_on_or_after":"session_valid_not_on_or_after","sp_binding":"","default_relay_state":"default_relay_state","acs_url":"https://openapi-generator.tech","issuer":"issuer","assertion_valid_not_before":"assertion_valid_not_before","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","digest_algorithm":"http://www.w3.org/2000/09/xmldsig#sha1","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","encryption_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sign_assertion":True,"name":"name","assertion_valid_not_on_or_after":"assertion_valid_not_on_or_after","signature_algorithm":"http://www.w3.org/2000/09/xmldsig#rsa-sha1","verification_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name_id_mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"signing_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/saml/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_preview_user_retrieve(client):
    """Test case for providers_saml_preview_user_retrieve

    
    """
    params = [('for_user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/saml/{id}/preview_user'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_retrieve(client):
    """Test case for providers_saml_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_update(client):
    """Test case for providers_saml_update

    
    """
    body = {"audience":"audience","sign_response":True,"session_valid_not_on_or_after":"session_valid_not_on_or_after","sp_binding":"","default_relay_state":"default_relay_state","acs_url":"https://openapi-generator.tech","issuer":"issuer","assertion_valid_not_before":"assertion_valid_not_before","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","digest_algorithm":"http://www.w3.org/2000/09/xmldsig#sha1","authorization_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","encryption_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sign_assertion":True,"name":"name","assertion_valid_not_on_or_after":"assertion_valid_not_on_or_after","signature_algorithm":"http://www.w3.org/2000/09/xmldsig#rsa-sha1","verification_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name_id_mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"signing_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/saml/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_saml_used_by_list(client):
    """Test case for providers_saml_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/saml/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_create(client):
    """Test case for providers_scim_create

    
    """
    body = {"property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"url":"url","token":"token","exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/scim/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_destroy(client):
    """Test case for providers_scim_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/scim/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_groups_create(client):
    """Test case for providers_scim_groups_create

    
    """
    body = {"scim_id":"scim_id","provider":0,"group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/scim_groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_groups_destroy(client):
    """Test case for providers_scim_groups_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/scim_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_groups_list(client):
    """Test case for providers_scim_groups_list

    
    """
    params = [('group__group_uuid', 'group__group_uuid_example'),
                    ('group__name', 'group__name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider__id', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim_groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_groups_retrieve(client):
    """Test case for providers_scim_groups_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_groups_used_by_list(client):
    """Test case for providers_scim_groups_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim_groups/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_list(client):
    """Test case for providers_scim_list

    
    """
    params = [('exclude_users_service_account', True),
                    ('filter_group', 'filter_group_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('url', 'url_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_partial_update(client):
    """Test case for providers_scim_partial_update

    
    """
    body = {"property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"url":"url","token":"token","exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/providers/scim/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_retrieve(client):
    """Test case for providers_scim_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_sync_object_create(client):
    """Test case for providers_scim_sync_object_create

    
    """
    body = {"sync_object_model":"authentik.core.models.User","sync_object_id":"sync_object_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/scim/{id}/sync/object'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_sync_status_retrieve(client):
    """Test case for providers_scim_sync_status_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim/{id}/sync/status'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_update(client):
    """Test case for providers_scim_update

    
    """
    body = {"property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"url":"url","token":"token","exclude_users_service_account":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/providers/scim/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_used_by_list(client):
    """Test case for providers_scim_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_users_create(client):
    """Test case for providers_scim_users_create

    
    """
    body = {"scim_id":"scim_id","provider":6,"user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/providers/scim_users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_users_destroy(client):
    """Test case for providers_scim_users_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/providers/scim_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_users_list(client):
    """Test case for providers_scim_users_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider__id', 56),
                    ('search', 'search_example'),
                    ('user__id', 56),
                    ('user__username', 'user__username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim_users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_users_retrieve(client):
    """Test case for providers_scim_users_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_providers_scim_users_used_by_list(client):
    """Test case for providers_scim_users_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/providers/scim_users/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

