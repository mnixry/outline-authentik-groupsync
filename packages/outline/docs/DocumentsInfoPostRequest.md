# DocumentsInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | [optional] 
**share_id** | **str** | Unique identifier for a document share, a shareId may be used in place of a document UUID | [optional] 

## Example

```python
from outline_openapi.models.documents_info_post_request import DocumentsInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsInfoPostRequest from a JSON string
documents_info_post_request_instance = DocumentsInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsInfoPostRequest.to_json())

# convert the object into a dict
documents_info_post_request_dict = documents_info_post_request_instance.to_dict()
# create an instance of DocumentsInfoPostRequest from a dict
documents_info_post_request_from_dict = DocumentsInfoPostRequest.from_dict(documents_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


