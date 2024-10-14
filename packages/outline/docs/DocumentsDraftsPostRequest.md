# DocumentsDraftsPostRequest


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
from outline_openapi.models.documents_drafts_post_request import DocumentsDraftsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsDraftsPostRequest from a JSON string
documents_drafts_post_request_instance = DocumentsDraftsPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsDraftsPostRequest.to_json())

# convert the object into a dict
documents_drafts_post_request_dict = documents_drafts_post_request_instance.to_dict()
# create an instance of DocumentsDraftsPostRequest from a dict
documents_drafts_post_request_from_dict = DocumentsDraftsPostRequest.from_dict(documents_drafts_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


