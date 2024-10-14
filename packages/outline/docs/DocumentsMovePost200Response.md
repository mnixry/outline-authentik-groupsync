# DocumentsMovePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DocumentsMovePost200ResponseData**](DocumentsMovePost200ResponseData.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_move_post200_response import DocumentsMovePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsMovePost200Response from a JSON string
documents_move_post200_response_instance = DocumentsMovePost200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentsMovePost200Response.to_json())

# convert the object into a dict
documents_move_post200_response_dict = documents_move_post200_response_instance.to_dict()
# create an instance of DocumentsMovePost200Response from a dict
documents_move_post200_response_from_dict = DocumentsMovePost200Response.from_dict(documents_move_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


