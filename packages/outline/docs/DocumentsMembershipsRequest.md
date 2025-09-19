# DocumentsMembershipsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 
**query** | **str** | If set, will filter the results by user name | [optional] 

## Example

```python
from outline_openapi.models.documents_memberships_request import DocumentsMembershipsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsMembershipsRequest from a JSON string
documents_memberships_request_instance = DocumentsMembershipsRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsMembershipsRequest.to_json())

# convert the object into a dict
documents_memberships_request_dict = documents_memberships_request_instance.to_dict()
# create an instance of DocumentsMembershipsRequest from a dict
documents_memberships_request_from_dict = DocumentsMembershipsRequest.from_dict(documents_memberships_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


