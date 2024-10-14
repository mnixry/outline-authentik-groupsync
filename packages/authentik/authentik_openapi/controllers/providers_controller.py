from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.google_workspace_provider import GoogleWorkspaceProvider
from authentik_openapi.models.google_workspace_provider_group import GoogleWorkspaceProviderGroup
from authentik_openapi.models.google_workspace_provider_group_request import GoogleWorkspaceProviderGroupRequest
from authentik_openapi.models.google_workspace_provider_request import GoogleWorkspaceProviderRequest
from authentik_openapi.models.google_workspace_provider_user import GoogleWorkspaceProviderUser
from authentik_openapi.models.google_workspace_provider_user_request import GoogleWorkspaceProviderUserRequest
from authentik_openapi.models.ldap_provider import LDAPProvider
from authentik_openapi.models.ldap_provider_request import LDAPProviderRequest
from authentik_openapi.models.microsoft_entra_provider import MicrosoftEntraProvider
from authentik_openapi.models.microsoft_entra_provider_group import MicrosoftEntraProviderGroup
from authentik_openapi.models.microsoft_entra_provider_group_request import MicrosoftEntraProviderGroupRequest
from authentik_openapi.models.microsoft_entra_provider_request import MicrosoftEntraProviderRequest
from authentik_openapi.models.microsoft_entra_provider_user import MicrosoftEntraProviderUser
from authentik_openapi.models.microsoft_entra_provider_user_request import MicrosoftEntraProviderUserRequest
from authentik_openapi.models.o_auth2_provider import OAuth2Provider
from authentik_openapi.models.o_auth2_provider_request import OAuth2ProviderRequest
from authentik_openapi.models.o_auth2_provider_setup_urls import OAuth2ProviderSetupURLs
from authentik_openapi.models.paginated_google_workspace_provider_group_list import PaginatedGoogleWorkspaceProviderGroupList
from authentik_openapi.models.paginated_google_workspace_provider_list import PaginatedGoogleWorkspaceProviderList
from authentik_openapi.models.paginated_google_workspace_provider_user_list import PaginatedGoogleWorkspaceProviderUserList
from authentik_openapi.models.paginated_ldap_provider_list import PaginatedLDAPProviderList
from authentik_openapi.models.paginated_microsoft_entra_provider_group_list import PaginatedMicrosoftEntraProviderGroupList
from authentik_openapi.models.paginated_microsoft_entra_provider_list import PaginatedMicrosoftEntraProviderList
from authentik_openapi.models.paginated_microsoft_entra_provider_user_list import PaginatedMicrosoftEntraProviderUserList
from authentik_openapi.models.paginated_o_auth2_provider_list import PaginatedOAuth2ProviderList
from authentik_openapi.models.paginated_provider_list import PaginatedProviderList
from authentik_openapi.models.paginated_proxy_provider_list import PaginatedProxyProviderList
from authentik_openapi.models.paginated_rac_provider_list import PaginatedRACProviderList
from authentik_openapi.models.paginated_radius_provider_list import PaginatedRadiusProviderList
from authentik_openapi.models.paginated_saml_provider_list import PaginatedSAMLProviderList
from authentik_openapi.models.paginated_scim_provider_group_list import PaginatedSCIMProviderGroupList
from authentik_openapi.models.paginated_scim_provider_list import PaginatedSCIMProviderList
from authentik_openapi.models.paginated_scim_provider_user_list import PaginatedSCIMProviderUserList
from authentik_openapi.models.patched_google_workspace_provider_request import PatchedGoogleWorkspaceProviderRequest
from authentik_openapi.models.patched_ldap_provider_request import PatchedLDAPProviderRequest
from authentik_openapi.models.patched_microsoft_entra_provider_request import PatchedMicrosoftEntraProviderRequest
from authentik_openapi.models.patched_o_auth2_provider_request import PatchedOAuth2ProviderRequest
from authentik_openapi.models.patched_proxy_provider_request import PatchedProxyProviderRequest
from authentik_openapi.models.patched_rac_provider_request import PatchedRACProviderRequest
from authentik_openapi.models.patched_radius_provider_request import PatchedRadiusProviderRequest
from authentik_openapi.models.patched_saml_provider_request import PatchedSAMLProviderRequest
from authentik_openapi.models.patched_scim_provider_request import PatchedSCIMProviderRequest
from authentik_openapi.models.property_mapping_preview import PropertyMappingPreview
from authentik_openapi.models.provider import Provider
from authentik_openapi.models.proxy_provider import ProxyProvider
from authentik_openapi.models.proxy_provider_request import ProxyProviderRequest
from authentik_openapi.models.rac_provider import RACProvider
from authentik_openapi.models.rac_provider_request import RACProviderRequest
from authentik_openapi.models.radius_provider import RadiusProvider
from authentik_openapi.models.radius_provider_request import RadiusProviderRequest
from authentik_openapi.models.saml_metadata import SAMLMetadata
from authentik_openapi.models.saml_provider import SAMLProvider
from authentik_openapi.models.saml_provider_request import SAMLProviderRequest
from authentik_openapi.models.scim_provider import SCIMProvider
from authentik_openapi.models.scim_provider_group import SCIMProviderGroup
from authentik_openapi.models.scim_provider_group_request import SCIMProviderGroupRequest
from authentik_openapi.models.scim_provider_request import SCIMProviderRequest
from authentik_openapi.models.scim_provider_user import SCIMProviderUser
from authentik_openapi.models.scim_provider_user_request import SCIMProviderUserRequest
from authentik_openapi.models.sync_object_request import SyncObjectRequest
from authentik_openapi.models.sync_object_result import SyncObjectResult
from authentik_openapi.models.sync_status import SyncStatus
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def providers_all_destroy(request: web.Request, id) -> web.Response:
    """providers_all_destroy

    Provider Viewset

    :param id: A unique integer value identifying this provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_all_list(request: web.Request, application__isnull=None, backchannel=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """providers_all_list

    Provider Viewset

    :param application__isnull: 
    :type application__isnull: bool
    :param backchannel: When not set all providers are returned. When set to true, only backchannel providers are returned. When set to false, backchannel providers are excluded
    :type backchannel: bool
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


async def providers_all_retrieve(request: web.Request, id) -> web.Response:
    """providers_all_retrieve

    Provider Viewset

    :param id: A unique integer value identifying this provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_all_types_list(request: web.Request, ) -> web.Response:
    """providers_all_types_list

    Get all creatable types


    """
    return web.Response(status=200)


async def providers_all_used_by_list(request: web.Request, id) -> web.Response:
    """providers_all_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_google_workspace_create(request: web.Request, body) -> web.Response:
    """providers_google_workspace_create

    GoogleWorkspaceProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = GoogleWorkspaceProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_google_workspace_destroy(request: web.Request, id) -> web.Response:
    """providers_google_workspace_destroy

    GoogleWorkspaceProvider Viewset

    :param id: A unique integer value identifying this Google Workspace Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_google_workspace_groups_create(request: web.Request, body) -> web.Response:
    """providers_google_workspace_groups_create

    GoogleWorkspaceProviderGroup Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = GoogleWorkspaceProviderGroupRequest.from_dict(body)
    return web.Response(status=200)


async def providers_google_workspace_groups_destroy(request: web.Request, id) -> web.Response:
    """providers_google_workspace_groups_destroy

    GoogleWorkspaceProviderGroup Viewset

    :param id: A UUID string identifying this Google Workspace Provider Group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_google_workspace_groups_list(request: web.Request, group__group_uuid=None, group__name=None, ordering=None, page=None, page_size=None, provider__id=None, search=None) -> web.Response:
    """providers_google_workspace_groups_list

    GoogleWorkspaceProviderGroup Viewset

    :param group__group_uuid: 
    :type group__group_uuid: str
    :type group__group_uuid: str
    :param group__name: 
    :type group__name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider__id: 
    :type provider__id: int
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def providers_google_workspace_groups_retrieve(request: web.Request, id) -> web.Response:
    """providers_google_workspace_groups_retrieve

    GoogleWorkspaceProviderGroup Viewset

    :param id: A UUID string identifying this Google Workspace Provider Group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_google_workspace_groups_used_by_list(request: web.Request, id) -> web.Response:
    """providers_google_workspace_groups_used_by_list

    Get a list of all objects that use this object

    :param id: A UUID string identifying this Google Workspace Provider Group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_google_workspace_list(request: web.Request, delegated_subject=None, exclude_users_service_account=None, filter_group=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """providers_google_workspace_list

    GoogleWorkspaceProvider Viewset

    :param delegated_subject: 
    :type delegated_subject: str
    :param exclude_users_service_account: 
    :type exclude_users_service_account: bool
    :param filter_group: 
    :type filter_group: str
    :type filter_group: str
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


async def providers_google_workspace_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_google_workspace_partial_update

    GoogleWorkspaceProvider Viewset

    :param id: A unique integer value identifying this Google Workspace Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedGoogleWorkspaceProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_google_workspace_retrieve(request: web.Request, id) -> web.Response:
    """providers_google_workspace_retrieve

    GoogleWorkspaceProvider Viewset

    :param id: A unique integer value identifying this Google Workspace Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_google_workspace_sync_object_create(request: web.Request, id, body) -> web.Response:
    """providers_google_workspace_sync_object_create

    Sync/Re-sync a single user/group object

    :param id: A unique integer value identifying this Google Workspace Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SyncObjectRequest.from_dict(body)
    return web.Response(status=200)


async def providers_google_workspace_sync_status_retrieve(request: web.Request, id) -> web.Response:
    """providers_google_workspace_sync_status_retrieve

    Get provider&#39;s sync status

    :param id: A unique integer value identifying this Google Workspace Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_google_workspace_update(request: web.Request, id, body) -> web.Response:
    """providers_google_workspace_update

    GoogleWorkspaceProvider Viewset

    :param id: A unique integer value identifying this Google Workspace Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleWorkspaceProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_google_workspace_used_by_list(request: web.Request, id) -> web.Response:
    """providers_google_workspace_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Google Workspace Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_google_workspace_users_create(request: web.Request, body) -> web.Response:
    """providers_google_workspace_users_create

    GoogleWorkspaceProviderUser Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = GoogleWorkspaceProviderUserRequest.from_dict(body)
    return web.Response(status=200)


async def providers_google_workspace_users_destroy(request: web.Request, id) -> web.Response:
    """providers_google_workspace_users_destroy

    GoogleWorkspaceProviderUser Viewset

    :param id: A UUID string identifying this Google Workspace Provider User.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_google_workspace_users_list(request: web.Request, ordering=None, page=None, page_size=None, provider__id=None, search=None, user__id=None, user__username=None) -> web.Response:
    """providers_google_workspace_users_list

    GoogleWorkspaceProviderUser Viewset

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider__id: 
    :type provider__id: int
    :param search: A search term.
    :type search: str
    :param user__id: 
    :type user__id: int
    :param user__username: 
    :type user__username: str

    """
    return web.Response(status=200)


async def providers_google_workspace_users_retrieve(request: web.Request, id) -> web.Response:
    """providers_google_workspace_users_retrieve

    GoogleWorkspaceProviderUser Viewset

    :param id: A UUID string identifying this Google Workspace Provider User.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_google_workspace_users_used_by_list(request: web.Request, id) -> web.Response:
    """providers_google_workspace_users_used_by_list

    Get a list of all objects that use this object

    :param id: A UUID string identifying this Google Workspace Provider User.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_ldap_create(request: web.Request, body) -> web.Response:
    """providers_ldap_create

    LDAPProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = LDAPProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_ldap_destroy(request: web.Request, id) -> web.Response:
    """providers_ldap_destroy

    LDAPProvider Viewset

    :param id: A unique integer value identifying this LDAP Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_ldap_list(request: web.Request, application__isnull=None, authorization_flow__slug__iexact=None, base_dn__iexact=None, certificate__kp_uuid__iexact=None, certificate__name__iexact=None, gid_start_number__iexact=None, name__iexact=None, ordering=None, page=None, page_size=None, search=None, tls_server_name__iexact=None, uid_start_number__iexact=None) -> web.Response:
    """providers_ldap_list

    LDAPProvider Viewset

    :param application__isnull: 
    :type application__isnull: bool
    :param authorization_flow__slug__iexact: 
    :type authorization_flow__slug__iexact: str
    :param base_dn__iexact: 
    :type base_dn__iexact: str
    :param certificate__kp_uuid__iexact: 
    :type certificate__kp_uuid__iexact: str
    :type certificate__kp_uuid__iexact: str
    :param certificate__name__iexact: 
    :type certificate__name__iexact: str
    :param gid_start_number__iexact: 
    :type gid_start_number__iexact: int
    :param name__iexact: 
    :type name__iexact: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param tls_server_name__iexact: 
    :type tls_server_name__iexact: str
    :param uid_start_number__iexact: 
    :type uid_start_number__iexact: int

    """
    return web.Response(status=200)


async def providers_ldap_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_ldap_partial_update

    LDAPProvider Viewset

    :param id: A unique integer value identifying this LDAP Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedLDAPProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_ldap_retrieve(request: web.Request, id) -> web.Response:
    """providers_ldap_retrieve

    LDAPProvider Viewset

    :param id: A unique integer value identifying this LDAP Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_ldap_update(request: web.Request, id, body) -> web.Response:
    """providers_ldap_update

    LDAPProvider Viewset

    :param id: A unique integer value identifying this LDAP Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = LDAPProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_ldap_used_by_list(request: web.Request, id) -> web.Response:
    """providers_ldap_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this LDAP Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_microsoft_entra_create(request: web.Request, body) -> web.Response:
    """providers_microsoft_entra_create

    MicrosoftEntraProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = MicrosoftEntraProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_microsoft_entra_destroy(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_destroy

    MicrosoftEntraProvider Viewset

    :param id: A unique integer value identifying this Microsoft Entra Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_microsoft_entra_groups_create(request: web.Request, body) -> web.Response:
    """providers_microsoft_entra_groups_create

    MicrosoftEntraProviderGroup Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = MicrosoftEntraProviderGroupRequest.from_dict(body)
    return web.Response(status=200)


async def providers_microsoft_entra_groups_destroy(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_groups_destroy

    MicrosoftEntraProviderGroup Viewset

    :param id: A UUID string identifying this Microsoft Entra Provider Group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_microsoft_entra_groups_list(request: web.Request, group__group_uuid=None, group__name=None, ordering=None, page=None, page_size=None, provider__id=None, search=None) -> web.Response:
    """providers_microsoft_entra_groups_list

    MicrosoftEntraProviderGroup Viewset

    :param group__group_uuid: 
    :type group__group_uuid: str
    :type group__group_uuid: str
    :param group__name: 
    :type group__name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider__id: 
    :type provider__id: int
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def providers_microsoft_entra_groups_retrieve(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_groups_retrieve

    MicrosoftEntraProviderGroup Viewset

    :param id: A UUID string identifying this Microsoft Entra Provider Group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_microsoft_entra_groups_used_by_list(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_groups_used_by_list

    Get a list of all objects that use this object

    :param id: A UUID string identifying this Microsoft Entra Provider Group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_microsoft_entra_list(request: web.Request, exclude_users_service_account=None, filter_group=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """providers_microsoft_entra_list

    MicrosoftEntraProvider Viewset

    :param exclude_users_service_account: 
    :type exclude_users_service_account: bool
    :param filter_group: 
    :type filter_group: str
    :type filter_group: str
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


async def providers_microsoft_entra_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_microsoft_entra_partial_update

    MicrosoftEntraProvider Viewset

    :param id: A unique integer value identifying this Microsoft Entra Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedMicrosoftEntraProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_microsoft_entra_retrieve(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_retrieve

    MicrosoftEntraProvider Viewset

    :param id: A unique integer value identifying this Microsoft Entra Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_microsoft_entra_sync_object_create(request: web.Request, id, body) -> web.Response:
    """providers_microsoft_entra_sync_object_create

    Sync/Re-sync a single user/group object

    :param id: A unique integer value identifying this Microsoft Entra Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SyncObjectRequest.from_dict(body)
    return web.Response(status=200)


async def providers_microsoft_entra_sync_status_retrieve(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_sync_status_retrieve

    Get provider&#39;s sync status

    :param id: A unique integer value identifying this Microsoft Entra Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_microsoft_entra_update(request: web.Request, id, body) -> web.Response:
    """providers_microsoft_entra_update

    MicrosoftEntraProvider Viewset

    :param id: A unique integer value identifying this Microsoft Entra Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = MicrosoftEntraProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_microsoft_entra_used_by_list(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Microsoft Entra Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_microsoft_entra_users_create(request: web.Request, body) -> web.Response:
    """providers_microsoft_entra_users_create

    MicrosoftEntraProviderUser Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = MicrosoftEntraProviderUserRequest.from_dict(body)
    return web.Response(status=200)


async def providers_microsoft_entra_users_destroy(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_users_destroy

    MicrosoftEntraProviderUser Viewset

    :param id: A UUID string identifying this Microsoft Entra Provider User.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_microsoft_entra_users_list(request: web.Request, ordering=None, page=None, page_size=None, provider__id=None, search=None, user__id=None, user__username=None) -> web.Response:
    """providers_microsoft_entra_users_list

    MicrosoftEntraProviderUser Viewset

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider__id: 
    :type provider__id: int
    :param search: A search term.
    :type search: str
    :param user__id: 
    :type user__id: int
    :param user__username: 
    :type user__username: str

    """
    return web.Response(status=200)


async def providers_microsoft_entra_users_retrieve(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_users_retrieve

    MicrosoftEntraProviderUser Viewset

    :param id: A UUID string identifying this Microsoft Entra Provider User.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_microsoft_entra_users_used_by_list(request: web.Request, id) -> web.Response:
    """providers_microsoft_entra_users_used_by_list

    Get a list of all objects that use this object

    :param id: A UUID string identifying this Microsoft Entra Provider User.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_oauth2_create(request: web.Request, body) -> web.Response:
    """providers_oauth2_create

    OAuth2Provider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = OAuth2ProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_oauth2_destroy(request: web.Request, id) -> web.Response:
    """providers_oauth2_destroy

    OAuth2Provider Viewset

    :param id: A unique integer value identifying this OAuth2/OpenID Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_oauth2_list(request: web.Request, access_code_validity=None, access_token_validity=None, application=None, authorization_flow=None, client_id=None, client_type=None, include_claims_in_id_token=None, issuer_mode=None, name=None, ordering=None, page=None, page_size=None, property_mappings=None, redirect_uris=None, refresh_token_validity=None, search=None, signing_key=None, sub_mode=None) -> web.Response:
    """providers_oauth2_list

    OAuth2Provider Viewset

    :param access_code_validity: 
    :type access_code_validity: str
    :param access_token_validity: 
    :type access_token_validity: str
    :param application: 
    :type application: str
    :type application: str
    :param authorization_flow: 
    :type authorization_flow: str
    :type authorization_flow: str
    :param client_id: 
    :type client_id: str
    :param client_type: Confidential clients are capable of maintaining the confidentiality of their credentials. Public clients are incapable  
    :type client_type: str
    :param include_claims_in_id_token: 
    :type include_claims_in_id_token: bool
    :param issuer_mode: Configure how the issuer field of the ID Token should be filled.  
    :type issuer_mode: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param property_mappings: 
    :type property_mappings: List[str]
    :param redirect_uris: 
    :type redirect_uris: str
    :param refresh_token_validity: 
    :type refresh_token_validity: str
    :param search: A search term.
    :type search: str
    :param signing_key: 
    :type signing_key: str
    :type signing_key: str
    :param sub_mode: Configure what data should be used as unique User Identifier. For most cases, the default should be fine.  
    :type sub_mode: str

    """
    return web.Response(status=200)


async def providers_oauth2_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_oauth2_partial_update

    OAuth2Provider Viewset

    :param id: A unique integer value identifying this OAuth2/OpenID Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedOAuth2ProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_oauth2_preview_user_retrieve(request: web.Request, id, for_user=None) -> web.Response:
    """providers_oauth2_preview_user_retrieve

    Preview user data for provider

    :param id: A unique integer value identifying this OAuth2/OpenID Provider.
    :type id: int
    :param for_user: 
    :type for_user: int

    """
    return web.Response(status=200)


async def providers_oauth2_retrieve(request: web.Request, id) -> web.Response:
    """providers_oauth2_retrieve

    OAuth2Provider Viewset

    :param id: A unique integer value identifying this OAuth2/OpenID Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_oauth2_setup_urls_retrieve(request: web.Request, id) -> web.Response:
    """providers_oauth2_setup_urls_retrieve

    Get Providers setup URLs

    :param id: A unique integer value identifying this OAuth2/OpenID Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_oauth2_update(request: web.Request, id, body) -> web.Response:
    """providers_oauth2_update

    OAuth2Provider Viewset

    :param id: A unique integer value identifying this OAuth2/OpenID Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = OAuth2ProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_oauth2_used_by_list(request: web.Request, id) -> web.Response:
    """providers_oauth2_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this OAuth2/OpenID Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_proxy_create(request: web.Request, body) -> web.Response:
    """providers_proxy_create

    ProxyProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = ProxyProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_proxy_destroy(request: web.Request, id) -> web.Response:
    """providers_proxy_destroy

    ProxyProvider Viewset

    :param id: A unique integer value identifying this Proxy Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_proxy_list(request: web.Request, application__isnull=None, authorization_flow__slug__iexact=None, basic_auth_enabled__iexact=None, basic_auth_password_attribute__iexact=None, basic_auth_user_attribute__iexact=None, certificate__kp_uuid__iexact=None, certificate__name__iexact=None, cookie_domain__iexact=None, external_host__iexact=None, internal_host__iexact=None, internal_host_ssl_validation__iexact=None, mode__iexact=None, name__iexact=None, ordering=None, page=None, page_size=None, property_mappings__iexact=None, redirect_uris__iexact=None, search=None, skip_path_regex__iexact=None) -> web.Response:
    """providers_proxy_list

    ProxyProvider Viewset

    :param application__isnull: 
    :type application__isnull: bool
    :param authorization_flow__slug__iexact: 
    :type authorization_flow__slug__iexact: str
    :param basic_auth_enabled__iexact: 
    :type basic_auth_enabled__iexact: bool
    :param basic_auth_password_attribute__iexact: 
    :type basic_auth_password_attribute__iexact: str
    :param basic_auth_user_attribute__iexact: 
    :type basic_auth_user_attribute__iexact: str
    :param certificate__kp_uuid__iexact: 
    :type certificate__kp_uuid__iexact: str
    :type certificate__kp_uuid__iexact: str
    :param certificate__name__iexact: 
    :type certificate__name__iexact: str
    :param cookie_domain__iexact: 
    :type cookie_domain__iexact: str
    :param external_host__iexact: 
    :type external_host__iexact: str
    :param internal_host__iexact: 
    :type internal_host__iexact: str
    :param internal_host_ssl_validation__iexact: 
    :type internal_host_ssl_validation__iexact: bool
    :param mode__iexact: 
    :type mode__iexact: str
    :param name__iexact: 
    :type name__iexact: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param property_mappings__iexact: 
    :type property_mappings__iexact: List[str]
    :param redirect_uris__iexact: 
    :type redirect_uris__iexact: str
    :param search: A search term.
    :type search: str
    :param skip_path_regex__iexact: 
    :type skip_path_regex__iexact: str

    """
    return web.Response(status=200)


async def providers_proxy_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_proxy_partial_update

    ProxyProvider Viewset

    :param id: A unique integer value identifying this Proxy Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedProxyProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_proxy_retrieve(request: web.Request, id) -> web.Response:
    """providers_proxy_retrieve

    ProxyProvider Viewset

    :param id: A unique integer value identifying this Proxy Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_proxy_update(request: web.Request, id, body) -> web.Response:
    """providers_proxy_update

    ProxyProvider Viewset

    :param id: A unique integer value identifying this Proxy Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = ProxyProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_proxy_used_by_list(request: web.Request, id) -> web.Response:
    """providers_proxy_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Proxy Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_rac_create(request: web.Request, body) -> web.Response:
    """providers_rac_create

    RACProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = RACProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_rac_destroy(request: web.Request, id) -> web.Response:
    """providers_rac_destroy

    RACProvider Viewset

    :param id: A unique integer value identifying this RAC Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_rac_list(request: web.Request, application__isnull=None, name__iexact=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """providers_rac_list

    RACProvider Viewset

    :param application__isnull: 
    :type application__isnull: bool
    :param name__iexact: 
    :type name__iexact: str
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


async def providers_rac_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_rac_partial_update

    RACProvider Viewset

    :param id: A unique integer value identifying this RAC Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedRACProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_rac_retrieve(request: web.Request, id) -> web.Response:
    """providers_rac_retrieve

    RACProvider Viewset

    :param id: A unique integer value identifying this RAC Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_rac_update(request: web.Request, id, body) -> web.Response:
    """providers_rac_update

    RACProvider Viewset

    :param id: A unique integer value identifying this RAC Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RACProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_rac_used_by_list(request: web.Request, id) -> web.Response:
    """providers_rac_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this RAC Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_radius_create(request: web.Request, body) -> web.Response:
    """providers_radius_create

    RadiusProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = RadiusProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_radius_destroy(request: web.Request, id) -> web.Response:
    """providers_radius_destroy

    RadiusProvider Viewset

    :param id: A unique integer value identifying this Radius Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_radius_list(request: web.Request, application__isnull=None, authorization_flow__slug__iexact=None, client_networks__iexact=None, name__iexact=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """providers_radius_list

    RadiusProvider Viewset

    :param application__isnull: 
    :type application__isnull: bool
    :param authorization_flow__slug__iexact: 
    :type authorization_flow__slug__iexact: str
    :param client_networks__iexact: 
    :type client_networks__iexact: str
    :param name__iexact: 
    :type name__iexact: str
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


async def providers_radius_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_radius_partial_update

    RadiusProvider Viewset

    :param id: A unique integer value identifying this Radius Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedRadiusProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_radius_retrieve(request: web.Request, id) -> web.Response:
    """providers_radius_retrieve

    RadiusProvider Viewset

    :param id: A unique integer value identifying this Radius Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_radius_update(request: web.Request, id, body) -> web.Response:
    """providers_radius_update

    RadiusProvider Viewset

    :param id: A unique integer value identifying this Radius Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RadiusProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_radius_used_by_list(request: web.Request, id) -> web.Response:
    """providers_radius_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Radius Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_saml_create(request: web.Request, body) -> web.Response:
    """providers_saml_create

    SAMLProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SAMLProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_saml_destroy(request: web.Request, id) -> web.Response:
    """providers_saml_destroy

    SAMLProvider Viewset

    :param id: A unique integer value identifying this SAML Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_saml_import_metadata_create(request: web.Request, name, authorization_flow, file) -> web.Response:
    """providers_saml_import_metadata_create

    Create provider from SAML Metadata

    :param name: 
    :type name: str
    :param authorization_flow: 
    :type authorization_flow: str
    :type authorization_flow: str
    :param file: 
    :type file: str

    """
    return web.Response(status=200)


async def providers_saml_list(request: web.Request, acs_url=None, assertion_valid_not_before=None, assertion_valid_not_on_or_after=None, audience=None, authentication_flow=None, authorization_flow=None, backchannel_application=None, default_relay_state=None, digest_algorithm=None, encryption_kp=None, is_backchannel=None, issuer=None, name=None, name_id_mapping=None, ordering=None, page=None, page_size=None, property_mappings=None, search=None, session_valid_not_on_or_after=None, sign_assertion=None, sign_response=None, signature_algorithm=None, signing_kp=None, sp_binding=None, verification_kp=None) -> web.Response:
    """providers_saml_list

    SAMLProvider Viewset

    :param acs_url: 
    :type acs_url: str
    :param assertion_valid_not_before: 
    :type assertion_valid_not_before: str
    :param assertion_valid_not_on_or_after: 
    :type assertion_valid_not_on_or_after: str
    :param audience: 
    :type audience: str
    :param authentication_flow: 
    :type authentication_flow: str
    :type authentication_flow: str
    :param authorization_flow: 
    :type authorization_flow: str
    :type authorization_flow: str
    :param backchannel_application: 
    :type backchannel_application: str
    :type backchannel_application: str
    :param default_relay_state: 
    :type default_relay_state: str
    :param digest_algorithm: 
    :type digest_algorithm: str
    :param encryption_kp: 
    :type encryption_kp: str
    :type encryption_kp: str
    :param is_backchannel: 
    :type is_backchannel: bool
    :param issuer: 
    :type issuer: str
    :param name: 
    :type name: str
    :param name_id_mapping: 
    :type name_id_mapping: str
    :type name_id_mapping: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param property_mappings: 
    :type property_mappings: List[str]
    :param search: A search term.
    :type search: str
    :param session_valid_not_on_or_after: 
    :type session_valid_not_on_or_after: str
    :param sign_assertion: 
    :type sign_assertion: bool
    :param sign_response: 
    :type sign_response: bool
    :param signature_algorithm: 
    :type signature_algorithm: str
    :param signing_kp: 
    :type signing_kp: str
    :type signing_kp: str
    :param sp_binding: This determines how authentik sends the response back to the Service Provider.  
    :type sp_binding: str
    :param verification_kp: 
    :type verification_kp: str
    :type verification_kp: str

    """
    return web.Response(status=200)


async def providers_saml_metadata_retrieve(request: web.Request, id, download=None, force_binding=None) -> web.Response:
    """providers_saml_metadata_retrieve

    Return metadata as XML string

    :param id: A unique integer value identifying this SAML Provider.
    :type id: int
    :param download: 
    :type download: bool
    :param force_binding: Optionally force the metadata to only include one binding.
    :type force_binding: str

    """
    return web.Response(status=200)


async def providers_saml_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_saml_partial_update

    SAMLProvider Viewset

    :param id: A unique integer value identifying this SAML Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSAMLProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_saml_preview_user_retrieve(request: web.Request, id, for_user=None) -> web.Response:
    """providers_saml_preview_user_retrieve

    Preview user data for provider

    :param id: A unique integer value identifying this SAML Provider.
    :type id: int
    :param for_user: 
    :type for_user: int

    """
    return web.Response(status=200)


async def providers_saml_retrieve(request: web.Request, id) -> web.Response:
    """providers_saml_retrieve

    SAMLProvider Viewset

    :param id: A unique integer value identifying this SAML Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_saml_update(request: web.Request, id, body) -> web.Response:
    """providers_saml_update

    SAMLProvider Viewset

    :param id: A unique integer value identifying this SAML Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SAMLProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_saml_used_by_list(request: web.Request, id) -> web.Response:
    """providers_saml_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this SAML Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_scim_create(request: web.Request, body) -> web.Response:
    """providers_scim_create

    SCIMProvider Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_scim_destroy(request: web.Request, id) -> web.Response:
    """providers_scim_destroy

    SCIMProvider Viewset

    :param id: A unique integer value identifying this SCIM Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_scim_groups_create(request: web.Request, body) -> web.Response:
    """providers_scim_groups_create

    SCIMProviderGroup Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMProviderGroupRequest.from_dict(body)
    return web.Response(status=200)


async def providers_scim_groups_destroy(request: web.Request, id) -> web.Response:
    """providers_scim_groups_destroy

    SCIMProviderGroup Viewset

    :param id: A UUID string identifying this scim provider group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_scim_groups_list(request: web.Request, group__group_uuid=None, group__name=None, ordering=None, page=None, page_size=None, provider__id=None, search=None) -> web.Response:
    """providers_scim_groups_list

    SCIMProviderGroup Viewset

    :param group__group_uuid: 
    :type group__group_uuid: str
    :type group__group_uuid: str
    :param group__name: 
    :type group__name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider__id: 
    :type provider__id: int
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def providers_scim_groups_retrieve(request: web.Request, id) -> web.Response:
    """providers_scim_groups_retrieve

    SCIMProviderGroup Viewset

    :param id: A UUID string identifying this scim provider group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_scim_groups_used_by_list(request: web.Request, id) -> web.Response:
    """providers_scim_groups_used_by_list

    Get a list of all objects that use this object

    :param id: A UUID string identifying this scim provider group.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_scim_list(request: web.Request, exclude_users_service_account=None, filter_group=None, name=None, ordering=None, page=None, page_size=None, search=None, url=None) -> web.Response:
    """providers_scim_list

    SCIMProvider Viewset

    :param exclude_users_service_account: 
    :type exclude_users_service_account: bool
    :param filter_group: 
    :type filter_group: str
    :type filter_group: str
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
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def providers_scim_partial_update(request: web.Request, id, body=None) -> web.Response:
    """providers_scim_partial_update

    SCIMProvider Viewset

    :param id: A unique integer value identifying this SCIM Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSCIMProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_scim_retrieve(request: web.Request, id) -> web.Response:
    """providers_scim_retrieve

    SCIMProvider Viewset

    :param id: A unique integer value identifying this SCIM Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_scim_sync_object_create(request: web.Request, id, body) -> web.Response:
    """providers_scim_sync_object_create

    Sync/Re-sync a single user/group object

    :param id: A unique integer value identifying this SCIM Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SyncObjectRequest.from_dict(body)
    return web.Response(status=200)


async def providers_scim_sync_status_retrieve(request: web.Request, id) -> web.Response:
    """providers_scim_sync_status_retrieve

    Get provider&#39;s sync status

    :param id: A unique integer value identifying this SCIM Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_scim_update(request: web.Request, id, body) -> web.Response:
    """providers_scim_update

    SCIMProvider Viewset

    :param id: A unique integer value identifying this SCIM Provider.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SCIMProviderRequest.from_dict(body)
    return web.Response(status=200)


async def providers_scim_used_by_list(request: web.Request, id) -> web.Response:
    """providers_scim_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this SCIM Provider.
    :type id: int

    """
    return web.Response(status=200)


async def providers_scim_users_create(request: web.Request, body) -> web.Response:
    """providers_scim_users_create

    SCIMProviderUser Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMProviderUserRequest.from_dict(body)
    return web.Response(status=200)


async def providers_scim_users_destroy(request: web.Request, id) -> web.Response:
    """providers_scim_users_destroy

    SCIMProviderUser Viewset

    :param id: A UUID string identifying this scim provider user.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_scim_users_list(request: web.Request, ordering=None, page=None, page_size=None, provider__id=None, search=None, user__id=None, user__username=None) -> web.Response:
    """providers_scim_users_list

    SCIMProviderUser Viewset

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider__id: 
    :type provider__id: int
    :param search: A search term.
    :type search: str
    :param user__id: 
    :type user__id: int
    :param user__username: 
    :type user__username: str

    """
    return web.Response(status=200)


async def providers_scim_users_retrieve(request: web.Request, id) -> web.Response:
    """providers_scim_users_retrieve

    SCIMProviderUser Viewset

    :param id: A UUID string identifying this scim provider user.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)


async def providers_scim_users_used_by_list(request: web.Request, id) -> web.Response:
    """providers_scim_users_used_by_list

    Get a list of all objects that use this object

    :param id: A UUID string identifying this scim provider user.
    :type id: str
    :type id: str

    """
    return web.Response(status=200)
