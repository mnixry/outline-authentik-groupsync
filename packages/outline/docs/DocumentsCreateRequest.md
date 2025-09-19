# DocumentsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**text** | **str** | The body of the document in markdown | [optional] 
**collection_id** | **str** |  | 
**parent_document_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**template** | **bool** | Whether this document should be considered to be a template. | [optional] 
**publish** | **bool** | Whether this document should be immediately published and made visible to other team members. | [optional] 

## Example

```python
from outline_openapi.models.documents_create_request import DocumentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsCreateRequest from a JSON string
documents_create_request_instance = DocumentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsCreateRequest.to_json())

# convert the object into a dict
documents_create_request_dict = documents_create_request_instance.to_dict()
# create an instance of DocumentsCreateRequest from a dict
documents_create_request_from_dict = DocumentsCreateRequest.from_dict(documents_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


