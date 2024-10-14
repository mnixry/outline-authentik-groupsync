from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def schema_retrieve(request: web.Request, format=None, lang=None) -> web.Response:
    """schema_retrieve

    OpenApi3 schema for this API. Format can be selected via content negotiation.  - YAML: application/vnd.oai.openapi - JSON: application/vnd.oai.openapi+json

    :param format: 
    :type format: str
    :param lang: 
    :type lang: str

    """
    return web.Response(status=200)
