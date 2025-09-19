# CollectionsAddGroupRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**group_id** | **str** |  | 
**permission** | [**Permission**](Permission.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_add_group_request import CollectionsAddGroupRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsAddGroupRequest from a JSON string
collections_add_group_request_instance = CollectionsAddGroupRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsAddGroupRequest.to_json())

# convert the object into a dict
collections_add_group_request_dict = collections_add_group_request_instance.to_dict()
# create an instance of CollectionsAddGroupRequest from a dict
collections_add_group_request_from_dict = CollectionsAddGroupRequest.from_dict(collections_add_group_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


