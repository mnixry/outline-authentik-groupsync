# CollectionsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**query** | **str** | If set, will filter the results by collection name. | [optional] 
**status_filter** | [**List[CollectionStatus]**](CollectionStatus.md) | An optional array of statuses to filter by. | [optional] 

## Example

```python
from outline_openapi.models.collections_list_request import CollectionsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsListRequest from a JSON string
collections_list_request_instance = CollectionsListRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsListRequest.to_json())

# convert the object into a dict
collections_list_request_dict = collections_list_request_instance.to_dict()
# create an instance of CollectionsListRequest from a dict
collections_list_request_from_dict = CollectionsListRequest.from_dict(collections_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


