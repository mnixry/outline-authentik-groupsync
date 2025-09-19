# CollectionsExportRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**format** | **str** |  | [optional] 
**id** | **str** |  | 

## Example

```python
from outline_openapi.models.collections_export_request import CollectionsExportRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsExportRequest from a JSON string
collections_export_request_instance = CollectionsExportRequest.from_json(json)
# print the JSON string representation of the object
print(CollectionsExportRequest.to_json())

# convert the object into a dict
collections_export_request_dict = collections_export_request_instance.to_dict()
# create an instance of CollectionsExportRequest from a dict
collections_export_request_from_dict = CollectionsExportRequest.from_dict(collections_export_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


