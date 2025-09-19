# AuthConfig200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**hostname** | **str** |  | [optional] 
**services** | [**List[AuthConfig200ResponseDataServicesInner]**](AuthConfig200ResponseDataServicesInner.md) |  | [optional] 

## Example

```python
from outline_openapi.models.auth_config200_response_data import AuthConfig200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of AuthConfig200ResponseData from a JSON string
auth_config200_response_data_instance = AuthConfig200ResponseData.from_json(json)
# print the JSON string representation of the object
print(AuthConfig200ResponseData.to_json())

# convert the object into a dict
auth_config200_response_data_dict = auth_config200_response_data_instance.to_dict()
# create an instance of AuthConfig200ResponseData from a dict
auth_config200_response_data_from_dict = AuthConfig200ResponseData.from_dict(auth_config200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


