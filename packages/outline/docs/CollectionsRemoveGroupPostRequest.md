# CollectionsRemoveGroupPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Identifier for the collection | 
**group_id** | **str** |  | 

## Example

```python
from outline_openapi.models.collections_remove_group_post_request import CollectionsRemoveGroupPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsRemoveGroupPostRequest from a JSON string
collections_remove_group_post_request_instance = CollectionsRemoveGroupPostRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsRemoveGroupPostRequest.to_json())

# convert the object into a dict
collections_remove_group_post_request_dict = collections_remove_group_post_request_instance.to_dict()
# create an instance of CollectionsRemoveGroupPostRequest from a dict
collections_remove_group_post_request_from_dict = CollectionsRemoveGroupPostRequest.from_dict(collections_remove_group_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


