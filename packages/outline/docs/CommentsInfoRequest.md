# CommentsInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**include_anchor_text** | **bool** | Include the document text that the comment is anchored to, if any, in the response. | [optional] 

## Example

```python
from outline_openapi.models.comments_info_request import CommentsInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsInfoRequest from a JSON string
comments_info_request_instance = CommentsInfoRequest.from_json(json)
# print the JSON string representation of the object
print(CommentsInfoRequest.to_json())

# convert the object into a dict
comments_info_request_dict = comments_info_request_instance.to_dict()
# create an instance of CommentsInfoRequest from a dict
comments_info_request_from_dict = CommentsInfoRequest.from_dict(comments_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


