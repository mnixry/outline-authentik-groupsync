# StarsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** |  | [optional] 
**collection_id** | **str** |  | [optional] 
**index** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.stars_create_request import StarsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of StarsCreateRequest from a JSON string
stars_create_request_instance = StarsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(StarsCreateRequest.to_json())

# convert the object into a dict
stars_create_request_dict = stars_create_request_instance.to_dict()
# create an instance of StarsCreateRequest from a dict
stars_create_request_from_dict = StarsCreateRequest.from_dict(stars_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


