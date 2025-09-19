# DocumentsExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 

## Example

```python
from outline_openapi.models.documents_export_request import DocumentsExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsExportRequest from a JSON string
documents_export_request_instance = DocumentsExportRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsExportRequest.to_json())

# convert the object into a dict
documents_export_request_dict = documents_export_request_instance.to_dict()
# create an instance of DocumentsExportRequest from a dict
documents_export_request_from_dict = DocumentsExportRequest.from_dict(documents_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


