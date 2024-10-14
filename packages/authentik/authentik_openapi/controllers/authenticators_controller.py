from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.device import Device
from authentik_openapi.models.duo_device import DuoDevice
from authentik_openapi.models.duo_device_request import DuoDeviceRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.paginated_duo_device_list import PaginatedDuoDeviceList
from authentik_openapi.models.paginated_sms_device_list import PaginatedSMSDeviceList
from authentik_openapi.models.paginated_static_device_list import PaginatedStaticDeviceList
from authentik_openapi.models.paginated_totp_device_list import PaginatedTOTPDeviceList
from authentik_openapi.models.paginated_web_authn_device_list import PaginatedWebAuthnDeviceList
from authentik_openapi.models.patched_duo_device_request import PatchedDuoDeviceRequest
from authentik_openapi.models.patched_sms_device_request import PatchedSMSDeviceRequest
from authentik_openapi.models.patched_static_device_request import PatchedStaticDeviceRequest
from authentik_openapi.models.patched_totp_device_request import PatchedTOTPDeviceRequest
from authentik_openapi.models.patched_web_authn_device_request import PatchedWebAuthnDeviceRequest
from authentik_openapi.models.sms_device import SMSDevice
from authentik_openapi.models.sms_device_request import SMSDeviceRequest
from authentik_openapi.models.static_device import StaticDevice
from authentik_openapi.models.static_device_request import StaticDeviceRequest
from authentik_openapi.models.totp_device import TOTPDevice
from authentik_openapi.models.totp_device_request import TOTPDeviceRequest
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi.models.web_authn_device import WebAuthnDevice
from authentik_openapi.models.web_authn_device_request import WebAuthnDeviceRequest
from authentik_openapi import util


async def authenticators_admin_all_list(request: web.Request, user=None) -> web.Response:
    """authenticators_admin_all_list

    Get all devices for current user

    :param user: 
    :type user: int

    """
    return web.Response(status=200)


async def authenticators_admin_duo_create(request: web.Request, body) -> web.Response:
    """authenticators_admin_duo_create

    Viewset for Duo authenticator devices (for admins)

    :param body: 
    :type body: dict | bytes

    """
    body = DuoDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_duo_destroy(request: web.Request, id) -> web.Response:
    """authenticators_admin_duo_destroy

    Viewset for Duo authenticator devices (for admins)

    :param id: A unique integer value identifying this Duo Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_duo_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_admin_duo_list

    Viewset for Duo authenticator devices (for admins)

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


async def authenticators_admin_duo_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_admin_duo_partial_update

    Viewset for Duo authenticator devices (for admins)

    :param id: A unique integer value identifying this Duo Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedDuoDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_duo_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_admin_duo_retrieve

    Viewset for Duo authenticator devices (for admins)

    :param id: A unique integer value identifying this Duo Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_duo_update(request: web.Request, id, body) -> web.Response:
    """authenticators_admin_duo_update

    Viewset for Duo authenticator devices (for admins)

    :param id: A unique integer value identifying this Duo Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DuoDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_sms_create(request: web.Request, body) -> web.Response:
    """authenticators_admin_sms_create

    Viewset for sms authenticator devices (for admins)

    :param body: 
    :type body: dict | bytes

    """
    body = SMSDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_sms_destroy(request: web.Request, id) -> web.Response:
    """authenticators_admin_sms_destroy

    Viewset for sms authenticator devices (for admins)

    :param id: A unique integer value identifying this SMS Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_sms_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_admin_sms_list

    Viewset for sms authenticator devices (for admins)

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


async def authenticators_admin_sms_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_admin_sms_partial_update

    Viewset for sms authenticator devices (for admins)

    :param id: A unique integer value identifying this SMS Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSMSDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_sms_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_admin_sms_retrieve

    Viewset for sms authenticator devices (for admins)

    :param id: A unique integer value identifying this SMS Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_sms_update(request: web.Request, id, body) -> web.Response:
    """authenticators_admin_sms_update

    Viewset for sms authenticator devices (for admins)

    :param id: A unique integer value identifying this SMS Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SMSDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_static_create(request: web.Request, body) -> web.Response:
    """authenticators_admin_static_create

    Viewset for static authenticator devices (for admins)

    :param body: 
    :type body: dict | bytes

    """
    body = StaticDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_static_destroy(request: web.Request, id) -> web.Response:
    """authenticators_admin_static_destroy

    Viewset for static authenticator devices (for admins)

    :param id: A unique integer value identifying this Static Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_static_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_admin_static_list

    Viewset for static authenticator devices (for admins)

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


async def authenticators_admin_static_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_admin_static_partial_update

    Viewset for static authenticator devices (for admins)

    :param id: A unique integer value identifying this Static Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedStaticDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_static_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_admin_static_retrieve

    Viewset for static authenticator devices (for admins)

    :param id: A unique integer value identifying this Static Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_static_update(request: web.Request, id, body) -> web.Response:
    """authenticators_admin_static_update

    Viewset for static authenticator devices (for admins)

    :param id: A unique integer value identifying this Static Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = StaticDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_totp_create(request: web.Request, body) -> web.Response:
    """authenticators_admin_totp_create

    Viewset for totp authenticator devices (for admins)

    :param body: 
    :type body: dict | bytes

    """
    body = TOTPDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_totp_destroy(request: web.Request, id) -> web.Response:
    """authenticators_admin_totp_destroy

    Viewset for totp authenticator devices (for admins)

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_totp_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_admin_totp_list

    Viewset for totp authenticator devices (for admins)

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


async def authenticators_admin_totp_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_admin_totp_partial_update

    Viewset for totp authenticator devices (for admins)

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedTOTPDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_totp_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_admin_totp_retrieve

    Viewset for totp authenticator devices (for admins)

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_totp_update(request: web.Request, id, body) -> web.Response:
    """authenticators_admin_totp_update

    Viewset for totp authenticator devices (for admins)

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TOTPDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_webauthn_create(request: web.Request, body) -> web.Response:
    """authenticators_admin_webauthn_create

    Viewset for WebAuthn authenticator devices (for admins)

    :param body: 
    :type body: dict | bytes

    """
    body = WebAuthnDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_webauthn_destroy(request: web.Request, id) -> web.Response:
    """authenticators_admin_webauthn_destroy

    Viewset for WebAuthn authenticator devices (for admins)

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_webauthn_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_admin_webauthn_list

    Viewset for WebAuthn authenticator devices (for admins)

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


async def authenticators_admin_webauthn_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_admin_webauthn_partial_update

    Viewset for WebAuthn authenticator devices (for admins)

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedWebAuthnDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_admin_webauthn_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_admin_webauthn_retrieve

    Viewset for WebAuthn authenticator devices (for admins)

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_admin_webauthn_update(request: web.Request, id, body) -> web.Response:
    """authenticators_admin_webauthn_update

    Viewset for WebAuthn authenticator devices (for admins)

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WebAuthnDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_all_list(request: web.Request, ) -> web.Response:
    """authenticators_all_list

    Get all devices for current user


    """
    return web.Response(status=200)


async def authenticators_duo_destroy(request: web.Request, id) -> web.Response:
    """authenticators_duo_destroy

    Viewset for Duo authenticator devices

    :param id: A unique integer value identifying this Duo Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_duo_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_duo_list

    Viewset for Duo authenticator devices

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


async def authenticators_duo_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_duo_partial_update

    Viewset for Duo authenticator devices

    :param id: A unique integer value identifying this Duo Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedDuoDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_duo_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_duo_retrieve

    Viewset for Duo authenticator devices

    :param id: A unique integer value identifying this Duo Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_duo_update(request: web.Request, id, body) -> web.Response:
    """authenticators_duo_update

    Viewset for Duo authenticator devices

    :param id: A unique integer value identifying this Duo Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = DuoDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_duo_used_by_list(request: web.Request, id) -> web.Response:
    """authenticators_duo_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Duo Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_sms_destroy(request: web.Request, id) -> web.Response:
    """authenticators_sms_destroy

    Viewset for sms authenticator devices

    :param id: A unique integer value identifying this SMS Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_sms_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_sms_list

    Viewset for sms authenticator devices

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


async def authenticators_sms_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_sms_partial_update

    Viewset for sms authenticator devices

    :param id: A unique integer value identifying this SMS Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSMSDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_sms_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_sms_retrieve

    Viewset for sms authenticator devices

    :param id: A unique integer value identifying this SMS Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_sms_update(request: web.Request, id, body) -> web.Response:
    """authenticators_sms_update

    Viewset for sms authenticator devices

    :param id: A unique integer value identifying this SMS Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = SMSDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_sms_used_by_list(request: web.Request, id) -> web.Response:
    """authenticators_sms_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this SMS Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_static_destroy(request: web.Request, id) -> web.Response:
    """authenticators_static_destroy

    Viewset for static authenticator devices

    :param id: A unique integer value identifying this Static Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_static_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_static_list

    Viewset for static authenticator devices

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


async def authenticators_static_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_static_partial_update

    Viewset for static authenticator devices

    :param id: A unique integer value identifying this Static Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedStaticDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_static_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_static_retrieve

    Viewset for static authenticator devices

    :param id: A unique integer value identifying this Static Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_static_update(request: web.Request, id, body) -> web.Response:
    """authenticators_static_update

    Viewset for static authenticator devices

    :param id: A unique integer value identifying this Static Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = StaticDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_static_used_by_list(request: web.Request, id) -> web.Response:
    """authenticators_static_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this Static Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_totp_destroy(request: web.Request, id) -> web.Response:
    """authenticators_totp_destroy

    Viewset for totp authenticator devices

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_totp_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_totp_list

    Viewset for totp authenticator devices

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


async def authenticators_totp_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_totp_partial_update

    Viewset for totp authenticator devices

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedTOTPDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_totp_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_totp_retrieve

    Viewset for totp authenticator devices

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_totp_update(request: web.Request, id, body) -> web.Response:
    """authenticators_totp_update

    Viewset for totp authenticator devices

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = TOTPDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_totp_used_by_list(request: web.Request, id) -> web.Response:
    """authenticators_totp_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this TOTP Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_webauthn_destroy(request: web.Request, id) -> web.Response:
    """authenticators_webauthn_destroy

    Viewset for WebAuthn authenticator devices

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_webauthn_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """authenticators_webauthn_list

    Viewset for WebAuthn authenticator devices

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


async def authenticators_webauthn_partial_update(request: web.Request, id, body=None) -> web.Response:
    """authenticators_webauthn_partial_update

    Viewset for WebAuthn authenticator devices

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedWebAuthnDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_webauthn_retrieve(request: web.Request, id) -> web.Response:
    """authenticators_webauthn_retrieve

    Viewset for WebAuthn authenticator devices

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int

    """
    return web.Response(status=200)


async def authenticators_webauthn_update(request: web.Request, id, body) -> web.Response:
    """authenticators_webauthn_update

    Viewset for WebAuthn authenticator devices

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = WebAuthnDeviceRequest.from_dict(body)
    return web.Response(status=200)


async def authenticators_webauthn_used_by_list(request: web.Request, id) -> web.Response:
    """authenticators_webauthn_used_by_list

    Get a list of all objects that use this object

    :param id: A unique integer value identifying this WebAuthn Device.
    :type id: int

    """
    return web.Response(status=200)
