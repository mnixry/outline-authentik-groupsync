# AuthInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Auth**](Auth.md) |  | [optional] 

## Example

```python
from outline_openapi.models.auth_info200_response import AuthInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthInfo200Response from a JSON string
auth_info200_response_instance = AuthInfo200Response.from_json(json)
# print the JSON string representation of the object
print(AuthInfo200Response.to_json())

# convert the object into a dict
auth_info200_response_dict = auth_info200_response_instance.to_dict()
# create an instance of AuthInfo200Response from a dict
auth_info200_response_from_dict = AuthInfo200Response.from_dict(auth_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


