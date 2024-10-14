from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.certificate_data import CertificateData
from authentik_openapi.models.certificate_generation_request import CertificateGenerationRequest
from authentik_openapi.models.certificate_key_pair import CertificateKeyPair
from authentik_openapi.models.certificate_key_pair_request import CertificateKeyPairRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_certificate_key_pair_list import PaginatedCertificateKeyPairList
from authentik_openapi.models.patched_certificate_key_pair_request import PatchedCertificateKeyPairRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi import util


async def crypto_certificatekeypairs_create(request: web.Request, body) -> web.Response:
    """crypto_certificatekeypairs_create

    CertificateKeyPair Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = CertificateKeyPairRequest.from_dict(body)
    return web.Response(status=200)


async def crypto_certificatekeypairs_destroy(request: web.Request, kp_uuid) -> web.Response:
    """crypto_certificatekeypairs_destroy

    CertificateKeyPair Viewset

    :param kp_uuid: A UUID string identifying this Certificate-Key Pair.
    :type kp_uuid: str
    :type kp_uuid: str

    """
    return web.Response(status=200)


async def crypto_certificatekeypairs_generate_create(request: web.Request, body) -> web.Response:
    """crypto_certificatekeypairs_generate_create

    Generate a new, self-signed certificate-key pair

    :param body: 
    :type body: dict | bytes

    """
    body = CertificateGenerationRequest.from_dict(body)
    return web.Response(status=200)


async def crypto_certificatekeypairs_list(request: web.Request, has_key=None, include_details=None, managed=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """crypto_certificatekeypairs_list

    CertificateKeyPair Viewset

    :param has_key: Only return certificate-key pairs with keys
    :type has_key: bool
    :param include_details: 
    :type include_details: bool
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

    """
    return web.Response(status=200)


async def crypto_certificatekeypairs_partial_update(request: web.Request, kp_uuid, body=None) -> web.Response:
    """crypto_certificatekeypairs_partial_update

    CertificateKeyPair Viewset

    :param kp_uuid: A UUID string identifying this Certificate-Key Pair.
    :type kp_uuid: str
    :type kp_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedCertificateKeyPairRequest.from_dict(body)
    return web.Response(status=200)


async def crypto_certificatekeypairs_retrieve(request: web.Request, kp_uuid) -> web.Response:
    """crypto_certificatekeypairs_retrieve

    CertificateKeyPair Viewset

    :param kp_uuid: A UUID string identifying this Certificate-Key Pair.
    :type kp_uuid: str
    :type kp_uuid: str

    """
    return web.Response(status=200)


async def crypto_certificatekeypairs_update(request: web.Request, kp_uuid, body) -> web.Response:
    """crypto_certificatekeypairs_update

    CertificateKeyPair Viewset

    :param kp_uuid: A UUID string identifying this Certificate-Key Pair.
    :type kp_uuid: str
    :type kp_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = CertificateKeyPairRequest.from_dict(body)
    return web.Response(status=200)


async def crypto_certificatekeypairs_used_by_list(request: web.Request, kp_uuid) -> web.Response:
    """crypto_certificatekeypairs_used_by_list

    Get a list of all objects that use this object

    :param kp_uuid: A UUID string identifying this Certificate-Key Pair.
    :type kp_uuid: str
    :type kp_uuid: str

    """
    return web.Response(status=200)


async def crypto_certificatekeypairs_view_certificate_retrieve(request: web.Request, kp_uuid, download=None) -> web.Response:
    """crypto_certificatekeypairs_view_certificate_retrieve

    Return certificate-key pairs certificate and log access

    :param kp_uuid: A UUID string identifying this Certificate-Key Pair.
    :type kp_uuid: str
    :type kp_uuid: str
    :param download: 
    :type download: bool

    """
    return web.Response(status=200)


async def crypto_certificatekeypairs_view_private_key_retrieve(request: web.Request, kp_uuid, download=None) -> web.Response:
    """crypto_certificatekeypairs_view_private_key_retrieve

    Return certificate-key pairs private key and log access

    :param kp_uuid: A UUID string identifying this Certificate-Key Pair.
    :type kp_uuid: str
    :type kp_uuid: str
    :param download: 
    :type download: bool

    """
    return web.Response(status=200)
