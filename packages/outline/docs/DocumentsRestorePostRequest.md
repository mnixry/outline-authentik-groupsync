# DocumentsRestorePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**revision_id** | **str** | Identifier for the revision to restore to. | [optional] 

## Example

```python
from outline_openapi.models.documents_restore_post_request import DocumentsRestorePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsRestorePostRequest from a JSON string
documents_restore_post_request_instance = DocumentsRestorePostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsRestorePostRequest.to_json())

# convert the object into a dict
documents_restore_post_request_dict = documents_restore_post_request_instance.to_dict()
# create an instance of DocumentsRestorePostRequest from a dict
documents_restore_post_request_from_dict = DocumentsRestorePostRequest.from_dict(documents_restore_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


