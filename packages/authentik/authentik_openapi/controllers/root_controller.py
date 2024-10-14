from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.config import Config
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def root_config_retrieve(request: web.Request, ) -> web.Response:
    """root_config_retrieve

    Retrieve public configuration options


    """
    return web.Response(status=200)
