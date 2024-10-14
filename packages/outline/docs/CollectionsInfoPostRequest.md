# CollectionsInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the collection. | 

## Example

```python
from outline_openapi.models.collections_info_post_request import CollectionsInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsInfoPostRequest from a JSON string
collections_info_post_request_instance = CollectionsInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsInfoPostRequest.to_json())

# convert the object into a dict
collections_info_post_request_dict = collections_info_post_request_instance.to_dict()
# create an instance of CollectionsInfoPostRequest from a dict
collections_info_post_request_from_dict = CollectionsInfoPostRequest.from_dict(collections_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


