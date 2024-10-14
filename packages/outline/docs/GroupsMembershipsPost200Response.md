# GroupsMembershipsPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupsMembershipsPost200ResponseData**](GroupsMembershipsPost200ResponseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_memberships_post200_response import GroupsMembershipsPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsMembershipsPost200Response from a JSON string
groups_memberships_post200_response_instance = GroupsMembershipsPost200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsMembershipsPost200Response.to_json())

# convert the object into a dict
groups_memberships_post200_response_dict = groups_memberships_post200_response_instance.to_dict()
# create an instance of GroupsMembershipsPost200Response from a dict
groups_memberships_post200_response_from_dict = GroupsMembershipsPost200Response.from_dict(groups_memberships_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


