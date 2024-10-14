# GroupsListPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) |  | [optional] 
**group_memberships** | [**List[GroupMembership]**](GroupMembership.md) | A preview of memberships in the group, note that this is not all memberships which can be queried from &#x60;groups.memberships&#x60;. | [optional] 

## Example

```python
from outline_openapi.models.groups_list_post200_response_data import GroupsListPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsListPost200ResponseData from a JSON string
groups_list_post200_response_data_instance = GroupsListPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GroupsListPost200ResponseData.to_json())

# convert the object into a dict
groups_list_post200_response_data_dict = groups_list_post200_response_data_instance.to_dict()
# create an instance of GroupsListPost200ResponseData from a dict
groups_list_post200_response_data_from_dict = GroupsListPost200ResponseData.from_dict(groups_list_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


