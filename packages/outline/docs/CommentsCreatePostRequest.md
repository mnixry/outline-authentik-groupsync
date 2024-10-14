# CommentsCreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**document_id** | **str** |  | 
**parent_comment_id** | **str** |  | [optional] 
**data** | **object** |  | 

## Example

```python
from outline_openapi.models.comments_create_post_request import CommentsCreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsCreatePostRequest from a JSON string
comments_create_post_request_instance = CommentsCreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsCreatePostRequest.to_json())

# convert the object into a dict
comments_create_post_request_dict = comments_create_post_request_instance.to_dict()
# create an instance of CommentsCreatePostRequest from a dict
comments_create_post_request_from_dict = CommentsCreatePostRequest.from_dict(comments_create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


