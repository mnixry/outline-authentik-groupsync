# GroupsRemoveUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupsRemoveUser200ResponseData**](GroupsRemoveUser200ResponseData.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_remove_user200_response import GroupsRemoveUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsRemoveUser200Response from a JSON string
groups_remove_user200_response_instance = GroupsRemoveUser200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsRemoveUser200Response.to_json())

# convert the object into a dict
groups_remove_user200_response_dict = groups_remove_user200_response_instance.to_dict()
# create an instance of GroupsRemoveUser200Response from a dict
groups_remove_user200_response_from_dict = GroupsRemoveUser200Response.from_dict(groups_remove_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


