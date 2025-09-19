# DocumentsDraftsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**collection_id** | **str** | A collection to search within | [optional] 
**date_filter** | **str** | Any documents that have not been updated within the specified period will be filtered out | [optional] 

## Example

```python
from outline_openapi.models.documents_drafts_request import DocumentsDraftsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsDraftsRequest from a JSON string
documents_drafts_request_instance = DocumentsDraftsRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsDraftsRequest.to_json())

# convert the object into a dict
documents_drafts_request_dict = documents_drafts_request_instance.to_dict()
# create an instance of DocumentsDraftsRequest from a dict
documents_drafts_request_from_dict = DocumentsDraftsRequest.from_dict(documents_drafts_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


