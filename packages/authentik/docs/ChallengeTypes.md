# ChallengeTypes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**flow_info** | [**ContextualFlowInfo**](ContextualFlowInfo.md) |  | [optional] 
**component** | **str** |  | [optional] [default to 'ak-stage-user-login']
**response_errors** | **Dict[str, List[ErrorDetail]]** |  | [optional] 
**pending_user** | **str** |  | 
**pending_user_avatar** | **str** |  | 
**error_message** | **str** |  | [optional] 
**client_id** | **str** |  | 
**scope** | **str** |  | 
**redirect_uri** | **str** |  | 
**state** | **str** |  | 
**activation_barcode** | **str** |  | 
**activation_code** | **str** |  | 
**stage_uuid** | **str** |  | 
**email** | **str** |  | [optional] 
**email_required** | **bool** |  | [optional] [default to True]
**phone_number_required** | **bool** |  | [optional] [default to True]
**codes** | **List[str]** |  | 
**config_url** | **str** |  | 
**device_challenges** | [**List[DeviceChallenge]**](DeviceChallenge.md) |  | 
**configuration_stages** | [**List[SelectableStage]**](SelectableStage.md) |  | 
**registration** | **Dict[str, object]** |  | 
**url** | **str** |  | 
**attrs** | **Dict[str, str]** |  | 
**title** | **str** |  | [optional] 
**site_key** | **str** |  | 
**js_url** | **str** |  | 
**interactive** | **bool** |  | 
**header_text** | **str** |  | [optional] 
**permissions** | [**List[ConsentPermission]**](ConsentPermission.md) |  | 
**additional_permissions** | [**List[ConsentPermission]**](ConsentPermission.md) |  | 
**token** | **str** |  | 
**name** | **str** |  | 
**request_id** | **str** |  | 
**error** | **str** |  | [optional] 
**traceback** | **str** |  | [optional] 
**loading_overlay** | **bool** |  | [optional] [default to False]
**loading_text** | **str** |  | 
**user_fields** | **List[str]** |  | 
**password_fields** | **bool** |  | 
**allow_show_password** | **bool** |  | [optional] [default to False]
**application_pre** | **str** |  | [optional] 
**flow_designation** | [**FlowDesignationEnum**](FlowDesignationEnum.md) |  | 
**captcha_stage** | [**CaptchaChallenge**](CaptchaChallenge.md) |  | [optional] 
**enroll_url** | **str** |  | [optional] 
**recovery_url** | **str** |  | [optional] 
**passwordless_url** | **str** |  | [optional] 
**primary_action** | **str** |  | 
**sources** | [**List[LoginSource]**](LoginSource.md) |  | [optional] 
**show_source_labels** | **bool** |  | 
**enable_remember_me** | **bool** |  | [optional] [default to True]
**slug** | **str** |  | 
**fields** | [**List[StagePrompt]**](StagePrompt.md) |  | 
**to** | **str** |  | 
**application_name** | **str** |  | [optional] 
**application_launch_url** | **str** |  | [optional] 
**invalidation_flow_url** | **str** |  | [optional] 
**brand_name** | **str** |  | 
**body** | **str** |  | 

## Example

```python
from authentik_openapi.models.challenge_types import ChallengeTypes

# TODO update the JSON string below
json = "{}"
# create an instance of ChallengeTypes from a JSON string
challenge_types_instance = ChallengeTypes.from_json(json)
# print the JSON string representation of the object
print(ChallengeTypes.to_json())

# convert the object into a dict
challenge_types_dict = challenge_types_instance.to_dict()
# create an instance of ChallengeTypes from a dict
challenge_types_from_dict = ChallengeTypes.from_dict(challenge_types_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


