# CommentsListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**document_id** | **str** | Filter to a specific document | [optional] 
**collection_id** | **str** | Filter to a specific collection | [optional] 
**include_anchor_text** | **bool** | Include the document text that the comment is anchored to, if any, in the response. | [optional] 

## Example

```python
from outline_openapi.models.comments_list_request import CommentsListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsListRequest from a JSON string
comments_list_request_instance = CommentsListRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsListRequest.to_json())

# convert the object into a dict
comments_list_request_dict = comments_list_request_instance.to_dict()
# create an instance of CommentsListRequest from a dict
comments_list_request_from_dict = CommentsListRequest.from_dict(comments_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


