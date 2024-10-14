# AttachmentsCreatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**document_id** | **str** | Identifier for the associated document, if any. | [optional] 
**content_type** | **str** |  | 
**size** | **float** | Size of the file attachment in bytes. | 

## Example

```python
from outline_openapi.models.attachments_create_post_request import AttachmentsCreatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsCreatePostRequest from a JSON string
attachments_create_post_request_instance = AttachmentsCreatePostRequest.from_json(json)
# print the JSON string representation of the object
print(AttachmentsCreatePostRequest.to_json())

# convert the object into a dict
attachments_create_post_request_dict = attachments_create_post_request_instance.to_dict()
# create an instance of AttachmentsCreatePostRequest from a dict
attachments_create_post_request_from_dict = AttachmentsCreatePostRequest.from_dict(attachments_create_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


