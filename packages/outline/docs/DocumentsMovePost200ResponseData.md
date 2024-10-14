# DocumentsMovePost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[Document]**](Document.md) |  | [optional] 
**collections** | [**List[Collection]**](Collection.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_move_post200_response_data import DocumentsMovePost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsMovePost200ResponseData from a JSON string
documents_move_post200_response_data_instance = DocumentsMovePost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(DocumentsMovePost200ResponseData.to_json())

# convert the object into a dict
documents_move_post200_response_data_dict = documents_move_post200_response_data_instance.to_dict()
# create an instance of DocumentsMovePost200ResponseData from a dict
documents_move_post200_response_data_from_dict = DocumentsMovePost200ResponseData.from_dict(documents_move_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


