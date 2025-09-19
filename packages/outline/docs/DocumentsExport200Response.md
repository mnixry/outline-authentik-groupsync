# DocumentsExport200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **str** | The document content in Markdown formatting | [optional] 

## Example

```python
from outline_openapi.models.documents_export200_response import DocumentsExport200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsExport200Response from a JSON string
documents_export200_response_instance = DocumentsExport200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentsExport200Response.to_json())

# convert the object into a dict
documents_export200_response_dict = documents_export200_response_instance.to_dict()
# create an instance of DocumentsExport200Response from a dict
documents_export200_response_from_dict = DocumentsExport200Response.from_dict(documents_export200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


