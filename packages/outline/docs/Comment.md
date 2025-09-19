# Comment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**data** | **object** | The editor data representing this comment. | [optional] 
**document_id** | **str** | Identifier for the document this is related to. | [optional] 
**parent_comment_id** | **str** | Identifier for the comment this is a child of, if any. | [optional] 
**created_at** | **datetime** | The date and time that this object was created | [optional] [readonly] 
**created_by** | [**User**](User.md) |  | [optional] 
**updated_at** | **datetime** | The date and time that this object was last changed | [optional] [readonly] 
**updated_by** | [**User**](User.md) |  | [optional] 
**anchor_text** | **str** | The document text that the comment is anchored to, only included if includeAnchorText&#x3D;true. | [optional] [readonly] 

## Example

```python
from outline_openapi.models.comment import Comment

# TODO update the JSON string below
json = "{}"
# create an instance of Comment from a JSON string
comment_instance = Comment.from_json(json)
# print the JSON string representation of the object
print(Comment.to_json())

# convert the object into a dict
comment_dict = comment_instance.to_dict()
# create an instance of Comment from a dict
comment_from_dict = Comment.from_dict(comment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


