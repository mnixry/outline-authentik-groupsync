# RevisionsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**document_id** | **str** | The document ID to retrieve revisions for | [optional] 

## Example

```python
from outline_openapi.models.revisions_list_request import RevisionsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionsListRequest from a JSON string
revisions_list_request_instance = RevisionsListRequest.from_json(json)
# print the JSON string representation of the object
print(RevisionsListRequest.to_json())

# convert the object into a dict
revisions_list_request_dict = revisions_list_request_instance.to_dict()
# create an instance of RevisionsListRequest from a dict
revisions_list_request_from_dict = RevisionsListRequest.from_dict(revisions_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


