# DocumentsSearch200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[DocumentsSearch200ResponseDataInner]**](DocumentsSearch200ResponseDataInner.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_search200_response import DocumentsSearch200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsSearch200Response from a JSON string
documents_search200_response_instance = DocumentsSearch200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentsSearch200Response.to_json())

# convert the object into a dict
documents_search200_response_dict = documents_search200_response_instance.to_dict()
# create an instance of DocumentsSearch200Response from a dict
documents_search200_response_from_dict = DocumentsSearch200Response.from_dict(documents_search200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


