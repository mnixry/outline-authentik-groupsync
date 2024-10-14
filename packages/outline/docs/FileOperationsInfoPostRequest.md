# FileOperationsInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the file operation. | 

## Example

```python
from outline_openapi.models.file_operations_info_post_request import FileOperationsInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationsInfoPostRequest from a JSON string
file_operations_info_post_request_instance = FileOperationsInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(FileOperationsInfoPostRequest.to_json())

# convert the object into a dict
file_operations_info_post_request_dict = file_operations_info_post_request_instance.to_dict()
# create an instance of FileOperationsInfoPostRequest from a dict
file_operations_info_post_request_from_dict = FileOperationsInfoPostRequest.from_dict(file_operations_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


