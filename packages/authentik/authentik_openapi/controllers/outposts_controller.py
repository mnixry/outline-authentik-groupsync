from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.docker_service_connection import DockerServiceConnection
from authentik_openapi.models.docker_service_connection_request import DockerServiceConnectionRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.kubernetes_service_connection import KubernetesServiceConnection
from authentik_openapi.models.kubernetes_service_connection_request import KubernetesServiceConnectionRequest
from authentik_openapi.models.ldap_check_access import LDAPCheckAccess
from authentik_openapi.models.outpost import Outpost
from authentik_openapi.models.outpost_default_config import OutpostDefaultConfig
from authentik_openapi.models.outpost_health import OutpostHealth
from authentik_openapi.models.outpost_request import OutpostRequest
from authentik_openapi.models.paginated_docker_service_connection_list import PaginatedDockerServiceConnectionList
from authentik_openapi.models.paginated_kubernetes_service_connection_list import PaginatedKubernetesServiceConnectionList
from authentik_openapi.models.paginated_ldap_outpost_config_list import PaginatedLDAPOutpostConfigList
from authentik_openapi.models.paginated_outpost_list import PaginatedOutpostList
from authentik_openapi.models.paginated_proxy_outpost_config_list import PaginatedProxyOutpostConfigList
from authentik_openapi.models.paginated_radius_outpost_config_list import PaginatedRadiusOutpostConfigList
from authentik_openapi.models.paginated_service_connection_list import PaginatedServiceConnectionList
from authentik_openapi.models.patched_docker_service_connection_request import PatchedDockerServiceConnectionRequest
from authentik_openapi.models.patched_kubernetes_service_connection_request import PatchedKubernetesServiceConnectionRequest
from authentik_openapi.models.patched_outpost_request import PatchedOutpostRequest
from authentik_openapi.models.radius_check_access import RadiusCheckAccess
from authentik_openapi.models.service_connection import ServiceConnection
from authentik_openapi.models.service_connection_state import ServiceConnectionState
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def outposts_instances_create(request: web.Request, body) -> web.Response:
    """outposts_instances_create

    Outpost Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = OutpostRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_instances_default_settings_retrieve(request: web.Request, ) -> web.Response:
    """outposts_instances_default_settings_retrieve

    Global default outpost config


    """
    return web.Response(status=200)


async def outposts_instances_destroy(request: web.Request, uuid) -> web.Response:
    """outposts_instances_destroy

    Outpost Viewset

    :param uuid: A UUID string identifying this Outpost.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_instances_health_list(request: web.Request, uuid, managed__icontains=None, managed__iexact=None, name__icontains=None, name__iexact=None, ordering=None, providers__isnull=None, providers_by_pk=None, search=None, service_connection__name__icontains=None, service_connection__name__iexact=None) -> web.Response:
    """outposts_instances_health_list

    Get outposts current health

    :param uuid: A UUID string identifying this Outpost.
    :type uuid: str
    :type uuid: str
    :param managed__icontains: 
    :type managed__icontains: str
    :param managed__iexact: 
    :type managed__iexact: str
    :param name__icontains: 
    :type name__icontains: str
    :param name__iexact: 
    :type name__iexact: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param providers__isnull: 
    :type providers__isnull: bool
    :param providers_by_pk: 
    :type providers_by_pk: List[int]
    :param search: A search term.
    :type search: str
    :param service_connection__name__icontains: 
    :type service_connection__name__icontains: str
    :param service_connection__name__iexact: 
    :type service_connection__name__iexact: str

    """
    return web.Response(status=200)


async def outposts_instances_list(request: web.Request, managed__icontains=None, managed__iexact=None, name__icontains=None, name__iexact=None, ordering=None, page=None, page_size=None, providers__isnull=None, providers_by_pk=None, search=None, service_connection__name__icontains=None, service_connection__name__iexact=None) -> web.Response:
    """outposts_instances_list

    Outpost Viewset

    :param managed__icontains: 
    :type managed__icontains: str
    :param managed__iexact: 
    :type managed__iexact: str
    :param name__icontains: 
    :type name__icontains: str
    :param name__iexact: 
    :type name__iexact: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param providers__isnull: 
    :type providers__isnull: bool
    :param providers_by_pk: 
    :type providers_by_pk: List[int]
    :param search: A search term.
    :type search: str
    :param service_connection__name__icontains: 
    :type service_connection__name__icontains: str
    :param service_connection__name__iexact: 
    :type service_connection__name__iexact: str

    """
    return web.Response(status=200)


async def outposts_instances_partial_update(request: web.Request, uuid, body=None) -> web.Response:
    """outposts_instances_partial_update

    Outpost Viewset

    :param uuid: A UUID string identifying this Outpost.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedOutpostRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_instances_retrieve(request: web.Request, uuid) -> web.Response:
    """outposts_instances_retrieve

    Outpost Viewset

    :param uuid: A UUID string identifying this Outpost.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_instances_update(request: web.Request, uuid, body) -> web.Response:
    """outposts_instances_update

    Outpost Viewset

    :param uuid: A UUID string identifying this Outpost.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = OutpostRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_instances_used_by_list(request: web.Request, uuid) -> web.Response:
    """outposts_instances_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Outpost.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_ldap_access_check(request: web.Request, id, app_slug=None) -> web.Response:
    """outposts_ldap_access_check

    Check access to a single application by slug

    :param id: A unique integer value identifying this LDAP Provider.
    :type id: int
    :param app_slug: 
    :type app_slug: str

    """
    return web.Response(status=200)


async def outposts_ldap_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """outposts_ldap_list

    LDAPProvider Viewset

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


async def outposts_proxy_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """outposts_proxy_list

    ProxyProvider Viewset

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


async def outposts_radius_access_check(request: web.Request, id, app_slug=None) -> web.Response:
    """outposts_radius_access_check

    Check access to a single application by slug

    :param id: A unique integer value identifying this Radius Provider.
    :type id: int
    :param app_slug: 
    :type app_slug: str

    """
    return web.Response(status=200)


async def outposts_radius_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """outposts_radius_list

    RadiusProvider Viewset

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


async def outposts_service_connections_all_destroy(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_all_destroy

    ServiceConnection Viewset

    :param uuid: A UUID string identifying this Outpost Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_all_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """outposts_service_connections_all_list

    ServiceConnection Viewset

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


async def outposts_service_connections_all_retrieve(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_all_retrieve

    ServiceConnection Viewset

    :param uuid: A UUID string identifying this Outpost Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_all_state_retrieve(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_all_state_retrieve

    Get the service connection&#39;s state

    :param uuid: A UUID string identifying this Outpost Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_all_types_list(request: web.Request, ) -> web.Response:
    """outposts_service_connections_all_types_list

    Get all creatable types


    """
    return web.Response(status=200)


async def outposts_service_connections_all_used_by_list(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_all_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Outpost Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_docker_create(request: web.Request, body) -> web.Response:
    """outposts_service_connections_docker_create

    DockerServiceConnection Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = DockerServiceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_service_connections_docker_destroy(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_docker_destroy

    DockerServiceConnection Viewset

    :param uuid: A UUID string identifying this Docker Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_docker_list(request: web.Request, local=None, name=None, ordering=None, page=None, page_size=None, search=None, tls_authentication=None, tls_verification=None, url=None) -> web.Response:
    """outposts_service_connections_docker_list

    DockerServiceConnection Viewset

    :param local: 
    :type local: bool
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
    :param tls_authentication: 
    :type tls_authentication: str
    :type tls_authentication: str
    :param tls_verification: 
    :type tls_verification: str
    :type tls_verification: str
    :param url: 
    :type url: str

    """
    return web.Response(status=200)


async def outposts_service_connections_docker_partial_update(request: web.Request, uuid, body=None) -> web.Response:
    """outposts_service_connections_docker_partial_update

    DockerServiceConnection Viewset

    :param uuid: A UUID string identifying this Docker Service-Connection.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedDockerServiceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_service_connections_docker_retrieve(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_docker_retrieve

    DockerServiceConnection Viewset

    :param uuid: A UUID string identifying this Docker Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_docker_update(request: web.Request, uuid, body) -> web.Response:
    """outposts_service_connections_docker_update

    DockerServiceConnection Viewset

    :param uuid: A UUID string identifying this Docker Service-Connection.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = DockerServiceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_service_connections_docker_used_by_list(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_docker_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Docker Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_kubernetes_create(request: web.Request, body) -> web.Response:
    """outposts_service_connections_kubernetes_create

    KubernetesServiceConnection Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = KubernetesServiceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_service_connections_kubernetes_destroy(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_kubernetes_destroy

    KubernetesServiceConnection Viewset

    :param uuid: A UUID string identifying this Kubernetes Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_kubernetes_list(request: web.Request, local=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """outposts_service_connections_kubernetes_list

    KubernetesServiceConnection Viewset

    :param local: 
    :type local: bool
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


async def outposts_service_connections_kubernetes_partial_update(request: web.Request, uuid, body=None) -> web.Response:
    """outposts_service_connections_kubernetes_partial_update

    KubernetesServiceConnection Viewset

    :param uuid: A UUID string identifying this Kubernetes Service-Connection.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedKubernetesServiceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_service_connections_kubernetes_retrieve(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_kubernetes_retrieve

    KubernetesServiceConnection Viewset

    :param uuid: A UUID string identifying this Kubernetes Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)


async def outposts_service_connections_kubernetes_update(request: web.Request, uuid, body) -> web.Response:
    """outposts_service_connections_kubernetes_update

    KubernetesServiceConnection Viewset

    :param uuid: A UUID string identifying this Kubernetes Service-Connection.
    :type uuid: str
    :type uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = KubernetesServiceConnectionRequest.from_dict(body)
    return web.Response(status=200)


async def outposts_service_connections_kubernetes_used_by_list(request: web.Request, uuid) -> web.Response:
    """outposts_service_connections_kubernetes_used_by_list

    Get a list of all objects that use this object

    :param uuid: A UUID string identifying this Kubernetes Service-Connection.
    :type uuid: str
    :type uuid: str

    """
    return web.Response(status=200)
