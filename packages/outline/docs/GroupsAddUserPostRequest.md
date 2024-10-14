# GroupsAddUserPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 

## Example

```python
from outline_openapi.models.groups_add_user_post_request import GroupsAddUserPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsAddUserPostRequest from a JSON string
groups_add_user_post_request_instance = GroupsAddUserPostRequest.from_json(json)
# print the JSON string representation of the object
print(GroupsAddUserPostRequest.to_json())

# convert the object into a dict
groups_add_user_post_request_dict = groups_add_user_post_request_instance.to_dict()
# create an instance of GroupsAddUserPostRequest from a dict
groups_add_user_post_request_from_dict = GroupsAddUserPostRequest.from_dict(groups_add_user_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


