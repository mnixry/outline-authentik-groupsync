# CommentsCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Comment**](Comment.md) |  | [optional] 

## Example

```python
from outline_openapi.models.comments_create200_response import CommentsCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsCreate200Response from a JSON string
comments_create200_response_instance = CommentsCreate200Response.from_json(json)
# print the JSON string representation of the object
print(CommentsCreate200Response.to_json())

# convert the object into a dict
comments_create200_response_dict = comments_create200_response_instance.to_dict()
# create an instance of CommentsCreate200Response from a dict
comments_create200_response_from_dict = CommentsCreate200Response.from_dict(comments_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


