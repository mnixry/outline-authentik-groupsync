# CommentsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Comment]**](Comment.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.comments_list200_response import CommentsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsList200Response from a JSON string
comments_list200_response_instance = CommentsList200Response.from_json(json)
# print the JSON string representation of the object
print(CommentsList200Response.to_json())

# convert the object into a dict
comments_list200_response_dict = comments_list200_response_instance.to_dict()
# create an instance of CommentsList200Response from a dict
comments_list200_response_from_dict = CommentsList200Response.from_dict(comments_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


