# DocumentsAddUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**user_id** | **str** |  | 
**permission** | [**Permission**](Permission.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_add_user_request import DocumentsAddUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsAddUserRequest from a JSON string
documents_add_user_request_instance = DocumentsAddUserRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsAddUserRequest.to_json())

# convert the object into a dict
documents_add_user_request_dict = documents_add_user_request_instance.to_dict()
# create an instance of DocumentsAddUserRequest from a dict
documents_add_user_request_from_dict = DocumentsAddUserRequest.from_dict(documents_add_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


