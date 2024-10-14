# GroupsMembershipsPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**id** | **str** | Group id | 
**query** | **str** | Filter memberships by user names | [optional] 

## Example

```python
from outline_openapi.models.groups_memberships_post_request import GroupsMembershipsPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsMembershipsPostRequest from a JSON string
groups_memberships_post_request_instance = GroupsMembershipsPostRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsMembershipsPostRequest.to_json())

# convert the object into a dict
groups_memberships_post_request_dict = groups_memberships_post_request_instance.to_dict()
# create an instance of GroupsMembershipsPostRequest from a dict
groups_memberships_post_request_from_dict = GroupsMembershipsPostRequest.from_dict(groups_memberships_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


