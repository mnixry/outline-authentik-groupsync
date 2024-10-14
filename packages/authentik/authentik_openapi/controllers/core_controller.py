from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.application import Application
from authentik_openapi.models.application_request import ApplicationRequest
from authentik_openapi.models.authenticated_session import AuthenticatedSession
from authentik_openapi.models.brand import Brand
from authentik_openapi.models.brand_request import BrandRequest
from authentik_openapi.models.coordinate import Coordinate
from authentik_openapi.models.current_brand import CurrentBrand
from authentik_openapi.models.file_path_request import FilePathRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.group import Group
from authentik_openapi.models.group_request import GroupRequest
from authentik_openapi.models.link import Link
from authentik_openapi.models.paginated_application_list import PaginatedApplicationList
from authentik_openapi.models.paginated_authenticated_session_list import PaginatedAuthenticatedSessionList
from authentik_openapi.models.paginated_brand_list import PaginatedBrandList
from authentik_openapi.models.paginated_group_list import PaginatedGroupList
from authentik_openapi.models.paginated_token_list import PaginatedTokenList
from authentik_openapi.models.paginated_user_consent_list import PaginatedUserConsentList
from authentik_openapi.models.paginated_user_list import PaginatedUserList
from authentik_openapi.models.patched_application_request import PatchedApplicationRequest
from authentik_openapi.models.patched_brand_request import PatchedBrandRequest
from authentik_openapi.models.patched_group_request import PatchedGroupRequest
from authentik_openapi.models.patched_token_request import PatchedTokenRequest
from authentik_openapi.models.patched_user_request import PatchedUserRequest
from authentik_openapi.models.policy_test_result import PolicyTestResult
from authentik_openapi.models.session_user import SessionUser
from authentik_openapi.models.token import Token
from authentik_openapi.models.token_request import TokenRequest
from authentik_openapi.models.token_set_key_request import TokenSetKeyRequest
from authentik_openapi.models.token_view import TokenView
from authentik_openapi.models.transaction_application_request import TransactionApplicationRequest
from authentik_openapi.models.transaction_application_response import TransactionApplicationResponse
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.user import User
from authentik_openapi.models.user_account_request import UserAccountRequest
from authentik_openapi.models.user_consent import UserConsent
from authentik_openapi.models.user_metrics import UserMetrics
from authentik_openapi.models.user_password_set_request import UserPasswordSetRequest
from authentik_openapi.models.user_path import UserPath
from authentik_openapi.models.user_request import UserRequest
from authentik_openapi.models.user_service_account_request import UserServiceAccountRequest
from authentik_openapi.models.user_service_account_response import UserServiceAccountResponse
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def core_applications_check_access_retrieve(request: web.Request, slug, for_user=None) -> web.Response:
    """core_applications_check_access_retrieve

    Check access to a single application by slug

    :param slug: 
    :type slug: str
    :param for_user: 
    :type for_user: int

    """
    return web.Response(status=200)


async def core_applications_create(request: web.Request, body) -> web.Response:
    """core_applications_create

    Application Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = ApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def core_applications_destroy(request: web.Request, slug) -> web.Response:
    """core_applications_destroy

    Application Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def core_applications_list(request: web.Request, for_user=None, group=None, meta_description=None, meta_launch_url=None, meta_publisher=None, name=None, only_with_launch_url=None, ordering=None, page=None, page_size=None, search=None, slug=None, superuser_full_list=None) -> web.Response:
    """core_applications_list

    Custom list method that checks Policy based access instead of guardian

    :param for_user: 
    :type for_user: int
    :param group: 
    :type group: str
    :param meta_description: 
    :type meta_description: str
    :param meta_launch_url: 
    :type meta_launch_url: str
    :param meta_publisher: 
    :type meta_publisher: str
    :param name: 
    :type name: str
    :param only_with_launch_url: 
    :type only_with_launch_url: bool
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
    :param superuser_full_list: 
    :type superuser_full_list: bool

    """
    return web.Response(status=200)


async def core_applications_metrics_list(request: web.Request, slug) -> web.Response:
    """core_applications_metrics_list

    Metrics for application logins

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def core_applications_partial_update(request: web.Request, slug, body=None) -> web.Response:
    """core_applications_partial_update

    Application Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def core_applications_retrieve(request: web.Request, slug) -> web.Response:
    """core_applications_retrieve

    Application Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def core_applications_set_icon_create(request: web.Request, slug, file=None, clear=None) -> web.Response:
    """core_applications_set_icon_create

    Set application icon

    :param slug: 
    :type slug: str
    :param file: 
    :type file: str
    :param clear: 
    :type clear: bool

    """
    return web.Response(status=200)


async def core_applications_set_icon_url_create(request: web.Request, slug, body) -> web.Response:
    """core_applications_set_icon_url_create

    Set application icon (as URL)

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = FilePathRequest.from_dict(body)
    return web.Response(status=200)


async def core_applications_update(request: web.Request, slug, body) -> web.Response:
    """core_applications_update

    Application Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def core_applications_used_by_list(request: web.Request, slug) -> web.Response:
    """core_applications_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def core_authenticated_sessions_destroy(request: web.Request, uuid) -> web.Response:
    """core_authenticated_sessions_destroy

    AuthenticatedSession Viewset

    :param uuid: A UUID string identifying this Authenticated Session.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def core_authenticated_sessions_list(request: web.Request, last_ip=None, last_user_agent=None, ordering=None, page=None, page_size=None, search=None, user__username=None) -> web.Response:
    """core_authenticated_sessions_list

    AuthenticatedSession Viewset

    :param last_ip: 
    :type last_ip: str
    :param last_user_agent: 
    :type last_user_agent: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param user__username: 
    :type user__username: str

    """
    return web.Response(status=200)


async def core_authenticated_sessions_retrieve(request: web.Request, uuid) -> web.Response:
    """core_authenticated_sessions_retrieve

    AuthenticatedSession Viewset

    :param uuid: A UUID string identifying this Authenticated Session.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def core_authenticated_sessions_used_by_list(request: web.Request, uuid) -> web.Response:
    """core_authenticated_sessions_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Authenticated Session.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def core_brands_create(request: web.Request, body) -> web.Response:
    """core_brands_create

    Brand Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = BrandRequest.from_dict(body)
    return web.Response(status=200)


async def core_brands_current_retrieve(request: web.Request, ) -> web.Response:
    """core_brands_current_retrieve

    Get current brand


    """
    return web.Response(status=200)


async def core_brands_destroy(request: web.Request, brand_uuid) -> web.Response:
    """core_brands_destroy

    Brand Viewset

    :param brand_uuid: A UUID string identifying this Brand.
    :type brand_uuid: str
    :type brand_uuid: str

    """
    return web.Response(status=200)


async def core_brands_list(request: web.Request, brand_uuid=None, branding_favicon=None, branding_logo=None, branding_title=None, default=None, domain=None, flow_authentication=None, flow_device_code=None, flow_invalidation=None, flow_recovery=None, flow_unenrollment=None, flow_user_settings=None, ordering=None, page=None, page_size=None, search=None, web_certificate=None) -> web.Response:
    """core_brands_list

    Brand Viewset

    :param brand_uuid: 
    :type brand_uuid: str
    :type brand_uuid: str
    :param branding_favicon: 
    :type branding_favicon: str
    :param branding_logo: 
    :type branding_logo: str
    :param branding_title: 
    :type branding_title: str
    :param default: 
    :type default: bool
    :param domain: 
    :type domain: str
    :param flow_authentication: 
    :type flow_authentication: str
    :type flow_authentication: str
    :param flow_device_code: 
    :type flow_device_code: str
    :type flow_device_code: str
    :param flow_invalidation: 
    :type flow_invalidation: str
    :type flow_invalidation: str
    :param flow_recovery: 
    :type flow_recovery: str
    :type flow_recovery: str
    :param flow_unenrollment: 
    :type flow_unenrollment: str
    :type flow_unenrollment: str
    :param flow_user_settings: 
    :type flow_user_settings: str
    :type flow_user_settings: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param web_certificate: 
    :type web_certificate: str
    :type web_certificate: str

    """
    return web.Response(status=200)


async def core_brands_partial_update(request: web.Request, brand_uuid, body=None) -> web.Response:
    """core_brands_partial_update

    Brand Viewset

    :param brand_uuid: A UUID string identifying this Brand.
    :type brand_uuid: str
    :type brand_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedBrandRequest.from_dict(body)
    return web.Response(status=200)


async def core_brands_retrieve(request: web.Request, brand_uuid) -> web.Response:
    """core_brands_retrieve

    Brand Viewset

    :param brand_uuid: A UUID string identifying this Brand.
    :type brand_uuid: str
    :type brand_uuid: str

    """
    return web.Response(status=200)


async def core_brands_update(request: web.Request, brand_uuid, body) -> web.Response:
    """core_brands_update

    Brand Viewset

    :param brand_uuid: A UUID string identifying this Brand.
    :type brand_uuid: str
    :type brand_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = BrandRequest.from_dict(body)
    return web.Response(status=200)


async def core_brands_used_by_list(request: web.Request, brand_uuid) -> web.Response:
    """core_brands_used_by_list

    Get a list of all objects that use this object

    :param brand_uuid: A UUID string identifying this Brand.
    :type brand_uuid: str
    :type brand_uuid: str

    """
    return web.Response(status=200)


async def core_groups_add_user_create(request: web.Request, group_uuid, body) -> web.Response:
    """core_groups_add_user_create

    Add user to group

    :param group_uuid: A UUID string identifying this Group.
    :type group_uuid: str
    :type group_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserAccountRequest.from_dict(body)
    return web.Response(status=200)


async def core_groups_create(request: web.Request, body) -> web.Response:
    """core_groups_create

    Group Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = GroupRequest.from_dict(body)
    return web.Response(status=200)


async def core_groups_destroy(request: web.Request, group_uuid) -> web.Response:
    """core_groups_destroy

    Group Viewset

    :param group_uuid: A UUID string identifying this Group.
    :type group_uuid: str
    :type group_uuid: str

    """
    return web.Response(status=200)


async def core_groups_list(request: web.Request, attributes=None, include_users=None, is_superuser=None, members_by_pk=None, members_by_username=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """core_groups_list

    Group Viewset

    :param attributes: Attributes
    :type attributes: str
    :param include_users: 
    :type include_users: bool
    :param is_superuser: 
    :type is_superuser: bool
    :param members_by_pk: 
    :type members_by_pk: List[int]
    :param members_by_username: Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.
    :type members_by_username: List[str]
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


async def core_groups_partial_update(request: web.Request, group_uuid, body=None) -> web.Response:
    """core_groups_partial_update

    Group Viewset

    :param group_uuid: A UUID string identifying this Group.
    :type group_uuid: str
    :type group_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedGroupRequest.from_dict(body)
    return web.Response(status=200)


async def core_groups_remove_user_create(request: web.Request, group_uuid, body) -> web.Response:
    """core_groups_remove_user_create

    Add user to group

    :param group_uuid: A UUID string identifying this Group.
    :type group_uuid: str
    :type group_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserAccountRequest.from_dict(body)
    return web.Response(status=200)


async def core_groups_retrieve(request: web.Request, group_uuid, include_users=None) -> web.Response:
    """core_groups_retrieve

    Group Viewset

    :param group_uuid: A UUID string identifying this Group.
    :type group_uuid: str
    :type group_uuid: str
    :param include_users: 
    :type include_users: bool

    """
    return web.Response(status=200)


async def core_groups_update(request: web.Request, group_uuid, body) -> web.Response:
    """core_groups_update

    Group Viewset

    :param group_uuid: A UUID string identifying this Group.
    :type group_uuid: str
    :type group_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = GroupRequest.from_dict(body)
    return web.Response(status=200)


async def core_groups_used_by_list(request: web.Request, group_uuid) -> web.Response:
    """core_groups_used_by_list

    Get a list of all objects that use this object

    :param group_uuid: A UUID string identifying this Group.
    :type group_uuid: str
    :type group_uuid: str

    """
    return web.Response(status=200)


async def core_tokens_create(request: web.Request, body) -> web.Response:
    """core_tokens_create

    Token Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = TokenRequest.from_dict(body)
    return web.Response(status=200)


async def core_tokens_destroy(request: web.Request, identifier) -> web.Response:
    """core_tokens_destroy

    Token Viewset

    :param identifier: 
    :type identifier: str

    """
    return web.Response(status=200)


async def core_tokens_list(request: web.Request, description=None, expires=None, expiring=None, identifier=None, intent=None, managed=None, ordering=None, page=None, page_size=None, search=None, user__username=None) -> web.Response:
    """core_tokens_list

    Token Viewset

    :param description: 
    :type description: str
    :param expires: 
    :type expires: str
    :param expiring: 
    :type expiring: bool
    :param identifier: 
    :type identifier: str
    :param intent: 
    :type intent: str
    :param managed: 
    :type managed: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param user__username: 
    :type user__username: str

    """
    expires = util.deserialize_datetime(expires)
    return web.Response(status=200)


async def core_tokens_partial_update(request: web.Request, identifier, body=None) -> web.Response:
    """core_tokens_partial_update

    Token Viewset

    :param identifier: 
    :type identifier: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedTokenRequest.from_dict(body)
    return web.Response(status=200)


async def core_tokens_retrieve(request: web.Request, identifier) -> web.Response:
    """core_tokens_retrieve

    Token Viewset

    :param identifier: 
    :type identifier: str

    """
    return web.Response(status=200)


async def core_tokens_set_key_create(request: web.Request, identifier, body) -> web.Response:
    """core_tokens_set_key_create

    Set token key. Action is logged as event. &#x60;authentik_core.set_token_key&#x60; permission is required.

    :param identifier: 
    :type identifier: str
    :param body: 
    :type body: dict | bytes

    """
    body = TokenSetKeyRequest.from_dict(body)
    return web.Response(status=200)


async def core_tokens_update(request: web.Request, identifier, body) -> web.Response:
    """core_tokens_update

    Token Viewset

    :param identifier: 
    :type identifier: str
    :param body: 
    :type body: dict | bytes

    """
    body = TokenRequest.from_dict(body)
    return web.Response(status=200)


async def core_tokens_used_by_list(request: web.Request, identifier) -> web.Response:
    """core_tokens_used_by_list

    Get a list of all objects that use this object

    :param identifier: 
    :type identifier: str

    """
    return web.Response(status=200)


async def core_tokens_view_key_retrieve(request: web.Request, identifier) -> web.Response:
    """core_tokens_view_key_retrieve

    Return token key and log access

    :param identifier: 
    :type identifier: str

    """
    return web.Response(status=200)


async def core_transactional_applications_update(request: web.Request, body) -> web.Response:
    """core_transactional_applications_update

    Convert data into a blueprint, validate it and apply it

    :param body: 
    :type body: dict | bytes

    """
    body = TransactionApplicationRequest.from_dict(body)
    return web.Response(status=200)


async def core_user_consent_destroy(request: web.Request, id) -> web.Response:
    """core_user_consent_destroy

    UserConsent Viewset

    :param id: A unique integer value identifying this User Consent.
    :type id: int

    """
    return web.Response(status=200)


async def core_user_consent_list(request: web.Request, application=None, ordering=None, page=None, page_size=None, search=None, user=None) -> web.Response:
    """core_user_consent_list

    UserConsent Viewset

    :param application: 
    :type application: str
    :type application: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def core_user_consent_retrieve(request: web.Request, id) -> web.Response:
    """core_user_consent_retrieve

    UserConsent Viewset

    :param id: A unique integer value identifying this User Consent.
    :type id: int

    """
    return web.Response(status=200)


async def core_user_consent_used_by_list(request: web.Request, id) -> web.Response:
    """core_user_consent_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this User Consent.
    :type id: int

    """
    return web.Response(status=200)


async def core_users_create(request: web.Request, body) -> web.Response:
    """core_users_create

    User Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = UserRequest.from_dict(body)
    return web.Response(status=200)


async def core_users_destroy(request: web.Request, id) -> web.Response:
    """core_users_destroy

    User Viewset

    :param id: A unique integer value identifying this User.
    :type id: int

    """
    return web.Response(status=200)


async def core_users_impersonate_create(request: web.Request, id) -> web.Response:
    """core_users_impersonate_create

    Impersonate a user

    :param id: A unique integer value identifying this User.
    :type id: int

    """
    return web.Response(status=200)


async def core_users_impersonate_end_retrieve(request: web.Request, ) -> web.Response:
    """core_users_impersonate_end_retrieve

    End Impersonation a user


    """
    return web.Response(status=200)


async def core_users_list(request: web.Request, attributes=None, email=None, groups_by_name=None, groups_by_pk=None, include_groups=None, is_active=None, is_superuser=None, name=None, ordering=None, page=None, page_size=None, path=None, path_startswith=None, search=None, type=None, username=None, uuid=None) -> web.Response:
    """core_users_list

    User Viewset

    :param attributes: Attributes
    :type attributes: str
    :param email: 
    :type email: str
    :param groups_by_name: 
    :type groups_by_name: List[str]
    :param groups_by_pk: 
    :type groups_by_pk: List[str]
    :param include_groups: 
    :type include_groups: bool
    :param is_active: 
    :type is_active: bool
    :param is_superuser: 
    :type is_superuser: bool
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
    :param path_startswith: 
    :type path_startswith: str
    :param search: A search term.
    :type search: str
    :param type: 
    :type type: List[str]
    :param username: 
    :type username: str
    :param uuid: 
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def core_users_me_retrieve(request: web.Request, ) -> web.Response:
    """core_users_me_retrieve

    Get information about current user


    """
    return web.Response(status=200)


async def core_users_metrics_retrieve(request: web.Request, id) -> web.Response:
    """core_users_metrics_retrieve

    User metrics per 1h

    :param id: A unique integer value identifying this User.
    :type id: int

    """
    return web.Response(status=200)


async def core_users_partial_update(request: web.Request, id, body=None) -> web.Response:
    """core_users_partial_update

    User Viewset

    :param id: A unique integer value identifying this User.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserRequest.from_dict(body)
    return web.Response(status=200)


async def core_users_paths_retrieve(request: web.Request, search=None) -> web.Response:
    """core_users_paths_retrieve

    Get all user paths

    :param search: 
    :type search: str

    """
    return web.Response(status=200)


async def core_users_recovery_create(request: web.Request, id) -> web.Response:
    """core_users_recovery_create

    Create a temporary link that a user can use to recover their accounts

    :param id: A unique integer value identifying this User.
    :type id: int

    """
    return web.Response(status=200)


async def core_users_recovery_email_create(request: web.Request, email_stage, id) -> web.Response:
    """core_users_recovery_email_create

    Create a temporary link that a user can use to recover their accounts

    :param email_stage: 
    :type email_stage: str
    :param id: A unique integer value identifying this User.
    :type id: int

    """
    return web.Response(status=200)


async def core_users_retrieve(request: web.Request, id) -> web.Response:
    """core_users_retrieve

    User Viewset

    :param id: A unique integer value identifying this User.
    :type id: int

    """
    return web.Response(status=200)


async def core_users_service_account_create(request: web.Request, body) -> web.Response:
    """core_users_service_account_create

    Create a new user account that is marked as a service account

    :param body: 
    :type body: dict | bytes

    """
    body = UserServiceAccountRequest.from_dict(body)
    return web.Response(status=200)


async def core_users_set_password_create(request: web.Request, id, body) -> web.Response:
    """core_users_set_password_create

    Set password for user

    :param id: A unique integer value identifying this User.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserPasswordSetRequest.from_dict(body)
    return web.Response(status=200)


async def core_users_update(request: web.Request, id, body) -> web.Response:
    """core_users_update

    User Viewset

    :param id: A unique integer value identifying this User.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserRequest.from_dict(body)
    return web.Response(status=200)


async def core_users_used_by_list(request: web.Request, id) -> web.Response:
    """core_users_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this User.
    :type id: int

    """
    return web.Response(status=200)
