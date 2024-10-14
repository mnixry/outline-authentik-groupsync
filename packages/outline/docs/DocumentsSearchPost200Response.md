# DocumentsSearchPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentsSearchPost200ResponseDataInner]**](DocumentsSearchPost200ResponseDataInner.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_search_post200_response import DocumentsSearchPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsSearchPost200Response from a JSON string
documents_search_post200_response_instance = DocumentsSearchPost200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentsSearchPost200Response.to_json())

# convert the object into a dict
documents_search_post200_response_dict = documents_search_post200_response_instance.to_dict()
# create an instance of DocumentsSearchPost200Response from a dict
documents_search_post200_response_from_dict = DocumentsSearchPost200Response.from_dict(documents_search_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


