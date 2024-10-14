# DocumentsCreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | 
**text** | **str** | The body of the document, may contain markdown formatting. | [optional] 
**collection_id** | **str** |  | 
**parent_document_id** | **str** |  | [optional] 
**template_id** | **str** |  | [optional] 
**template** | **bool** | Whether this document should be considered to be a template. | [optional] 
**publish** | **bool** | Whether this document should be immediately published and made visible to other team members. | [optional] 

## Example

```python
from outline_openapi.models.documents_create_post_request import DocumentsCreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsCreatePostRequest from a JSON string
documents_create_post_request_instance = DocumentsCreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsCreatePostRequest.to_json())

# convert the object into a dict
documents_create_post_request_dict = documents_create_post_request_instance.to_dict()
# create an instance of DocumentsCreatePostRequest from a dict
documents_create_post_request_from_dict = DocumentsCreatePostRequest.from_dict(documents_create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


