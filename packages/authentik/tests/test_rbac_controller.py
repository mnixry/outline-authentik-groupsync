# coding: utf-8

import pytest
import json
from aiohttp import web

from authentik_openapi.models.extra_role_object_permission import ExtraRoleObjectPermission
from authentik_openapi.models.extra_role_object_permission_request import ExtraRoleObjectPermissionRequest
from authentik_openapi.models.extra_user_object_permission import ExtraUserObjectPermission
from authentik_openapi.models.extra_user_object_permission_request import ExtraUserObjectPermissionRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_extra_role_object_permission_list import PaginatedExtraRoleObjectPermissionList
from authentik_openapi.models.paginated_extra_user_object_permission_list import PaginatedExtraUserObjectPermissionList
from authentik_openapi.models.paginated_permission_list import PaginatedPermissionList
from authentik_openapi.models.paginated_role_assigned_object_permission_list import PaginatedRoleAssignedObjectPermissionList
from authentik_openapi.models.paginated_role_list import PaginatedRoleList
from authentik_openapi.models.paginated_user_assigned_object_permission_list import PaginatedUserAssignedObjectPermissionList
from authentik_openapi.models.patched_extra_role_object_permission_request import PatchedExtraRoleObjectPermissionRequest
from authentik_openapi.models.patched_extra_user_object_permission_request import PatchedExtraUserObjectPermissionRequest
from authentik_openapi.models.patched_permission_assign_request import PatchedPermissionAssignRequest
from authentik_openapi.models.patched_role_request import PatchedRoleRequest
from authentik_openapi.models.permission import Permission
from authentik_openapi.models.permission_assign_request import PermissionAssignRequest
from authentik_openapi.models.permission_assign_result import PermissionAssignResult
from authentik_openapi.models.role import Role
from authentik_openapi.models.role_request import RoleRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_assigned_by_roles_assign(client):
    """Test case for rbac_permissions_assigned_by_roles_assign

    
    """
    body = {"permissions":["permissions","permissions"],"model":"authentik_tenants.domain","object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/rbac/permissions/assigned_by_roles/{uuid}/assign'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_assigned_by_roles_list(client):
    """Test case for rbac_permissions_assigned_by_roles_list

    
    """
    params = [('model', 'model_example'),
                    ('object_pk', 'object_pk_example'),
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
        path='/api/v3/rbac/permissions/assigned_by_roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_assigned_by_roles_unassign_partial_update(client):
    """Test case for rbac_permissions_assigned_by_roles_unassign_partial_update

    
    """
    body = {"permissions":["permissions","permissions"],"model":"authentik_tenants.domain","object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/rbac/permissions/assigned_by_roles/{uuid}/unassign'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_assigned_by_users_assign(client):
    """Test case for rbac_permissions_assigned_by_users_assign

    
    """
    body = {"permissions":["permissions","permissions"],"model":"authentik_tenants.domain","object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/rbac/permissions/assigned_by_users/{id}/assign'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_assigned_by_users_list(client):
    """Test case for rbac_permissions_assigned_by_users_list

    
    """
    params = [('model', 'model_example'),
                    ('object_pk', 'object_pk_example'),
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
        path='/api/v3/rbac/permissions/assigned_by_users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_assigned_by_users_unassign_partial_update(client):
    """Test case for rbac_permissions_assigned_by_users_unassign_partial_update

    
    """
    body = {"permissions":["permissions","permissions"],"model":"authentik_tenants.domain","object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/rbac/permissions/assigned_by_users/{id}/unassign'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_list(client):
    """Test case for rbac_permissions_list

    
    """
    params = [('codename', 'codename_example'),
                    ('content_type__app_label', 'content_type__app_label_example'),
                    ('content_type__model', 'content_type__model_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('role', 'role_example'),
                    ('search', 'search_example'),
                    ('user', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/permissions/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_retrieve(client):
    """Test case for rbac_permissions_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/permissions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_roles_destroy(client):
    """Test case for rbac_permissions_roles_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/rbac/permissions/roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_roles_list(client):
    """Test case for rbac_permissions_roles_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('uuid', 'uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/permissions/roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_roles_partial_update(client):
    """Test case for rbac_permissions_roles_partial_update

    
    """
    body = {"object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/rbac/permissions/roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_roles_retrieve(client):
    """Test case for rbac_permissions_roles_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/permissions/roles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_roles_update(client):
    """Test case for rbac_permissions_roles_update

    
    """
    body = {"object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/rbac/permissions/roles/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_users_destroy(client):
    """Test case for rbac_permissions_users_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/rbac/permissions/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_users_list(client):
    """Test case for rbac_permissions_users_list

    
    """
    params = [('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('user_id', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/permissions/users/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_users_partial_update(client):
    """Test case for rbac_permissions_users_partial_update

    
    """
    body = {"object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/rbac/permissions/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_users_retrieve(client):
    """Test case for rbac_permissions_users_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/permissions/users/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_permissions_users_update(client):
    """Test case for rbac_permissions_users_update

    
    """
    body = {"object_pk":"object_pk"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/rbac/permissions/users/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_roles_create(client):
    """Test case for rbac_roles_create

    
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/rbac/roles/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_roles_destroy(client):
    """Test case for rbac_roles_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/rbac/roles/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_roles_list(client):
    """Test case for rbac_roles_list

    
    """
    params = [('group__name', 'group__name_example'),
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
        path='/api/v3/rbac/roles/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_roles_partial_update(client):
    """Test case for rbac_roles_partial_update

    
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/rbac/roles/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_roles_retrieve(client):
    """Test case for rbac_roles_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/roles/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_roles_update(client):
    """Test case for rbac_roles_update

    
    """
    body = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/rbac/roles/{uuid}'.format(uuid='uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_rbac_roles_used_by_list(client):
    """Test case for rbac_roles_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/rbac/roles/{uuid}/used_by'.format(uuid='uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

