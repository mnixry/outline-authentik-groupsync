# UsersInfoPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**User**](User.md) |  | [optional] 

## Example

```python
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInfoPost200Response from a JSON string
users_info_post200_response_instance = UsersInfoPost200Response.from_json(json)
# print the JSON string representation of the object
print(UsersInfoPost200Response.to_json())

# convert the object into a dict
users_info_post200_response_dict = users_info_post200_response_instance.to_dict()
# create an instance of UsersInfoPost200Response from a dict
users_info_post200_response_from_dict = UsersInfoPost200Response.from_dict(users_info_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


