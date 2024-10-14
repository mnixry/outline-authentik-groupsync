# AuthInfoPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Auth**](Auth.md) |  | [optional] 

## Example

```python
from outline_openapi.models.auth_info_post200_response import AuthInfoPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthInfoPost200Response from a JSON string
auth_info_post200_response_instance = AuthInfoPost200Response.from_json(json)
# print the JSON string representation of the object
print(AuthInfoPost200Response.to_json())

# convert the object into a dict
auth_info_post200_response_dict = auth_info_post200_response_instance.to_dict()
# create an instance of AuthInfoPost200Response from a dict
auth_info_post200_response_from_dict = AuthInfoPost200Response.from_dict(auth_info_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


