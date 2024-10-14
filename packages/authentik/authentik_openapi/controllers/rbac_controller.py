from typing import List, Dict
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
from authentik_openapi import util


async def rbac_permissions_assigned_by_roles_assign(request: web.Request, uuid, body) -> web.Response:
    """rbac_permissions_assigned_by_roles_assign

    Assign permission(s) to role. When &#x60;object_pk&#x60; is set, the permissions are only assigned to the specific object, otherwise they are assigned globally.

    :param uuid: A UUID string identifying this Role.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PermissionAssignRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_permissions_assigned_by_roles_list(request: web.Request, model, object_pk=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """rbac_permissions_assigned_by_roles_list

    Get assigned object permissions for a single object

    :param model: 
    :type model: str
    :param object_pk: 
    :type object_pk: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def rbac_permissions_assigned_by_roles_unassign_partial_update(request: web.Request, uuid, body=None) -> web.Response:
    """rbac_permissions_assigned_by_roles_unassign_partial_update

    Unassign permission(s) to role. When &#x60;object_pk&#x60; is set, the permissions are only assigned to the specific object, otherwise they are assigned globally.

    :param uuid: A UUID string identifying this Role.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPermissionAssignRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_permissions_assigned_by_users_assign(request: web.Request, id, body) -> web.Response:
    """rbac_permissions_assigned_by_users_assign

    Assign permission(s) to user

    :param id: A unique integer value identifying this User.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PermissionAssignRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_permissions_assigned_by_users_list(request: web.Request, model, object_pk=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """rbac_permissions_assigned_by_users_list

    Get assigned object permissions for a single object

    :param model: 
    :type model: str
    :param object_pk: 
    :type object_pk: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def rbac_permissions_assigned_by_users_unassign_partial_update(request: web.Request, id, body=None) -> web.Response:
    """rbac_permissions_assigned_by_users_unassign_partial_update

    Unassign permission(s) to user. When &#x60;object_pk&#x60; is set, the permissions are only assigned to the specific object, otherwise they are assigned globally.

    :param id: A unique integer value identifying this User.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPermissionAssignRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_permissions_list(request: web.Request, codename=None, content_type__app_label=None, content_type__model=None, ordering=None, page=None, page_size=None, role=None, search=None, user=None) -> web.Response:
    """rbac_permissions_list

    Read-only list of all permissions, filterable by model and app

    :param codename: 
    :type codename: str
    :param content_type__app_label: 
    :type content_type__app_label: str
    :param content_type__model: 
    :type content_type__model: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param role: 
    :type role: str
    :param search: A search term.
    :type search: str
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def rbac_permissions_retrieve(request: web.Request, id) -> web.Response:
    """rbac_permissions_retrieve

    Read-only list of all permissions, filterable by model and app

    :param id: A unique integer value identifying this permission.
    :type id: int

    """
    return web.Response(status=200)


async def rbac_permissions_roles_destroy(request: web.Request, id) -> web.Response:
    """rbac_permissions_roles_destroy

    Get a role&#39;s assigned object permissions

    :param id: A unique integer value identifying this group object permission.
    :type id: int

    """
    return web.Response(status=200)


async def rbac_permissions_roles_list(request: web.Request, ordering=None, page=None, page_size=None, search=None, uuid=None) -> web.Response:
    """rbac_permissions_roles_list

    Get a role&#39;s assigned object permissions

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param uuid: 
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def rbac_permissions_roles_partial_update(request: web.Request, id, body=None) -> web.Response:
    """rbac_permissions_roles_partial_update

    Get a role&#39;s assigned object permissions

    :param id: A unique integer value identifying this group object permission.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedExtraRoleObjectPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_permissions_roles_retrieve(request: web.Request, id) -> web.Response:
    """rbac_permissions_roles_retrieve

    Get a role&#39;s assigned object permissions

    :param id: A unique integer value identifying this group object permission.
    :type id: int

    """
    return web.Response(status=200)


async def rbac_permissions_roles_update(request: web.Request, id, body) -> web.Response:
    """rbac_permissions_roles_update

    Get a role&#39;s assigned object permissions

    :param id: A unique integer value identifying this group object permission.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ExtraRoleObjectPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_permissions_users_destroy(request: web.Request, id) -> web.Response:
    """rbac_permissions_users_destroy

    Get a users&#39;s assigned object permissions

    :param id: A unique integer value identifying this user object permission.
    :type id: int

    """
    return web.Response(status=200)


async def rbac_permissions_users_list(request: web.Request, ordering=None, page=None, page_size=None, search=None, user_id=None) -> web.Response:
    """rbac_permissions_users_list

    Get a users&#39;s assigned object permissions

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param user_id: 
    :type user_id: int

    """
    return web.Response(status=200)


async def rbac_permissions_users_partial_update(request: web.Request, id, body=None) -> web.Response:
    """rbac_permissions_users_partial_update

    Get a users&#39;s assigned object permissions

    :param id: A unique integer value identifying this user object permission.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedExtraUserObjectPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_permissions_users_retrieve(request: web.Request, id) -> web.Response:
    """rbac_permissions_users_retrieve

    Get a users&#39;s assigned object permissions

    :param id: A unique integer value identifying this user object permission.
    :type id: int

    """
    return web.Response(status=200)


async def rbac_permissions_users_update(request: web.Request, id, body) -> web.Response:
    """rbac_permissions_users_update

    Get a users&#39;s assigned object permissions

    :param id: A unique integer value identifying this user object permission.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ExtraUserObjectPermissionRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_roles_create(request: web.Request, body) -> web.Response:
    """rbac_roles_create

    Role viewset

    :param body: 
    :type body: dict | bytes

    """
    body = RoleRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_roles_destroy(request: web.Request, uuid) -> web.Response:
    """rbac_roles_destroy

    Role viewset

    :param uuid: A UUID string identifying this Role.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def rbac_roles_list(request: web.Request, group__name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """rbac_roles_list

    Role viewset

    :param group__name: 
    :type group__name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def rbac_roles_partial_update(request: web.Request, uuid, body=None) -> web.Response:
    """rbac_roles_partial_update

    Role viewset

    :param uuid: A UUID string identifying this Role.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedRoleRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_roles_retrieve(request: web.Request, uuid) -> web.Response:
    """rbac_roles_retrieve

    Role viewset

    :param uuid: A UUID string identifying this Role.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def rbac_roles_update(request: web.Request, uuid, body) -> web.Response:
    """rbac_roles_update

    Role viewset

    :param uuid: A UUID string identifying this Role.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = RoleRequest.from_dict(body)
    return web.Response(status=200)


async def rbac_roles_used_by_list(request: web.Request, uuid) -> web.Response:
    """rbac_roles_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Role.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)
