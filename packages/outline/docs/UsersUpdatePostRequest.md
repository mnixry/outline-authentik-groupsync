# UsersUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.users_update_post_request import UsersUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdatePostRequest from a JSON string
users_update_post_request_instance = UsersUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(UsersUpdatePostRequest.to_json())

# convert the object into a dict
users_update_post_request_dict = users_update_post_request_instance.to_dict()
# create an instance of UsersUpdatePostRequest from a dict
users_update_post_request_from_dict = UsersUpdatePostRequest.from_dict(users_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


