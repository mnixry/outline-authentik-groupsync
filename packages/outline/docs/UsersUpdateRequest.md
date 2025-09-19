# UsersUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**language** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.users_update_request import UsersUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersUpdateRequest from a JSON string
users_update_request_instance = UsersUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(UsersUpdateRequest.to_json())

# convert the object into a dict
users_update_request_dict = users_update_request_instance.to_dict()
# create an instance of UsersUpdateRequest from a dict
users_update_request_from_dict = UsersUpdateRequest.from_dict(users_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


