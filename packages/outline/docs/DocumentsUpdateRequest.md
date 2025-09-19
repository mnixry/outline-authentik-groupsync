# DocumentsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**title** | **str** | The title of the document. | [optional] 
**text** | **str** | The body of the document in markdown. | [optional] 
**append** | **bool** | If true the text field will be appended to the end of the existing document, rather than the default behavior of replacing it. This is potentially useful for things like logging into a document. | [optional] 
**publish** | **bool** | Whether this document should be published and made visible to other team members, if a draft | [optional] 
**done** | **bool** | Whether the editing session has finished, this will trigger any notifications. This property will soon be deprecated. | [optional] 

## Example

```python
from outline_openapi.models.documents_update_request import DocumentsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsUpdateRequest from a JSON string
documents_update_request_instance = DocumentsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsUpdateRequest.to_json())

# convert the object into a dict
documents_update_request_dict = documents_update_request_instance.to_dict()
# create an instance of DocumentsUpdateRequest from a dict
documents_update_request_from_dict = DocumentsUpdateRequest.from_dict(documents_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


