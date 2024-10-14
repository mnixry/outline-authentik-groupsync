# CollectionGroupMembership


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**group_id** | **str** | Identifier for the associated group. | [optional] [readonly] 
**collection_id** | **str** | Identifier for the associated collection. | [optional] [readonly] 
**permission** | [**Permission**](Permission.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collection_group_membership import CollectionGroupMembership

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionGroupMembership from a JSON string
collection_group_membership_instance = CollectionGroupMembership.from_json(json)
# print the JSON string representation of the object
print(CollectionGroupMembership.to_json())

# convert the object into a dict
collection_group_membership_dict = collection_group_membership_instance.to_dict()
# create an instance of CollectionGroupMembership from a dict
collection_group_membership_from_dict = CollectionGroupMembership.from_dict(collection_group_membership_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


