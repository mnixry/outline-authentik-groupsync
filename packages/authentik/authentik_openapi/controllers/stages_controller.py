from typing import List, Dict
from aiohttp import web

from authentik_openapi.models.authenticator_duo_stage import AuthenticatorDuoStage
from authentik_openapi.models.authenticator_duo_stage_device_import_response import AuthenticatorDuoStageDeviceImportResponse
from authentik_openapi.models.authenticator_duo_stage_manual_device_import_request import AuthenticatorDuoStageManualDeviceImportRequest
from authentik_openapi.models.authenticator_duo_stage_request import AuthenticatorDuoStageRequest
from authentik_openapi.models.authenticator_sms_stage import AuthenticatorSMSStage
from authentik_openapi.models.authenticator_sms_stage_request import AuthenticatorSMSStageRequest
from authentik_openapi.models.authenticator_static_stage import AuthenticatorStaticStage
from authentik_openapi.models.authenticator_static_stage_request import AuthenticatorStaticStageRequest
from authentik_openapi.models.authenticator_totp_stage import AuthenticatorTOTPStage
from authentik_openapi.models.authenticator_totp_stage_request import AuthenticatorTOTPStageRequest
from authentik_openapi.models.authenticator_validate_stage import AuthenticatorValidateStage
from authentik_openapi.models.authenticator_validate_stage_request import AuthenticatorValidateStageRequest
from authentik_openapi.models.authenticator_web_authn_stage import AuthenticatorWebAuthnStage
from authentik_openapi.models.authenticator_web_authn_stage_request import AuthenticatorWebAuthnStageRequest
from authentik_openapi.models.captcha_stage import CaptchaStage
from authentik_openapi.models.captcha_stage_request import CaptchaStageRequest
from authentik_openapi.models.consent_stage import ConsentStage
from authentik_openapi.models.consent_stage_request import ConsentStageRequest
from authentik_openapi.models.deny_stage import DenyStage
from authentik_openapi.models.deny_stage_request import DenyStageRequest
from authentik_openapi.models.dummy_stage import DummyStage
from authentik_openapi.models.dummy_stage_request import DummyStageRequest
from authentik_openapi.models.duo_device_enrollment_status import DuoDeviceEnrollmentStatus
from authentik_openapi.models.email_stage import EmailStage
from authentik_openapi.models.email_stage_request import EmailStageRequest
from authentik_openapi.models.generic_error import GenericError
from authentik_openapi.models.identification_stage import IdentificationStage
from authentik_openapi.models.identification_stage_request import IdentificationStageRequest
from authentik_openapi.models.invitation import Invitation
from authentik_openapi.models.invitation_request import InvitationRequest
from authentik_openapi.models.invitation_stage import InvitationStage
from authentik_openapi.models.invitation_stage_request import InvitationStageRequest
from authentik_openapi.models.paginated_authenticator_duo_stage_list import PaginatedAuthenticatorDuoStageList
from authentik_openapi.models.paginated_authenticator_sms_stage_list import PaginatedAuthenticatorSMSStageList
from authentik_openapi.models.paginated_authenticator_static_stage_list import PaginatedAuthenticatorStaticStageList
from authentik_openapi.models.paginated_authenticator_totp_stage_list import PaginatedAuthenticatorTOTPStageList
from authentik_openapi.models.paginated_authenticator_validate_stage_list import PaginatedAuthenticatorValidateStageList
from authentik_openapi.models.paginated_authenticator_web_authn_stage_list import PaginatedAuthenticatorWebAuthnStageList
from authentik_openapi.models.paginated_captcha_stage_list import PaginatedCaptchaStageList
from authentik_openapi.models.paginated_consent_stage_list import PaginatedConsentStageList
from authentik_openapi.models.paginated_deny_stage_list import PaginatedDenyStageList
from authentik_openapi.models.paginated_dummy_stage_list import PaginatedDummyStageList
from authentik_openapi.models.paginated_email_stage_list import PaginatedEmailStageList
from authentik_openapi.models.paginated_identification_stage_list import PaginatedIdentificationStageList
from authentik_openapi.models.paginated_invitation_list import PaginatedInvitationList
from authentik_openapi.models.paginated_invitation_stage_list import PaginatedInvitationStageList
from authentik_openapi.models.paginated_password_stage_list import PaginatedPasswordStageList
from authentik_openapi.models.paginated_prompt_list import PaginatedPromptList
from authentik_openapi.models.paginated_prompt_stage_list import PaginatedPromptStageList
from authentik_openapi.models.paginated_source_stage_list import PaginatedSourceStageList
from authentik_openapi.models.paginated_stage_list import PaginatedStageList
from authentik_openapi.models.paginated_user_delete_stage_list import PaginatedUserDeleteStageList
from authentik_openapi.models.paginated_user_login_stage_list import PaginatedUserLoginStageList
from authentik_openapi.models.paginated_user_logout_stage_list import PaginatedUserLogoutStageList
from authentik_openapi.models.paginated_user_write_stage_list import PaginatedUserWriteStageList
from authentik_openapi.models.paginated_web_authn_device_type_list import PaginatedWebAuthnDeviceTypeList
from authentik_openapi.models.password_stage import PasswordStage
from authentik_openapi.models.password_stage_request import PasswordStageRequest
from authentik_openapi.models.patched_authenticator_duo_stage_request import PatchedAuthenticatorDuoStageRequest
from authentik_openapi.models.patched_authenticator_sms_stage_request import PatchedAuthenticatorSMSStageRequest
from authentik_openapi.models.patched_authenticator_static_stage_request import PatchedAuthenticatorStaticStageRequest
from authentik_openapi.models.patched_authenticator_totp_stage_request import PatchedAuthenticatorTOTPStageRequest
from authentik_openapi.models.patched_authenticator_validate_stage_request import PatchedAuthenticatorValidateStageRequest
from authentik_openapi.models.patched_authenticator_web_authn_stage_request import PatchedAuthenticatorWebAuthnStageRequest
from authentik_openapi.models.patched_captcha_stage_request import PatchedCaptchaStageRequest
from authentik_openapi.models.patched_consent_stage_request import PatchedConsentStageRequest
from authentik_openapi.models.patched_deny_stage_request import PatchedDenyStageRequest
from authentik_openapi.models.patched_dummy_stage_request import PatchedDummyStageRequest
from authentik_openapi.models.patched_email_stage_request import PatchedEmailStageRequest
from authentik_openapi.models.patched_identification_stage_request import PatchedIdentificationStageRequest
from authentik_openapi.models.patched_invitation_request import PatchedInvitationRequest
from authentik_openapi.models.patched_invitation_stage_request import PatchedInvitationStageRequest
from authentik_openapi.models.patched_password_stage_request import PatchedPasswordStageRequest
from authentik_openapi.models.patched_prompt_request import PatchedPromptRequest
from authentik_openapi.models.patched_prompt_stage_request import PatchedPromptStageRequest
from authentik_openapi.models.patched_source_stage_request import PatchedSourceStageRequest
from authentik_openapi.models.patched_user_delete_stage_request import PatchedUserDeleteStageRequest
from authentik_openapi.models.patched_user_login_stage_request import PatchedUserLoginStageRequest
from authentik_openapi.models.patched_user_logout_stage_request import PatchedUserLogoutStageRequest
from authentik_openapi.models.patched_user_write_stage_request import PatchedUserWriteStageRequest
from authentik_openapi.models.prompt import Prompt
from authentik_openapi.models.prompt_challenge import PromptChallenge
from authentik_openapi.models.prompt_request import PromptRequest
from authentik_openapi.models.prompt_stage import PromptStage
from authentik_openapi.models.prompt_stage_request import PromptStageRequest
from authentik_openapi.models.source_stage import SourceStage
from authentik_openapi.models.source_stage_request import SourceStageRequest
from authentik_openapi.models.stage import Stage
from authentik_openapi.models.type_create import TypeCreate
from authentik_openapi.models.used_by import UsedBy
from authentik_openapi.models.user_delete_stage import UserDeleteStage
from authentik_openapi.models.user_delete_stage_request import UserDeleteStageRequest
from authentik_openapi.models.user_login_stage import UserLoginStage
from authentik_openapi.models.user_login_stage_request import UserLoginStageRequest
from authentik_openapi.models.user_logout_stage import UserLogoutStage
from authentik_openapi.models.user_logout_stage_request import UserLogoutStageRequest
from authentik_openapi.models.user_setting import UserSetting
from authentik_openapi.models.user_write_stage import UserWriteStage
from authentik_openapi.models.user_write_stage_request import UserWriteStageRequest
from authentik_openapi.models.validation_error import ValidationError
from authentik_openapi.models.web_authn_device_type import WebAuthnDeviceType
from authentik_openapi import util


async def stages_all_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_all_destroy

    Stage Viewset

    :param stage_uuid: A UUID string identifying this authentik.providers.oauth2.views.authorize.OAuthFulfillmentStage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_all_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """stages_all_list

    Stage Viewset

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


async def stages_all_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_all_retrieve

    Stage Viewset

    :param stage_uuid: A UUID string identifying this authentik.providers.oauth2.views.authorize.OAuthFulfillmentStage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_all_types_list(request: web.Request, ) -> web.Response:
    """stages_all_types_list

    Get all creatable types


    """
    return web.Response(status=200)


async def stages_all_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_all_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this authentik.providers.oauth2.views.authorize.OAuthFulfillmentStage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_all_user_settings_list(request: web.Request, ) -> web.Response:
    """stages_all_user_settings_list

    Get all stages the user can configure


    """
    return web.Response(status=200)


async def stages_authenticator_duo_create(request: web.Request, body) -> web.Response:
    """stages_authenticator_duo_create

    AuthenticatorDuoStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorDuoStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_duo_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_duo_destroy

    AuthenticatorDuoStage Viewset

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_duo_enrollment_status_create(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_duo_enrollment_status_create

    Check enrollment status of user details in current session

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_duo_import_device_manual_create(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_authenticator_duo_import_device_manual_create

    Import duo devices into authentik

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorDuoStageManualDeviceImportRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_duo_import_devices_automatic_create(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_duo_import_devices_automatic_create

    Import duo devices into authentik

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_duo_list(request: web.Request, api_hostname=None, client_id=None, configure_flow=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """stages_authenticator_duo_list

    AuthenticatorDuoStage Viewset

    :param api_hostname: 
    :type api_hostname: str
    :param client_id: 
    :type client_id: str
    :param configure_flow: 
    :type configure_flow: str
    :type configure_flow: str
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


async def stages_authenticator_duo_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_authenticator_duo_partial_update

    AuthenticatorDuoStage Viewset

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedAuthenticatorDuoStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_duo_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_duo_retrieve

    AuthenticatorDuoStage Viewset

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_duo_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_authenticator_duo_update

    AuthenticatorDuoStage Viewset

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorDuoStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_duo_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_duo_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Duo Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_sms_create(request: web.Request, body) -> web.Response:
    """stages_authenticator_sms_create

    AuthenticatorSMSStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorSMSStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_sms_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_sms_destroy

    AuthenticatorSMSStage Viewset

    :param stage_uuid: A UUID string identifying this SMS Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_sms_list(request: web.Request, account_sid=None, auth=None, auth_password=None, auth_type=None, configure_flow=None, friendly_name=None, from_number=None, mapping=None, name=None, ordering=None, page=None, page_size=None, provider=None, search=None, stage_uuid=None, verify_only=None) -> web.Response:
    """stages_authenticator_sms_list

    AuthenticatorSMSStage Viewset

    :param account_sid: 
    :type account_sid: str
    :param auth: 
    :type auth: str
    :param auth_password: 
    :type auth_password: str
    :param auth_type: 
    :type auth_type: str
    :param configure_flow: 
    :type configure_flow: str
    :type configure_flow: str
    :param friendly_name: 
    :type friendly_name: str
    :param from_number: 
    :type from_number: str
    :param mapping: 
    :type mapping: str
    :type mapping: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param provider: 
    :type provider: str
    :param search: A search term.
    :type search: str
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str
    :param verify_only: 
    :type verify_only: bool

    """
    return web.Response(status=200)


async def stages_authenticator_sms_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_authenticator_sms_partial_update

    AuthenticatorSMSStage Viewset

    :param stage_uuid: A UUID string identifying this SMS Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedAuthenticatorSMSStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_sms_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_sms_retrieve

    AuthenticatorSMSStage Viewset

    :param stage_uuid: A UUID string identifying this SMS Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_sms_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_authenticator_sms_update

    AuthenticatorSMSStage Viewset

    :param stage_uuid: A UUID string identifying this SMS Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorSMSStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_sms_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_sms_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this SMS Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_static_create(request: web.Request, body) -> web.Response:
    """stages_authenticator_static_create

    AuthenticatorStaticStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorStaticStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_static_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_static_destroy

    AuthenticatorStaticStage Viewset

    :param stage_uuid: A UUID string identifying this Static Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_static_list(request: web.Request, configure_flow=None, friendly_name=None, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None, token_count=None, token_length=None) -> web.Response:
    """stages_authenticator_static_list

    AuthenticatorStaticStage Viewset

    :param configure_flow: 
    :type configure_flow: str
    :type configure_flow: str
    :param friendly_name: 
    :type friendly_name: str
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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str
    :param token_count: 
    :type token_count: int
    :param token_length: 
    :type token_length: int

    """
    return web.Response(status=200)


async def stages_authenticator_static_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_authenticator_static_partial_update

    AuthenticatorStaticStage Viewset

    :param stage_uuid: A UUID string identifying this Static Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedAuthenticatorStaticStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_static_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_static_retrieve

    AuthenticatorStaticStage Viewset

    :param stage_uuid: A UUID string identifying this Static Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_static_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_authenticator_static_update

    AuthenticatorStaticStage Viewset

    :param stage_uuid: A UUID string identifying this Static Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorStaticStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_static_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_static_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Static Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_totp_create(request: web.Request, body) -> web.Response:
    """stages_authenticator_totp_create

    AuthenticatorTOTPStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorTOTPStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_totp_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_totp_destroy

    AuthenticatorTOTPStage Viewset

    :param stage_uuid: A UUID string identifying this TOTP Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_totp_list(request: web.Request, configure_flow=None, digits=None, friendly_name=None, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None) -> web.Response:
    """stages_authenticator_totp_list

    AuthenticatorTOTPStage Viewset

    :param configure_flow: 
    :type configure_flow: str
    :type configure_flow: str
    :param digits: 
    :type digits: str
    :param friendly_name: 
    :type friendly_name: str
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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_totp_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_authenticator_totp_partial_update

    AuthenticatorTOTPStage Viewset

    :param stage_uuid: A UUID string identifying this TOTP Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedAuthenticatorTOTPStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_totp_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_totp_retrieve

    AuthenticatorTOTPStage Viewset

    :param stage_uuid: A UUID string identifying this TOTP Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_totp_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_authenticator_totp_update

    AuthenticatorTOTPStage Viewset

    :param stage_uuid: A UUID string identifying this TOTP Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorTOTPStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_totp_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_totp_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this TOTP Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_validate_create(request: web.Request, body) -> web.Response:
    """stages_authenticator_validate_create

    AuthenticatorValidateStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorValidateStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_validate_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_validate_destroy

    AuthenticatorValidateStage Viewset

    :param stage_uuid: A UUID string identifying this Authenticator Validation Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_validate_list(request: web.Request, configuration_stages=None, name=None, not_configured_action=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """stages_authenticator_validate_list

    AuthenticatorValidateStage Viewset

    :param configuration_stages: 
    :type configuration_stages: List[str]
    :param name: 
    :type name: str
    :param not_configured_action: 
    :type not_configured_action: str
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


async def stages_authenticator_validate_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_authenticator_validate_partial_update

    AuthenticatorValidateStage Viewset

    :param stage_uuid: A UUID string identifying this Authenticator Validation Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedAuthenticatorValidateStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_validate_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_validate_retrieve

    AuthenticatorValidateStage Viewset

    :param stage_uuid: A UUID string identifying this Authenticator Validation Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_validate_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_authenticator_validate_update

    AuthenticatorValidateStage Viewset

    :param stage_uuid: A UUID string identifying this Authenticator Validation Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorValidateStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_validate_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_validate_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Authenticator Validation Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_webauthn_create(request: web.Request, body) -> web.Response:
    """stages_authenticator_webauthn_create

    AuthenticatorWebAuthnStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorWebAuthnStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_webauthn_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_webauthn_destroy

    AuthenticatorWebAuthnStage Viewset

    :param stage_uuid: A UUID string identifying this WebAuthn Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_webauthn_device_types_list(request: web.Request, aaguid=None, description=None, icon=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """stages_authenticator_webauthn_device_types_list

    WebAuthnDeviceType Viewset

    :param aaguid: 
    :type aaguid: str
    :type aaguid: str
    :param description: 
    :type description: str
    :param icon: 
    :type icon: str
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


async def stages_authenticator_webauthn_device_types_retrieve(request: web.Request, aaguid) -> web.Response:
    """stages_authenticator_webauthn_device_types_retrieve

    WebAuthnDeviceType Viewset

    :param aaguid: A UUID string identifying this WebAuthn Device type.
    :type aaguid: str
    :type aaguid: str

    """
    return web.Response(status=200)


async def stages_authenticator_webauthn_list(request: web.Request, authenticator_attachment=None, configure_flow=None, device_type_restrictions=None, friendly_name=None, name=None, ordering=None, page=None, page_size=None, resident_key_requirement=None, search=None, stage_uuid=None, user_verification=None) -> web.Response:
    """stages_authenticator_webauthn_list

    AuthenticatorWebAuthnStage Viewset

    :param authenticator_attachment: 
    :type authenticator_attachment: str
    :param configure_flow: 
    :type configure_flow: str
    :type configure_flow: str
    :param device_type_restrictions: 
    :type device_type_restrictions: List[str]
    :param friendly_name: 
    :type friendly_name: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param resident_key_requirement: 
    :type resident_key_requirement: str
    :param search: A search term.
    :type search: str
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str
    :param user_verification: 
    :type user_verification: str

    """
    return web.Response(status=200)


async def stages_authenticator_webauthn_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_authenticator_webauthn_partial_update

    AuthenticatorWebAuthnStage Viewset

    :param stage_uuid: A UUID string identifying this WebAuthn Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedAuthenticatorWebAuthnStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_webauthn_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_webauthn_retrieve

    AuthenticatorWebAuthnStage Viewset

    :param stage_uuid: A UUID string identifying this WebAuthn Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_authenticator_webauthn_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_authenticator_webauthn_update

    AuthenticatorWebAuthnStage Viewset

    :param stage_uuid: A UUID string identifying this WebAuthn Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = AuthenticatorWebAuthnStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_authenticator_webauthn_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_authenticator_webauthn_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this WebAuthn Authenticator Setup Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_captcha_create(request: web.Request, body) -> web.Response:
    """stages_captcha_create

    CaptchaStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = CaptchaStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_captcha_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_captcha_destroy

    CaptchaStage Viewset

    :param stage_uuid: A UUID string identifying this Captcha Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_captcha_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, public_key=None, search=None) -> web.Response:
    """stages_captcha_list

    CaptchaStage Viewset

    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param public_key: 
    :type public_key: str
    :param search: A search term.
    :type search: str

    """
    return web.Response(status=200)


async def stages_captcha_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_captcha_partial_update

    CaptchaStage Viewset

    :param stage_uuid: A UUID string identifying this Captcha Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedCaptchaStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_captcha_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_captcha_retrieve

    CaptchaStage Viewset

    :param stage_uuid: A UUID string identifying this Captcha Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_captcha_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_captcha_update

    CaptchaStage Viewset

    :param stage_uuid: A UUID string identifying this Captcha Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = CaptchaStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_captcha_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_captcha_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Captcha Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_consent_create(request: web.Request, body) -> web.Response:
    """stages_consent_create

    ConsentStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = ConsentStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_consent_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_consent_destroy

    ConsentStage Viewset

    :param stage_uuid: A UUID string identifying this Consent Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_consent_list(request: web.Request, consent_expire_in=None, mode=None, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None) -> web.Response:
    """stages_consent_list

    ConsentStage Viewset

    :param consent_expire_in: 
    :type consent_expire_in: str
    :param mode: 
    :type mode: str
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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_consent_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_consent_partial_update

    ConsentStage Viewset

    :param stage_uuid: A UUID string identifying this Consent Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedConsentStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_consent_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_consent_retrieve

    ConsentStage Viewset

    :param stage_uuid: A UUID string identifying this Consent Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_consent_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_consent_update

    ConsentStage Viewset

    :param stage_uuid: A UUID string identifying this Consent Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = ConsentStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_consent_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_consent_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Consent Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_deny_create(request: web.Request, body) -> web.Response:
    """stages_deny_create

    DenyStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = DenyStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_deny_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_deny_destroy

    DenyStage Viewset

    :param stage_uuid: A UUID string identifying this Deny Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_deny_list(request: web.Request, deny_message=None, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None) -> web.Response:
    """stages_deny_list

    DenyStage Viewset

    :param deny_message: 
    :type deny_message: str
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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_deny_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_deny_partial_update

    DenyStage Viewset

    :param stage_uuid: A UUID string identifying this Deny Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedDenyStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_deny_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_deny_retrieve

    DenyStage Viewset

    :param stage_uuid: A UUID string identifying this Deny Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_deny_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_deny_update

    DenyStage Viewset

    :param stage_uuid: A UUID string identifying this Deny Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = DenyStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_deny_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_deny_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Deny Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_dummy_create(request: web.Request, body) -> web.Response:
    """stages_dummy_create

    DummyStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = DummyStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_dummy_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_dummy_destroy

    DummyStage Viewset

    :param stage_uuid: A UUID string identifying this Dummy Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_dummy_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None, throw_error=None) -> web.Response:
    """stages_dummy_list

    DummyStage Viewset

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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str
    :param throw_error: 
    :type throw_error: bool

    """
    return web.Response(status=200)


async def stages_dummy_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_dummy_partial_update

    DummyStage Viewset

    :param stage_uuid: A UUID string identifying this Dummy Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedDummyStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_dummy_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_dummy_retrieve

    DummyStage Viewset

    :param stage_uuid: A UUID string identifying this Dummy Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_dummy_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_dummy_update

    DummyStage Viewset

    :param stage_uuid: A UUID string identifying this Dummy Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = DummyStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_dummy_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_dummy_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Dummy Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_email_create(request: web.Request, body) -> web.Response:
    """stages_email_create

    EmailStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = EmailStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_email_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_email_destroy

    EmailStage Viewset

    :param stage_uuid: A UUID string identifying this Email Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_email_list(request: web.Request, activate_user_on_success=None, from_address=None, host=None, name=None, ordering=None, page=None, page_size=None, port=None, search=None, subject=None, template=None, timeout=None, token_expiry=None, use_global_settings=None, use_ssl=None, use_tls=None, username=None) -> web.Response:
    """stages_email_list

    EmailStage Viewset

    :param activate_user_on_success: 
    :type activate_user_on_success: bool
    :param from_address: 
    :type from_address: str
    :param host: 
    :type host: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param port: 
    :type port: int
    :param search: A search term.
    :type search: str
    :param subject: 
    :type subject: str
    :param template: 
    :type template: str
    :param timeout: 
    :type timeout: int
    :param token_expiry: 
    :type token_expiry: int
    :param use_global_settings: 
    :type use_global_settings: bool
    :param use_ssl: 
    :type use_ssl: bool
    :param use_tls: 
    :type use_tls: bool
    :param username: 
    :type username: str

    """
    return web.Response(status=200)


async def stages_email_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_email_partial_update

    EmailStage Viewset

    :param stage_uuid: A UUID string identifying this Email Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedEmailStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_email_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_email_retrieve

    EmailStage Viewset

    :param stage_uuid: A UUID string identifying this Email Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_email_templates_list(request: web.Request, ) -> web.Response:
    """stages_email_templates_list

    Get all available templates, including custom templates


    """
    return web.Response(status=200)


async def stages_email_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_email_update

    EmailStage Viewset

    :param stage_uuid: A UUID string identifying this Email Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = EmailStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_email_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_email_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Email Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_identification_create(request: web.Request, body) -> web.Response:
    """stages_identification_create

    IdentificationStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = IdentificationStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_identification_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_identification_destroy

    IdentificationStage Viewset

    :param stage_uuid: A UUID string identifying this Identification Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_identification_list(request: web.Request, case_insensitive_matching=None, enrollment_flow=None, name=None, ordering=None, page=None, page_size=None, password_stage=None, passwordless_flow=None, recovery_flow=None, search=None, show_matched_user=None, show_source_labels=None) -> web.Response:
    """stages_identification_list

    IdentificationStage Viewset

    :param case_insensitive_matching: 
    :type case_insensitive_matching: bool
    :param enrollment_flow: 
    :type enrollment_flow: str
    :type enrollment_flow: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param password_stage: 
    :type password_stage: str
    :type password_stage: str
    :param passwordless_flow: 
    :type passwordless_flow: str
    :type passwordless_flow: str
    :param recovery_flow: 
    :type recovery_flow: str
    :type recovery_flow: str
    :param search: A search term.
    :type search: str
    :param show_matched_user: 
    :type show_matched_user: bool
    :param show_source_labels: 
    :type show_source_labels: bool

    """
    return web.Response(status=200)


async def stages_identification_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_identification_partial_update

    IdentificationStage Viewset

    :param stage_uuid: A UUID string identifying this Identification Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedIdentificationStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_identification_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_identification_retrieve

    IdentificationStage Viewset

    :param stage_uuid: A UUID string identifying this Identification Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_identification_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_identification_update

    IdentificationStage Viewset

    :param stage_uuid: A UUID string identifying this Identification Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = IdentificationStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_identification_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_identification_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Identification Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_invitation_invitations_create(request: web.Request, body) -> web.Response:
    """stages_invitation_invitations_create

    Invitation Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = InvitationRequest.from_dict(body)
    return web.Response(status=200)


async def stages_invitation_invitations_destroy(request: web.Request, invite_uuid) -> web.Response:
    """stages_invitation_invitations_destroy

    Invitation Viewset

    :param invite_uuid: A UUID string identifying this Invitation.
    :type invite_uuid: str
    :type invite_uuid: str

    """
    return web.Response(status=200)


async def stages_invitation_invitations_list(request: web.Request, created_by__username=None, expires=None, flow__slug=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """stages_invitation_invitations_list

    Invitation Viewset

    :param created_by__username: 
    :type created_by__username: str
    :param expires: 
    :type expires: str
    :param flow__slug: 
    :type flow__slug: str
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
    expires = util.deserialize_datetime(expires)
    return web.Response(status=200)


async def stages_invitation_invitations_partial_update(request: web.Request, invite_uuid, body=None) -> web.Response:
    """stages_invitation_invitations_partial_update

    Invitation Viewset

    :param invite_uuid: A UUID string identifying this Invitation.
    :type invite_uuid: str
    :type invite_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedInvitationRequest.from_dict(body)
    return web.Response(status=200)


async def stages_invitation_invitations_retrieve(request: web.Request, invite_uuid) -> web.Response:
    """stages_invitation_invitations_retrieve

    Invitation Viewset

    :param invite_uuid: A UUID string identifying this Invitation.
    :type invite_uuid: str
    :type invite_uuid: str

    """
    return web.Response(status=200)


async def stages_invitation_invitations_update(request: web.Request, invite_uuid, body) -> web.Response:
    """stages_invitation_invitations_update

    Invitation Viewset

    :param invite_uuid: A UUID string identifying this Invitation.
    :type invite_uuid: str
    :type invite_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvitationRequest.from_dict(body)
    return web.Response(status=200)


async def stages_invitation_invitations_used_by_list(request: web.Request, invite_uuid) -> web.Response:
    """stages_invitation_invitations_used_by_list

    Get a list of all objects that use this object

    :param invite_uuid: A UUID string identifying this Invitation.
    :type invite_uuid: str
    :type invite_uuid: str

    """
    return web.Response(status=200)


async def stages_invitation_stages_create(request: web.Request, body) -> web.Response:
    """stages_invitation_stages_create

    InvitationStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = InvitationStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_invitation_stages_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_invitation_stages_destroy

    InvitationStage Viewset

    :param stage_uuid: A UUID string identifying this Invitation Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_invitation_stages_list(request: web.Request, continue_flow_without_invitation=None, name=None, no_flows=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None) -> web.Response:
    """stages_invitation_stages_list

    InvitationStage Viewset

    :param continue_flow_without_invitation: 
    :type continue_flow_without_invitation: bool
    :param name: 
    :type name: str
    :param no_flows: 
    :type no_flows: bool
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param search: A search term.
    :type search: str
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_invitation_stages_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_invitation_stages_partial_update

    InvitationStage Viewset

    :param stage_uuid: A UUID string identifying this Invitation Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedInvitationStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_invitation_stages_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_invitation_stages_retrieve

    InvitationStage Viewset

    :param stage_uuid: A UUID string identifying this Invitation Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_invitation_stages_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_invitation_stages_update

    InvitationStage Viewset

    :param stage_uuid: A UUID string identifying this Invitation Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = InvitationStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_invitation_stages_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_invitation_stages_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Invitation Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_password_create(request: web.Request, body) -> web.Response:
    """stages_password_create

    PasswordStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PasswordStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_password_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_password_destroy

    PasswordStage Viewset

    :param stage_uuid: A UUID string identifying this Password Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_password_list(request: web.Request, allow_show_password=None, configure_flow=None, failed_attempts_before_cancel=None, name=None, ordering=None, page=None, page_size=None, search=None) -> web.Response:
    """stages_password_list

    PasswordStage Viewset

    :param allow_show_password: 
    :type allow_show_password: bool
    :param configure_flow: 
    :type configure_flow: str
    :type configure_flow: str
    :param failed_attempts_before_cancel: 
    :type failed_attempts_before_cancel: int
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


async def stages_password_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_password_partial_update

    PasswordStage Viewset

    :param stage_uuid: A UUID string identifying this Password Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPasswordStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_password_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_password_retrieve

    PasswordStage Viewset

    :param stage_uuid: A UUID string identifying this Password Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_password_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_password_update

    PasswordStage Viewset

    :param stage_uuid: A UUID string identifying this Password Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PasswordStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_password_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_password_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Password Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_prompt_prompts_create(request: web.Request, body) -> web.Response:
    """stages_prompt_prompts_create

    Prompt Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PromptRequest.from_dict(body)
    return web.Response(status=200)


async def stages_prompt_prompts_destroy(request: web.Request, prompt_uuid) -> web.Response:
    """stages_prompt_prompts_destroy

    Prompt Viewset

    :param prompt_uuid: A UUID string identifying this Prompt.
    :type prompt_uuid: str
    :type prompt_uuid: str

    """
    return web.Response(status=200)


async def stages_prompt_prompts_list(request: web.Request, field_key=None, label=None, name=None, ordering=None, page=None, page_size=None, placeholder=None, search=None, type=None) -> web.Response:
    """stages_prompt_prompts_list

    Prompt Viewset

    :param field_key: 
    :type field_key: str
    :param label: 
    :type label: str
    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param placeholder: 
    :type placeholder: str
    :param search: A search term.
    :type search: str
    :param type: 
    :type type: str

    """
    return web.Response(status=200)


async def stages_prompt_prompts_partial_update(request: web.Request, prompt_uuid, body=None) -> web.Response:
    """stages_prompt_prompts_partial_update

    Prompt Viewset

    :param prompt_uuid: A UUID string identifying this Prompt.
    :type prompt_uuid: str
    :type prompt_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPromptRequest.from_dict(body)
    return web.Response(status=200)


async def stages_prompt_prompts_preview_create(request: web.Request, body) -> web.Response:
    """stages_prompt_prompts_preview_create

    Preview a prompt as a challenge, just like a flow would receive

    :param body: 
    :type body: dict | bytes

    """
    body = PromptRequest.from_dict(body)
    return web.Response(status=200)


async def stages_prompt_prompts_retrieve(request: web.Request, prompt_uuid) -> web.Response:
    """stages_prompt_prompts_retrieve

    Prompt Viewset

    :param prompt_uuid: A UUID string identifying this Prompt.
    :type prompt_uuid: str
    :type prompt_uuid: str

    """
    return web.Response(status=200)


async def stages_prompt_prompts_update(request: web.Request, prompt_uuid, body) -> web.Response:
    """stages_prompt_prompts_update

    Prompt Viewset

    :param prompt_uuid: A UUID string identifying this Prompt.
    :type prompt_uuid: str
    :type prompt_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PromptRequest.from_dict(body)
    return web.Response(status=200)


async def stages_prompt_prompts_used_by_list(request: web.Request, prompt_uuid) -> web.Response:
    """stages_prompt_prompts_used_by_list

    Get a list of all objects that use this object

    :param prompt_uuid: A UUID string identifying this Prompt.
    :type prompt_uuid: str
    :type prompt_uuid: str

    """
    return web.Response(status=200)


async def stages_prompt_stages_create(request: web.Request, body) -> web.Response:
    """stages_prompt_stages_create

    PromptStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = PromptStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_prompt_stages_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_prompt_stages_destroy

    PromptStage Viewset

    :param stage_uuid: A UUID string identifying this Prompt Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_prompt_stages_list(request: web.Request, fields=None, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None, validation_policies=None) -> web.Response:
    """stages_prompt_stages_list

    PromptStage Viewset

    :param fields: 
    :type fields: List[str]
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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str
    :param validation_policies: 
    :type validation_policies: List[str]

    """
    return web.Response(status=200)


async def stages_prompt_stages_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_prompt_stages_partial_update

    PromptStage Viewset

    :param stage_uuid: A UUID string identifying this Prompt Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedPromptStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_prompt_stages_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_prompt_stages_retrieve

    PromptStage Viewset

    :param stage_uuid: A UUID string identifying this Prompt Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_prompt_stages_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_prompt_stages_update

    PromptStage Viewset

    :param stage_uuid: A UUID string identifying this Prompt Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PromptStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_prompt_stages_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_prompt_stages_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Prompt Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_source_create(request: web.Request, body) -> web.Response:
    """stages_source_create

    SourceStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = SourceStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_source_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_source_destroy

    SourceStage Viewset

    :param stage_uuid: A UUID string identifying this Source Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_source_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, resume_timeout=None, search=None, source=None, stage_uuid=None) -> web.Response:
    """stages_source_list

    SourceStage Viewset

    :param name: 
    :type name: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param resume_timeout: 
    :type resume_timeout: str
    :param search: A search term.
    :type search: str
    :param source: 
    :type source: str
    :type source: str
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_source_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_source_partial_update

    SourceStage Viewset

    :param stage_uuid: A UUID string identifying this Source Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedSourceStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_source_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_source_retrieve

    SourceStage Viewset

    :param stage_uuid: A UUID string identifying this Source Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_source_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_source_update

    SourceStage Viewset

    :param stage_uuid: A UUID string identifying this Source Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = SourceStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_source_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_source_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this Source Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_delete_create(request: web.Request, body) -> web.Response:
    """stages_user_delete_create

    UserDeleteStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = UserDeleteStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_delete_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_delete_destroy

    UserDeleteStage Viewset

    :param stage_uuid: A UUID string identifying this User Delete Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_delete_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None) -> web.Response:
    """stages_user_delete_list

    UserDeleteStage Viewset

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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_delete_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_user_delete_partial_update

    UserDeleteStage Viewset

    :param stage_uuid: A UUID string identifying this User Delete Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserDeleteStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_delete_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_delete_retrieve

    UserDeleteStage Viewset

    :param stage_uuid: A UUID string identifying this User Delete Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_delete_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_user_delete_update

    UserDeleteStage Viewset

    :param stage_uuid: A UUID string identifying this User Delete Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserDeleteStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_delete_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_delete_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this User Delete Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_login_create(request: web.Request, body) -> web.Response:
    """stages_user_login_create

    UserLoginStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = UserLoginStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_login_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_login_destroy

    UserLoginStage Viewset

    :param stage_uuid: A UUID string identifying this User Login Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_login_list(request: web.Request, geoip_binding=None, name=None, network_binding=None, ordering=None, page=None, page_size=None, remember_me_offset=None, search=None, session_duration=None, stage_uuid=None, terminate_other_sessions=None) -> web.Response:
    """stages_user_login_list

    UserLoginStage Viewset

    :param geoip_binding: Bind sessions created by this stage to the configured GeoIP location  
    :type geoip_binding: str
    :param name: 
    :type name: str
    :param network_binding: Bind sessions created by this stage to the configured network  
    :type network_binding: str
    :param ordering: Which field to use when ordering the results.
    :type ordering: str
    :param page: A page number within the paginated result set.
    :type page: int
    :param page_size: Number of results to return per page.
    :type page_size: int
    :param remember_me_offset: 
    :type remember_me_offset: str
    :param search: A search term.
    :type search: str
    :param session_duration: 
    :type session_duration: str
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str
    :param terminate_other_sessions: 
    :type terminate_other_sessions: bool

    """
    return web.Response(status=200)


async def stages_user_login_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_user_login_partial_update

    UserLoginStage Viewset

    :param stage_uuid: A UUID string identifying this User Login Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserLoginStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_login_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_login_retrieve

    UserLoginStage Viewset

    :param stage_uuid: A UUID string identifying this User Login Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_login_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_user_login_update

    UserLoginStage Viewset

    :param stage_uuid: A UUID string identifying this User Login Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserLoginStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_login_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_login_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this User Login Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_logout_create(request: web.Request, body) -> web.Response:
    """stages_user_logout_create

    UserLogoutStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = UserLogoutStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_logout_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_logout_destroy

    UserLogoutStage Viewset

    :param stage_uuid: A UUID string identifying this User Logout Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_logout_list(request: web.Request, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None) -> web.Response:
    """stages_user_logout_list

    UserLogoutStage Viewset

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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_logout_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_user_logout_partial_update

    UserLogoutStage Viewset

    :param stage_uuid: A UUID string identifying this User Logout Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserLogoutStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_logout_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_logout_retrieve

    UserLogoutStage Viewset

    :param stage_uuid: A UUID string identifying this User Logout Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_logout_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_user_logout_update

    UserLogoutStage Viewset

    :param stage_uuid: A UUID string identifying this User Logout Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserLogoutStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_logout_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_logout_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this User Logout Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_write_create(request: web.Request, body) -> web.Response:
    """stages_user_write_create

    UserWriteStage Viewset

    :param body: 
    :type body: dict | bytes

    """
    body = UserWriteStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_write_destroy(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_write_destroy

    UserWriteStage Viewset

    :param stage_uuid: A UUID string identifying this User Write Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_write_list(request: web.Request, create_users_as_inactive=None, create_users_group=None, name=None, ordering=None, page=None, page_size=None, search=None, stage_uuid=None, user_creation_mode=None, user_path_template=None, user_type=None) -> web.Response:
    """stages_user_write_list

    UserWriteStage Viewset

    :param create_users_as_inactive: 
    :type create_users_as_inactive: bool
    :param create_users_group: 
    :type create_users_group: str
    :type create_users_group: str
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
    :param stage_uuid: 
    :type stage_uuid: str
    :type stage_uuid: str
    :param user_creation_mode: 
    :type user_creation_mode: str
    :param user_path_template: 
    :type user_path_template: str
    :param user_type: 
    :type user_type: str

    """
    return web.Response(status=200)


async def stages_user_write_partial_update(request: web.Request, stage_uuid, body=None) -> web.Response:
    """stages_user_write_partial_update

    UserWriteStage Viewset

    :param stage_uuid: A UUID string identifying this User Write Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = PatchedUserWriteStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_write_retrieve(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_write_retrieve

    UserWriteStage Viewset

    :param stage_uuid: A UUID string identifying this User Write Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)


async def stages_user_write_update(request: web.Request, stage_uuid, body) -> web.Response:
    """stages_user_write_update

    UserWriteStage Viewset

    :param stage_uuid: A UUID string identifying this User Write Stage.
    :type stage_uuid: str
    :type stage_uuid: str
    :param body: 
    :type body: dict | bytes

    """
    body = UserWriteStageRequest.from_dict(body)
    return web.Response(status=200)


async def stages_user_write_used_by_list(request: web.Request, stage_uuid) -> web.Response:
    """stages_user_write_used_by_list

    Get a list of all objects that use this object

    :param stage_uuid: A UUID string identifying this User Write Stage.
    :type stage_uuid: str
    :type stage_uuid: str

    """
    return web.Response(status=200)
