# UsersInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the user. | 

## Example

```python
from outline_openapi.models.users_info_request import UsersInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersInfoRequest from a JSON string
users_info_request_instance = UsersInfoRequest.from_json(json)
# print the JSON string representation of the object
print(UsersInfoRequest.to_json())

# convert the object into a dict
users_info_request_dict = users_info_request_instance.to_dict()
# create an instance of UsersInfoRequest from a dict
users_info_request_from_dict = UsersInfoRequest.from_dict(users_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


