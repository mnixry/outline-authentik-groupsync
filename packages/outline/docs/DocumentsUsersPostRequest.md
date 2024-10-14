# DocumentsUsersPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**query** | **str** | If set, will filter the results by user name. | [optional] 

## Example

```python
from outline_openapi.models.documents_users_post_request import DocumentsUsersPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsUsersPostRequest from a JSON string
documents_users_post_request_instance = DocumentsUsersPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsUsersPostRequest.to_json())

# convert the object into a dict
documents_users_post_request_dict = documents_users_post_request_instance.to_dict()
# create an instance of DocumentsUsersPostRequest from a dict
documents_users_post_request_from_dict = DocumentsUsersPostRequest.from_dict(documents_users_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


