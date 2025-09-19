# UsersInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**User**](User.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.users_info200_response import UsersInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInfo200Response from a JSON string
users_info200_response_instance = UsersInfo200Response.from_json(json)
# print the JSON string representation of the object
print(UsersInfo200Response.to_json())

# convert the object into a dict
users_info200_response_dict = users_info200_response_instance.to_dict()
# create an instance of UsersInfo200Response from a dict
users_info200_response_from_dict = UsersInfo200Response.from_dict(users_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


