# DocumentsStarPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. Either the UUID or the urlId is acceptable. | 

## Example

```python
from outline_openapi.models.documents_star_post_request import DocumentsStarPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsStarPostRequest from a JSON string
documents_star_post_request_instance = DocumentsStarPostRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsStarPostRequest.to_json())

# convert the object into a dict
documents_star_post_request_dict = documents_star_post_request_instance.to_dict()
# create an instance of DocumentsStarPostRequest from a dict
documents_star_post_request_from_dict = DocumentsStarPostRequest.from_dict(documents_star_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


