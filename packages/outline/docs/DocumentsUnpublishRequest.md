# DocumentsUnpublishRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 

## Example

```python
from outline_openapi.models.documents_unpublish_request import DocumentsUnpublishRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsUnpublishRequest from a JSON string
documents_unpublish_request_instance = DocumentsUnpublishRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsUnpublishRequest.to_json())

# convert the object into a dict
documents_unpublish_request_dict = documents_unpublish_request_instance.to_dict()
# create an instance of DocumentsUnpublishRequest from a dict
documents_unpublish_request_from_dict = DocumentsUnpublishRequest.from_dict(documents_unpublish_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


