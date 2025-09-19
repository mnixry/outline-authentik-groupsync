# UsersInviteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites** | [**List[Invite]**](Invite.md) |  | 

## Example

```python
from outline_openapi.models.users_invite_request import UsersInviteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInviteRequest from a JSON string
users_invite_request_instance = UsersInviteRequest.from_json(json)
# print the JSON string representation of the object
print(UsersInviteRequest.to_json())

# convert the object into a dict
users_invite_request_dict = users_invite_request_instance.to_dict()
# create an instance of UsersInviteRequest from a dict
users_invite_request_from_dict = UsersInviteRequest.from_dict(users_invite_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


