# UsersListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[User]**](User.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.users_list_post200_response import UsersListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersListPost200Response from a JSON string
users_list_post200_response_instance = UsersListPost200Response.from_json(json)
# print the JSON string representation of the object
print(UsersListPost200Response.to_json())

# convert the object into a dict
users_list_post200_response_dict = users_list_post200_response_instance.to_dict()
# create an instance of UsersListPost200Response from a dict
users_list_post200_response_from_dict = UsersListPost200Response.from_dict(users_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


