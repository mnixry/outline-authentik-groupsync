# StarsList200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stars** | [**List[Star]**](Star.md) |  | [optional] 
**documents** | [**List[Document]**](Document.md) |  | [optional] 

## Example

```python
from outline_openapi.models.stars_list200_response_data import StarsList200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of StarsList200ResponseData from a JSON string
stars_list200_response_data_instance = StarsList200ResponseData.from_json(json)
# print the JSON string representation of the object
print(StarsList200ResponseData.to_json())

# convert the object into a dict
stars_list200_response_data_dict = stars_list200_response_data_instance.to_dict()
# create an instance of StarsList200ResponseData from a dict
stars_list200_response_data_from_dict = StarsList200ResponseData.from_dict(stars_list200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


