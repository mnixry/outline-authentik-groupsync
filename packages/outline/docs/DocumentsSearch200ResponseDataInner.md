# DocumentsSearch200ResponseDataInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**context** | **str** | A short snippet of context from the document that includes the search query. | [optional] 
**ranking** | **float** | The ranking used to order search results based on relevance. | [optional] 
**document** | [**Document**](Document.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_search200_response_data_inner import DocumentsSearch200ResponseDataInner

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsSearch200ResponseDataInner from a JSON string
documents_search200_response_data_inner_instance = DocumentsSearch200ResponseDataInner.from_json(json)
# print the JSON string representation of the object
print(DocumentsSearch200ResponseDataInner.to_json())

# convert the object into a dict
documents_search200_response_data_inner_dict = documents_search200_response_data_inner_instance.to_dict()
# create an instance of DocumentsSearch200ResponseDataInner from a dict
documents_search200_response_data_inner_from_dict = DocumentsSearch200ResponseDataInner.from_dict(documents_search200_response_data_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


