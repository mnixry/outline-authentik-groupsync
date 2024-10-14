from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.expiring_base_grant_model import ExpiringBaseGrantModel
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_expiring_base_grant_model_list import PaginatedExpiringBaseGrantModelList
from authentik_openapi.models.paginated_token_model_list import PaginatedTokenModelList
from authentik_openapi.models.token_model import TokenModel
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def oauth2_access_tokens_destroy(request: web.Request, id) -> web.Response:
    """oauth2_access_tokens_destroy

    AccessToken Viewset

    :param id: A unique integer value identifying this OAuth2 Access Token.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_access_tokens_list(request: web.Request, ordering=None, page=None, page_size=None, provider=None, search=None, user=None) -> web.Response:
    """oauth2_access_tokens_list

    AccessToken Viewset

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
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def oauth2_access_tokens_retrieve(request: web.Request, id) -> web.Response:
    """oauth2_access_tokens_retrieve

    AccessToken Viewset

    :param id: A unique integer value identifying this OAuth2 Access Token.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_access_tokens_used_by_list(request: web.Request, id) -> web.Response:
    """oauth2_access_tokens_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this OAuth2 Access Token.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_authorization_codes_destroy(request: web.Request, id) -> web.Response:
    """oauth2_authorization_codes_destroy

    AuthorizationCode Viewset

    :param id: A unique integer value identifying this Authorization Code.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_authorization_codes_list(request: web.Request, ordering=None, page=None, page_size=None, provider=None, search=None, user=None) -> web.Response:
    """oauth2_authorization_codes_list

    AuthorizationCode Viewset

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
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def oauth2_authorization_codes_retrieve(request: web.Request, id) -> web.Response:
    """oauth2_authorization_codes_retrieve

    AuthorizationCode Viewset

    :param id: A unique integer value identifying this Authorization Code.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_authorization_codes_used_by_list(request: web.Request, id) -> web.Response:
    """oauth2_authorization_codes_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Authorization Code.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_refresh_tokens_destroy(request: web.Request, id) -> web.Response:
    """oauth2_refresh_tokens_destroy

    RefreshToken Viewset

    :param id: A unique integer value identifying this OAuth2 Refresh Token.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_refresh_tokens_list(request: web.Request, ordering=None, page=None, page_size=None, provider=None, search=None, user=None) -> web.Response:
    """oauth2_refresh_tokens_list

    RefreshToken Viewset

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
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def oauth2_refresh_tokens_retrieve(request: web.Request, id) -> web.Response:
    """oauth2_refresh_tokens_retrieve

    RefreshToken Viewset

    :param id: A unique integer value identifying this OAuth2 Refresh Token.
    :type id: int

    """
    return web.Response(status=200)


async def oauth2_refresh_tokens_used_by_list(request: web.Request, id) -> web.Response:
    """oauth2_refresh_tokens_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this OAuth2 Refresh Token.
    :type id: int

    """
    return web.Response(status=200)
