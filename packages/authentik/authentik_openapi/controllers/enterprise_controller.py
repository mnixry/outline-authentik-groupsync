from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.install_id import InstallID
from authentik_openapi.models.license import License
from authentik_openapi.models.license_forecast import LicenseForecast
from authentik_openapi.models.license_request import LicenseRequest
from authentik_openapi.models.license_summary import LicenseSummary
from authentik_openapi.models.paginated_license_list import PaginatedLicenseList
from authentik_openapi.models.patched_license_request import PatchedLicenseRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def enterprise_license_create(request: web.Request, body) -> web.Response:
    """enterprise_license_create

    License Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = LicenseRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_license_destroy(request: web.Request, license_uuid) -> web.Response:
    """enterprise_license_destroy

    License Viewset

    :param license_uuid: A UUID string identifying this License.
    :type license_uuid: str
    :type license_uuid: str

    """
    return web.Response(status=200)


async def enterprise_license_forecast_retrieve(request: web.Request, ) -> web.Response:
    """enterprise_license_forecast_retrieve

    Forecast how many users will be required in a year


    """
    return web.Response(status=200)


async def enterprise_license_install_id_retrieve(request: web.Request, ) -> web.Response:
    """enterprise_license_install_id_retrieve

    Get install_id


    """
    return web.Response(status=200)


async def enterprise_license_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """enterprise_license_list

    License Viewset

    :param name: 
    :type name: str
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


async def enterprise_license_partial_update(request: web.Request, license_uuid, body=None) -> web.Response:
    """enterprise_license_partial_update

    License Viewset

    :param license_uuid: A UUID string identifying this License.
    :type license_uuid: str
    :type license_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedLicenseRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_license_retrieve(request: web.Request, license_uuid) -> web.Response:
    """enterprise_license_retrieve

    License Viewset

    :param license_uuid: A UUID string identifying this License.
    :type license_uuid: str
    :type license_uuid: str

    """
    return web.Response(status=200)


async def enterprise_license_summary_retrieve(request: web.Request, cached=None) -> web.Response:
    """enterprise_license_summary_retrieve

    Get the total license status

    :param cached: 
    :type cached: bool

    """
    return web.Response(status=200)


async def enterprise_license_update(request: web.Request, license_uuid, body) -> web.Response:
    """enterprise_license_update

    License Viewset

    :param license_uuid: A UUID string identifying this License.
    :type license_uuid: str
    :type license_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = LicenseRequest.from_dict(body)
    return web.Response(status=200)


async def enterprise_license_used_by_list(request: web.Request, license_uuid) -> web.Response:
    """enterprise_license_used_by_list

    Get a list of all objects that use this object

    :param license_uuid: A UUID string identifying this License.
    :type license_uuid: str
    :type license_uuid: str

    """
    return web.Response(status=200)
