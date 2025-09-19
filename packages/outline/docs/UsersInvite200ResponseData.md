# UsersInvite200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sent** | [**List[Invite]**](Invite.md) |  | [optional] 
**users** | [**List[User]**](User.md) |  | [optional] 

## Example

```python
from outline_openapi.models.users_invite200_response_data import UsersInvite200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInvite200ResponseData from a JSON string
users_invite200_response_data_instance = UsersInvite200ResponseData.from_json(json)
# print the JSON string representation of the object
print(UsersInvite200ResponseData.to_json())

# convert the object into a dict
users_invite200_response_data_dict = users_invite200_response_data_instance.to_dict()
# create an instance of UsersInvite200ResponseData from a dict
users_invite200_response_data_from_dict = UsersInvite200ResponseData.from_dict(users_invite200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


