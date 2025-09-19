# CollectionsGroupMembershipsRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**id** | **str** | Identifier for the collection | 
**query** | **str** | Filter memberships by group names | [optional] 
**permission** | [**Permission**](Permission.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_group_memberships_request import CollectionsGroupMembershipsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsGroupMembershipsRequest from a JSON string
collections_group_memberships_request_instance = CollectionsGroupMembershipsRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsGroupMembershipsRequest.to_json())

# convert the object into a dict
collections_group_memberships_request_dict = collections_group_memberships_request_instance.to_dict()
# create an instance of CollectionsGroupMembershipsRequest from a dict
collections_group_memberships_request_from_dict = CollectionsGroupMembershipsRequest.from_dict(collections_group_memberships_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


