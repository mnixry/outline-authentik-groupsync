# StarsCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Star**](Star.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.stars_create200_response import StarsCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of StarsCreate200Response from a JSON string
stars_create200_response_instance = StarsCreate200Response.from_json(json)
# print the JSON string representation of the object
print(StarsCreate200Response.to_json())

# convert the object into a dict
stars_create200_response_dict = stars_create200_response_instance.to_dict()
# create an instance of StarsCreate200Response from a dict
stars_create200_response_from_dict = StarsCreate200Response.from_dict(stars_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


