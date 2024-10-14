# FileOperationCollection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**name** | **str** | The name of the collection. | [optional] 
**description** | **str** | A description of the collection, may contain markdown formatting | [optional] 
**sort** | [**CollectionSort**](CollectionSort.md) |  | [optional] 
**index** | **str** | The position of the collection in the sidebar | [optional] 
**color** | **str** | A color representing the collection, this is used to help make collections more identifiable in the UI. It should be in HEX format including the # | [optional] 
**icon** | **str** | A string that represents an icon in the outline-icons package | [optional] 
**permission** | [**Permission**](Permission.md) |  | [optional] 
**created_at** | **datetime** | The date and time that this object was created | [optional] [readonly] 
**updated_at** | **datetime** | The date and time that this object was last changed | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time that this object was deleted | [optional] [readonly] 

## Example

```python
from outline_openapi.models.file_operation_collection import FileOperationCollection

# TODO update the JSON string below
json = "{}"
# create an instance of FileOperationCollection from a JSON string
file_operation_collection_instance = FileOperationCollection.from_json(json)
# print the JSON string representation of the object
print(FileOperationCollection.to_json())

# convert the object into a dict
file_operation_collection_dict = file_operation_collection_instance.to_dict()
# create an instance of FileOperationCollection from a dict
file_operation_collection_from_dict = FileOperationCollection.from_dict(file_operation_collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


