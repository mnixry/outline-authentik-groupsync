# Auth


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**user** | [**User**](User.md) |  | [optional] 
**team** | [**Team**](Team.md) |  | [optional] 

## Example

```python
from outline_openapi.models.auth import Auth

# TODO update the JSON string below
json = "{}"
# create an instance of Auth from a JSON string
auth_instance = Auth.from_json(json)
# print the JSON string representation of the object
print(Auth.to_json())

# convert the object into a dict
auth_dict = auth_instance.to_dict()
# create an instance of Auth from a dict
auth_from_dict = Auth.from_dict(auth_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


