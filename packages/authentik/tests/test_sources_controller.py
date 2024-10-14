# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from authentik_openapi.models.file_path_request import FilePathRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.group_o_auth_source_connection import GroupOAuthSourceConnection
from authentik_openapi.models.group_plex_source_connection import GroupPlexSourceConnection
from authentik_openapi.models.group_saml_source_connection import GroupSAMLSourceConnection
from authentik_openapi.models.ldap_debug import LDAPDebug
from authentik_openapi.models.ldap_source import LDAPSource
from authentik_openapi.models.ldap_source_request import LDAPSourceRequest
from authentik_openapi.models.o_auth_source import OAuthSource
from authentik_openapi.models.o_auth_source_request import OAuthSourceRequest
from authentik_openapi.models.paginated_group_o_auth_source_connection_list import PaginatedGroupOAuthSourceConnectionList
from authentik_openapi.models.paginated_group_plex_source_connection_list import PaginatedGroupPlexSourceConnectionList
from authentik_openapi.models.paginated_group_saml_source_connection_list import PaginatedGroupSAMLSourceConnectionList
from authentik_openapi.models.paginated_ldap_source_list import PaginatedLDAPSourceList
from authentik_openapi.models.paginated_o_auth_source_list import PaginatedOAuthSourceList
from authentik_openapi.models.paginated_plex_source_list import PaginatedPlexSourceList
from authentik_openapi.models.paginated_saml_source_list import PaginatedSAMLSourceList
from authentik_openapi.models.paginated_scim_source_group_list import PaginatedSCIMSourceGroupList
from authentik_openapi.models.paginated_scim_source_list import PaginatedSCIMSourceList
from authentik_openapi.models.paginated_scim_source_user_list import PaginatedSCIMSourceUserList
from authentik_openapi.models.paginated_source_list import PaginatedSourceList
from authentik_openapi.models.paginated_user_o_auth_source_connection_list import PaginatedUserOAuthSourceConnectionList
from authentik_openapi.models.paginated_user_plex_source_connection_list import PaginatedUserPlexSourceConnectionList
from authentik_openapi.models.paginated_user_saml_source_connection_list import PaginatedUserSAMLSourceConnectionList
from authentik_openapi.models.paginated_user_source_connection_list import PaginatedUserSourceConnectionList
from authentik_openapi.models.patched_ldap_source_request import PatchedLDAPSourceRequest
from authentik_openapi.models.patched_o_auth_source_request import PatchedOAuthSourceRequest
from authentik_openapi.models.patched_plex_source_request import PatchedPlexSourceRequest
from authentik_openapi.models.patched_saml_source_request import PatchedSAMLSourceRequest
from authentik_openapi.models.patched_scim_source_group_request import PatchedSCIMSourceGroupRequest
from authentik_openapi.models.patched_scim_source_request import PatchedSCIMSourceRequest
from authentik_openapi.models.patched_scim_source_user_request import PatchedSCIMSourceUserRequest
from authentik_openapi.models.patched_user_o_auth_source_connection_request import PatchedUserOAuthSourceConnectionRequest
from authentik_openapi.models.patched_user_plex_source_connection_request import PatchedUserPlexSourceConnectionRequest
from authentik_openapi.models.patched_user_saml_source_connection_request import PatchedUserSAMLSourceConnectionRequest
from authentik_openapi.models.plex_source import PlexSource
from authentik_openapi.models.plex_source_request import PlexSourceRequest
from authentik_openapi.models.plex_token_redeem_request import PlexTokenRedeemRequest
from authentik_openapi.models.redirect_challenge import RedirectChallenge
from authentik_openapi.models.saml_metadata import SAMLMetadata
from authentik_openapi.models.saml_source import SAMLSource
from authentik_openapi.models.saml_source_request import SAMLSourceRequest
from authentik_openapi.models.scim_source import SCIMSource
from authentik_openapi.models.scim_source_group import SCIMSourceGroup
from authentik_openapi.models.scim_source_group_request import SCIMSourceGroupRequest
from authentik_openapi.models.scim_source_request import SCIMSourceRequest
from authentik_openapi.models.scim_source_user import SCIMSourceUser
from authentik_openapi.models.scim_source_user_request import SCIMSourceUserRequest
from authentik_openapi.models.source import Source
from authentik_openapi.models.source_type import SourceType
from authentik_openapi.models.sync_status import SyncStatus
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik_openapi.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest
from authentik_openapi.models.user_plex_source_connection import UserPlexSourceConnection
from authentik_openapi.models.user_plex_source_connection_request import UserPlexSourceConnectionRequest
from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik_openapi.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest
from authentik_openapi.models.user_setting import UserSetting
from authentik_openapi.models.user_source_connection import UserSourceConnection
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_sources_all_destroy(client):
    """Test case for sources_all_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/all/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_all_list(client):
    """Test case for sources_all_list

    
    """
    params = [('managed', 'managed_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('slug', 'slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/all/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_all_retrieve(client):
    """Test case for sources_all_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/all/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_sources_all_set_icon_create(client):
    """Test case for sources_all_set_icon_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('clear', False)
    response = await client.request(
        method='POST',
        path='/api/v3/sources/all/{slug}/set_icon'.format(slug='slug_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_all_set_icon_url_create(client):
    """Test case for sources_all_set_icon_url_create

    
    """
    body = {"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/all/{slug}/set_icon_url'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_all_types_list(client):
    """Test case for sources_all_types_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/all/types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_all_used_by_list(client):
    """Test case for sources_all_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/all/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_all_user_settings_list(client):
    """Test case for sources_all_user_settings_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/all/user_settings/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_oauth_create(client):
    """Test case for sources_group_connections_oauth_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/group_connections/oauth/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_oauth_destroy(client):
    """Test case for sources_group_connections_oauth_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/group_connections/oauth/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_oauth_list(client):
    """Test case for sources_group_connections_oauth_list

    
    """
    params = [('group', 'group_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/oauth/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_oauth_partial_update(client):
    """Test case for sources_group_connections_oauth_partial_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/group_connections/oauth/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_oauth_retrieve(client):
    """Test case for sources_group_connections_oauth_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/oauth/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_oauth_update(client):
    """Test case for sources_group_connections_oauth_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/group_connections/oauth/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_oauth_used_by_list(client):
    """Test case for sources_group_connections_oauth_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/oauth/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_plex_create(client):
    """Test case for sources_group_connections_plex_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/group_connections/plex/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_plex_destroy(client):
    """Test case for sources_group_connections_plex_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/group_connections/plex/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_plex_list(client):
    """Test case for sources_group_connections_plex_list

    
    """
    params = [('group', 'group_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/plex/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_plex_partial_update(client):
    """Test case for sources_group_connections_plex_partial_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/group_connections/plex/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_plex_retrieve(client):
    """Test case for sources_group_connections_plex_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/plex/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_plex_update(client):
    """Test case for sources_group_connections_plex_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/group_connections/plex/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_plex_used_by_list(client):
    """Test case for sources_group_connections_plex_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/plex/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_saml_destroy(client):
    """Test case for sources_group_connections_saml_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/group_connections/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_saml_list(client):
    """Test case for sources_group_connections_saml_list

    
    """
    params = [('group', 'group_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/saml/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_saml_partial_update(client):
    """Test case for sources_group_connections_saml_partial_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/group_connections/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_saml_retrieve(client):
    """Test case for sources_group_connections_saml_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_saml_update(client):
    """Test case for sources_group_connections_saml_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/group_connections/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_group_connections_saml_used_by_list(client):
    """Test case for sources_group_connections_saml_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/group_connections/saml/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_create(client):
    """Test case for sources_ldap_create

    
    """
    body = {"object_uniqueness_field":"object_uniqueness_field","user_matching_mode":"","start_tls":True,"group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"additional_user_dn":"additional_user_dn","sync_users":True,"enabled":True,"client_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","base_dn":"base_dn","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"additional_group_dn":"additional_group_dn","sync_parent_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","slug":"slug","group_membership_field":"group_membership_field","server_uri":"https://openapi-generator.tech","bind_cn":"bind_cn","user_path_template":"user_path_template","sync_groups":True,"group_object_filter":"group_object_filter","sni":True,"password_login_update_internal_password":True,"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sync_users_password":True,"bind_password":"bind_password","name":"name","user_object_filter":"user_object_filter","peer_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/ldap/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_debug_retrieve(client):
    """Test case for sources_ldap_debug_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/ldap/{slug}/debug'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_destroy(client):
    """Test case for sources_ldap_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/ldap/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_list(client):
    """Test case for sources_ldap_list

    
    """
    params = [('additional_group_dn', 'additional_group_dn_example'),
                    ('additional_user_dn', 'additional_user_dn_example'),
                    ('base_dn', 'base_dn_example'),
                    ('bind_cn', 'bind_cn_example'),
                    ('client_certificate', 'client_certificate_example'),
                    ('enabled', True),
                    ('group_membership_field', 'group_membership_field_example'),
                    ('group_object_filter', 'group_object_filter_example'),
                    ('group_property_mappings', ['group_property_mappings_example']),
                    ('name', 'name_example'),
                    ('object_uniqueness_field', 'object_uniqueness_field_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('password_login_update_internal_password', True),
                    ('peer_certificate', 'peer_certificate_example'),
                    ('search', 'search_example'),
                    ('server_uri', 'server_uri_example'),
                    ('slug', 'slug_example'),
                    ('sni', True),
                    ('start_tls', True),
                    ('sync_groups', True),
                    ('sync_parent_group', 'sync_parent_group_example'),
                    ('sync_users', True),
                    ('sync_users_password', True),
                    ('user_object_filter', 'user_object_filter_example'),
                    ('user_property_mappings', ['user_property_mappings_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/ldap/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_partial_update(client):
    """Test case for sources_ldap_partial_update

    
    """
    body = {"object_uniqueness_field":"object_uniqueness_field","user_matching_mode":"","start_tls":True,"group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"additional_user_dn":"additional_user_dn","sync_users":True,"enabled":True,"client_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","base_dn":"base_dn","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"additional_group_dn":"additional_group_dn","sync_parent_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","slug":"slug","group_membership_field":"group_membership_field","server_uri":"https://openapi-generator.tech","bind_cn":"bind_cn","user_path_template":"user_path_template","sync_groups":True,"group_object_filter":"group_object_filter","sni":True,"password_login_update_internal_password":True,"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sync_users_password":True,"bind_password":"bind_password","name":"name","user_object_filter":"user_object_filter","peer_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/ldap/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_retrieve(client):
    """Test case for sources_ldap_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/ldap/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_sync_status_retrieve(client):
    """Test case for sources_ldap_sync_status_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/ldap/{slug}/sync/status'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_update(client):
    """Test case for sources_ldap_update

    
    """
    body = {"object_uniqueness_field":"object_uniqueness_field","user_matching_mode":"","start_tls":True,"group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"additional_user_dn":"additional_user_dn","sync_users":True,"enabled":True,"client_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","base_dn":"base_dn","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"additional_group_dn":"additional_group_dn","sync_parent_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","slug":"slug","group_membership_field":"group_membership_field","server_uri":"https://openapi-generator.tech","bind_cn":"bind_cn","user_path_template":"user_path_template","sync_groups":True,"group_object_filter":"group_object_filter","sni":True,"password_login_update_internal_password":True,"authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","sync_users_password":True,"bind_password":"bind_password","name":"name","user_object_filter":"user_object_filter","peer_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/ldap/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_ldap_used_by_list(client):
    """Test case for sources_ldap_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/ldap/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_create(client):
    """Test case for sources_oauth_create

    
    """
    body = {"provider_type":"apple","user_matching_mode":"","consumer_secret":"consumer_secret","oidc_jwks_url":"oidc_jwks_url","user_path_template":"user_path_template","request_token_url":"request_token_url","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"profile_url":"profile_url","authorization_url":"authorization_url","oidc_jwks":"","additional_scopes":"additional_scopes","enabled":True,"group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","consumer_key":"consumer_key","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","oidc_well_known_url":"oidc_well_known_url","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"access_token_url":"access_token_url","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/oauth/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_destroy(client):
    """Test case for sources_oauth_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/oauth/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_list(client):
    """Test case for sources_oauth_list

    
    """
    params = [('access_token_url', 'access_token_url_example'),
                    ('additional_scopes', 'additional_scopes_example'),
                    ('authentication_flow', 'authentication_flow_example'),
                    ('authorization_url', 'authorization_url_example'),
                    ('consumer_key', 'consumer_key_example'),
                    ('enabled', True),
                    ('enrollment_flow', 'enrollment_flow_example'),
                    ('group_matching_mode', 'group_matching_mode_example'),
                    ('has_jwks', True),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_engine_mode', 'policy_engine_mode_example'),
                    ('profile_url', 'profile_url_example'),
                    ('provider_type', 'provider_type_example'),
                    ('request_token_url', 'request_token_url_example'),
                    ('search', 'search_example'),
                    ('slug', 'slug_example'),
                    ('user_matching_mode', 'user_matching_mode_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/oauth/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_partial_update(client):
    """Test case for sources_oauth_partial_update

    
    """
    body = {"provider_type":"apple","user_matching_mode":"","consumer_secret":"consumer_secret","oidc_jwks_url":"oidc_jwks_url","user_path_template":"user_path_template","request_token_url":"request_token_url","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"profile_url":"profile_url","authorization_url":"authorization_url","oidc_jwks":"","additional_scopes":"additional_scopes","enabled":True,"group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","consumer_key":"consumer_key","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","oidc_well_known_url":"oidc_well_known_url","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"access_token_url":"access_token_url","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/oauth/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_retrieve(client):
    """Test case for sources_oauth_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/oauth/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_source_types_list(client):
    """Test case for sources_oauth_source_types_list

    
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/oauth/source_types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_update(client):
    """Test case for sources_oauth_update

    
    """
    body = {"provider_type":"apple","user_matching_mode":"","consumer_secret":"consumer_secret","oidc_jwks_url":"oidc_jwks_url","user_path_template":"user_path_template","request_token_url":"request_token_url","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"profile_url":"profile_url","authorization_url":"authorization_url","oidc_jwks":"","additional_scopes":"additional_scopes","enabled":True,"group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","consumer_key":"consumer_key","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","oidc_well_known_url":"oidc_well_known_url","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"access_token_url":"access_token_url","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/oauth/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_oauth_used_by_list(client):
    """Test case for sources_oauth_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/oauth/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_create(client):
    """Test case for sources_plex_create

    
    """
    body = {"allowed_servers":["allowed_servers","allowed_servers"],"user_matching_mode":"","user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"enabled":True,"client_id":"client_id","group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"allow_friends":True,"plex_token":"plex_token","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/plex/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_destroy(client):
    """Test case for sources_plex_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/plex/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_list(client):
    """Test case for sources_plex_list

    
    """
    params = [('allow_friends', True),
                    ('authentication_flow', 'authentication_flow_example'),
                    ('client_id', 'client_id_example'),
                    ('enabled', True),
                    ('enrollment_flow', 'enrollment_flow_example'),
                    ('group_matching_mode', 'group_matching_mode_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_engine_mode', 'policy_engine_mode_example'),
                    ('search', 'search_example'),
                    ('slug', 'slug_example'),
                    ('user_matching_mode', 'user_matching_mode_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/plex/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_partial_update(client):
    """Test case for sources_plex_partial_update

    
    """
    body = {"allowed_servers":["allowed_servers","allowed_servers"],"user_matching_mode":"","user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"enabled":True,"client_id":"client_id","group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"allow_friends":True,"plex_token":"plex_token","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/plex/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_redeem_token_authenticated_create(client):
    """Test case for sources_plex_redeem_token_authenticated_create

    
    """
    body = {"plex_token":"plex_token"}
    params = [('slug', 'slug_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/plex/redeem_token_authenticated/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_redeem_token_create(client):
    """Test case for sources_plex_redeem_token_create

    
    """
    body = {"plex_token":"plex_token"}
    params = [('slug', 'slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/plex/redeem_token/',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_retrieve(client):
    """Test case for sources_plex_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/plex/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_update(client):
    """Test case for sources_plex_update

    
    """
    body = {"allowed_servers":["allowed_servers","allowed_servers"],"user_matching_mode":"","user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"enabled":True,"client_id":"client_id","group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"allow_friends":True,"plex_token":"plex_token","slug":"slug"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/plex/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_plex_used_by_list(client):
    """Test case for sources_plex_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/plex/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_create(client):
    """Test case for sources_saml_create

    
    """
    body = {"binding_type":"REDIRECT","allow_idp_initiated":True,"user_matching_mode":"","user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"slo_url":"https://openapi-generator.tech","sso_url":"https://openapi-generator.tech","enabled":True,"issuer":"issuer","group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","digest_algorithm":"http://www.w3.org/2000/09/xmldsig#sha1","pre_authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","encryption_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name_id_policy":"","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"verification_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","signature_algorithm":"http://www.w3.org/2000/09/xmldsig#rsa-sha1","slug":"slug","signing_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","temporary_user_delete_after":"temporary_user_delete_after"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/saml/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_destroy(client):
    """Test case for sources_saml_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/saml/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_list(client):
    """Test case for sources_saml_list

    
    """
    params = [('allow_idp_initiated', True),
                    ('authentication_flow', 'authentication_flow_example'),
                    ('binding_type', 'binding_type_example'),
                    ('digest_algorithm', 'digest_algorithm_example'),
                    ('enabled', True),
                    ('enrollment_flow', 'enrollment_flow_example'),
                    ('issuer', 'issuer_example'),
                    ('managed', 'managed_example'),
                    ('name', 'name_example'),
                    ('name_id_policy', 'name_id_policy_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('policy_engine_mode', 'policy_engine_mode_example'),
                    ('pre_authentication_flow', 'pre_authentication_flow_example'),
                    ('search', 'search_example'),
                    ('signature_algorithm', 'signature_algorithm_example'),
                    ('signing_kp', 'signing_kp_example'),
                    ('slo_url', 'slo_url_example'),
                    ('slug', 'slug_example'),
                    ('sso_url', 'sso_url_example'),
                    ('temporary_user_delete_after', 'temporary_user_delete_after_example'),
                    ('user_matching_mode', 'user_matching_mode_example'),
                    ('verification_kp', 'verification_kp_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/saml/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_metadata_retrieve(client):
    """Test case for sources_saml_metadata_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/saml/{slug}/metadata'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_partial_update(client):
    """Test case for sources_saml_partial_update

    
    """
    body = {"binding_type":"REDIRECT","allow_idp_initiated":True,"user_matching_mode":"","user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"slo_url":"https://openapi-generator.tech","sso_url":"https://openapi-generator.tech","enabled":True,"issuer":"issuer","group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","digest_algorithm":"http://www.w3.org/2000/09/xmldsig#sha1","pre_authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","encryption_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name_id_policy":"","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"verification_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","signature_algorithm":"http://www.w3.org/2000/09/xmldsig#rsa-sha1","slug":"slug","signing_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","temporary_user_delete_after":"temporary_user_delete_after"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/saml/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_retrieve(client):
    """Test case for sources_saml_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/saml/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_update(client):
    """Test case for sources_saml_update

    
    """
    body = {"binding_type":"REDIRECT","allow_idp_initiated":True,"user_matching_mode":"","user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"slo_url":"https://openapi-generator.tech","sso_url":"https://openapi-generator.tech","enabled":True,"issuer":"issuer","group_matching_mode":"","authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","policy_engine_mode":"all","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","digest_algorithm":"http://www.w3.org/2000/09/xmldsig#sha1","pre_authentication_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","encryption_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name_id_policy":"","name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"verification_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","signature_algorithm":"http://www.w3.org/2000/09/xmldsig#rsa-sha1","slug":"slug","signing_kp":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","temporary_user_delete_after":"temporary_user_delete_after"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/saml/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_saml_used_by_list(client):
    """Test case for sources_saml_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/saml/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_create(client):
    """Test case for sources_scim_create

    
    """
    body = {"user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"slug":"slug","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/scim/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_destroy(client):
    """Test case for sources_scim_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/scim/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_groups_create(client):
    """Test case for sources_scim_groups_create

    
    """
    body = {"attributes":"","id":"id","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/scim_groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_groups_destroy(client):
    """Test case for sources_scim_groups_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/scim_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_groups_list(client):
    """Test case for sources_scim_groups_list

    
    """
    params = [('group__group_uuid', 'group__group_uuid_example'),
                    ('group__name', 'group__name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim_groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_groups_partial_update(client):
    """Test case for sources_scim_groups_partial_update

    
    """
    body = {"attributes":"","id":"id","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/scim_groups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_groups_retrieve(client):
    """Test case for sources_scim_groups_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim_groups/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_groups_update(client):
    """Test case for sources_scim_groups_update

    
    """
    body = {"attributes":"","id":"id","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/scim_groups/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_groups_used_by_list(client):
    """Test case for sources_scim_groups_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim_groups/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_list(client):
    """Test case for sources_scim_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('slug', 'slug_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_partial_update(client):
    """Test case for sources_scim_partial_update

    
    """
    body = {"user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"slug":"slug","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/scim/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_retrieve(client):
    """Test case for sources_scim_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_update(client):
    """Test case for sources_scim_update

    
    """
    body = {"user_path_template":"user_path_template","group_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","user_property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"slug":"slug","enabled":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/scim/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_used_by_list(client):
    """Test case for sources_scim_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_users_create(client):
    """Test case for sources_scim_users_create

    
    """
    body = {"attributes":"","id":"id","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/scim_users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_users_destroy(client):
    """Test case for sources_scim_users_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/scim_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_users_list(client):
    """Test case for sources_scim_users_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example'),
                    ('user__id', 56),
                    ('user__username', 'user__username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim_users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_users_partial_update(client):
    """Test case for sources_scim_users_partial_update

    
    """
    body = {"attributes":"","id":"id","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/scim_users/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_users_retrieve(client):
    """Test case for sources_scim_users_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim_users/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_users_update(client):
    """Test case for sources_scim_users_update

    
    """
    body = {"attributes":"","id":"id","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/scim_users/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_scim_users_used_by_list(client):
    """Test case for sources_scim_users_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/scim_users/{id}/used_by'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_all_destroy(client):
    """Test case for sources_user_connections_all_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/user_connections/all/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_all_list(client):
    """Test case for sources_user_connections_all_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/all/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_all_partial_update(client):
    """Test case for sources_user_connections_all_partial_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/user_connections/all/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_all_retrieve(client):
    """Test case for sources_user_connections_all_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/all/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_all_update(client):
    """Test case for sources_user_connections_all_update

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/user_connections/all/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_all_used_by_list(client):
    """Test case for sources_user_connections_all_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/all/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_oauth_create(client):
    """Test case for sources_user_connections_oauth_create

    
    """
    body = {"access_token":"access_token","identifier":"identifier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/user_connections/oauth/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_oauth_destroy(client):
    """Test case for sources_user_connections_oauth_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/user_connections/oauth/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_oauth_list(client):
    """Test case for sources_user_connections_oauth_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/oauth/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_oauth_partial_update(client):
    """Test case for sources_user_connections_oauth_partial_update

    
    """
    body = {"access_token":"access_token","identifier":"identifier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/user_connections/oauth/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_oauth_retrieve(client):
    """Test case for sources_user_connections_oauth_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/oauth/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_oauth_update(client):
    """Test case for sources_user_connections_oauth_update

    
    """
    body = {"access_token":"access_token","identifier":"identifier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/user_connections/oauth/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_oauth_used_by_list(client):
    """Test case for sources_user_connections_oauth_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/oauth/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_plex_create(client):
    """Test case for sources_user_connections_plex_create

    
    """
    body = {"identifier":"identifier","plex_token":"plex_token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/user_connections/plex/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_plex_destroy(client):
    """Test case for sources_user_connections_plex_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/user_connections/plex/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_plex_list(client):
    """Test case for sources_user_connections_plex_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/plex/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_plex_partial_update(client):
    """Test case for sources_user_connections_plex_partial_update

    
    """
    body = {"identifier":"identifier","plex_token":"plex_token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/user_connections/plex/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_plex_retrieve(client):
    """Test case for sources_user_connections_plex_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/plex/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_plex_update(client):
    """Test case for sources_user_connections_plex_update

    
    """
    body = {"identifier":"identifier","plex_token":"plex_token"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/user_connections/plex/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_plex_used_by_list(client):
    """Test case for sources_user_connections_plex_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/plex/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_saml_create(client):
    """Test case for sources_user_connections_saml_create

    
    """
    body = {"identifier":"identifier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/sources/user_connections/saml/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_saml_destroy(client):
    """Test case for sources_user_connections_saml_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/sources/user_connections/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_saml_list(client):
    """Test case for sources_user_connections_saml_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('source__slug', 'source__slug_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/saml/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_saml_partial_update(client):
    """Test case for sources_user_connections_saml_partial_update

    
    """
    body = {"identifier":"identifier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/sources/user_connections/saml/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_saml_retrieve(client):
    """Test case for sources_user_connections_saml_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/saml/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_saml_update(client):
    """Test case for sources_user_connections_saml_update

    
    """
    body = {"identifier":"identifier"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/sources/user_connections/saml/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sources_user_connections_saml_used_by_list(client):
    """Test case for sources_user_connections_saml_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/sources/user_connections/saml/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

