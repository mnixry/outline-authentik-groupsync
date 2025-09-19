# DocumentsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**collection_id** | **str** | Optionally filter to a specific collection | [optional] 
**user_id** | **str** |  | [optional] 
**backlink_document_id** | **str** |  | [optional] 
**parent_document_id** | **str** |  | [optional] 
**template** | **bool** | Optionally filter to only templates | [optional] 

## Example

```python
from outline_openapi.models.documents_list_request import DocumentsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsListRequest from a JSON string
documents_list_request_instance = DocumentsListRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsListRequest.to_json())

# convert the object into a dict
documents_list_request_dict = documents_list_request_instance.to_dict()
# create an instance of DocumentsListRequest from a dict
documents_list_request_from_dict = DocumentsListRequest.from_dict(documents_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


