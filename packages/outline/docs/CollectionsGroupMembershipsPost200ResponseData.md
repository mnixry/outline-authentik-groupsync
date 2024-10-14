# CollectionsGroupMembershipsPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) |  | [optional] 
**collection_group_memberships** | [**List[CollectionGroupMembership]**](CollectionGroupMembership.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_group_memberships_post200_response_data import CollectionsGroupMembershipsPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsGroupMembershipsPost200ResponseData from a JSON string
collections_group_memberships_post200_response_data_instance = CollectionsGroupMembershipsPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CollectionsGroupMembershipsPost200ResponseData.to_json())

# convert the object into a dict
collections_group_memberships_post200_response_data_dict = collections_group_memberships_post200_response_data_instance.to_dict()
# create an instance of CollectionsGroupMembershipsPost200ResponseData from a dict
collections_group_memberships_post200_response_data_from_dict = CollectionsGroupMembershipsPost200ResponseData.from_dict(collections_group_memberships_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


