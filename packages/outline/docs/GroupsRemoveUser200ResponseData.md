# GroupsRemoveUser200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[Group]**](Group.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_remove_user200_response_data import GroupsRemoveUser200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsRemoveUser200ResponseData from a JSON string
groups_remove_user200_response_data_instance = GroupsRemoveUser200ResponseData.from_json(json)
# print the JSON string representation of the object
print(GroupsRemoveUser200ResponseData.to_json())

# convert the object into a dict
groups_remove_user200_response_data_dict = groups_remove_user200_response_data_instance.to_dict()
# create an instance of GroupsRemoveUser200ResponseData from a dict
groups_remove_user200_response_data_from_dict = GroupsRemoveUser200ResponseData.from_dict(groups_remove_user200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


