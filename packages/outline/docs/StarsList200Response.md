# StarsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**StarsList200ResponseData**](StarsList200ResponseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.stars_list200_response import StarsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StarsList200Response from a JSON string
stars_list200_response_instance = StarsList200Response.from_json(json)
# print the JSON string representation of the object
print(StarsList200Response.to_json())

# convert the object into a dict
stars_list200_response_dict = stars_list200_response_instance.to_dict()
# create an instance of StarsList200Response from a dict
stars_list200_response_from_dict = StarsList200Response.from_dict(stars_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


