# DocumentsMembershipsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**query** | **str** | If set, will filter the results by user name | [optional] 

## Example

```python
from outline_openapi.models.documents_memberships_post_request import DocumentsMembershipsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsMembershipsPostRequest from a JSON string
documents_memberships_post_request_instance = DocumentsMembershipsPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsMembershipsPostRequest.to_json())

# convert the object into a dict
documents_memberships_post_request_dict = documents_memberships_post_request_instance.to_dict()
# create an instance of DocumentsMembershipsPostRequest from a dict
documents_memberships_post_request_from_dict = DocumentsMembershipsPostRequest.from_dict(documents_memberships_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


