# GroupsUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | 

## Example

```python
from outline_openapi.models.groups_update_post_request import GroupsUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsUpdatePostRequest from a JSON string
groups_update_post_request_instance = GroupsUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsUpdatePostRequest.to_json())

# convert the object into a dict
groups_update_post_request_dict = groups_update_post_request_instance.to_dict()
# create an instance of GroupsUpdatePostRequest from a dict
groups_update_post_request_from_dict = GroupsUpdatePostRequest.from_dict(groups_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


