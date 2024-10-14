# DocumentsMovePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**collection_id** | **str** |  | [optional] 
**parent_document_id** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.documents_move_post_request import DocumentsMovePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsMovePostRequest from a JSON string
documents_move_post_request_instance = DocumentsMovePostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsMovePostRequest.to_json())

# convert the object into a dict
documents_move_post_request_dict = documents_move_post_request_instance.to_dict()
# create an instance of DocumentsMovePostRequest from a dict
documents_move_post_request_from_dict = DocumentsMovePostRequest.from_dict(documents_move_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


