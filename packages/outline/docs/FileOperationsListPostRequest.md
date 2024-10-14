# FileOperationsListPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**type** | **str** | The type of fileOperation | 

## Example

```python
from outline_openapi.models.file_operations_list_post_request import FileOperationsListPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationsListPostRequest from a JSON string
file_operations_list_post_request_instance = FileOperationsListPostRequest.from_json(json)
# print the JSON string representation of the object
print(FileOperationsListPostRequest.to_json())

# convert the object into a dict
file_operations_list_post_request_dict = file_operations_list_post_request_instance.to_dict()
# create an instance of FileOperationsListPostRequest from a dict
file_operations_list_post_request_from_dict = FileOperationsListPostRequest.from_dict(file_operations_list_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


