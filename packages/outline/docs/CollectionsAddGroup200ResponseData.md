# CollectionsAddGroup200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**collection_group_memberships** | [**List[CollectionGroupMembership]**](CollectionGroupMembership.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_add_group200_response_data import CollectionsAddGroup200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsAddGroup200ResponseData from a JSON string
collections_add_group200_response_data_instance = CollectionsAddGroup200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CollectionsAddGroup200ResponseData.to_json())

# convert the object into a dict
collections_add_group200_response_data_dict = collections_add_group200_response_data_instance.to_dict()
# create an instance of CollectionsAddGroup200ResponseData from a dict
collections_add_group200_response_data_from_dict = CollectionsAddGroup200ResponseData.from_dict(collections_add_group200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


