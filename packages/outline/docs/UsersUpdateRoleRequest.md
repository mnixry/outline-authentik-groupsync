# UsersUpdateRoleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the user. | 
**role** | [**UserRole**](UserRole.md) |  | 

## Example

```python
from outline_openapi.models.users_update_role_request import UsersUpdateRoleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateRoleRequest from a JSON string
users_update_role_request_instance = UsersUpdateRoleRequest.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateRoleRequest.to_json())

# convert the object into a dict
users_update_role_request_dict = users_update_role_request_instance.to_dict()
# create an instance of UsersUpdateRoleRequest from a dict
users_update_role_request_from_dict = UsersUpdateRoleRequest.from_dict(users_update_role_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


