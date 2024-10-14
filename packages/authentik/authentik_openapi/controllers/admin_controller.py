from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.app import App
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.login_metrics import LoginMetrics
from authentik_openapi.models.patched_settings_request import PatchedSettingsRequest
from authentik_openapi.models.settings import Settings
from authentik_openapi.models.settings_request import SettingsRequest
from authentik_openapi.models.system_info import SystemInfo
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi.models.version import Version
from authentik_openapi.models.workers import Workers
from authentik_openapi import util


async def admin_apps_list(request: web.Request, ) -> web.Response:
    """admin_apps_list

    Read-only view list all installed apps


    """
    return web.Response(status=200)


async def admin_metrics_retrieve(request: web.Request, ) -> web.Response:
    """admin_metrics_retrieve

    Login Metrics per 1h


    """
    return web.Response(status=200)


async def admin_models_list(request: web.Request, ) -> web.Response:
    """admin_models_list

    Read-only view list all installed models


    """
    return web.Response(status=200)


async def admin_settings_partial_update(request: web.Request, body=None) -> web.Response:
    """admin_settings_partial_update

    Settings view

    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSettingsRequest.from_dict(body)
    return web.Response(status=200)


async def admin_settings_retrieve(request: web.Request, ) -> web.Response:
    """admin_settings_retrieve

    Settings view


    """
    return web.Response(status=200)


async def admin_settings_update(request: web.Request, body=None) -> web.Response:
    """admin_settings_update

    Settings view

    :param body: 
    :type body: dict | bytes

    """
    body = SettingsRequest.from_dict(body)
    return web.Response(status=200)


async def admin_system_create(request: web.Request, ) -> web.Response:
    """admin_system_create

    Get system information.


    """
    return web.Response(status=200)


async def admin_system_retrieve(request: web.Request, ) -> web.Response:
    """admin_system_retrieve

    Get system information.


    """
    return web.Response(status=200)


async def admin_version_retrieve(request: web.Request, ) -> web.Response:
    """admin_version_retrieve

    Get running and latest version.


    """
    return web.Response(status=200)


async def admin_workers_retrieve(request: web.Request, ) -> web.Response:
    """admin_workers_retrieve

    Get currently connected worker count.


    """
    return web.Response(status=200)
