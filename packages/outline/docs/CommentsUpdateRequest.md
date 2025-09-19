# CommentsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**data** | **object** |  | 

## Example

```python
from outline_openapi.models.comments_update_request import CommentsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsUpdateRequest from a JSON string
comments_update_request_instance = CommentsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsUpdateRequest.to_json())

# convert the object into a dict
comments_update_request_dict = comments_update_request_instance.to_dict()
# create an instance of CommentsUpdateRequest from a dict
comments_update_request_from_dict = CommentsUpdateRequest.from_dict(comments_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


