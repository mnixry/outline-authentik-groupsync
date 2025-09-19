# FileoperationsInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the file operation. | 

## Example

```python
from outline_openapi.models.fileoperations_info_request import FileoperationsInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileoperationsInfoRequest from a JSON string
fileoperations_info_request_instance = FileoperationsInfoRequest.from_json(json)
# print the JSON string representation of the object
print(FileoperationsInfoRequest.to_json())

# convert the object into a dict
fileoperations_info_request_dict = fileoperations_info_request_instance.to_dict()
# create an instance of FileoperationsInfoRequest from a dict
fileoperations_info_request_from_dict = FileoperationsInfoRequest.from_dict(fileoperations_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


