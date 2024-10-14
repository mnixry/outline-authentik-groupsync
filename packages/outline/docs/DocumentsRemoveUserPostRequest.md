# DocumentsRemoveUserPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**user_id** | **str** |  | 

## Example

```python
from outline_openapi.models.documents_remove_user_post_request import DocumentsRemoveUserPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsRemoveUserPostRequest from a JSON string
documents_remove_user_post_request_instance = DocumentsRemoveUserPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsRemoveUserPostRequest.to_json())

# convert the object into a dict
documents_remove_user_post_request_dict = documents_remove_user_post_request_instance.to_dict()
# create an instance of DocumentsRemoveUserPostRequest from a dict
documents_remove_user_post_request_from_dict = DocumentsRemoveUserPostRequest.from_dict(documents_remove_user_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


