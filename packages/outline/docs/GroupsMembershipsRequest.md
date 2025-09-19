# GroupsMembershipsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**id** | **str** | Group id | 
**query** | **str** | Filter memberships by user names | [optional] 

## Example

```python
from outline_openapi.models.groups_memberships_request import GroupsMembershipsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsMembershipsRequest from a JSON string
groups_memberships_request_instance = GroupsMembershipsRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsMembershipsRequest.to_json())

# convert the object into a dict
groups_memberships_request_dict = groups_memberships_request_instance.to_dict()
# create an instance of GroupsMembershipsRequest from a dict
groups_memberships_request_from_dict = GroupsMembershipsRequest.from_dict(groups_memberships_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


