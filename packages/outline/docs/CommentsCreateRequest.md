# CommentsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**document_id** | **str** |  | 
**parent_comment_id** | **str** |  | [optional] 
**data** | **object** | The body of the comment. | [optional] 
**text** | **str** | The body of the comment in markdown. | [optional] 

## Example

```python
from outline_openapi.models.comments_create_request import CommentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsCreateRequest from a JSON string
comments_create_request_instance = CommentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsCreateRequest.to_json())

# convert the object into a dict
comments_create_request_dict = comments_create_request_instance.to_dict()
# create an instance of CommentsCreateRequest from a dict
comments_create_request_from_dict = CommentsCreateRequest.from_dict(comments_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


