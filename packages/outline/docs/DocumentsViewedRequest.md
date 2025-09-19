# DocumentsViewedRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.documents_viewed_request import DocumentsViewedRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsViewedRequest from a JSON string
documents_viewed_request_instance = DocumentsViewedRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsViewedRequest.to_json())

# convert the object into a dict
documents_viewed_request_dict = documents_viewed_request_instance.to_dict()
# create an instance of DocumentsViewedRequest from a dict
documents_viewed_request_from_dict = DocumentsViewedRequest.from_dict(documents_viewed_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


