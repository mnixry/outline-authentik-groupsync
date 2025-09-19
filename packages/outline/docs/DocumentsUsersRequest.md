# DocumentsUsersRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**query** | **str** | If set, will filter the results by user name. | [optional] 

## Example

```python
from outline_openapi.models.documents_users_request import DocumentsUsersRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsUsersRequest from a JSON string
documents_users_request_instance = DocumentsUsersRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsUsersRequest.to_json())

# convert the object into a dict
documents_users_request_dict = documents_users_request_instance.to_dict()
# create an instance of DocumentsUsersRequest from a dict
documents_users_request_from_dict = DocumentsUsersRequest.from_dict(documents_users_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


