# GroupsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from outline_openapi.models.groups_update_request import GroupsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsUpdateRequest from a JSON string
groups_update_request_instance = GroupsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsUpdateRequest.to_json())

# convert the object into a dict
groups_update_request_dict = groups_update_request_instance.to_dict()
# create an instance of GroupsUpdateRequest from a dict
groups_update_request_from_dict = GroupsUpdateRequest.from_dict(groups_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


