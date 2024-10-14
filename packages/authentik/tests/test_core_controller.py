# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from authentik_openapi.models.application import Application
from authentik_openapi.models.application_request import ApplicationRequest
from authentik_openapi.models.authenticated_session import AuthenticatedSession
from authentik_openapi.models.brand import Brand
from authentik_openapi.models.brand_request import BrandRequest
from authentik_openapi.models.coordinate import Coordinate
from authentik_openapi.models.current_brand import CurrentBrand
from authentik_openapi.models.file_path_request import FilePathRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.group import Group
from authentik_openapi.models.group_request import GroupRequest
from authentik_openapi.models.link import Link
from authentik_openapi.models.paginated_application_list import PaginatedApplicationList
from authentik_openapi.models.paginated_authenticated_session_list import PaginatedAuthenticatedSessionList
from authentik_openapi.models.paginated_brand_list import PaginatedBrandList
from authentik_openapi.models.paginated_group_list import PaginatedGroupList
from authentik_openapi.models.paginated_token_list import PaginatedTokenList
from authentik_openapi.models.paginated_user_consent_list import PaginatedUserConsentList
from authentik_openapi.models.paginated_user_list import PaginatedUserList
from authentik_openapi.models.patched_application_request import PatchedApplicationRequest
from authentik_openapi.models.patched_brand_request import PatchedBrandRequest
from authentik_openapi.models.patched_group_request import PatchedGroupRequest
from authentik_openapi.models.patched_token_request import PatchedTokenRequest
from authentik_openapi.models.patched_user_request import PatchedUserRequest
from authentik_openapi.models.policy_test_result import PolicyTestResult
from authentik_openapi.models.session_user import SessionUser
from authentik_openapi.models.token import Token
from authentik_openapi.models.token_request import TokenRequest
from authentik_openapi.models.token_set_key_request import TokenSetKeyRequest
from authentik_openapi.models.token_view import TokenView
from authentik_openapi.models.transaction_application_request import TransactionApplicationRequest
from authentik_openapi.models.transaction_application_response import TransactionApplicationResponse
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.user import User
from authentik_openapi.models.user_account_request import UserAccountRequest
from authentik_openapi.models.user_consent import UserConsent
from authentik_openapi.models.user_metrics import UserMetrics
from authentik_openapi.models.user_password_set_request import UserPasswordSetRequest
from authentik_openapi.models.user_path import UserPath
from authentik_openapi.models.user_request import UserRequest
from authentik_openapi.models.user_service_account_request import UserServiceAccountRequest
from authentik_openapi.models.user_service_account_response import UserServiceAccountResponse
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_core_applications_check_access_retrieve(client):
    """Test case for core_applications_check_access_retrieve

    
    """
    params = [('for_user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/applications/{slug}/check_access'.format(slug='slug_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_create(client):
    """Test case for core_applications_create

    
    """
    body = {"policy_engine_mode":"all","meta_description":"meta_description","backchannel_providers":[6,6],"provider":0,"open_in_new_tab":True,"name":"name","meta_launch_url":"https://openapi-generator.tech","slug":"slug","meta_publisher":"meta_publisher","group":"group"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/applications/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_destroy(client):
    """Test case for core_applications_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/core/applications/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_list(client):
    """Test case for core_applications_list

    
    """
    params = [('for_user', 56),
                    ('group', 'group_example'),
                    ('meta_description', 'meta_description_example'),
                    ('meta_launch_url', 'meta_launch_url_example'),
                    ('meta_publisher', 'meta_publisher_example'),
                    ('name', 'name_example'),
                    ('only_with_launch_url', True),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('slug', 'slug_example'),
                    ('superuser_full_list', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/applications/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_metrics_list(client):
    """Test case for core_applications_metrics_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/applications/{slug}/metrics'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_partial_update(client):
    """Test case for core_applications_partial_update

    
    """
    body = {"policy_engine_mode":"all","meta_description":"meta_description","backchannel_providers":[6,6],"provider":0,"open_in_new_tab":True,"name":"name","meta_launch_url":"https://openapi-generator.tech","slug":"slug","meta_publisher":"meta_publisher","group":"group"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/core/applications/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_retrieve(client):
    """Test case for core_applications_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/applications/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_core_applications_set_icon_create(client):
    """Test case for core_applications_set_icon_create

    
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
        path='/api/v3/core/applications/{slug}/set_icon'.format(slug='slug_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_set_icon_url_create(client):
    """Test case for core_applications_set_icon_url_create

    
    """
    body = {"url":"url"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/applications/{slug}/set_icon_url'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_update(client):
    """Test case for core_applications_update

    
    """
    body = {"policy_engine_mode":"all","meta_description":"meta_description","backchannel_providers":[6,6],"provider":0,"open_in_new_tab":True,"name":"name","meta_launch_url":"https://openapi-generator.tech","slug":"slug","meta_publisher":"meta_publisher","group":"group"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/core/applications/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_applications_used_by_list(client):
    """Test case for core_applications_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/applications/{slug}/used_by'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_authenticated_sessions_destroy(client):
    """Test case for core_authenticated_sessions_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/core/authenticated_sessions/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_authenticated_sessions_list(client):
    """Test case for core_authenticated_sessions_list

    
    """
    params = [('last_ip', 'last_ip_example'),
                    ('last_user_agent', 'last_user_agent_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('user__username', 'user__username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/authenticated_sessions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_authenticated_sessions_retrieve(client):
    """Test case for core_authenticated_sessions_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/authenticated_sessions/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_authenticated_sessions_used_by_list(client):
    """Test case for core_authenticated_sessions_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/authenticated_sessions/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_create(client):
    """Test case for core_brands_create

    
    """
    body = {"branding_logo":"branding_logo","default_application":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_device_code":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_authentication":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_recovery":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","default":True,"flow_invalidation":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","domain":"domain","flow_unenrollment":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","attributes":"","branding_title":"branding_title","branding_favicon":"branding_favicon","flow_user_settings":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","web_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/brands/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_current_retrieve(client):
    """Test case for core_brands_current_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/brands/current/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_destroy(client):
    """Test case for core_brands_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/core/brands/{brand_uuid}'.format(brand_uuid='brand_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_list(client):
    """Test case for core_brands_list

    
    """
    params = [('brand_uuid', 'brand_uuid_example'),
                    ('branding_favicon', 'branding_favicon_example'),
                    ('branding_logo', 'branding_logo_example'),
                    ('branding_title', 'branding_title_example'),
                    ('default', True),
                    ('domain', 'domain_example'),
                    ('flow_authentication', 'flow_authentication_example'),
                    ('flow_device_code', 'flow_device_code_example'),
                    ('flow_invalidation', 'flow_invalidation_example'),
                    ('flow_recovery', 'flow_recovery_example'),
                    ('flow_unenrollment', 'flow_unenrollment_example'),
                    ('flow_user_settings', 'flow_user_settings_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('web_certificate', 'web_certificate_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/brands/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_partial_update(client):
    """Test case for core_brands_partial_update

    
    """
    body = {"branding_logo":"branding_logo","default_application":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_device_code":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_authentication":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_recovery":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","default":True,"flow_invalidation":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","domain":"domain","flow_unenrollment":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","attributes":"","branding_title":"branding_title","branding_favicon":"branding_favicon","flow_user_settings":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","web_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/core/brands/{brand_uuid}'.format(brand_uuid='brand_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_retrieve(client):
    """Test case for core_brands_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/brands/{brand_uuid}'.format(brand_uuid='brand_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_update(client):
    """Test case for core_brands_update

    
    """
    body = {"branding_logo":"branding_logo","default_application":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_device_code":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_authentication":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_recovery":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","default":True,"flow_invalidation":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","domain":"domain","flow_unenrollment":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","attributes":"","branding_title":"branding_title","branding_favicon":"branding_favicon","flow_user_settings":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","web_certificate":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/core/brands/{brand_uuid}'.format(brand_uuid='brand_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_brands_used_by_list(client):
    """Test case for core_brands_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/brands/{brand_uuid}/used_by'.format(brand_uuid='brand_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_add_user_create(client):
    """Test case for core_groups_add_user_create

    
    """
    body = {"pk":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/groups/{group_uuid}/add_user'.format(group_uuid='group_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_create(client):
    """Test case for core_groups_create

    
    """
    body = {"parent":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","is_superuser":True,"roles":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","attributes":{"key":""},"users":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/groups/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_destroy(client):
    """Test case for core_groups_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/core/groups/{group_uuid}'.format(group_uuid='group_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_list(client):
    """Test case for core_groups_list

    
    """
    params = [('attributes', 'attributes_example'),
                    ('include_users', True),
                    ('is_superuser', True),
                    ('members_by_pk', [56]),
                    ('members_by_username', ['members_by_username_example']),
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
        path='/api/v3/core/groups/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_partial_update(client):
    """Test case for core_groups_partial_update

    
    """
    body = {"parent":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","is_superuser":True,"roles":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","attributes":{"key":""},"users":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/core/groups/{group_uuid}'.format(group_uuid='group_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_remove_user_create(client):
    """Test case for core_groups_remove_user_create

    
    """
    body = {"pk":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/groups/{group_uuid}/remove_user'.format(group_uuid='group_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_retrieve(client):
    """Test case for core_groups_retrieve

    
    """
    params = [('include_users', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/groups/{group_uuid}'.format(group_uuid='group_uuid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_update(client):
    """Test case for core_groups_update

    
    """
    body = {"parent":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","is_superuser":True,"roles":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","attributes":{"key":""},"users":[0,0]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/core/groups/{group_uuid}'.format(group_uuid='group_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_groups_used_by_list(client):
    """Test case for core_groups_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/groups/{group_uuid}/used_by'.format(group_uuid='group_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_create(client):
    """Test case for core_tokens_create

    
    """
    body = {"identifier":"identifier","expires":"2000-01-23T04:56:07.000+00:00","expiring":True,"managed":"managed","description":"description","intent":"verification","user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/tokens/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_destroy(client):
    """Test case for core_tokens_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/core/tokens/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_list(client):
    """Test case for core_tokens_list

    
    """
    params = [('description', 'description_example'),
                    ('expires', '2013-10-20T19:20:30+01:00'),
                    ('expiring', True),
                    ('identifier', 'identifier_example'),
                    ('intent', 'intent_example'),
                    ('managed', 'managed_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('user__username', 'user__username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/tokens/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_partial_update(client):
    """Test case for core_tokens_partial_update

    
    """
    body = {"identifier":"identifier","expires":"2000-01-23T04:56:07.000+00:00","expiring":True,"managed":"managed","description":"description","intent":"verification","user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/core/tokens/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_retrieve(client):
    """Test case for core_tokens_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/tokens/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_set_key_create(client):
    """Test case for core_tokens_set_key_create

    
    """
    body = {"key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/tokens/{identifier}/set_key'.format(identifier='identifier_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_update(client):
    """Test case for core_tokens_update

    
    """
    body = {"identifier":"identifier","expires":"2000-01-23T04:56:07.000+00:00","expiring":True,"managed":"managed","description":"description","intent":"verification","user":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/core/tokens/{identifier}'.format(identifier='identifier_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_used_by_list(client):
    """Test case for core_tokens_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/tokens/{identifier}/used_by'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_tokens_view_key_retrieve(client):
    """Test case for core_tokens_view_key_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/tokens/{identifier}/view_key'.format(identifier='identifier_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_transactional_applications_update(client):
    """Test case for core_transactional_applications_update

    
    """
    body = {"app":{"policy_engine_mode":"all","meta_description":"meta_description","backchannel_providers":[6,6],"provider":0,"open_in_new_tab":True,"name":"name","meta_launch_url":"https://openapi-generator.tech","slug":"slug","meta_publisher":"meta_publisher","group":"group"},"provider_model":"authentik_providers_google_workspace.googleworkspaceprovider","provider":{"default_group_email_domain":"default_group_email_domain","delegated_subject":"delegated_subject","property_mappings_group":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"credentials":"","filter_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","name":"name","scopes":"scopes","user_delete_action":"do_nothing","property_mappings":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"exclude_users_service_account":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/core/transactional/applications/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_user_consent_destroy(client):
    """Test case for core_user_consent_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/core/user_consent/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_user_consent_list(client):
    """Test case for core_user_consent_list

    
    """
    params = [('application', 'application_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/user_consent/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_user_consent_retrieve(client):
    """Test case for core_user_consent_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/user_consent/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_user_consent_used_by_list(client):
    """Test case for core_user_consent_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/user_consent/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_create(client):
    """Test case for core_users_create

    
    """
    body = {"path":"path","is_active":True,"last_login":"2000-01-23T04:56:07.000+00:00","name":"name","groups":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"attributes":{"key":""},"type":"internal","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/users/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_destroy(client):
    """Test case for core_users_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/core/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_impersonate_create(client):
    """Test case for core_users_impersonate_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/users/{id}/impersonate'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_impersonate_end_retrieve(client):
    """Test case for core_users_impersonate_end_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/users/impersonate_end/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_list(client):
    """Test case for core_users_list

    
    """
    params = [('attributes', 'attributes_example'),
                    ('email', 'email_example'),
                    ('groups_by_name', ['groups_by_name_example']),
                    ('groups_by_pk', ['groups_by_pk_example']),
                    ('include_groups', True),
                    ('is_active', True),
                    ('is_superuser', True),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('path', 'path_example'),
                    ('path_startswith', 'path_startswith_example'),
                    ('search', 'search_example'),
                    ('type', ['type_example']),
                    ('username', 'username_example'),
                    ('uuid', 'uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_me_retrieve(client):
    """Test case for core_users_me_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/users/me/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_metrics_retrieve(client):
    """Test case for core_users_metrics_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/users/{id}/metrics'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_partial_update(client):
    """Test case for core_users_partial_update

    
    """
    body = {"path":"path","is_active":True,"last_login":"2000-01-23T04:56:07.000+00:00","name":"name","groups":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"attributes":{"key":""},"type":"internal","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/core/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_paths_retrieve(client):
    """Test case for core_users_paths_retrieve

    
    """
    params = [('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/users/paths/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_recovery_create(client):
    """Test case for core_users_recovery_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/users/{id}/recovery'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_recovery_email_create(client):
    """Test case for core_users_recovery_email_create

    
    """
    params = [('email_stage', 'email_stage_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/users/{id}/recovery_email'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_retrieve(client):
    """Test case for core_users_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_service_account_create(client):
    """Test case for core_users_service_account_create

    
    """
    body = {"create_group":False,"expiring":True,"expires":"2000-01-23T04:56:07.000+00:00","name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/users/service_account/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_set_password_create(client):
    """Test case for core_users_set_password_create

    
    """
    body = {"password":"password"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/core/users/{id}/set_password'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_update(client):
    """Test case for core_users_update

    
    """
    body = {"path":"path","is_active":True,"last_login":"2000-01-23T04:56:07.000+00:00","name":"name","groups":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"attributes":{"key":""},"type":"internal","email":"email","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/core/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_core_users_used_by_list(client):
    """Test case for core_users_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/core/users/{id}/used_by'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

