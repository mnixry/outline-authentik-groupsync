from typing import List, Dict
from aiohttp import web

from outline_openapi.models.auth_config_post200_response import AuthConfigPost200Response
from outline_openapi.models.auth_info_post200_response import AuthInfoPost200Response
from outline_openapi.models.error import Error
from outline_openapi import util


async def auth_config_post(request: web.Request, ) -> web.Response:
    """Retrieve auth config

    Retrieve authentication options


    """
    return web.Response(status=200)


async def auth_info_post(request: web.Request, ) -> web.Response:
    """Retrieve auth

    Retrieve authentication details for the current API key


    """
    return web.Response(status=200)
