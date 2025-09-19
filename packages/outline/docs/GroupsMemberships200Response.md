# GroupsMemberships200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupsMemberships200ResponseData**](GroupsMemberships200ResponseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_memberships200_response import GroupsMemberships200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsMemberships200Response from a JSON string
groups_memberships200_response_instance = GroupsMemberships200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsMemberships200Response.to_json())

# convert the object into a dict
groups_memberships200_response_dict = groups_memberships200_response_instance.to_dict()
# create an instance of GroupsMemberships200Response from a dict
groups_memberships200_response_from_dict = GroupsMemberships200Response.from_dict(groups_memberships200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


