# FileoperationsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[FileOperation]**](FileOperation.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.fileoperations_list200_response import FileoperationsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of FileoperationsList200Response from a JSON string
fileoperations_list200_response_instance = FileoperationsList200Response.from_json(json)
# print the JSON string representation of the object
print(FileoperationsList200Response.to_json())

# convert the object into a dict
fileoperations_list200_response_dict = fileoperations_list200_response_instance.to_dict()
# create an instance of FileoperationsList200Response from a dict
fileoperations_list200_response_from_dict = FileoperationsList200Response.from_dict(fileoperations_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


