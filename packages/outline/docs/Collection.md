# Collection


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**url_id** | **str** | A short unique identifier that can be used to identify the collection instead of the UUID. | [optional] [readonly] 
**name** | **str** | The name of the collection. | [optional] 
**description** | **str** | A description of the collection, may contain markdown formatting | [optional] 
**sort** | [**CollectionSort**](CollectionSort.md) |  | [optional] 
**index** | **str** | The position of the collection in the sidebar | [optional] 
**color** | **str** | A color representing the collection, this is used to help make collections more identifiable in the UI. It should be in HEX format including the # | [optional] 
**icon** | **str** | A string that represents an icon in the outline-icons package or an emoji | [optional] 
**permission** | [**Permission**](Permission.md) |  | [optional] 
**sharing** | **bool** | Whether public document sharing is enabled in this collection | [optional] [default to False]
**created_at** | **datetime** | The date and time that this object was created | [optional] [readonly] 
**updated_at** | **datetime** | The date and time that this object was last changed | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time that this object was deleted | [optional] [readonly] 
**archived_at** | **datetime** | The date and time that this object was archived | [optional] [readonly] 
**archived_by** | [**User**](User.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collection import Collection

# TODO update the JSON string below
json = "{}"
# create an instance of Collection from a JSON string
collection_instance = Collection.from_json(json)
# print the JSON string representation of the object
print(Collection.to_json())

# convert the object into a dict
collection_dict = collection_instance.to_dict()
# create an instance of Collection from a dict
collection_from_dict = Collection.from_dict(collection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


