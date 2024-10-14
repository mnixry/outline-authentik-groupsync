# UsersInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the user. | 

## Example

```python
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInfoPostRequest from a JSON string
users_info_post_request_instance = UsersInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(UsersInfoPostRequest.to_json())

# convert the object into a dict
users_info_post_request_dict = users_info_post_request_instance.to_dict()
# create an instance of UsersInfoPostRequest from a dict
users_info_post_request_from_dict = UsersInfoPostRequest.from_dict(users_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


