# DocumentsCreatePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Document**](Document.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsCreatePost200Response from a JSON string
documents_create_post200_response_instance = DocumentsCreatePost200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentsCreatePost200Response.to_json())

# convert the object into a dict
documents_create_post200_response_dict = documents_create_post200_response_instance.to_dict()
# create an instance of DocumentsCreatePost200Response from a dict
documents_create_post200_response_from_dict = DocumentsCreatePost200Response.from_dict(documents_create_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


