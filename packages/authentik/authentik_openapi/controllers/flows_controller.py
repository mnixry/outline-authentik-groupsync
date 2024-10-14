from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.cache import Cache
from authentik_openapi.models.challenge_types import ChallengeTypes
from authentik_openapi.models.file_path_request import FilePathRequest
from authentik_openapi.models.flow import Flow
from authentik_openapi.models.flow_challenge_response_request import FlowChallengeResponseRequest
from authentik_openapi.models.flow_diagram import FlowDiagram
from authentik_openapi.models.flow_import_result import FlowImportResult
from authentik_openapi.models.flow_inspection import FlowInspection
from authentik_openapi.models.flow_request import FlowRequest
from authentik_openapi.models.flow_stage_binding import FlowStageBinding
from authentik_openapi.models.flow_stage_binding_request import FlowStageBindingRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.link import Link
from authentik_openapi.models.paginated_flow_list import PaginatedFlowList
from authentik_openapi.models.paginated_flow_stage_binding_list import PaginatedFlowStageBindingList
from authentik_openapi.models.patched_flow_request import PatchedFlowRequest
from authentik_openapi.models.patched_flow_stage_binding_request import PatchedFlowStageBindingRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def flows_bindings_create(request: web.Request, body) -> web.Response:
    """flows_bindings_create

    FlowStageBinding Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = FlowStageBindingRequest.from_dict(body)
    return web.Response(status=200)


async def flows_bindings_destroy(request: web.Request, fsb_uuid) -> web.Response:
    """flows_bindings_destroy

    FlowStageBinding Viewset

    :param fsb_uuid: A UUID string identifying this Flow Stage Binding.
    :type fsb_uuid: str
    :type fsb_uuid: str

    """
    return web.Response(status=200)


async def flows_bindings_list(request: web.Request, evaluate_on_plan=None, fsb_uuid=None, invalid_response_action=None, order=None, ordering=None, page=None, page_size=None, pbm_uuid=None, policies=None, policy_engine_mode=None, re_evaluate_policies=None, search=None, stage=None, target=None) -> web.Response:
    """flows_bindings_list

    FlowStageBinding Viewset

    :param evaluate_on_plan: 
    :type evaluate_on_plan: bool
    :param fsb_uuid: 
    :type fsb_uuid: str
    :type fsb_uuid: str
    :param invalid_response_action: Configure how the flow executor should handle an invalid response to a challenge. RETRY returns the error message and a similar challenge to the executor. RESTART restarts the flow from the beginning, and RESTART_WITH_CONTEXT restarts the flow while keeping the current context.  
    :type invalid_response_action: str
    :param order: 
    :type order: int
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param pbm_uuid: 
    :type pbm_uuid: str
    :type pbm_uuid: str
    :param policies: 
    :type policies: List[str]
    :param policy_engine_mode: 
    :type policy_engine_mode: str
    :param re_evaluate_policies: 
    :type re_evaluate_policies: bool
    :param search: A search term.
    :type search: str
    :param stage: 
    :type stage: str
    :type stage: str
    :param target: 
    :type target: str
    :type target: str

    """
    return web.Response(status=200)


async def flows_bindings_partial_update(request: web.Request, fsb_uuid, body=None) -> web.Response:
    """flows_bindings_partial_update

    FlowStageBinding Viewset

    :param fsb_uuid: A UUID string identifying this Flow Stage Binding.
    :type fsb_uuid: str
    :type fsb_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedFlowStageBindingRequest.from_dict(body)
    return web.Response(status=200)


async def flows_bindings_retrieve(request: web.Request, fsb_uuid) -> web.Response:
    """flows_bindings_retrieve

    FlowStageBinding Viewset

    :param fsb_uuid: A UUID string identifying this Flow Stage Binding.
    :type fsb_uuid: str
    :type fsb_uuid: str

    """
    return web.Response(status=200)


async def flows_bindings_update(request: web.Request, fsb_uuid, body) -> web.Response:
    """flows_bindings_update

    FlowStageBinding Viewset

    :param fsb_uuid: A UUID string identifying this Flow Stage Binding.
    :type fsb_uuid: str
    :type fsb_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = FlowStageBindingRequest.from_dict(body)
    return web.Response(status=200)


async def flows_bindings_used_by_list(request: web.Request, fsb_uuid) -> web.Response:
    """flows_bindings_used_by_list

    Get a list of all objects that use this object

    :param fsb_uuid: A UUID string identifying this Flow Stage Binding.
    :type fsb_uuid: str
    :type fsb_uuid: str

    """
    return web.Response(status=200)


async def flows_executor_get(request: web.Request, flow_slug, query) -> web.Response:
    """flows_executor_get

    Get the next pending challenge from the currently active flow.

    :param flow_slug: 
    :type flow_slug: str
    :param query: Querystring as received
    :type query: str

    """
    return web.Response(status=200)


async def flows_executor_solve(request: web.Request, flow_slug, query, body=None) -> web.Response:
    """flows_executor_solve

    Solve the previously retrieved challenge and advanced to the next stage.

    :param flow_slug: 
    :type flow_slug: str
    :param query: Querystring as received
    :type query: str
    :param body: 
    :type body: dict | bytes

    """
    body = FlowChallengeResponseRequest.from_dict(body)
    return web.Response(status=200)


async def flows_inspector_get(request: web.Request, flow_slug) -> web.Response:
    """flows_inspector_get

    Get current flow state and record it

    :param flow_slug: 
    :type flow_slug: str

    """
    return web.Response(status=200)


async def flows_instances_cache_clear_create(request: web.Request, ) -> web.Response:
    """flows_instances_cache_clear_create

    Clear flow cache


    """
    return web.Response(status=200)


async def flows_instances_cache_info_retrieve(request: web.Request, ) -> web.Response:
    """flows_instances_cache_info_retrieve

    Info about cached flows


    """
    return web.Response(status=200)


async def flows_instances_create(request: web.Request, body) -> web.Response:
    """flows_instances_create

    Flow Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = FlowRequest.from_dict(body)
    return web.Response(status=200)


async def flows_instances_destroy(request: web.Request, slug) -> web.Response:
    """flows_instances_destroy

    Flow Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def flows_instances_diagram_retrieve(request: web.Request, slug) -> web.Response:
    """flows_instances_diagram_retrieve

    Return diagram for flow with slug &#x60;slug&#x60;, in the format used by flowchart.js

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def flows_instances_execute_retrieve(request: web.Request, slug) -> web.Response:
    """flows_instances_execute_retrieve

    Execute flow for current user

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def flows_instances_export_retrieve(request: web.Request, slug) -> web.Response:
    """flows_instances_export_retrieve

    Export flow to .yaml file

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def flows_instances_import_create(request: web.Request, file=None, clear=None) -> web.Response:
    """flows_instances_import_create

    Import flow from .yaml file

    :param file: 
    :type file: str
    :param clear: 
    :type clear: bool

    """
    return web.Response(status=200)


async def flows_instances_list(request: web.Request, denied_action=None, designation=None, flow_uuid=None, name=None, ordering=None, page=None, page_size=None, search=None, slug=None) -> web.Response:
    """flows_instances_list

    Flow Viewset

    :param denied_action: Configure what should happen when a flow denies access to a user.  
    :type denied_action: str
    :param designation: Decides what this Flow is used for. For example, the Authentication flow is redirect to when an un-authenticated user visits authentik.  
    :type designation: str
    :param flow_uuid: 
    :type flow_uuid: str
    :type flow_uuid: str
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
    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def flows_instances_partial_update(request: web.Request, slug, body=None) -> web.Response:
    """flows_instances_partial_update

    Flow Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedFlowRequest.from_dict(body)
    return web.Response(status=200)


async def flows_instances_retrieve(request: web.Request, slug) -> web.Response:
    """flows_instances_retrieve

    Flow Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def flows_instances_set_background_create(request: web.Request, slug, file=None, clear=None) -> web.Response:
    """flows_instances_set_background_create

    Set Flow background

    :param slug: 
    :type slug: str
    :param file: 
    :type file: str
    :param clear: 
    :type clear: bool

    """
    return web.Response(status=200)


async def flows_instances_set_background_url_create(request: web.Request, slug, body) -> web.Response:
    """flows_instances_set_background_url_create

    Set Flow background (as URL)

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = FilePathRequest.from_dict(body)
    return web.Response(status=200)


async def flows_instances_update(request: web.Request, slug, body) -> web.Response:
    """flows_instances_update

    Flow Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = FlowRequest.from_dict(body)
    return web.Response(status=200)


async def flows_instances_used_by_list(request: web.Request, slug) -> web.Response:
    """flows_instances_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)
