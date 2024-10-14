# DocumentsDeletePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**permanent** | **bool** | If set to true the document will be destroyed with no way to recover rather than moved to the trash. | [optional] 

## Example

```python
from outline_openapi.models.documents_delete_post_request import DocumentsDeletePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsDeletePostRequest from a JSON string
documents_delete_post_request_instance = DocumentsDeletePostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsDeletePostRequest.to_json())

# convert the object into a dict
documents_delete_post_request_dict = documents_delete_post_request_instance.to_dict()
# create an instance of DocumentsDeletePostRequest from a dict
documents_delete_post_request_from_dict = DocumentsDeletePostRequest.from_dict(documents_delete_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


