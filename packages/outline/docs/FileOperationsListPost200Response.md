# FileOperationsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FileOperation]**](FileOperation.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.file_operations_list_post200_response import FileOperationsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationsListPost200Response from a JSON string
file_operations_list_post200_response_instance = FileOperationsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(FileOperationsListPost200Response.to_json())

# convert the object into a dict
file_operations_list_post200_response_dict = file_operations_list_post200_response_instance.to_dict()
# create an instance of FileOperationsListPost200Response from a dict
file_operations_list_post200_response_from_dict = FileOperationsListPost200Response.from_dict(file_operations_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


