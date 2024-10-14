from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.cache import Cache
from authentik_openapi.models.detailed_country import DetailedCountry
from authentik_openapi.models.dummy_policy import DummyPolicy
from authentik_openapi.models.dummy_policy_request import DummyPolicyRequest
from authentik_openapi.models.event_matcher_policy import EventMatcherPolicy
from authentik_openapi.models.event_matcher_policy_request import EventMatcherPolicyRequest
from authentik_openapi.models.expression_policy import ExpressionPolicy
from authentik_openapi.models.expression_policy_request import ExpressionPolicyRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.geo_ip_policy import GeoIPPolicy
from authentik_openapi.models.geo_ip_policy_request import GeoIPPolicyRequest
from authentik_openapi.models.paginated_dummy_policy_list import PaginatedDummyPolicyList
from authentik_openapi.models.paginated_event_matcher_policy_list import PaginatedEventMatcherPolicyList
from authentik_openapi.models.paginated_expression_policy_list import PaginatedExpressionPolicyList
from authentik_openapi.models.paginated_geo_ip_policy_list import PaginatedGeoIPPolicyList
from authentik_openapi.models.paginated_password_expiry_policy_list import PaginatedPasswordExpiryPolicyList
from authentik_openapi.models.paginated_password_policy_list import PaginatedPasswordPolicyList
from authentik_openapi.models.paginated_policy_binding_list import PaginatedPolicyBindingList
from authentik_openapi.models.paginated_policy_list import PaginatedPolicyList
from authentik_openapi.models.paginated_reputation_list import PaginatedReputationList
from authentik_openapi.models.paginated_reputation_policy_list import PaginatedReputationPolicyList
from authentik_openapi.models.password_expiry_policy import PasswordExpiryPolicy
from authentik_openapi.models.password_expiry_policy_request import PasswordExpiryPolicyRequest
from authentik_openapi.models.password_policy import PasswordPolicy
from authentik_openapi.models.password_policy_request import PasswordPolicyRequest
from authentik_openapi.models.patched_dummy_policy_request import PatchedDummyPolicyRequest
from authentik_openapi.models.patched_event_matcher_policy_request import PatchedEventMatcherPolicyRequest
from authentik_openapi.models.patched_expression_policy_request import PatchedExpressionPolicyRequest
from authentik_openapi.models.patched_geo_ip_policy_request import PatchedGeoIPPolicyRequest
from authentik_openapi.models.patched_password_expiry_policy_request import PatchedPasswordExpiryPolicyRequest
from authentik_openapi.models.patched_password_policy_request import PatchedPasswordPolicyRequest
from authentik_openapi.models.patched_policy_binding_request import PatchedPolicyBindingRequest
from authentik_openapi.models.patched_reputation_policy_request import PatchedReputationPolicyRequest
from authentik_openapi.models.policy import Policy
from authentik_openapi.models.policy_binding import PolicyBinding
from authentik_openapi.models.policy_binding_request import PolicyBindingRequest
from authentik_openapi.models.policy_test_request import PolicyTestRequest
from authentik_openapi.models.policy_test_result import PolicyTestResult
from authentik_openapi.models.reputation import Reputation
from authentik_openapi.models.reputation_policy import ReputationPolicy
from authentik_openapi.models.reputation_policy_request import ReputationPolicyRequest
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def policies_all_cache_clear_create(request: web.Request, ) -> web.Response:
    """policies_all_cache_clear_create

    Clear policy cache


    """
    return web.Response(status=200)


async def policies_all_cache_info_retrieve(request: web.Request, ) -> web.Response:
    """policies_all_cache_info_retrieve

    Info about cached policies


    """
    return web.Response(status=200)


async def policies_all_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_all_destroy

    Policy Viewset

    :param policy_uuid: A UUID string identifying this Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_all_list(request: web.Request, bindings__isnull=None, ordering=None, page=None, page_size=None, promptstage__isnull=None, search=None) -> web.Response:
    """policies_all_list

    Policy Viewset

    :param bindings__isnull: 
    :type bindings__isnull: bool
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param promptstage__isnull: 
    :type promptstage__isnull: bool
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def policies_all_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_all_retrieve

    Policy Viewset

    :param policy_uuid: A UUID string identifying this Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_all_test_create(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_all_test_create

    Test policy

    :param policy_uuid: A UUID string identifying this Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PolicyTestRequest.from_dict(body)
    return web.Response(status=200)


async def policies_all_types_list(request: web.Request, ) -> web.Response:
    """policies_all_types_list

    Get all creatable types


    """
    return web.Response(status=200)


async def policies_all_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_all_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_bindings_create(request: web.Request, body) -> web.Response:
    """policies_bindings_create

    PolicyBinding Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PolicyBindingRequest.from_dict(body)
    return web.Response(status=200)


async def policies_bindings_destroy(request: web.Request, policy_binding_uuid) -> web.Response:
    """policies_bindings_destroy

    PolicyBinding Viewset

    :param policy_binding_uuid: A UUID string identifying this Policy Binding.
    :type policy_binding_uuid: str
    :type policy_binding_uuid: str

    """
    return web.Response(status=200)


async def policies_bindings_list(request: web.Request, enabled=None, order=None, ordering=None, page=None, page_size=None, policy=None, policy__isnull=None, search=None, target=None, target_in=None, timeout=None) -> web.Response:
    """policies_bindings_list

    PolicyBinding Viewset

    :param enabled: 
    :type enabled: bool
    :param order: 
    :type order: int
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy: 
    :type policy: str
    :type policy: str
    :param policy__isnull: 
    :type policy__isnull: bool
    :param search: A search term.
    :type search: str
    :param target: 
    :type target: str
    :type target: str
    :param target_in: 
    :type target_in: List[str]
    :param timeout: 
    :type timeout: int

    """
    return web.Response(status=200)


async def policies_bindings_partial_update(request: web.Request, policy_binding_uuid, body=None) -> web.Response:
    """policies_bindings_partial_update

    PolicyBinding Viewset

    :param policy_binding_uuid: A UUID string identifying this Policy Binding.
    :type policy_binding_uuid: str
    :type policy_binding_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPolicyBindingRequest.from_dict(body)
    return web.Response(status=200)


async def policies_bindings_retrieve(request: web.Request, policy_binding_uuid) -> web.Response:
    """policies_bindings_retrieve

    PolicyBinding Viewset

    :param policy_binding_uuid: A UUID string identifying this Policy Binding.
    :type policy_binding_uuid: str
    :type policy_binding_uuid: str

    """
    return web.Response(status=200)


async def policies_bindings_update(request: web.Request, policy_binding_uuid, body) -> web.Response:
    """policies_bindings_update

    PolicyBinding Viewset

    :param policy_binding_uuid: A UUID string identifying this Policy Binding.
    :type policy_binding_uuid: str
    :type policy_binding_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PolicyBindingRequest.from_dict(body)
    return web.Response(status=200)


async def policies_bindings_used_by_list(request: web.Request, policy_binding_uuid) -> web.Response:
    """policies_bindings_used_by_list

    Get a list of all objects that use this object

    :param policy_binding_uuid: A UUID string identifying this Policy Binding.
    :type policy_binding_uuid: str
    :type policy_binding_uuid: str

    """
    return web.Response(status=200)


async def policies_dummy_create(request: web.Request, body) -> web.Response:
    """policies_dummy_create

    Dummy Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = DummyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_dummy_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_dummy_destroy

    Dummy Viewset

    :param policy_uuid: A UUID string identifying this Dummy Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_dummy_list(request: web.Request, created=None, execution_logging=None, last_updated=None, name=None, ordering=None, page=None, page_size=None, policy_uuid=None, result=None, search=None, wait_max=None, wait_min=None) -> web.Response:
    """policies_dummy_list

    Dummy Viewset

    :param created: 
    :type created: str
    :param execution_logging: 
    :type execution_logging: bool
    :param last_updated: 
    :type last_updated: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_uuid: 
    :type policy_uuid: str
    :type policy_uuid: str
    :param result: 
    :type result: bool
    :param search: A search term.
    :type search: str
    :param wait_max: 
    :type wait_max: int
    :param wait_min: 
    :type wait_min: int

    """
    created = util.deserialize_datetime(created)
    last_updated = util.deserialize_datetime(last_updated)
    return web.Response(status=200)


async def policies_dummy_partial_update(request: web.Request, policy_uuid, body=None) -> web.Response:
    """policies_dummy_partial_update

    Dummy Viewset

    :param policy_uuid: A UUID string identifying this Dummy Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedDummyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_dummy_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_dummy_retrieve

    Dummy Viewset

    :param policy_uuid: A UUID string identifying this Dummy Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_dummy_update(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_dummy_update

    Dummy Viewset

    :param policy_uuid: A UUID string identifying this Dummy Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = DummyPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_dummy_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_dummy_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this Dummy Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_event_matcher_create(request: web.Request, body) -> web.Response:
    """policies_event_matcher_create

    Event Matcher Policy Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = EventMatcherPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_event_matcher_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_event_matcher_destroy

    Event Matcher Policy Viewset

    :param policy_uuid: A UUID string identifying this Event Matcher Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_event_matcher_list(request: web.Request, action=None, app=None, client_ip=None, created=None, execution_logging=None, last_updated=None, model=None, name=None, ordering=None, page=None, page_size=None, policy_uuid=None, search=None) -> web.Response:
    """policies_event_matcher_list

    Event Matcher Policy Viewset

    :param action: Match created events with this action type. When left empty, all action types will be matched.  
    :type action: str
    :param app: 
    :type app: str
    :param client_ip: 
    :type client_ip: str
    :param created: 
    :type created: str
    :param execution_logging: 
    :type execution_logging: bool
    :param last_updated: 
    :type last_updated: str
    :param model: 
    :type model: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_uuid: 
    :type policy_uuid: str
    :type policy_uuid: str
    :param search: A search term.
    :type search: str

    """
    created = util.deserialize_datetime(created)
    last_updated = util.deserialize_datetime(last_updated)
    return web.Response(status=200)


async def policies_event_matcher_partial_update(request: web.Request, policy_uuid, body=None) -> web.Response:
    """policies_event_matcher_partial_update

    Event Matcher Policy Viewset

    :param policy_uuid: A UUID string identifying this Event Matcher Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedEventMatcherPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_event_matcher_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_event_matcher_retrieve

    Event Matcher Policy Viewset

    :param policy_uuid: A UUID string identifying this Event Matcher Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_event_matcher_update(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_event_matcher_update

    Event Matcher Policy Viewset

    :param policy_uuid: A UUID string identifying this Event Matcher Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = EventMatcherPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_event_matcher_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_event_matcher_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this Event Matcher Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_expression_create(request: web.Request, body) -> web.Response:
    """policies_expression_create

    Source Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = ExpressionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_expression_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_expression_destroy

    Source Viewset

    :param policy_uuid: A UUID string identifying this Expression Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_expression_list(request: web.Request, created=None, execution_logging=None, expression=None, last_updated=None, name=None, ordering=None, page=None, page_size=None, policy_uuid=None, search=None) -> web.Response:
    """policies_expression_list

    Source Viewset

    :param created: 
    :type created: str
    :param execution_logging: 
    :type execution_logging: bool
    :param expression: 
    :type expression: str
    :param last_updated: 
    :type last_updated: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_uuid: 
    :type policy_uuid: str
    :type policy_uuid: str
    :param search: A search term.
    :type search: str

    """
    created = util.deserialize_datetime(created)
    last_updated = util.deserialize_datetime(last_updated)
    return web.Response(status=200)


async def policies_expression_partial_update(request: web.Request, policy_uuid, body=None) -> web.Response:
    """policies_expression_partial_update

    Source Viewset

    :param policy_uuid: A UUID string identifying this Expression Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedExpressionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_expression_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_expression_retrieve

    Source Viewset

    :param policy_uuid: A UUID string identifying this Expression Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_expression_update(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_expression_update

    Source Viewset

    :param policy_uuid: A UUID string identifying this Expression Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = ExpressionPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_expression_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_expression_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this Expression Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_geoip_create(request: web.Request, body) -> web.Response:
    """policies_geoip_create

    GeoIP Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = GeoIPPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_geoip_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_geoip_destroy

    GeoIP Viewset

    :param policy_uuid: A UUID string identifying this GeoIP Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_geoip_iso3166_list(request: web.Request, ) -> web.Response:
    """policies_geoip_iso3166_list

    Get all countries in ISO-3166-1


    """
    return web.Response(status=200)


async def policies_geoip_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """policies_geoip_list

    GeoIP Viewset

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


async def policies_geoip_partial_update(request: web.Request, policy_uuid, body=None) -> web.Response:
    """policies_geoip_partial_update

    GeoIP Viewset

    :param policy_uuid: A UUID string identifying this GeoIP Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedGeoIPPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_geoip_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_geoip_retrieve

    GeoIP Viewset

    :param policy_uuid: A UUID string identifying this GeoIP Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_geoip_update(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_geoip_update

    GeoIP Viewset

    :param policy_uuid: A UUID string identifying this GeoIP Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = GeoIPPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_geoip_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_geoip_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this GeoIP Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_password_create(request: web.Request, body) -> web.Response:
    """policies_password_create

    Password Policy Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PasswordPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_password_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_password_destroy

    Password Policy Viewset

    :param policy_uuid: A UUID string identifying this Password Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_password_expiry_create(request: web.Request, body) -> web.Response:
    """policies_password_expiry_create

    Password Expiry Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PasswordExpiryPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_password_expiry_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_password_expiry_destroy

    Password Expiry Viewset

    :param policy_uuid: A UUID string identifying this Password Expiry Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_password_expiry_list(request: web.Request, created=None, days=None, deny_only=None, execution_logging=None, last_updated=None, name=None, ordering=None, page=None, page_size=None, policy_uuid=None, search=None) -> web.Response:
    """policies_password_expiry_list

    Password Expiry Viewset

    :param created: 
    :type created: str
    :param days: 
    :type days: int
    :param deny_only: 
    :type deny_only: bool
    :param execution_logging: 
    :type execution_logging: bool
    :param last_updated: 
    :type last_updated: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_uuid: 
    :type policy_uuid: str
    :type policy_uuid: str
    :param search: A search term.
    :type search: str

    """
    created = util.deserialize_datetime(created)
    last_updated = util.deserialize_datetime(last_updated)
    return web.Response(status=200)


async def policies_password_expiry_partial_update(request: web.Request, policy_uuid, body=None) -> web.Response:
    """policies_password_expiry_partial_update

    Password Expiry Viewset

    :param policy_uuid: A UUID string identifying this Password Expiry Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPasswordExpiryPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_password_expiry_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_password_expiry_retrieve

    Password Expiry Viewset

    :param policy_uuid: A UUID string identifying this Password Expiry Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_password_expiry_update(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_password_expiry_update

    Password Expiry Viewset

    :param policy_uuid: A UUID string identifying this Password Expiry Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PasswordExpiryPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_password_expiry_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_password_expiry_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this Password Expiry Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_password_list(request: web.Request, amount_digits=None, amount_lowercase=None, amount_symbols=None, amount_uppercase=None, check_have_i_been_pwned=None, check_static_rules=None, check_zxcvbn=None, created=None, error_message=None, execution_logging=None, hibp_allowed_count=None, last_updated=None, length_min=None, name=None, ordering=None, page=None, page_size=None, password_field=None, policy_uuid=None, search=None, symbol_charset=None, zxcvbn_score_threshold=None) -> web.Response:
    """policies_password_list

    Password Policy Viewset

    :param amount_digits: 
    :type amount_digits: int
    :param amount_lowercase: 
    :type amount_lowercase: int
    :param amount_symbols: 
    :type amount_symbols: int
    :param amount_uppercase: 
    :type amount_uppercase: int
    :param check_have_i_been_pwned: 
    :type check_have_i_been_pwned: bool
    :param check_static_rules: 
    :type check_static_rules: bool
    :param check_zxcvbn: 
    :type check_zxcvbn: bool
    :param created: 
    :type created: str
    :param error_message: 
    :type error_message: str
    :param execution_logging: 
    :type execution_logging: bool
    :param hibp_allowed_count: 
    :type hibp_allowed_count: int
    :param last_updated: 
    :type last_updated: str
    :param length_min: 
    :type length_min: int
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param password_field: 
    :type password_field: str
    :param policy_uuid: 
    :type policy_uuid: str
    :type policy_uuid: str
    :param search: A search term.
    :type search: str
    :param symbol_charset: 
    :type symbol_charset: str
    :param zxcvbn_score_threshold: 
    :type zxcvbn_score_threshold: int

    """
    created = util.deserialize_datetime(created)
    last_updated = util.deserialize_datetime(last_updated)
    return web.Response(status=200)


async def policies_password_partial_update(request: web.Request, policy_uuid, body=None) -> web.Response:
    """policies_password_partial_update

    Password Policy Viewset

    :param policy_uuid: A UUID string identifying this Password Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPasswordPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_password_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_password_retrieve

    Password Policy Viewset

    :param policy_uuid: A UUID string identifying this Password Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_password_update(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_password_update

    Password Policy Viewset

    :param policy_uuid: A UUID string identifying this Password Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PasswordPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_password_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_password_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this Password Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_reputation_create(request: web.Request, body) -> web.Response:
    """policies_reputation_create

    Reputation Policy Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = ReputationPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_reputation_destroy(request: web.Request, policy_uuid) -> web.Response:
    """policies_reputation_destroy

    Reputation Policy Viewset

    :param policy_uuid: A UUID string identifying this Reputation Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_reputation_list(request: web.Request, check_ip=None, check_username=None, created=None, execution_logging=None, last_updated=None, name=None, ordering=None, page=None, page_size=None, policy_uuid=None, search=None, threshold=None) -> web.Response:
    """policies_reputation_list

    Reputation Policy Viewset

    :param check_ip: 
    :type check_ip: bool
    :param check_username: 
    :type check_username: bool
    :param created: 
    :type created: str
    :param execution_logging: 
    :type execution_logging: bool
    :param last_updated: 
    :type last_updated: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_uuid: 
    :type policy_uuid: str
    :type policy_uuid: str
    :param search: A search term.
    :type search: str
    :param threshold: 
    :type threshold: int

    """
    created = util.deserialize_datetime(created)
    last_updated = util.deserialize_datetime(last_updated)
    return web.Response(status=200)


async def policies_reputation_partial_update(request: web.Request, policy_uuid, body=None) -> web.Response:
    """policies_reputation_partial_update

    Reputation Policy Viewset

    :param policy_uuid: A UUID string identifying this Reputation Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedReputationPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_reputation_retrieve(request: web.Request, policy_uuid) -> web.Response:
    """policies_reputation_retrieve

    Reputation Policy Viewset

    :param policy_uuid: A UUID string identifying this Reputation Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)


async def policies_reputation_scores_destroy(request: web.Request, reputation_uuid) -> web.Response:
    """policies_reputation_scores_destroy

    Reputation Viewset

    :param reputation_uuid: A UUID string identifying this Reputation Score.
    :type reputation_uuid: str
    :type reputation_uuid: str

    """
    return web.Response(status=200)


async def policies_reputation_scores_list(request: web.Request, identifier=None, identifier_in=None, ip=None, ordering=None, page=None, page_size=None, score=None, search=None) -> web.Response:
    """policies_reputation_scores_list

    Reputation Viewset

    :param identifier: 
    :type identifier: str
    :param identifier_in: Multiple values may be separated by commas.
    :type identifier_in: List[str]
    :param ip: 
    :type ip: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param score: 
    :type score: int
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def policies_reputation_scores_retrieve(request: web.Request, reputation_uuid) -> web.Response:
    """policies_reputation_scores_retrieve

    Reputation Viewset

    :param reputation_uuid: A UUID string identifying this Reputation Score.
    :type reputation_uuid: str
    :type reputation_uuid: str

    """
    return web.Response(status=200)


async def policies_reputation_scores_used_by_list(request: web.Request, reputation_uuid) -> web.Response:
    """policies_reputation_scores_used_by_list

    Get a list of all objects that use this object

    :param reputation_uuid: A UUID string identifying this Reputation Score.
    :type reputation_uuid: str
    :type reputation_uuid: str

    """
    return web.Response(status=200)


async def policies_reputation_update(request: web.Request, policy_uuid, body) -> web.Response:
    """policies_reputation_update

    Reputation Policy Viewset

    :param policy_uuid: A UUID string identifying this Reputation Policy.
    :type policy_uuid: str
    :type policy_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = ReputationPolicyRequest.from_dict(body)
    return web.Response(status=200)


async def policies_reputation_used_by_list(request: web.Request, policy_uuid) -> web.Response:
    """policies_reputation_used_by_list

    Get a list of all objects that use this object

    :param policy_uuid: A UUID string identifying this Reputation Policy.
    :type policy_uuid: str
    :type policy_uuid: str

    """
    return web.Response(status=200)
