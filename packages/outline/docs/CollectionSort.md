# CollectionSort

The sort of documents in the collection. Note that not all API responses respect this and it is left as a frontend concern to implement.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.collection_sort import CollectionSort

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionSort from a JSON string
collection_sort_instance = CollectionSort.from_json(json)
# print the JSON string representation of the object
print(CollectionSort.to_json())

# convert the object into a dict
collection_sort_dict = collection_sort_instance.to_dict()
# create an instance of CollectionSort from a dict
collection_sort_from_dict = CollectionSort.from_dict(collection_sort_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


