# ViewsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**document_id** | **str** | The document ID to retrieve views for | 

## Example

```python
from outline_openapi.models.views_list_request import ViewsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of ViewsListRequest from a JSON string
views_list_request_instance = ViewsListRequest.from_json(json)
# print the JSON string representation of the object
print(ViewsListRequest.to_json())

# convert the object into a dict
views_list_request_dict = views_list_request_instance.to_dict()
# create an instance of ViewsListRequest from a dict
views_list_request_from_dict = ViewsListRequest.from_dict(views_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


