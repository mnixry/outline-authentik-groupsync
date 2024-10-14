# UsersUpdateRolePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the user. | 
**role** | [**UserRole**](UserRole.md) |  | 

## Example

```python
from outline_openapi.models.users_update_role_post_request import UsersUpdateRolePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateRolePostRequest from a JSON string
users_update_role_post_request_instance = UsersUpdateRolePostRequest.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateRolePostRequest.to_json())

# convert the object into a dict
users_update_role_post_request_dict = users_update_role_post_request_instance.to_dict()
# create an instance of UsersUpdateRolePostRequest from a dict
users_update_role_post_request_from_dict = UsersUpdateRolePostRequest.from_dict(users_update_role_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


