# GroupsAddUserPost200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) |  | [optional] 
**groups** | [**List[Group]**](Group.md) |  | [optional] 
**group_memberships** | [**List[Membership]**](Membership.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_add_user_post200_response_data import GroupsAddUserPost200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsAddUserPost200ResponseData from a JSON string
groups_add_user_post200_response_data_instance = GroupsAddUserPost200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GroupsAddUserPost200ResponseData.to_json())

# convert the object into a dict
groups_add_user_post200_response_data_dict = groups_add_user_post200_response_data_instance.to_dict()
# create an instance of GroupsAddUserPost200ResponseData from a dict
groups_add_user_post200_response_data_from_dict = GroupsAddUserPost200ResponseData.from_dict(groups_add_user_post200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


