# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**name** | **str** | The name of this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary. | [optional] 
**avatar_url** | **str** | The URL for the image associated with this user, it will be displayed in the application UI and email notifications. | [optional] 
**email** | **str** | The email associated with this user, it is migrated from Slack or Google Workspace when the SSO connection is made but can be changed if neccessary. | [optional] [readonly] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 
**is_suspended** | **bool** | Whether this user has been suspended. | [optional] [readonly] 
**last_active_at** | **datetime** | The last time this user made an API request, this value is updated at most every 5 minutes. | [optional] [readonly] 
**created_at** | **datetime** | The date and time that this user first signed in or was invited as a guest. | [optional] [readonly] 

## Example

```python
from outline_openapi.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


