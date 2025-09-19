# CommentsInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Comment**](Comment.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.comments_info200_response import CommentsInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CommentsInfo200Response from a JSON string
comments_info200_response_instance = CommentsInfo200Response.from_json(json)
# print the JSON string representation of the object
print(CommentsInfo200Response.to_json())

# convert the object into a dict
comments_info200_response_dict = comments_info200_response_instance.to_dict()
# create an instance of CommentsInfo200Response from a dict
comments_info200_response_from_dict = CommentsInfo200Response.from_dict(comments_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


