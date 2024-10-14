# Revision


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**document_id** | **str** | Identifier for the associated document. | [optional] [readonly] 
**title** | **str** | Title of the document. | [optional] [readonly] 
**text** | **str** | Body of the document, may contain markdown formatting | [optional] [readonly] 
**created_at** | **datetime** | Date and time when this revision was created | [optional] [readonly] 
**created_by** | [**User**](User.md) |  | [optional] 

## Example

```python
from outline_openapi.models.revision import Revision

# TODO update the JSON string below
json = "{}"
# create an instance of Revision from a JSON string
revision_instance = Revision.from_json(json)
# print the JSON string representation of the object
print(Revision.to_json())

# convert the object into a dict
revision_dict = revision_instance.to_dict()
# create an instance of Revision from a dict
revision_from_dict = Revision.from_dict(revision_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


