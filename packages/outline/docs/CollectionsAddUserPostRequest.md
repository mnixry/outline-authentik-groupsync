# CollectionsAddUserPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**user_id** | **str** |  | 
**permission** | [**Permission**](Permission.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_add_user_post_request import CollectionsAddUserPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsAddUserPostRequest from a JSON string
collections_add_user_post_request_instance = CollectionsAddUserPostRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsAddUserPostRequest.to_json())

# convert the object into a dict
collections_add_user_post_request_dict = collections_add_user_post_request_instance.to_dict()
# create an instance of CollectionsAddUserPostRequest from a dict
collections_add_user_post_request_from_dict = CollectionsAddUserPostRequest.from_dict(collections_add_user_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


