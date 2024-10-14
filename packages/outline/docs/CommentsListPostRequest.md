# CommentsListPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**document_id** | **str** | Filter to a specific document | [optional] 
**collection_id** | **str** | Filter to a specific collection | [optional] 

## Example

```python
from outline_openapi.models.comments_list_post_request import CommentsListPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsListPostRequest from a JSON string
comments_list_post_request_instance = CommentsListPostRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsListPostRequest.to_json())

# convert the object into a dict
comments_list_post_request_dict = comments_list_post_request_instance.to_dict()
# create an instance of CommentsListPostRequest from a dict
comments_list_post_request_from_dict = CommentsListPostRequest.from_dict(comments_list_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


