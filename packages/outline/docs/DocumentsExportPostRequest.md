# DocumentsExportPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | [optional] 

## Example

```python
from outline_openapi.models.documents_export_post_request import DocumentsExportPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsExportPostRequest from a JSON string
documents_export_post_request_instance = DocumentsExportPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsExportPostRequest.to_json())

# convert the object into a dict
documents_export_post_request_dict = documents_export_post_request_instance.to_dict()
# create an instance of DocumentsExportPostRequest from a dict
documents_export_post_request_from_dict = DocumentsExportPostRequest.from_dict(documents_export_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


