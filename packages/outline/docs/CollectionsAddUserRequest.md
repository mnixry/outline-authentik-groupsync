# CollectionsAddUserRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**permission** | [**Permission**](Permission.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_add_user_request import CollectionsAddUserRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsAddUserRequest from a JSON string
collections_add_user_request_instance = CollectionsAddUserRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsAddUserRequest.to_json())

# convert the object into a dict
collections_add_user_request_dict = collections_add_user_request_instance.to_dict()
# create an instance of CollectionsAddUserRequest from a dict
collections_add_user_request_from_dict = CollectionsAddUserRequest.from_dict(collections_add_user_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


