# FileoperationsListRequest


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
from outline_openapi.models.fileoperations_list_request import FileoperationsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of FileoperationsListRequest from a JSON string
fileoperations_list_request_instance = FileoperationsListRequest.from_json(json)
# print the JSON string representation of the object
print(FileoperationsListRequest.to_json())

# convert the object into a dict
fileoperations_list_request_dict = fileoperations_list_request_instance.to_dict()
# create an instance of FileoperationsListRequest from a dict
fileoperations_list_request_from_dict = FileoperationsListRequest.from_dict(fileoperations_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


