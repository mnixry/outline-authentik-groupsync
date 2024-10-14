# CollectionsCreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**description** | **str** |  | [optional] 
**permission** | [**Permission**](Permission.md) |  | [optional] 
**color** | **str** |  | [optional] 
**private** | **bool** |  | [optional] 

## Example

```python
from outline_openapi.models.collections_create_post_request import CollectionsCreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsCreatePostRequest from a JSON string
collections_create_post_request_instance = CollectionsCreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsCreatePostRequest.to_json())

# convert the object into a dict
collections_create_post_request_dict = collections_create_post_request_instance.to_dict()
# create an instance of CollectionsCreatePostRequest from a dict
collections_create_post_request_from_dict = CollectionsCreatePostRequest.from_dict(collections_create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


