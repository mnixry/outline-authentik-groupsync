# coding: utf-8

import pytest
import json
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


pytestmark = pytest.mark.asyncio

async def test_stages_all_destroy(client):
    """Test case for stages_all_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/all/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_all_list(client):
    """Test case for stages_all_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/all/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_all_retrieve(client):
    """Test case for stages_all_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/all/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_all_types_list(client):
    """Test case for stages_all_types_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/all/types/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_all_used_by_list(client):
    """Test case for stages_all_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/all/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_all_user_settings_list(client):
    """Test case for stages_all_user_settings_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/all/user_settings/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_create(client):
    """Test case for stages_authenticator_duo_create

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","name":"name","client_secret":"client_secret","api_hostname":"api_hostname","admin_integration_key":"admin_integration_key","admin_secret_key":"admin_secret_key","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"client_id":"client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/duo/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_destroy(client):
    """Test case for stages_authenticator_duo_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_enrollment_status_create(client):
    """Test case for stages_authenticator_duo_enrollment_status_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}/enrollment_status'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_import_device_manual_create(client):
    """Test case for stages_authenticator_duo_import_device_manual_create

    
    """
    body = {"duo_user_id":"duo_user_id","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}/import_device_manual'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_import_devices_automatic_create(client):
    """Test case for stages_authenticator_duo_import_devices_automatic_create

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}/import_devices_automatic'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_list(client):
    """Test case for stages_authenticator_duo_list

    
    """
    params = [('api_hostname', 'api_hostname_example'),
                    ('client_id', 'client_id_example'),
                    ('configure_flow', 'configure_flow_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/duo/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_partial_update(client):
    """Test case for stages_authenticator_duo_partial_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","name":"name","client_secret":"client_secret","api_hostname":"api_hostname","admin_integration_key":"admin_integration_key","admin_secret_key":"admin_secret_key","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"client_id":"client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_retrieve(client):
    """Test case for stages_authenticator_duo_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_update(client):
    """Test case for stages_authenticator_duo_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","name":"name","client_secret":"client_secret","api_hostname":"api_hostname","admin_integration_key":"admin_integration_key","admin_secret_key":"admin_secret_key","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"client_id":"client_id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_duo_used_by_list(client):
    """Test case for stages_authenticator_duo_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/duo/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_sms_create(client):
    """Test case for stages_authenticator_sms_create

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","auth_type":"basic","mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","provider":"twilio","auth":"auth","from_number":"from_number","name":"name","account_sid":"account_sid","auth_password":"auth_password","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"verify_only":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/sms/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_sms_destroy(client):
    """Test case for stages_authenticator_sms_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/authenticator/sms/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_sms_list(client):
    """Test case for stages_authenticator_sms_list

    
    """
    params = [('account_sid', 'account_sid_example'),
                    ('auth', 'auth_example'),
                    ('auth_password', 'auth_password_example'),
                    ('auth_type', 'auth_type_example'),
                    ('configure_flow', 'configure_flow_example'),
                    ('friendly_name', 'friendly_name_example'),
                    ('from_number', 'from_number_example'),
                    ('mapping', 'mapping_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('provider', 'provider_example'),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example'),
                    ('verify_only', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/sms/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_sms_partial_update(client):
    """Test case for stages_authenticator_sms_partial_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","auth_type":"basic","mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","provider":"twilio","auth":"auth","from_number":"from_number","name":"name","account_sid":"account_sid","auth_password":"auth_password","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"verify_only":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/authenticator/sms/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_sms_retrieve(client):
    """Test case for stages_authenticator_sms_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/sms/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_sms_update(client):
    """Test case for stages_authenticator_sms_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","auth_type":"basic","mapping":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","provider":"twilio","auth":"auth","from_number":"from_number","name":"name","account_sid":"account_sid","auth_password":"auth_password","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"verify_only":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/authenticator/sms/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_sms_used_by_list(client):
    """Test case for stages_authenticator_sms_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/sms/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_static_create(client):
    """Test case for stages_authenticator_static_create

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","token_count":171976544,"token_length":1294386358,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/static/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_static_destroy(client):
    """Test case for stages_authenticator_static_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/authenticator/static/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_static_list(client):
    """Test case for stages_authenticator_static_list

    
    """
    params = [('configure_flow', 'configure_flow_example'),
                    ('friendly_name', 'friendly_name_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example'),
                    ('token_count', 56),
                    ('token_length', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/static/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_static_partial_update(client):
    """Test case for stages_authenticator_static_partial_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","token_count":171976544,"token_length":1294386358,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/authenticator/static/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_static_retrieve(client):
    """Test case for stages_authenticator_static_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/static/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_static_update(client):
    """Test case for stages_authenticator_static_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","token_count":171976544,"token_length":1294386358,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/authenticator/static/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_static_used_by_list(client):
    """Test case for stages_authenticator_static_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/static/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_totp_create(client):
    """Test case for stages_authenticator_totp_create

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","name":"name","digits":"6","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/totp/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_totp_destroy(client):
    """Test case for stages_authenticator_totp_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/authenticator/totp/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_totp_list(client):
    """Test case for stages_authenticator_totp_list

    
    """
    params = [('configure_flow', 'configure_flow_example'),
                    ('digits', 'digits_example'),
                    ('friendly_name', 'friendly_name_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/totp/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_totp_partial_update(client):
    """Test case for stages_authenticator_totp_partial_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","name":"name","digits":"6","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/authenticator/totp/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_totp_retrieve(client):
    """Test case for stages_authenticator_totp_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/totp/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_totp_update(client):
    """Test case for stages_authenticator_totp_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","name":"name","digits":"6","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/authenticator/totp/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_totp_used_by_list(client):
    """Test case for stages_authenticator_totp_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/totp/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_validate_create(client):
    """Test case for stages_authenticator_validate_create

    
    """
    body = {"webauthn_user_verification":"","not_configured_action":"skip","webauthn_allowed_device_types":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"device_classes":["static","static"],"name":"name","last_auth_threshold":"last_auth_threshold","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"configuration_stages":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/validate/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_validate_destroy(client):
    """Test case for stages_authenticator_validate_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/authenticator/validate/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_validate_list(client):
    """Test case for stages_authenticator_validate_list

    
    """
    params = [('configuration_stages', ['configuration_stages_example']),
                    ('name', 'name_example'),
                    ('not_configured_action', 'not_configured_action_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/validate/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_validate_partial_update(client):
    """Test case for stages_authenticator_validate_partial_update

    
    """
    body = {"webauthn_user_verification":"","not_configured_action":"skip","webauthn_allowed_device_types":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"device_classes":["static","static"],"name":"name","last_auth_threshold":"last_auth_threshold","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"configuration_stages":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/authenticator/validate/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_validate_retrieve(client):
    """Test case for stages_authenticator_validate_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/validate/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_validate_update(client):
    """Test case for stages_authenticator_validate_update

    
    """
    body = {"webauthn_user_verification":"","not_configured_action":"skip","webauthn_allowed_device_types":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"device_classes":["static","static"],"name":"name","last_auth_threshold":"last_auth_threshold","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"configuration_stages":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/authenticator/validate/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_validate_used_by_list(client):
    """Test case for stages_authenticator_validate_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/validate/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_create(client):
    """Test case for stages_authenticator_webauthn_create

    
    """
    body = {"resident_key_requirement":"discouraged","configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","device_type_restrictions":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","user_verification":"required","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"authenticator_attachment":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/authenticator/webauthn/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_destroy(client):
    """Test case for stages_authenticator_webauthn_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/authenticator/webauthn/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_device_types_list(client):
    """Test case for stages_authenticator_webauthn_device_types_list

    
    """
    params = [('aaguid', 'aaguid_example'),
                    ('description', 'description_example'),
                    ('icon', 'icon_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/webauthn_device_types/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_device_types_retrieve(client):
    """Test case for stages_authenticator_webauthn_device_types_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/webauthn_device_types/{aaguid}'.format(aaguid='aaguid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_list(client):
    """Test case for stages_authenticator_webauthn_list

    
    """
    params = [('authenticator_attachment', 'authenticator_attachment_example'),
                    ('configure_flow', 'configure_flow_example'),
                    ('device_type_restrictions', ['device_type_restrictions_example']),
                    ('friendly_name', 'friendly_name_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('resident_key_requirement', 'resident_key_requirement_example'),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example'),
                    ('user_verification', 'user_verification_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/webauthn/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_partial_update(client):
    """Test case for stages_authenticator_webauthn_partial_update

    
    """
    body = {"resident_key_requirement":"discouraged","configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","device_type_restrictions":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","user_verification":"required","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"authenticator_attachment":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/authenticator/webauthn/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_retrieve(client):
    """Test case for stages_authenticator_webauthn_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/webauthn/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_update(client):
    """Test case for stages_authenticator_webauthn_update

    
    """
    body = {"resident_key_requirement":"discouraged","configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","friendly_name":"friendly_name","device_type_restrictions":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","user_verification":"required","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"authenticator_attachment":""}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/authenticator/webauthn/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_authenticator_webauthn_used_by_list(client):
    """Test case for stages_authenticator_webauthn_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/authenticator/webauthn/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_captcha_create(client):
    """Test case for stages_captcha_create

    
    """
    body = {"public_key":"public_key","error_on_invalid_score":True,"api_url":"api_url","name":"name","private_key":"private_key","js_url":"js_url","score_min_threshold":0.8008281904610115,"score_max_threshold":6.027456183070403,"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/captcha/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_captcha_destroy(client):
    """Test case for stages_captcha_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/captcha/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_captcha_list(client):
    """Test case for stages_captcha_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('public_key', 'public_key_example'),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/captcha/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_captcha_partial_update(client):
    """Test case for stages_captcha_partial_update

    
    """
    body = {"public_key":"public_key","error_on_invalid_score":True,"api_url":"api_url","name":"name","private_key":"private_key","js_url":"js_url","score_min_threshold":0.8008281904610115,"score_max_threshold":6.027456183070403,"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/captcha/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_captcha_retrieve(client):
    """Test case for stages_captcha_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/captcha/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_captcha_update(client):
    """Test case for stages_captcha_update

    
    """
    body = {"public_key":"public_key","error_on_invalid_score":True,"api_url":"api_url","name":"name","private_key":"private_key","js_url":"js_url","score_min_threshold":0.8008281904610115,"score_max_threshold":6.027456183070403,"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/captcha/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_captcha_used_by_list(client):
    """Test case for stages_captcha_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/captcha/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_consent_create(client):
    """Test case for stages_consent_create

    
    """
    body = {"mode":"always_require","name":"name","consent_expire_in":"consent_expire_in","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/consent/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_consent_destroy(client):
    """Test case for stages_consent_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/consent/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_consent_list(client):
    """Test case for stages_consent_list

    
    """
    params = [('consent_expire_in', 'consent_expire_in_example'),
                    ('mode', 'mode_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/consent/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_consent_partial_update(client):
    """Test case for stages_consent_partial_update

    
    """
    body = {"mode":"always_require","name":"name","consent_expire_in":"consent_expire_in","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/consent/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_consent_retrieve(client):
    """Test case for stages_consent_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/consent/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_consent_update(client):
    """Test case for stages_consent_update

    
    """
    body = {"mode":"always_require","name":"name","consent_expire_in":"consent_expire_in","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/consent/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_consent_used_by_list(client):
    """Test case for stages_consent_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/consent/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_deny_create(client):
    """Test case for stages_deny_create

    
    """
    body = {"deny_message":"deny_message","name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/deny/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_deny_destroy(client):
    """Test case for stages_deny_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/deny/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_deny_list(client):
    """Test case for stages_deny_list

    
    """
    params = [('deny_message', 'deny_message_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/deny/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_deny_partial_update(client):
    """Test case for stages_deny_partial_update

    
    """
    body = {"deny_message":"deny_message","name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/deny/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_deny_retrieve(client):
    """Test case for stages_deny_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/deny/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_deny_update(client):
    """Test case for stages_deny_update

    
    """
    body = {"deny_message":"deny_message","name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/deny/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_deny_used_by_list(client):
    """Test case for stages_deny_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/deny/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_dummy_create(client):
    """Test case for stages_dummy_create

    
    """
    body = {"throw_error":True,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/dummy/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_dummy_destroy(client):
    """Test case for stages_dummy_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/dummy/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_dummy_list(client):
    """Test case for stages_dummy_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example'),
                    ('throw_error', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/dummy/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_dummy_partial_update(client):
    """Test case for stages_dummy_partial_update

    
    """
    body = {"throw_error":True,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/dummy/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_dummy_retrieve(client):
    """Test case for stages_dummy_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/dummy/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_dummy_update(client):
    """Test case for stages_dummy_update

    
    """
    body = {"throw_error":True,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/dummy/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_dummy_used_by_list(client):
    """Test case for stages_dummy_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/dummy/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_create(client):
    """Test case for stages_email_create

    
    """
    body = {"template":"template","use_global_settings":True,"use_ssl":True,"subject":"subject","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"token_expiry":-1517921766,"timeout":441289069,"use_tls":True,"password":"password","port":-1803530559,"activate_user_on_success":True,"name":"name","host":"host","from_address":"from_address","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/email/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_destroy(client):
    """Test case for stages_email_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/email/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_list(client):
    """Test case for stages_email_list

    
    """
    params = [('activate_user_on_success', True),
                    ('from_address', 'from_address_example'),
                    ('host', 'host_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('port', 56),
                    ('search', 'search_example'),
                    ('subject', 'subject_example'),
                    ('template', 'template_example'),
                    ('timeout', 56),
                    ('token_expiry', 56),
                    ('use_global_settings', True),
                    ('use_ssl', True),
                    ('use_tls', True),
                    ('username', 'username_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/email/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_partial_update(client):
    """Test case for stages_email_partial_update

    
    """
    body = {"template":"template","use_global_settings":True,"use_ssl":True,"subject":"subject","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"token_expiry":-1517921766,"timeout":441289069,"use_tls":True,"password":"password","port":-1803530559,"activate_user_on_success":True,"name":"name","host":"host","from_address":"from_address","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/email/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_retrieve(client):
    """Test case for stages_email_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/email/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_templates_list(client):
    """Test case for stages_email_templates_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/email/templates/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_update(client):
    """Test case for stages_email_update

    
    """
    body = {"template":"template","use_global_settings":True,"use_ssl":True,"subject":"subject","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"token_expiry":-1517921766,"timeout":441289069,"use_tls":True,"password":"password","port":-1803530559,"activate_user_on_success":True,"name":"name","host":"host","from_address":"from_address","username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/email/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_email_used_by_list(client):
    """Test case for stages_email_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/email/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_identification_create(client):
    """Test case for stages_identification_create

    
    """
    body = {"passwordless_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","show_source_labels":True,"user_fields":["email","email"],"show_matched_user":True,"sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","password_stage":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"recovery_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","pretend_user_exists":True,"case_insensitive_matching":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/identification/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_identification_destroy(client):
    """Test case for stages_identification_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/identification/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_identification_list(client):
    """Test case for stages_identification_list

    
    """
    params = [('case_insensitive_matching', True),
                    ('enrollment_flow', 'enrollment_flow_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('password_stage', 'password_stage_example'),
                    ('passwordless_flow', 'passwordless_flow_example'),
                    ('recovery_flow', 'recovery_flow_example'),
                    ('search', 'search_example'),
                    ('show_matched_user', True),
                    ('show_source_labels', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/identification/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_identification_partial_update(client):
    """Test case for stages_identification_partial_update

    
    """
    body = {"passwordless_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","show_source_labels":True,"user_fields":["email","email"],"show_matched_user":True,"sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","password_stage":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"recovery_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","pretend_user_exists":True,"case_insensitive_matching":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/identification/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_identification_retrieve(client):
    """Test case for stages_identification_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/identification/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_identification_update(client):
    """Test case for stages_identification_update

    
    """
    body = {"passwordless_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","enrollment_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","show_source_labels":True,"user_fields":["email","email"],"show_matched_user":True,"sources":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"name":"name","password_stage":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"recovery_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","pretend_user_exists":True,"case_insensitive_matching":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/identification/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_identification_used_by_list(client):
    """Test case for stages_identification_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/identification/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_invitations_create(client):
    """Test case for stages_invitation_invitations_create

    
    """
    body = {"fixed_data":{"key":""},"expires":"2000-01-23T04:56:07.000+00:00","name":"name","single_use":True,"flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/invitation/invitations/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_invitations_destroy(client):
    """Test case for stages_invitation_invitations_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/invitation/invitations/{invite_uuid}'.format(invite_uuid='invite_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_invitations_list(client):
    """Test case for stages_invitation_invitations_list

    
    """
    params = [('created_by__username', 'created_by__username_example'),
                    ('expires', '2013-10-20T19:20:30+01:00'),
                    ('flow__slug', 'flow__slug_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/invitation/invitations/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_invitations_partial_update(client):
    """Test case for stages_invitation_invitations_partial_update

    
    """
    body = {"fixed_data":{"key":""},"expires":"2000-01-23T04:56:07.000+00:00","name":"name","single_use":True,"flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/invitation/invitations/{invite_uuid}'.format(invite_uuid='invite_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_invitations_retrieve(client):
    """Test case for stages_invitation_invitations_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/invitation/invitations/{invite_uuid}'.format(invite_uuid='invite_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_invitations_update(client):
    """Test case for stages_invitation_invitations_update

    
    """
    body = {"fixed_data":{"key":""},"expires":"2000-01-23T04:56:07.000+00:00","name":"name","single_use":True,"flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/invitation/invitations/{invite_uuid}'.format(invite_uuid='invite_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_invitations_used_by_list(client):
    """Test case for stages_invitation_invitations_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/invitation/invitations/{invite_uuid}/used_by'.format(invite_uuid='invite_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_stages_create(client):
    """Test case for stages_invitation_stages_create

    
    """
    body = {"continue_flow_without_invitation":True,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/invitation/stages/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_stages_destroy(client):
    """Test case for stages_invitation_stages_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/invitation/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_stages_list(client):
    """Test case for stages_invitation_stages_list

    
    """
    params = [('continue_flow_without_invitation', True),
                    ('name', 'name_example'),
                    ('no_flows', True),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/invitation/stages/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_stages_partial_update(client):
    """Test case for stages_invitation_stages_partial_update

    
    """
    body = {"continue_flow_without_invitation":True,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/invitation/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_stages_retrieve(client):
    """Test case for stages_invitation_stages_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/invitation/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_stages_update(client):
    """Test case for stages_invitation_stages_update

    
    """
    body = {"continue_flow_without_invitation":True,"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/invitation/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_invitation_stages_used_by_list(client):
    """Test case for stages_invitation_stages_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/invitation/stages/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_password_create(client):
    """Test case for stages_password_create

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","allow_show_password":True,"name":"name","failed_attempts_before_cancel":-1803530559,"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"backends":["authentik.core.auth.InbuiltBackend","authentik.core.auth.InbuiltBackend"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/password/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_password_destroy(client):
    """Test case for stages_password_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/password/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_password_list(client):
    """Test case for stages_password_list

    
    """
    params = [('allow_show_password', True),
                    ('configure_flow', 'configure_flow_example'),
                    ('failed_attempts_before_cancel', 56),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/password/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_password_partial_update(client):
    """Test case for stages_password_partial_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","allow_show_password":True,"name":"name","failed_attempts_before_cancel":-1803530559,"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"backends":["authentik.core.auth.InbuiltBackend","authentik.core.auth.InbuiltBackend"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/password/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_password_retrieve(client):
    """Test case for stages_password_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/password/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_password_update(client):
    """Test case for stages_password_update

    
    """
    body = {"configure_flow":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","allow_show_password":True,"name":"name","failed_attempts_before_cancel":-1803530559,"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"backends":["authentik.core.auth.InbuiltBackend","authentik.core.auth.InbuiltBackend"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/password/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_password_used_by_list(client):
    """Test case for stages_password_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/password/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_create(client):
    """Test case for stages_prompt_prompts_create

    
    """
    body = {"sub_text":"sub_text","promptstage_set":[{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]},{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}],"initial_value":"initial_value","initial_value_expression":True,"field_key":"field_key","name":"name","label":"label","placeholder":"placeholder","type":"text","placeholder_expression":True,"required":True,"order":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/prompt/prompts/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_destroy(client):
    """Test case for stages_prompt_prompts_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/prompt/prompts/{prompt_uuid}'.format(prompt_uuid='prompt_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_list(client):
    """Test case for stages_prompt_prompts_list

    
    """
    params = [('field_key', 'field_key_example'),
                    ('label', 'label_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('placeholder', 'placeholder_example'),
                    ('search', 'search_example'),
                    ('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/prompt/prompts/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_partial_update(client):
    """Test case for stages_prompt_prompts_partial_update

    
    """
    body = {"sub_text":"sub_text","promptstage_set":[{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]},{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}],"initial_value":"initial_value","initial_value_expression":True,"field_key":"field_key","name":"name","label":"label","placeholder":"placeholder","type":"text","placeholder_expression":True,"required":True,"order":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/prompt/prompts/{prompt_uuid}'.format(prompt_uuid='prompt_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_preview_create(client):
    """Test case for stages_prompt_prompts_preview_create

    
    """
    body = {"sub_text":"sub_text","promptstage_set":[{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]},{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}],"initial_value":"initial_value","initial_value_expression":True,"field_key":"field_key","name":"name","label":"label","placeholder":"placeholder","type":"text","placeholder_expression":True,"required":True,"order":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/prompt/prompts/preview/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_retrieve(client):
    """Test case for stages_prompt_prompts_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/prompt/prompts/{prompt_uuid}'.format(prompt_uuid='prompt_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_update(client):
    """Test case for stages_prompt_prompts_update

    
    """
    body = {"sub_text":"sub_text","promptstage_set":[{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]},{"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}],"initial_value":"initial_value","initial_value_expression":True,"field_key":"field_key","name":"name","label":"label","placeholder":"placeholder","type":"text","placeholder_expression":True,"required":True,"order":-1803530559}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/prompt/prompts/{prompt_uuid}'.format(prompt_uuid='prompt_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_prompts_used_by_list(client):
    """Test case for stages_prompt_prompts_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/prompt/prompts/{prompt_uuid}/used_by'.format(prompt_uuid='prompt_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_stages_create(client):
    """Test case for stages_prompt_stages_create

    
    """
    body = {"name":"name","validation_policies":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"fields":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/prompt/stages/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_stages_destroy(client):
    """Test case for stages_prompt_stages_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/prompt/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_stages_list(client):
    """Test case for stages_prompt_stages_list

    
    """
    params = [('fields', ['fields_example']),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example'),
                    ('validation_policies', ['validation_policies_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/prompt/stages/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_stages_partial_update(client):
    """Test case for stages_prompt_stages_partial_update

    
    """
    body = {"name":"name","validation_policies":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"fields":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/prompt/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_stages_retrieve(client):
    """Test case for stages_prompt_stages_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/prompt/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_stages_update(client):
    """Test case for stages_prompt_stages_update

    
    """
    body = {"name":"name","validation_policies":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"fields":["046b6c7f-0b8a-43b9-b35d-6489e6daee91","046b6c7f-0b8a-43b9-b35d-6489e6daee91"],"flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/prompt/stages/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_prompt_stages_used_by_list(client):
    """Test case for stages_prompt_stages_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/prompt/stages/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_source_create(client):
    """Test case for stages_source_create

    
    """
    body = {"resume_timeout":"resume_timeout","name":"name","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/source/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_source_destroy(client):
    """Test case for stages_source_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/source/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_source_list(client):
    """Test case for stages_source_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('resume_timeout', 'resume_timeout_example'),
                    ('search', 'search_example'),
                    ('source', 'source_example'),
                    ('stage_uuid', 'stage_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/source/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_source_partial_update(client):
    """Test case for stages_source_partial_update

    
    """
    body = {"resume_timeout":"resume_timeout","name":"name","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/source/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_source_retrieve(client):
    """Test case for stages_source_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/source/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_source_update(client):
    """Test case for stages_source_update

    
    """
    body = {"resume_timeout":"resume_timeout","name":"name","source":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/source/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_source_used_by_list(client):
    """Test case for stages_source_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/source/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_delete_create(client):
    """Test case for stages_user_delete_create

    
    """
    body = {"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/user_delete/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_delete_destroy(client):
    """Test case for stages_user_delete_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/user_delete/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_delete_list(client):
    """Test case for stages_user_delete_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_delete/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_delete_partial_update(client):
    """Test case for stages_user_delete_partial_update

    
    """
    body = {"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/user_delete/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_delete_retrieve(client):
    """Test case for stages_user_delete_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_delete/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_delete_update(client):
    """Test case for stages_user_delete_update

    
    """
    body = {"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/user_delete/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_delete_used_by_list(client):
    """Test case for stages_user_delete_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_delete/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_login_create(client):
    """Test case for stages_user_login_create

    
    """
    body = {"terminate_other_sessions":True,"remember_me_offset":"remember_me_offset","name":"name","network_binding":"","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"geoip_binding":"","session_duration":"session_duration"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/user_login/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_login_destroy(client):
    """Test case for stages_user_login_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/user_login/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_login_list(client):
    """Test case for stages_user_login_list

    
    """
    params = [('geoip_binding', 'geoip_binding_example'),
                    ('name', 'name_example'),
                    ('network_binding', 'network_binding_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('remember_me_offset', 'remember_me_offset_example'),
                    ('search', 'search_example'),
                    ('session_duration', 'session_duration_example'),
                    ('stage_uuid', 'stage_uuid_example'),
                    ('terminate_other_sessions', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_login/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_login_partial_update(client):
    """Test case for stages_user_login_partial_update

    
    """
    body = {"terminate_other_sessions":True,"remember_me_offset":"remember_me_offset","name":"name","network_binding":"","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"geoip_binding":"","session_duration":"session_duration"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/user_login/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_login_retrieve(client):
    """Test case for stages_user_login_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_login/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_login_update(client):
    """Test case for stages_user_login_update

    
    """
    body = {"terminate_other_sessions":True,"remember_me_offset":"remember_me_offset","name":"name","network_binding":"","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"geoip_binding":"","session_duration":"session_duration"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/user_login/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_login_used_by_list(client):
    """Test case for stages_user_login_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_login/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_logout_create(client):
    """Test case for stages_user_logout_create

    
    """
    body = {"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/user_logout/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_logout_destroy(client):
    """Test case for stages_user_logout_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/user_logout/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_logout_list(client):
    """Test case for stages_user_logout_list

    
    """
    params = [('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_logout/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_logout_partial_update(client):
    """Test case for stages_user_logout_partial_update

    
    """
    body = {"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/user_logout/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_logout_retrieve(client):
    """Test case for stages_user_logout_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_logout/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_logout_update(client):
    """Test case for stages_user_logout_update

    
    """
    body = {"name":"name","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/user_logout/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_logout_used_by_list(client):
    """Test case for stages_user_logout_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_logout/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_write_create(client):
    """Test case for stages_user_write_create

    
    """
    body = {"user_type":"internal","user_path_template":"user_path_template","name":"name","create_users_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","user_creation_mode":"never_create","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"create_users_as_inactive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v3/stages/user_write/',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_write_destroy(client):
    """Test case for stages_user_write_destroy

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v3/stages/user_write/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_write_list(client):
    """Test case for stages_user_write_list

    
    """
    params = [('create_users_as_inactive', True),
                    ('create_users_group', 'create_users_group_example'),
                    ('name', 'name_example'),
                    ('ordering', 'ordering_example'),
                    ('page', 56),
                    ('page_size', 56),
                    ('search', 'search_example'),
                    ('stage_uuid', 'stage_uuid_example'),
                    ('user_creation_mode', 'user_creation_mode_example'),
                    ('user_path_template', 'user_path_template_example'),
                    ('user_type', 'user_type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_write/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_write_partial_update(client):
    """Test case for stages_user_write_partial_update

    
    """
    body = {"user_type":"internal","user_path_template":"user_path_template","name":"name","create_users_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","user_creation_mode":"never_create","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"create_users_as_inactive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v3/stages/user_write/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_write_retrieve(client):
    """Test case for stages_user_write_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_write/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_write_update(client):
    """Test case for stages_user_write_update

    
    """
    body = {"user_type":"internal","user_path_template":"user_path_template","name":"name","create_users_group":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","user_creation_mode":"never_create","flow_set":[{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"},{"policy_engine_mode":"all","compatibility_mode":True,"layout":"stacked","denied_action":"","name":"name","designation":"","title":"title","slug":"slug"}],"create_users_as_inactive":True}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v3/stages/user_write/{stage_uuid}'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stages_user_write_used_by_list(client):
    """Test case for stages_user_write_used_by_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/stages/user_write/{stage_uuid}/used_by'.format(stage_uuid='stage_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

