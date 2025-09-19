# GroupsInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Group**](Group.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_info200_response import GroupsInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsInfo200Response from a JSON string
groups_info200_response_instance = GroupsInfo200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsInfo200Response.to_json())

# convert the object into a dict
groups_info200_response_dict = groups_info200_response_instance.to_dict()
# create an instance of GroupsInfo200Response from a dict
groups_info200_response_from_dict = GroupsInfo200Response.from_dict(groups_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


