# CollectionsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**name** | **str** |  | [optional] 
**description** | **str** | A brief description of the collection, markdown supported. | [optional] 
**permission** | [**Permission**](Permission.md) |  | [optional] 
**icon** | **str** | A string that represents an icon in the outline-icons package or an emoji | [optional] 
**color** | **str** | A hex color code for the collection icon | [optional] 
**sharing** | **bool** | Whether public sharing of documents is allowed | [optional] 

## Example

```python
from outline_openapi.models.collections_update_request import CollectionsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsUpdateRequest from a JSON string
collections_update_request_instance = CollectionsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsUpdateRequest.to_json())

# convert the object into a dict
collections_update_request_dict = collections_update_request_instance.to_dict()
# create an instance of CollectionsUpdateRequest from a dict
collections_update_request_from_dict = CollectionsUpdateRequest.from_dict(collections_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


