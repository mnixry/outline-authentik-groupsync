# UsersListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**query** | **str** |  | [optional] 
**emails** | **List[str]** | Array of emails | [optional] 
**filter** | **str** | The status to filter by | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 

## Example

```python
from outline_openapi.models.users_list_request import UsersListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UsersListRequest from a JSON string
users_list_request_instance = UsersListRequest.from_json(json)
# print the JSON string representation of the object
print(UsersListRequest.to_json())

# convert the object into a dict
users_list_request_dict = users_list_request_instance.to_dict()
# create an instance of UsersListRequest from a dict
users_list_request_from_dict = UsersListRequest.from_dict(users_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


