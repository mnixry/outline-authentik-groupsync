# GroupsCreatePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Group**](Group.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_create_post200_response import GroupsCreatePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsCreatePost200Response from a JSON string
groups_create_post200_response_instance = GroupsCreatePost200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsCreatePost200Response.to_json())

# convert the object into a dict
groups_create_post200_response_dict = groups_create_post200_response_instance.to_dict()
# create an instance of GroupsCreatePost200Response from a dict
groups_create_post200_response_from_dict = GroupsCreatePost200Response.from_dict(groups_create_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


