from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.connection_token import ConnectionToken
from authentik_openapi.models.connection_token_request import ConnectionTokenRequest
from authentik_openapi.models.endpoint import Endpoint
from authentik_openapi.models.endpoint_request import EndpointRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_connection_token_list import PaginatedConnectionTokenList
from authentik_openapi.models.paginated_endpoint_list import PaginatedEndpointList
from authentik_openapi.models.patched_connection_token_request import PatchedConnectionTokenRequest
from authentik_openapi.models.patched_endpoint_request import PatchedEndpointRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def rac_connection_tokens_destroy(request: web.Request, connection_token_uuid) -> web.Response:
    """rac_connection_tokens_destroy

    ConnectionToken Viewset

    :param connection_token_uuid: A UUID string identifying this RAC Connection token.
    :type connection_token_uuid: str
    :type connection_token_uuid: str

    """
    return web.Response(status=200)


async def rac_connection_tokens_list(request: web.Request, endpoint=None, ordering=None, page=None, page_size=None, provider=None, search=None, session__user=None) -> web.Response:
    """rac_connection_tokens_list

    ConnectionToken Viewset

    :param endpoint: 
    :type endpoint: str
    :type endpoint: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider: 
    :type provider: int
    :param search: A search term.
    :type search: str
    :param session__user: 
    :type session__user: int

    """
    return web.Response(status=200)


async def rac_connection_tokens_partial_update(request: web.Request, connection_token_uuid, body=None) -> web.Response:
    """rac_connection_tokens_partial_update

    ConnectionToken Viewset

    :param connection_token_uuid: A UUID string identifying this RAC Connection token.
    :type connection_token_uuid: str
    :type connection_token_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedConnectionTokenRequest.from_dict(body)
    return web.Response(status=200)


async def rac_connection_tokens_retrieve(request: web.Request, connection_token_uuid) -> web.Response:
    """rac_connection_tokens_retrieve

    ConnectionToken Viewset

    :param connection_token_uuid: A UUID string identifying this RAC Connection token.
    :type connection_token_uuid: str
    :type connection_token_uuid: str

    """
    return web.Response(status=200)


async def rac_connection_tokens_update(request: web.Request, connection_token_uuid, body) -> web.Response:
    """rac_connection_tokens_update

    ConnectionToken Viewset

    :param connection_token_uuid: A UUID string identifying this RAC Connection token.
    :type connection_token_uuid: str
    :type connection_token_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionTokenRequest.from_dict(body)
    return web.Response(status=200)


async def rac_connection_tokens_used_by_list(request: web.Request, connection_token_uuid) -> web.Response:
    """rac_connection_tokens_used_by_list

    Get a list of all objects that use this object

    :param connection_token_uuid: A UUID string identifying this RAC Connection token.
    :type connection_token_uuid: str
    :type connection_token_uuid: str

    """
    return web.Response(status=200)


async def rac_endpoints_create(request: web.Request, body) -> web.Response:
    """rac_endpoints_create

    Endpoint Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = EndpointRequest.from_dict(body)
    return web.Response(status=200)


async def rac_endpoints_destroy(request: web.Request, pbm_uuid) -> web.Response:
    """rac_endpoints_destroy

    Endpoint Viewset

    :param pbm_uuid: A UUID string identifying this RAC Endpoint.
    :type pbm_uuid: str
    :type pbm_uuid: str

    """
    return web.Response(status=200)


async def rac_endpoints_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, provider=None, search=None, superuser_full_list=None) -> web.Response:
    """rac_endpoints_list

    List accessible endpoints

    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider: 
    :type provider: int
    :param search: 
    :type search: str
    :param superuser_full_list: 
    :type superuser_full_list: bool

    """
    return web.Response(status=200)


async def rac_endpoints_partial_update(request: web.Request, pbm_uuid, body=None) -> web.Response:
    """rac_endpoints_partial_update

    Endpoint Viewset

    :param pbm_uuid: A UUID string identifying this RAC Endpoint.
    :type pbm_uuid: str
    :type pbm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedEndpointRequest.from_dict(body)
    return web.Response(status=200)


async def rac_endpoints_retrieve(request: web.Request, pbm_uuid) -> web.Response:
    """rac_endpoints_retrieve

    Endpoint Viewset

    :param pbm_uuid: A UUID string identifying this RAC Endpoint.
    :type pbm_uuid: str
    :type pbm_uuid: str

    """
    return web.Response(status=200)


async def rac_endpoints_update(request: web.Request, pbm_uuid, body) -> web.Response:
    """rac_endpoints_update

    Endpoint Viewset

    :param pbm_uuid: A UUID string identifying this RAC Endpoint.
    :type pbm_uuid: str
    :type pbm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = EndpointRequest.from_dict(body)
    return web.Response(status=200)


async def rac_endpoints_used_by_list(request: web.Request, pbm_uuid) -> web.Response:
    """rac_endpoints_used_by_list

    Get a list of all objects that use this object

    :param pbm_uuid: A UUID string identifying this RAC Endpoint.
    :type pbm_uuid: str
    :type pbm_uuid: str

    """
    return web.Response(status=200)
