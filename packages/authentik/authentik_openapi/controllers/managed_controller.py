from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.blueprint_file import BlueprintFile
from authentik_openapi.models.blueprint_instance import BlueprintInstance
from authentik_openapi.models.blueprint_instance_request import BlueprintInstanceRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_blueprint_instance_list import PaginatedBlueprintInstanceList
from authentik_openapi.models.patched_blueprint_instance_request import PatchedBlueprintInstanceRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def managed_blueprints_apply_create(request: web.Request, instance_uuid) -> web.Response:
    """managed_blueprints_apply_create

    Apply a blueprint

    :param instance_uuid: A UUID string identifying this Blueprint Instance.
    :type instance_uuid: str
    :type instance_uuid: str

    """
    return web.Response(status=200)


async def managed_blueprints_available_list(request: web.Request, ) -> web.Response:
    """managed_blueprints_available_list

    Get blueprints


    """
    return web.Response(status=200)


async def managed_blueprints_create(request: web.Request, body) -> web.Response:
    """managed_blueprints_create

    Blueprint instances

    :param body: 
    :type body: dict | bytes

    """
    body = BlueprintInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def managed_blueprints_destroy(request: web.Request, instance_uuid) -> web.Response:
    """managed_blueprints_destroy

    Blueprint instances

    :param instance_uuid: A UUID string identifying this Blueprint Instance.
    :type instance_uuid: str
    :type instance_uuid: str

    """
    return web.Response(status=200)


async def managed_blueprints_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, path=None, search=None) -> web.Response:
    """managed_blueprints_list

    Blueprint instances

    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param path: 
    :type path: str
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def managed_blueprints_partial_update(request: web.Request, instance_uuid, body=None) -> web.Response:
    """managed_blueprints_partial_update

    Blueprint instances

    :param instance_uuid: A UUID string identifying this Blueprint Instance.
    :type instance_uuid: str
    :type instance_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedBlueprintInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def managed_blueprints_retrieve(request: web.Request, instance_uuid) -> web.Response:
    """managed_blueprints_retrieve

    Blueprint instances

    :param instance_uuid: A UUID string identifying this Blueprint Instance.
    :type instance_uuid: str
    :type instance_uuid: str

    """
    return web.Response(status=200)


async def managed_blueprints_update(request: web.Request, instance_uuid, body) -> web.Response:
    """managed_blueprints_update

    Blueprint instances

    :param instance_uuid: A UUID string identifying this Blueprint Instance.
    :type instance_uuid: str
    :type instance_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = BlueprintInstanceRequest.from_dict(body)
    return web.Response(status=200)


async def managed_blueprints_used_by_list(request: web.Request, instance_uuid) -> web.Response:
    """managed_blueprints_used_by_list

    Get a list of all objects that use this object

    :param instance_uuid: A UUID string identifying this Blueprint Instance.
    :type instance_uuid: str
    :type instance_uuid: str

    """
    return web.Response(status=200)
