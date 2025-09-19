# AuthConfig200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AuthConfig200ResponseData**](AuthConfig200ResponseData.md) |  | [optional] 

## Example

```python
from outline_openapi.models.auth_config200_response import AuthConfig200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfig200Response from a JSON string
auth_config200_response_instance = AuthConfig200Response.from_json(json)
# print the JSON string representation of the object
print(AuthConfig200Response.to_json())

# convert the object into a dict
auth_config200_response_dict = auth_config200_response_instance.to_dict()
# create an instance of AuthConfig200Response from a dict
auth_config200_response_from_dict = AuthConfig200Response.from_dict(auth_config200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


