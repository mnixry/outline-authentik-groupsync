# CollectionsRemoveGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the collection | 
**group_id** | **str** |  | 

## Example

```python
from outline_openapi.models.collections_remove_group_request import CollectionsRemoveGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsRemoveGroupRequest from a JSON string
collections_remove_group_request_instance = CollectionsRemoveGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsRemoveGroupRequest.to_json())

# convert the object into a dict
collections_remove_group_request_dict = collections_remove_group_request_instance.to_dict()
# create an instance of CollectionsRemoveGroupRequest from a dict
collections_remove_group_request_from_dict = CollectionsRemoveGroupRequest.from_dict(collections_remove_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


