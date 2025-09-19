# GroupsAddUser200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupsAddUser200ResponseData**](GroupsAddUser200ResponseData.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_add_user200_response import GroupsAddUser200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsAddUser200Response from a JSON string
groups_add_user200_response_instance = GroupsAddUser200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsAddUser200Response.to_json())

# convert the object into a dict
groups_add_user200_response_dict = groups_add_user200_response_instance.to_dict()
# create an instance of GroupsAddUser200Response from a dict
groups_add_user200_response_from_dict = GroupsAddUser200Response.from_dict(groups_add_user200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


