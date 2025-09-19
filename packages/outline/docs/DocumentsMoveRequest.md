# DocumentsMoveRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**collection_id** | **str** |  | [optional] 
**parent_document_id** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.documents_move_request import DocumentsMoveRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsMoveRequest from a JSON string
documents_move_request_instance = DocumentsMoveRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsMoveRequest.to_json())

# convert the object into a dict
documents_move_request_dict = documents_move_request_instance.to_dict()
# create an instance of DocumentsMoveRequest from a dict
documents_move_request_from_dict = DocumentsMoveRequest.from_dict(documents_move_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


