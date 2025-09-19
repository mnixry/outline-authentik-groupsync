# Star


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**index** | **str** | Index of the star in the list of stars. | [optional] 
**document_id** | **str** | Unique identifier for the starred document. | [optional] [readonly] 
**collection_id** | **str** | Unique identifier for the starred collection. | [optional] [readonly] 
**document_url** | **str** | URL of the original document. | [optional] [readonly] 
**created_at** | **datetime** | Date and time when this star was created | [optional] [readonly] 

## Example

```python
from outline_openapi.models.star import Star

# TODO update the JSON string below
json = "{}"
# create an instance of Star from a JSON string
star_instance = Star.from_json(json)
# print the JSON string representation of the object
print(Star.to_json())

# convert the object into a dict
star_dict = star_instance.to_dict()
# create an instance of Star from a dict
star_from_dict = Star.from_dict(star_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


