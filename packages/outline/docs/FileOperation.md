# FileOperation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**type** | **str** | The type of file operation. | [optional] [readonly] 
**state** | **str** | The state of the file operation. | [optional] [readonly] 
**collection** | [**Collection**](Collection.md) |  | [optional] 
**user** | [**User**](User.md) |  | [optional] 
**size** | **float** | The size of the resulting file in bytes | [optional] [readonly] 
**created_at** | **datetime** | The date and time that this object was created | [optional] [readonly] 

## Example

```python
from outline_openapi.models.file_operation import FileOperation

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperation from a JSON string
file_operation_instance = FileOperation.from_json(json)
# print the JSON string representation of the object
print(FileOperation.to_json())

# convert the object into a dict
file_operation_dict = file_operation_instance.to_dict()
# create an instance of FileOperation from a dict
file_operation_from_dict = FileOperation.from_dict(file_operation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


