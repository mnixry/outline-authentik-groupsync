# GroupsMembershipsPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) |  | [optional] 
**group_memberships** | [**List[GroupMembership]**](GroupMembership.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_memberships_post200_response_data import GroupsMembershipsPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsMembershipsPost200ResponseData from a JSON string
groups_memberships_post200_response_data_instance = GroupsMembershipsPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GroupsMembershipsPost200ResponseData.to_json())

# convert the object into a dict
groups_memberships_post200_response_data_dict = groups_memberships_post200_response_data_instance.to_dict()
# create an instance of GroupsMembershipsPost200ResponseData from a dict
groups_memberships_post200_response_data_from_dict = GroupsMembershipsPost200ResponseData.from_dict(groups_memberships_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


