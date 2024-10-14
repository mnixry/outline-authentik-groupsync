from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.google_workspace_provider_mapping import GoogleWorkspaceProviderMapping
from authentik_openapi.models.google_workspace_provider_mapping_request import GoogleWorkspaceProviderMappingRequest
from authentik_openapi.models.ldap_source_property_mapping import LDAPSourcePropertyMapping
from authentik_openapi.models.ldap_source_property_mapping_request import LDAPSourcePropertyMappingRequest
from authentik_openapi.models.microsoft_entra_provider_mapping import MicrosoftEntraProviderMapping
from authentik_openapi.models.microsoft_entra_provider_mapping_request import MicrosoftEntraProviderMappingRequest
from authentik_openapi.models.notification_webhook_mapping import NotificationWebhookMapping
from authentik_openapi.models.notification_webhook_mapping_request import NotificationWebhookMappingRequest
from authentik_openapi.models.o_auth_source_property_mapping import OAuthSourcePropertyMapping
from authentik_openapi.models.o_auth_source_property_mapping_request import OAuthSourcePropertyMappingRequest
from authentik_openapi.models.paginated_google_workspace_provider_mapping_list import PaginatedGoogleWorkspaceProviderMappingList
from authentik_openapi.models.paginated_ldap_source_property_mapping_list import PaginatedLDAPSourcePropertyMappingList
from authentik_openapi.models.paginated_microsoft_entra_provider_mapping_list import PaginatedMicrosoftEntraProviderMappingList
from authentik_openapi.models.paginated_notification_webhook_mapping_list import PaginatedNotificationWebhookMappingList
from authentik_openapi.models.paginated_o_auth_source_property_mapping_list import PaginatedOAuthSourcePropertyMappingList
from authentik_openapi.models.paginated_plex_source_property_mapping_list import PaginatedPlexSourcePropertyMappingList
from authentik_openapi.models.paginated_property_mapping_list import PaginatedPropertyMappingList
from authentik_openapi.models.paginated_rac_property_mapping_list import PaginatedRACPropertyMappingList
from authentik_openapi.models.paginated_radius_provider_property_mapping_list import PaginatedRadiusProviderPropertyMappingList
from authentik_openapi.models.paginated_saml_property_mapping_list import PaginatedSAMLPropertyMappingList
from authentik_openapi.models.paginated_saml_source_property_mapping_list import PaginatedSAMLSourcePropertyMappingList
from authentik_openapi.models.paginated_scim_mapping_list import PaginatedSCIMMappingList
from authentik_openapi.models.paginated_scim_source_property_mapping_list import PaginatedSCIMSourcePropertyMappingList
from authentik_openapi.models.paginated_scope_mapping_list import PaginatedScopeMappingList
from authentik_openapi.models.patched_google_workspace_provider_mapping_request import PatchedGoogleWorkspaceProviderMappingRequest
from authentik_openapi.models.patched_ldap_source_property_mapping_request import PatchedLDAPSourcePropertyMappingRequest
from authentik_openapi.models.patched_microsoft_entra_provider_mapping_request import PatchedMicrosoftEntraProviderMappingRequest
from authentik_openapi.models.patched_notification_webhook_mapping_request import PatchedNotificationWebhookMappingRequest
from authentik_openapi.models.patched_o_auth_source_property_mapping_request import PatchedOAuthSourcePropertyMappingRequest
from authentik_openapi.models.patched_plex_source_property_mapping_request import PatchedPlexSourcePropertyMappingRequest
from authentik_openapi.models.patched_rac_property_mapping_request import PatchedRACPropertyMappingRequest
from authentik_openapi.models.patched_radius_provider_property_mapping_request import PatchedRadiusProviderPropertyMappingRequest
from authentik_openapi.models.patched_saml_property_mapping_request import PatchedSAMLPropertyMappingRequest
from authentik_openapi.models.patched_saml_source_property_mapping_request import PatchedSAMLSourcePropertyMappingRequest
from authentik_openapi.models.patched_scim_mapping_request import PatchedSCIMMappingRequest
from authentik_openapi.models.patched_scim_source_property_mapping_request import PatchedSCIMSourcePropertyMappingRequest
from authentik_openapi.models.patched_scope_mapping_request import PatchedScopeMappingRequest
from authentik_openapi.models.plex_source_property_mapping import PlexSourcePropertyMapping
from authentik_openapi.models.plex_source_property_mapping_request import PlexSourcePropertyMappingRequest
from authentik_openapi.models.property_mapping import PropertyMapping
from authentik_openapi.models.property_mapping_test_request import PropertyMappingTestRequest
from authentik_openapi.models.property_mapping_test_result import PropertyMappingTestResult
from authentik_openapi.models.rac_property_mapping import RACPropertyMapping
from authentik_openapi.models.rac_property_mapping_request import RACPropertyMappingRequest
from authentik_openapi.models.radius_provider_property_mapping import RadiusProviderPropertyMapping
from authentik_openapi.models.radius_provider_property_mapping_request import RadiusProviderPropertyMappingRequest
from authentik_openapi.models.saml_property_mapping import SAMLPropertyMapping
from authentik_openapi.models.saml_property_mapping_request import SAMLPropertyMappingRequest
from authentik_openapi.models.saml_source_property_mapping import SAMLSourcePropertyMapping
from authentik_openapi.models.saml_source_property_mapping_request import SAMLSourcePropertyMappingRequest
from authentik_openapi.models.scim_mapping import SCIMMapping
from authentik_openapi.models.scim_mapping_request import SCIMMappingRequest
from authentik_openapi.models.scim_source_property_mapping import SCIMSourcePropertyMapping
from authentik_openapi.models.scim_source_property_mapping_request import SCIMSourcePropertyMappingRequest
from authentik_openapi.models.scope_mapping import ScopeMapping
from authentik_openapi.models.scope_mapping_request import ScopeMappingRequest
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def propertymappings_all_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_all_destroy

    PropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_all_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_all_list

    PropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_all_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_all_retrieve

    PropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_all_test_create(request: web.Request, pm_uuid, format_result=None, body=None) -> web.Response:
    """propertymappings_all_test_create

    Test Property Mapping

    :param pm_uuid: A UUID string identifying this Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param format_result: 
    :type format_result: bool
    :param body: 
    :type body: dict | bytes

    """
    body = PropertyMappingTestRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_all_types_list(request: web.Request, ) -> web.Response:
    """propertymappings_all_types_list

    Get all creatable types


    """
    return web.Response(status=200)


async def propertymappings_all_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_all_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_notification_create(request: web.Request, body) -> web.Response:
    """propertymappings_notification_create

    NotificationWebhookMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = NotificationWebhookMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_notification_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_notification_destroy

    NotificationWebhookMapping Viewset

    :param pm_uuid: A UUID string identifying this Webhook Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_notification_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_notification_list

    NotificationWebhookMapping Viewset

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


async def propertymappings_notification_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_notification_partial_update

    NotificationWebhookMapping Viewset

    :param pm_uuid: A UUID string identifying this Webhook Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedNotificationWebhookMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_notification_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_notification_retrieve

    NotificationWebhookMapping Viewset

    :param pm_uuid: A UUID string identifying this Webhook Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_notification_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_notification_update

    NotificationWebhookMapping Viewset

    :param pm_uuid: A UUID string identifying this Webhook Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = NotificationWebhookMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_notification_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_notification_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this Webhook Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_google_workspace_create(request: web.Request, body) -> web.Response:
    """propertymappings_provider_google_workspace_create

    GoogleWorkspaceProviderMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = GoogleWorkspaceProviderMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_google_workspace_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_google_workspace_destroy

    GoogleWorkspaceProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Google Workspace Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_google_workspace_list(request: web.Request, expression=None, managed=None, name=None, ordering=None, page=None, page_size=None, pm_uuid=None, search=None) -> web.Response:
    """propertymappings_provider_google_workspace_list

    GoogleWorkspaceProviderMapping Viewset

    :param expression: 
    :type expression: str
    :param managed: 
    :type managed: List[str]
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param pm_uuid: 
    :type pm_uuid: str
    :type pm_uuid: str
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def propertymappings_provider_google_workspace_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_provider_google_workspace_partial_update

    GoogleWorkspaceProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Google Workspace Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedGoogleWorkspaceProviderMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_google_workspace_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_google_workspace_retrieve

    GoogleWorkspaceProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Google Workspace Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_google_workspace_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_provider_google_workspace_update

    GoogleWorkspaceProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Google Workspace Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleWorkspaceProviderMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_google_workspace_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_google_workspace_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this Google Workspace Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_microsoft_entra_create(request: web.Request, body) -> web.Response:
    """propertymappings_provider_microsoft_entra_create

    MicrosoftEntraProviderMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = MicrosoftEntraProviderMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_microsoft_entra_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_microsoft_entra_destroy

    MicrosoftEntraProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Microsoft Entra Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_microsoft_entra_list(request: web.Request, expression=None, managed=None, name=None, ordering=None, page=None, page_size=None, pm_uuid=None, search=None) -> web.Response:
    """propertymappings_provider_microsoft_entra_list

    MicrosoftEntraProviderMapping Viewset

    :param expression: 
    :type expression: str
    :param managed: 
    :type managed: List[str]
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param pm_uuid: 
    :type pm_uuid: str
    :type pm_uuid: str
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def propertymappings_provider_microsoft_entra_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_provider_microsoft_entra_partial_update

    MicrosoftEntraProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Microsoft Entra Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedMicrosoftEntraProviderMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_microsoft_entra_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_microsoft_entra_retrieve

    MicrosoftEntraProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Microsoft Entra Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_microsoft_entra_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_provider_microsoft_entra_update

    MicrosoftEntraProviderMapping Viewset

    :param pm_uuid: A UUID string identifying this Microsoft Entra Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = MicrosoftEntraProviderMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_microsoft_entra_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_microsoft_entra_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this Microsoft Entra Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_rac_create(request: web.Request, body) -> web.Response:
    """propertymappings_provider_rac_create

    RACPropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = RACPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_rac_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_rac_destroy

    RACPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this RAC Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_rac_list(request: web.Request, managed=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_provider_rac_list

    RACPropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
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


async def propertymappings_provider_rac_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_provider_rac_partial_update

    RACPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this RAC Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedRACPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_rac_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_rac_retrieve

    RACPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this RAC Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_rac_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_provider_rac_update

    RACPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this RAC Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = RACPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_rac_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_rac_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this RAC Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_radius_create(request: web.Request, body) -> web.Response:
    """propertymappings_provider_radius_create

    RadiusProviderPropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = RadiusProviderPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_radius_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_radius_destroy

    RadiusProviderPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Radius Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_radius_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_provider_radius_list

    RadiusProviderPropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_provider_radius_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_provider_radius_partial_update

    RadiusProviderPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Radius Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedRadiusProviderPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_radius_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_radius_retrieve

    RadiusProviderPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Radius Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_radius_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_provider_radius_update

    RadiusProviderPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Radius Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = RadiusProviderPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_radius_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_radius_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this Radius Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_saml_create(request: web.Request, body) -> web.Response:
    """propertymappings_provider_saml_create

    SAMLPropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SAMLPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_saml_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_saml_destroy

    SAMLPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_saml_list(request: web.Request, friendly_name=None, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, saml_name=None, search=None) -> web.Response:
    """propertymappings_provider_saml_list

    SAMLPropertyMapping Viewset

    :param friendly_name: 
    :type friendly_name: str
    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param saml_name: 
    :type saml_name: str
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def propertymappings_provider_saml_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_provider_saml_partial_update

    SAMLPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSAMLPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_saml_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_saml_retrieve

    SAMLPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_saml_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_provider_saml_update

    SAMLPropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = SAMLPropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_saml_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_saml_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this SAML Provider Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_scim_create(request: web.Request, body) -> web.Response:
    """propertymappings_provider_scim_create

    SCIMMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_scim_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_scim_destroy

    SCIMMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_scim_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_provider_scim_list

    SCIMMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_provider_scim_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_provider_scim_partial_update

    SCIMMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSCIMMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_scim_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_scim_retrieve

    SCIMMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_scim_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_provider_scim_update

    SCIMMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = SCIMMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_scim_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_scim_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this SCIM Provider Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_scope_create(request: web.Request, body) -> web.Response:
    """propertymappings_provider_scope_create

    ScopeMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = ScopeMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_scope_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_scope_destroy

    ScopeMapping Viewset

    :param pm_uuid: A UUID string identifying this Scope Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_scope_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, scope_name=None, search=None) -> web.Response:
    """propertymappings_provider_scope_list

    ScopeMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param scope_name: 
    :type scope_name: str
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def propertymappings_provider_scope_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_provider_scope_partial_update

    ScopeMapping Viewset

    :param pm_uuid: A UUID string identifying this Scope Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedScopeMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_scope_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_scope_retrieve

    ScopeMapping Viewset

    :param pm_uuid: A UUID string identifying this Scope Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_provider_scope_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_provider_scope_update

    ScopeMapping Viewset

    :param pm_uuid: A UUID string identifying this Scope Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = ScopeMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_provider_scope_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_provider_scope_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this Scope Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_ldap_create(request: web.Request, body) -> web.Response:
    """propertymappings_source_ldap_create

    LDAP PropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = LDAPSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_ldap_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_ldap_destroy

    LDAP PropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this LDAP Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_ldap_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_source_ldap_list

    LDAP PropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_source_ldap_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_source_ldap_partial_update

    LDAP PropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this LDAP Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedLDAPSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_ldap_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_ldap_retrieve

    LDAP PropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this LDAP Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_ldap_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_source_ldap_update

    LDAP PropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this LDAP Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = LDAPSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_ldap_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_ldap_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this LDAP Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_oauth_create(request: web.Request, body) -> web.Response:
    """propertymappings_source_oauth_create

    OAuthSourcePropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = OAuthSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_oauth_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_oauth_destroy

    OAuthSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this OAuth Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_oauth_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_source_oauth_list

    OAuthSourcePropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_source_oauth_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_source_oauth_partial_update

    OAuthSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this OAuth Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedOAuthSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_oauth_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_oauth_retrieve

    OAuthSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this OAuth Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_oauth_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_source_oauth_update

    OAuthSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this OAuth Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = OAuthSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_oauth_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_oauth_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this OAuth Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_plex_create(request: web.Request, body) -> web.Response:
    """propertymappings_source_plex_create

    PlexSourcePropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PlexSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_plex_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_plex_destroy

    PlexSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Plex Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_plex_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_source_plex_list

    PlexSourcePropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_source_plex_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_source_plex_partial_update

    PlexSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Plex Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPlexSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_plex_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_plex_retrieve

    PlexSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Plex Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_plex_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_source_plex_update

    PlexSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this Plex Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PlexSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_plex_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_plex_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this Plex Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_saml_create(request: web.Request, body) -> web.Response:
    """propertymappings_source_saml_create

    SAMLSourcePropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SAMLSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_saml_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_saml_destroy

    SAMLSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_saml_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_source_saml_list

    SAMLSourcePropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_source_saml_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_source_saml_partial_update

    SAMLSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSAMLSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_saml_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_saml_retrieve

    SAMLSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_saml_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_source_saml_update

    SAMLSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SAML Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = SAMLSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_saml_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_saml_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this SAML Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_scim_create(request: web.Request, body) -> web.Response:
    """propertymappings_source_scim_create

    SCIMSourcePropertyMapping Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_scim_destroy(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_scim_destroy

    SCIMSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_scim_list(request: web.Request, managed=None, managed__isnull=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """propertymappings_source_scim_list

    SCIMSourcePropertyMapping Viewset

    :param managed: 
    :type managed: List[str]
    :param managed__isnull: 
    :type managed__isnull: bool
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


async def propertymappings_source_scim_partial_update(request: web.Request, pm_uuid, body=None) -> web.Response:
    """propertymappings_source_scim_partial_update

    SCIMSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSCIMSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_scim_retrieve(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_scim_retrieve

    SCIMSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)


async def propertymappings_source_scim_update(request: web.Request, pm_uuid, body) -> web.Response:
    """propertymappings_source_scim_update

    SCIMSourcePropertyMapping Viewset

    :param pm_uuid: A UUID string identifying this SCIM Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = SCIMSourcePropertyMappingRequest.from_dict(body)
    return web.Response(status=200)


async def propertymappings_source_scim_used_by_list(request: web.Request, pm_uuid) -> web.Response:
    """propertymappings_source_scim_used_by_list

    Get a list of all objects that use this object

    :param pm_uuid: A UUID string identifying this SCIM Source Property Mapping.
    :type pm_uuid: str
    :type pm_uuid: str

    """
    return web.Response(status=200)
