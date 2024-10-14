# CollectionsUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**permission** | [**Permission**](Permission.md) |  | [optional] 
**description** | **str** |  | [optional] 
**color** | **str** |  | [optional] 

## Example

```python
from outline_openapi.models.collections_update_post_request import CollectionsUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsUpdatePostRequest from a JSON string
collections_update_post_request_instance = CollectionsUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsUpdatePostRequest.to_json())

# convert the object into a dict
collections_update_post_request_dict = collections_update_post_request_instance.to_dict()
# create an instance of CollectionsUpdatePostRequest from a dict
collections_update_post_request_from_dict = CollectionsUpdatePostRequest.from_dict(collections_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


