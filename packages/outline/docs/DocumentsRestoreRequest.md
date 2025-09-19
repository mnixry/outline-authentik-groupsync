# DocumentsRestoreRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**revision_id** | **str** | Identifier for the revision to restore to. | [optional] 

## Example

```python
from outline_openapi.models.documents_restore_request import DocumentsRestoreRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsRestoreRequest from a JSON string
documents_restore_request_instance = DocumentsRestoreRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsRestoreRequest.to_json())

# convert the object into a dict
documents_restore_request_dict = documents_restore_request_instance.to_dict()
# create an instance of DocumentsRestoreRequest from a dict
documents_restore_request_from_dict = DocumentsRestoreRequest.from_dict(documents_restore_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


