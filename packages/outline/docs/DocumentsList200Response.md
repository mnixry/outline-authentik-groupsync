# DocumentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Document]**](Document.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_list200_response import DocumentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsList200Response from a JSON string
documents_list200_response_instance = DocumentsList200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentsList200Response.to_json())

# convert the object into a dict
documents_list200_response_dict = documents_list200_response_instance.to_dict()
# create an instance of DocumentsList200Response from a dict
documents_list200_response_from_dict = DocumentsList200Response.from_dict(documents_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


