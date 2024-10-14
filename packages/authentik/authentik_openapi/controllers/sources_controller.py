from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.file_path_request import FilePathRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.group_o_auth_source_connection import GroupOAuthSourceConnection
from authentik_openapi.models.group_plex_source_connection import GroupPlexSourceConnection
from authentik_openapi.models.group_saml_source_connection import GroupSAMLSourceConnection
from authentik_openapi.models.ldap_debug import LDAPDebug
from authentik_openapi.models.ldap_source import LDAPSource
from authentik_openapi.models.ldap_source_request import LDAPSourceRequest
from authentik_openapi.models.o_auth_source import OAuthSource
from authentik_openapi.models.o_auth_source_request import OAuthSourceRequest
from authentik_openapi.models.paginated_group_o_auth_source_connection_list import PaginatedGroupOAuthSourceConnectionList
from authentik_openapi.models.paginated_group_plex_source_connection_list import PaginatedGroupPlexSourceConnectionList
from authentik_openapi.models.paginated_group_saml_source_connection_list import PaginatedGroupSAMLSourceConnectionList
from authentik_openapi.models.paginated_ldap_source_list import PaginatedLDAPSourceList
from authentik_openapi.models.paginated_o_auth_source_list import PaginatedOAuthSourceList
from authentik_openapi.models.paginated_plex_source_list import PaginatedPlexSourceList
from authentik_openapi.models.paginated_saml_source_list import PaginatedSAMLSourceList
from authentik_openapi.models.paginated_scim_source_group_list import PaginatedSCIMSourceGroupList
from authentik_openapi.models.paginated_scim_source_list import PaginatedSCIMSourceList
from authentik_openapi.models.paginated_scim_source_user_list import PaginatedSCIMSourceUserList
from authentik_openapi.models.paginated_source_list import PaginatedSourceList
from authentik_openapi.models.paginated_user_o_auth_source_connection_list import PaginatedUserOAuthSourceConnectionList
from authentik_openapi.models.paginated_user_plex_source_connection_list import PaginatedUserPlexSourceConnectionList
from authentik_openapi.models.paginated_user_saml_source_connection_list import PaginatedUserSAMLSourceConnectionList
from authentik_openapi.models.paginated_user_source_connection_list import PaginatedUserSourceConnectionList
from authentik_openapi.models.patched_ldap_source_request import PatchedLDAPSourceRequest
from authentik_openapi.models.patched_o_auth_source_request import PatchedOAuthSourceRequest
from authentik_openapi.models.patched_plex_source_request import PatchedPlexSourceRequest
from authentik_openapi.models.patched_saml_source_request import PatchedSAMLSourceRequest
from authentik_openapi.models.patched_scim_source_group_request import PatchedSCIMSourceGroupRequest
from authentik_openapi.models.patched_scim_source_request import PatchedSCIMSourceRequest
from authentik_openapi.models.patched_scim_source_user_request import PatchedSCIMSourceUserRequest
from authentik_openapi.models.patched_user_o_auth_source_connection_request import PatchedUserOAuthSourceConnectionRequest
from authentik_openapi.models.patched_user_plex_source_connection_request import PatchedUserPlexSourceConnectionRequest
from authentik_openapi.models.patched_user_saml_source_connection_request import PatchedUserSAMLSourceConnectionRequest
from authentik_openapi.models.plex_source import PlexSource
from authentik_openapi.models.plex_source_request import PlexSourceRequest
from authentik_openapi.models.plex_token_redeem_request import PlexTokenRedeemRequest
from authentik_openapi.models.redirect_challenge import RedirectChallenge
from authentik_openapi.models.saml_metadata import SAMLMetadata
from authentik_openapi.models.saml_source import SAMLSource
from authentik_openapi.models.saml_source_request import SAMLSourceRequest
from authentik_openapi.models.scim_source import SCIMSource
from authentik_openapi.models.scim_source_group import SCIMSourceGroup
from authentik_openapi.models.scim_source_group_request import SCIMSourceGroupRequest
from authentik_openapi.models.scim_source_request import SCIMSourceRequest
from authentik_openapi.models.scim_source_user import SCIMSourceUser
from authentik_openapi.models.scim_source_user_request import SCIMSourceUserRequest
from authentik_openapi.models.source import Source
from authentik_openapi.models.source_type import SourceType
from authentik_openapi.models.sync_status import SyncStatus
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.user_o_auth_source_connection import UserOAuthSourceConnection
from authentik_openapi.models.user_o_auth_source_connection_request import UserOAuthSourceConnectionRequest
from authentik_openapi.models.user_plex_source_connection import UserPlexSourceConnection
from authentik_openapi.models.user_plex_source_connection_request import UserPlexSourceConnectionRequest
from authentik_openapi.models.user_saml_source_connection import UserSAMLSourceConnection
from authentik_openapi.models.user_saml_source_connection_request import UserSAMLSourceConnectionRequest
from authentik_openapi.models.user_setting import UserSetting
from authentik_openapi.models.user_source_connection import UserSourceConnection
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def sources_all_destroy(request: web.Request, slug) -> web.Response:
    """sources_all_destroy

    Source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_all_list(request: web.Request, managed=None, name=None, ordering=None, page=None, page_size=None, search=None, slug=None) -> web.Response:
    """sources_all_list

    Source Viewset

    :param managed: 
    :type managed: str
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


async def sources_all_retrieve(request: web.Request, slug) -> web.Response:
    """sources_all_retrieve

    Source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_all_set_icon_create(request: web.Request, slug, file=None, clear=None) -> web.Response:
    """sources_all_set_icon_create

    Set source icon

    :param slug: 
    :type slug: str
    :param file: 
    :type file: str
    :param clear: 
    :type clear: bool

    """
    return web.Response(status=200)


async def sources_all_set_icon_url_create(request: web.Request, slug, body) -> web.Response:
    """sources_all_set_icon_url_create

    Set source icon (as URL)

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = FilePathRequest.from_dict(body)
    return web.Response(status=200)


async def sources_all_types_list(request: web.Request, ) -> web.Response:
    """sources_all_types_list

    Get all creatable types


    """
    return web.Response(status=200)


async def sources_all_used_by_list(request: web.Request, slug) -> web.Response:
    """sources_all_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_all_user_settings_list(request: web.Request, ) -> web.Response:
    """sources_all_user_settings_list

    Get all sources the user can configure


    """
    return web.Response(status=200)


async def sources_group_connections_oauth_create(request: web.Request, ) -> web.Response:
    """sources_group_connections_oauth_create

    Group-source connection Viewset


    """
    return web.Response(status=200)


async def sources_group_connections_oauth_destroy(request: web.Request, id) -> web.Response:
    """sources_group_connections_oauth_destroy

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_oauth_list(request: web.Request, group=None, ordering=None, page=None, page_size=None, search=None, source__slug=None) -> web.Response:
    """sources_group_connections_oauth_list

    Group-source connection Viewset

    :param group: 
    :type group: str
    :type group: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str

    """
    return web.Response(status=200)


async def sources_group_connections_oauth_partial_update(request: web.Request, id) -> web.Response:
    """sources_group_connections_oauth_partial_update

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_oauth_retrieve(request: web.Request, id) -> web.Response:
    """sources_group_connections_oauth_retrieve

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_oauth_update(request: web.Request, id) -> web.Response:
    """sources_group_connections_oauth_update

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_oauth_used_by_list(request: web.Request, id) -> web.Response:
    """sources_group_connections_oauth_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Group OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_plex_create(request: web.Request, ) -> web.Response:
    """sources_group_connections_plex_create

    Group-source connection Viewset


    """
    return web.Response(status=200)


async def sources_group_connections_plex_destroy(request: web.Request, id) -> web.Response:
    """sources_group_connections_plex_destroy

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_plex_list(request: web.Request, group=None, ordering=None, page=None, page_size=None, search=None, source__slug=None) -> web.Response:
    """sources_group_connections_plex_list

    Group-source connection Viewset

    :param group: 
    :type group: str
    :type group: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str

    """
    return web.Response(status=200)


async def sources_group_connections_plex_partial_update(request: web.Request, id) -> web.Response:
    """sources_group_connections_plex_partial_update

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_plex_retrieve(request: web.Request, id) -> web.Response:
    """sources_group_connections_plex_retrieve

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_plex_update(request: web.Request, id) -> web.Response:
    """sources_group_connections_plex_update

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_plex_used_by_list(request: web.Request, id) -> web.Response:
    """sources_group_connections_plex_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Group Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_saml_destroy(request: web.Request, id) -> web.Response:
    """sources_group_connections_saml_destroy

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_saml_list(request: web.Request, group=None, ordering=None, page=None, page_size=None, search=None, source__slug=None) -> web.Response:
    """sources_group_connections_saml_list

    Group-source connection Viewset

    :param group: 
    :type group: str
    :type group: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str

    """
    return web.Response(status=200)


async def sources_group_connections_saml_partial_update(request: web.Request, id) -> web.Response:
    """sources_group_connections_saml_partial_update

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_saml_retrieve(request: web.Request, id) -> web.Response:
    """sources_group_connections_saml_retrieve

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_saml_update(request: web.Request, id) -> web.Response:
    """sources_group_connections_saml_update

    Group-source connection Viewset

    :param id: A unique integer value identifying this Group SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_group_connections_saml_used_by_list(request: web.Request, id) -> web.Response:
    """sources_group_connections_saml_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Group SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_ldap_create(request: web.Request, body) -> web.Response:
    """sources_ldap_create

    LDAP Source Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = LDAPSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_ldap_debug_retrieve(request: web.Request, slug) -> web.Response:
    """sources_ldap_debug_retrieve

    Get raw LDAP data to debug

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_ldap_destroy(request: web.Request, slug) -> web.Response:
    """sources_ldap_destroy

    LDAP Source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_ldap_list(request: web.Request, additional_group_dn=None, additional_user_dn=None, base_dn=None, bind_cn=None, client_certificate=None, enabled=None, group_membership_field=None, group_object_filter=None, group_property_mappings=None, name=None, object_uniqueness_field=None, ordering=None, page=None, page_size=None, password_login_update_internal_password=None, peer_certificate=None, search=None, server_uri=None, slug=None, sni=None, start_tls=None, sync_groups=None, sync_parent_group=None, sync_users=None, sync_users_password=None, user_object_filter=None, user_property_mappings=None) -> web.Response:
    """sources_ldap_list

    LDAP Source Viewset

    :param additional_group_dn: 
    :type additional_group_dn: str
    :param additional_user_dn: 
    :type additional_user_dn: str
    :param base_dn: 
    :type base_dn: str
    :param bind_cn: 
    :type bind_cn: str
    :param client_certificate: 
    :type client_certificate: str
    :type client_certificate: str
    :param enabled: 
    :type enabled: bool
    :param group_membership_field: 
    :type group_membership_field: str
    :param group_object_filter: 
    :type group_object_filter: str
    :param group_property_mappings: 
    :type group_property_mappings: List[str]
    :param name: 
    :type name: str
    :param object_uniqueness_field: 
    :type object_uniqueness_field: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param password_login_update_internal_password: 
    :type password_login_update_internal_password: bool
    :param peer_certificate: 
    :type peer_certificate: str
    :type peer_certificate: str
    :param search: A search term.
    :type search: str
    :param server_uri: 
    :type server_uri: str
    :param slug: 
    :type slug: str
    :param sni: 
    :type sni: bool
    :param start_tls: 
    :type start_tls: bool
    :param sync_groups: 
    :type sync_groups: bool
    :param sync_parent_group: 
    :type sync_parent_group: str
    :type sync_parent_group: str
    :param sync_users: 
    :type sync_users: bool
    :param sync_users_password: 
    :type sync_users_password: bool
    :param user_object_filter: 
    :type user_object_filter: str
    :param user_property_mappings: 
    :type user_property_mappings: List[str]

    """
    return web.Response(status=200)


async def sources_ldap_partial_update(request: web.Request, slug, body=None) -> web.Response:
    """sources_ldap_partial_update

    LDAP Source Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedLDAPSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_ldap_retrieve(request: web.Request, slug) -> web.Response:
    """sources_ldap_retrieve

    LDAP Source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_ldap_sync_status_retrieve(request: web.Request, slug) -> web.Response:
    """sources_ldap_sync_status_retrieve

    Get source&#39;s sync status

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_ldap_update(request: web.Request, slug, body) -> web.Response:
    """sources_ldap_update

    LDAP Source Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = LDAPSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_ldap_used_by_list(request: web.Request, slug) -> web.Response:
    """sources_ldap_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_oauth_create(request: web.Request, body) -> web.Response:
    """sources_oauth_create

    Source Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = OAuthSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_oauth_destroy(request: web.Request, slug) -> web.Response:
    """sources_oauth_destroy

    Source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_oauth_list(request: web.Request, access_token_url=None, additional_scopes=None, authentication_flow=None, authorization_url=None, consumer_key=None, enabled=None, enrollment_flow=None, group_matching_mode=None, has_jwks=None, name=None, ordering=None, page=None, page_size=None, policy_engine_mode=None, profile_url=None, provider_type=None, request_token_url=None, search=None, slug=None, user_matching_mode=None) -> web.Response:
    """sources_oauth_list

    Source Viewset

    :param access_token_url: 
    :type access_token_url: str
    :param additional_scopes: 
    :type additional_scopes: str
    :param authentication_flow: 
    :type authentication_flow: str
    :type authentication_flow: str
    :param authorization_url: 
    :type authorization_url: str
    :param consumer_key: 
    :type consumer_key: str
    :param enabled: 
    :type enabled: bool
    :param enrollment_flow: 
    :type enrollment_flow: str
    :type enrollment_flow: str
    :param group_matching_mode: How the source determines if an existing group should be used or a new group created.  
    :type group_matching_mode: str
    :param has_jwks: Only return sources with JWKS data
    :type has_jwks: bool
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_engine_mode: 
    :type policy_engine_mode: str
    :param profile_url: 
    :type profile_url: str
    :param provider_type: 
    :type provider_type: str
    :param request_token_url: 
    :type request_token_url: str
    :param search: A search term.
    :type search: str
    :param slug: 
    :type slug: str
    :param user_matching_mode: How the source determines if an existing user should be authenticated or a new user enrolled.  
    :type user_matching_mode: str

    """
    return web.Response(status=200)


async def sources_oauth_partial_update(request: web.Request, slug, body=None) -> web.Response:
    """sources_oauth_partial_update

    Source Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedOAuthSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_oauth_retrieve(request: web.Request, slug) -> web.Response:
    """sources_oauth_retrieve

    Source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_oauth_source_types_list(request: web.Request, name=None) -> web.Response:
    """sources_oauth_source_types_list

    Get all creatable source types. If ?name is set, only returns the type for &lt;name&gt;. If &lt;name&gt; isn&#39;t found, returns the default type.

    :param name: 
    :type name: str

    """
    return web.Response(status=200)


async def sources_oauth_update(request: web.Request, slug, body) -> web.Response:
    """sources_oauth_update

    Source Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = OAuthSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_oauth_used_by_list(request: web.Request, slug) -> web.Response:
    """sources_oauth_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_plex_create(request: web.Request, body) -> web.Response:
    """sources_plex_create

    Plex source Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PlexSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_plex_destroy(request: web.Request, slug) -> web.Response:
    """sources_plex_destroy

    Plex source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_plex_list(request: web.Request, allow_friends=None, authentication_flow=None, client_id=None, enabled=None, enrollment_flow=None, group_matching_mode=None, name=None, ordering=None, page=None, page_size=None, policy_engine_mode=None, search=None, slug=None, user_matching_mode=None) -> web.Response:
    """sources_plex_list

    Plex source Viewset

    :param allow_friends: 
    :type allow_friends: bool
    :param authentication_flow: 
    :type authentication_flow: str
    :type authentication_flow: str
    :param client_id: 
    :type client_id: str
    :param enabled: 
    :type enabled: bool
    :param enrollment_flow: 
    :type enrollment_flow: str
    :type enrollment_flow: str
    :param group_matching_mode: How the source determines if an existing group should be used or a new group created.  
    :type group_matching_mode: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_engine_mode: 
    :type policy_engine_mode: str
    :param search: A search term.
    :type search: str
    :param slug: 
    :type slug: str
    :param user_matching_mode: How the source determines if an existing user should be authenticated or a new user enrolled.  
    :type user_matching_mode: str

    """
    return web.Response(status=200)


async def sources_plex_partial_update(request: web.Request, slug, body=None) -> web.Response:
    """sources_plex_partial_update

    Plex source Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPlexSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_plex_redeem_token_authenticated_create(request: web.Request, body, slug=None) -> web.Response:
    """sources_plex_redeem_token_authenticated_create

    Redeem a plex token for an authenticated user, creating a connection

    :param body: 
    :type body: dict | bytes
    :param slug: 
    :type slug: str

    """
    body = PlexTokenRedeemRequest.from_dict(body)
    return web.Response(status=200)


async def sources_plex_redeem_token_create(request: web.Request, body, slug=None) -> web.Response:
    """sources_plex_redeem_token_create

    Redeem a plex token, check it&#39;s access to resources against what&#39;s allowed for the source, and redirect to an authentication/enrollment flow.

    :param body: 
    :type body: dict | bytes
    :param slug: 
    :type slug: str

    """
    body = PlexTokenRedeemRequest.from_dict(body)
    return web.Response(status=200)


async def sources_plex_retrieve(request: web.Request, slug) -> web.Response:
    """sources_plex_retrieve

    Plex source Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_plex_update(request: web.Request, slug, body) -> web.Response:
    """sources_plex_update

    Plex source Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlexSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_plex_used_by_list(request: web.Request, slug) -> web.Response:
    """sources_plex_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_saml_create(request: web.Request, body) -> web.Response:
    """sources_saml_create

    SAMLSource Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SAMLSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_saml_destroy(request: web.Request, slug) -> web.Response:
    """sources_saml_destroy

    SAMLSource Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_saml_list(request: web.Request, allow_idp_initiated=None, authentication_flow=None, binding_type=None, digest_algorithm=None, enabled=None, enrollment_flow=None, issuer=None, managed=None, name=None, name_id_policy=None, ordering=None, page=None, page_size=None, policy_engine_mode=None, pre_authentication_flow=None, search=None, signature_algorithm=None, signing_kp=None, slo_url=None, slug=None, sso_url=None, temporary_user_delete_after=None, user_matching_mode=None, verification_kp=None) -> web.Response:
    """sources_saml_list

    SAMLSource Viewset

    :param allow_idp_initiated: 
    :type allow_idp_initiated: bool
    :param authentication_flow: 
    :type authentication_flow: str
    :type authentication_flow: str
    :param binding_type: 
    :type binding_type: str
    :param digest_algorithm: 
    :type digest_algorithm: str
    :param enabled: 
    :type enabled: bool
    :param enrollment_flow: 
    :type enrollment_flow: str
    :type enrollment_flow: str
    :param issuer: 
    :type issuer: str
    :param managed: 
    :type managed: str
    :param name: 
    :type name: str
    :param name_id_policy: NameID Policy sent to the IdP. Can be unset, in which case no Policy is sent.  
    :type name_id_policy: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param policy_engine_mode: 
    :type policy_engine_mode: str
    :param pre_authentication_flow: 
    :type pre_authentication_flow: str
    :type pre_authentication_flow: str
    :param search: A search term.
    :type search: str
    :param signature_algorithm: 
    :type signature_algorithm: str
    :param signing_kp: 
    :type signing_kp: str
    :type signing_kp: str
    :param slo_url: 
    :type slo_url: str
    :param slug: 
    :type slug: str
    :param sso_url: 
    :type sso_url: str
    :param temporary_user_delete_after: 
    :type temporary_user_delete_after: str
    :param user_matching_mode: How the source determines if an existing user should be authenticated or a new user enrolled.  
    :type user_matching_mode: str
    :param verification_kp: 
    :type verification_kp: str
    :type verification_kp: str

    """
    return web.Response(status=200)


async def sources_saml_metadata_retrieve(request: web.Request, slug) -> web.Response:
    """sources_saml_metadata_retrieve

    Return metadata as XML string

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_saml_partial_update(request: web.Request, slug, body=None) -> web.Response:
    """sources_saml_partial_update

    SAMLSource Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSAMLSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_saml_retrieve(request: web.Request, slug) -> web.Response:
    """sources_saml_retrieve

    SAMLSource Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_saml_update(request: web.Request, slug, body) -> web.Response:
    """sources_saml_update

    SAMLSource Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = SAMLSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_saml_used_by_list(request: web.Request, slug) -> web.Response:
    """sources_saml_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_scim_create(request: web.Request, body) -> web.Response:
    """sources_scim_create

    SCIMSource Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_destroy(request: web.Request, slug) -> web.Response:
    """sources_scim_destroy

    SCIMSource Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_scim_groups_create(request: web.Request, body) -> web.Response:
    """sources_scim_groups_create

    SCIMSourceGroup Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourceGroupRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_groups_destroy(request: web.Request, id) -> web.Response:
    """sources_scim_groups_destroy

    SCIMSourceGroup Viewset

    :param id: A unique value identifying this scim source group.
    :type id: str

    """
    return web.Response(status=200)


async def sources_scim_groups_list(request: web.Request, group__group_uuid=None, group__name=None, ordering=None, page=None, page_size=None, search=None, source__slug=None) -> web.Response:
    """sources_scim_groups_list

    SCIMSourceGroup Viewset

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
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str

    """
    return web.Response(status=200)


async def sources_scim_groups_partial_update(request: web.Request, id, body=None) -> web.Response:
    """sources_scim_groups_partial_update

    SCIMSourceGroup Viewset

    :param id: A unique value identifying this scim source group.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSCIMSourceGroupRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_groups_retrieve(request: web.Request, id) -> web.Response:
    """sources_scim_groups_retrieve

    SCIMSourceGroup Viewset

    :param id: A unique value identifying this scim source group.
    :type id: str

    """
    return web.Response(status=200)


async def sources_scim_groups_update(request: web.Request, id, body) -> web.Response:
    """sources_scim_groups_update

    SCIMSourceGroup Viewset

    :param id: A unique value identifying this scim source group.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourceGroupRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_groups_used_by_list(request: web.Request, id) -> web.Response:
    """sources_scim_groups_used_by_list

    Get a list of all objects that use this object

    :param id: A unique value identifying this scim source group.
    :type id: str

    """
    return web.Response(status=200)


async def sources_scim_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None, slug=None) -> web.Response:
    """sources_scim_list

    SCIMSource Viewset

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


async def sources_scim_partial_update(request: web.Request, slug, body=None) -> web.Response:
    """sources_scim_partial_update

    SCIMSource Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSCIMSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_retrieve(request: web.Request, slug) -> web.Response:
    """sources_scim_retrieve

    SCIMSource Viewset

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_scim_update(request: web.Request, slug, body) -> web.Response:
    """sources_scim_update

    SCIMSource Viewset

    :param slug: 
    :type slug: str
    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourceRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_used_by_list(request: web.Request, slug) -> web.Response:
    """sources_scim_used_by_list

    Get a list of all objects that use this object

    :param slug: 
    :type slug: str

    """
    return web.Response(status=200)


async def sources_scim_users_create(request: web.Request, body) -> web.Response:
    """sources_scim_users_create

    SCIMSourceUser Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourceUserRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_users_destroy(request: web.Request, id) -> web.Response:
    """sources_scim_users_destroy

    SCIMSourceUser Viewset

    :param id: A unique value identifying this scim source user.
    :type id: str

    """
    return web.Response(status=200)


async def sources_scim_users_list(request: web.Request, ordering=None, page=None, page_size=None, search=None, source__slug=None, user__id=None, user__username=None) -> web.Response:
    """sources_scim_users_list

    SCIMSourceUser Viewset

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str
    :param user__id: 
    :type user__id: int
    :param user__username: 
    :type user__username: str

    """
    return web.Response(status=200)


async def sources_scim_users_partial_update(request: web.Request, id, body=None) -> web.Response:
    """sources_scim_users_partial_update

    SCIMSourceUser Viewset

    :param id: A unique value identifying this scim source user.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSCIMSourceUserRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_users_retrieve(request: web.Request, id) -> web.Response:
    """sources_scim_users_retrieve

    SCIMSourceUser Viewset

    :param id: A unique value identifying this scim source user.
    :type id: str

    """
    return web.Response(status=200)


async def sources_scim_users_update(request: web.Request, id, body) -> web.Response:
    """sources_scim_users_update

    SCIMSourceUser Viewset

    :param id: A unique value identifying this scim source user.
    :type id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourceUserRequest.from_dict(body)
    return web.Response(status=200)


async def sources_scim_users_used_by_list(request: web.Request, id) -> web.Response:
    """sources_scim_users_used_by_list

    Get a list of all objects that use this object

    :param id: A unique value identifying this scim source user.
    :type id: str

    """
    return web.Response(status=200)


async def sources_user_connections_all_destroy(request: web.Request, id) -> web.Response:
    """sources_user_connections_all_destroy

    User-source connection Viewset

    :param id: A unique integer value identifying this user source connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_all_list(request: web.Request, ordering=None, page=None, page_size=None, search=None, source__slug=None, user=None) -> web.Response:
    """sources_user_connections_all_list

    User-source connection Viewset

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def sources_user_connections_all_partial_update(request: web.Request, id) -> web.Response:
    """sources_user_connections_all_partial_update

    User-source connection Viewset

    :param id: A unique integer value identifying this user source connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_all_retrieve(request: web.Request, id) -> web.Response:
    """sources_user_connections_all_retrieve

    User-source connection Viewset

    :param id: A unique integer value identifying this user source connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_all_update(request: web.Request, id) -> web.Response:
    """sources_user_connections_all_update

    User-source connection Viewset

    :param id: A unique integer value identifying this user source connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_all_used_by_list(request: web.Request, id) -> web.Response:
    """sources_user_connections_all_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this user source connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_oauth_create(request: web.Request, body) -> web.Response:
    """sources_user_connections_oauth_create

    Source Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = UserOAuthSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_oauth_destroy(request: web.Request, id) -> web.Response:
    """sources_user_connections_oauth_destroy

    Source Viewset

    :param id: A unique integer value identifying this User OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_oauth_list(request: web.Request, ordering=None, page=None, page_size=None, search=None, source__slug=None, user=None) -> web.Response:
    """sources_user_connections_oauth_list

    Source Viewset

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def sources_user_connections_oauth_partial_update(request: web.Request, id, body=None) -> web.Response:
    """sources_user_connections_oauth_partial_update

    Source Viewset

    :param id: A unique integer value identifying this User OAuth Source Connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserOAuthSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_oauth_retrieve(request: web.Request, id) -> web.Response:
    """sources_user_connections_oauth_retrieve

    Source Viewset

    :param id: A unique integer value identifying this User OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_oauth_update(request: web.Request, id, body) -> web.Response:
    """sources_user_connections_oauth_update

    Source Viewset

    :param id: A unique integer value identifying this User OAuth Source Connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserOAuthSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_oauth_used_by_list(request: web.Request, id) -> web.Response:
    """sources_user_connections_oauth_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this User OAuth Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_plex_create(request: web.Request, body) -> web.Response:
    """sources_user_connections_plex_create

    Plex Source connection Serializer

    :param body: 
    :type body: dict | bytes

    """
    body = UserPlexSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_plex_destroy(request: web.Request, id) -> web.Response:
    """sources_user_connections_plex_destroy

    Plex Source connection Serializer

    :param id: A unique integer value identifying this User Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_plex_list(request: web.Request, ordering=None, page=None, page_size=None, search=None, source__slug=None, user=None) -> web.Response:
    """sources_user_connections_plex_list

    Plex Source connection Serializer

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def sources_user_connections_plex_partial_update(request: web.Request, id, body=None) -> web.Response:
    """sources_user_connections_plex_partial_update

    Plex Source connection Serializer

    :param id: A unique integer value identifying this User Plex Source Connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserPlexSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_plex_retrieve(request: web.Request, id) -> web.Response:
    """sources_user_connections_plex_retrieve

    Plex Source connection Serializer

    :param id: A unique integer value identifying this User Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_plex_update(request: web.Request, id, body) -> web.Response:
    """sources_user_connections_plex_update

    Plex Source connection Serializer

    :param id: A unique integer value identifying this User Plex Source Connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserPlexSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_plex_used_by_list(request: web.Request, id) -> web.Response:
    """sources_user_connections_plex_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this User Plex Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_saml_create(request: web.Request, body) -> web.Response:
    """sources_user_connections_saml_create

    Source Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = UserSAMLSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_saml_destroy(request: web.Request, id) -> web.Response:
    """sources_user_connections_saml_destroy

    Source Viewset

    :param id: A unique integer value identifying this User SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_saml_list(request: web.Request, ordering=None, page=None, page_size=None, search=None, source__slug=None, user=None) -> web.Response:
    """sources_user_connections_saml_list

    Source Viewset

    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param source__slug: 
    :type source__slug: str
    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def sources_user_connections_saml_partial_update(request: web.Request, id, body=None) -> web.Response:
    """sources_user_connections_saml_partial_update

    Source Viewset

    :param id: A unique integer value identifying this User SAML Source Connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserSAMLSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_saml_retrieve(request: web.Request, id) -> web.Response:
    """sources_user_connections_saml_retrieve

    Source Viewset

    :param id: A unique integer value identifying this User SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)


async def sources_user_connections_saml_update(request: web.Request, id, body) -> web.Response:
    """sources_user_connections_saml_update

    Source Viewset

    :param id: A unique integer value identifying this User SAML Source Connection.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = UserSAMLSourceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def sources_user_connections_saml_used_by_list(request: web.Request, id) -> web.Response:
    """sources_user_connections_saml_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this User SAML Source Connection.
    :type id: int

    """
    return web.Response(status=200)
