# RevisionsInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the revision. | 

## Example

```python
from outline_openapi.models.revisions_info_request import RevisionsInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionsInfoRequest from a JSON string
revisions_info_request_instance = RevisionsInfoRequest.from_json(json)
# print the JSON string representation of the object
print(RevisionsInfoRequest.to_json())

# convert the object into a dict
revisions_info_request_dict = revisions_info_request_instance.to_dict()
# create an instance of RevisionsInfoRequest from a dict
revisions_info_request_from_dict = RevisionsInfoRequest.from_dict(revisions_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


