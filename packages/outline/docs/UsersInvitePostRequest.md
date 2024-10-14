# UsersInvitePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invites** | [**List[Invite]**](Invite.md) |  | 

## Example

```python
from outline_openapi.models.users_invite_post_request import UsersInvitePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInvitePostRequest from a JSON string
users_invite_post_request_instance = UsersInvitePostRequest.from_json(json)
# print the JSON string representation of the object
print(UsersInvitePostRequest.to_json())

# convert the object into a dict
users_invite_post_request_dict = users_invite_post_request_instance.to_dict()
# create an instance of UsersInvitePostRequest from a dict
users_invite_post_request_from_dict = UsersInvitePostRequest.from_dict(users_invite_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


