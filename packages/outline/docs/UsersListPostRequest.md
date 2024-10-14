# UsersListPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**emails** | **List[str]** |  | [optional] 
**filter** | **str** | The status to filter by | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 

## Example

```python
from outline_openapi.models.users_list_post_request import UsersListPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersListPostRequest from a JSON string
users_list_post_request_instance = UsersListPostRequest.from_json(json)
# print the JSON string representation of the object
print(UsersListPostRequest.to_json())

# convert the object into a dict
users_list_post_request_dict = users_list_post_request_instance.to_dict()
# create an instance of UsersListPostRequest from a dict
users_list_post_request_from_dict = UsersListPostRequest.from_dict(users_list_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


