# AttachmentsRedirectPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the attachment. | 

## Example

```python
from outline_openapi.models.attachments_redirect_post_request import AttachmentsRedirectPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsRedirectPostRequest from a JSON string
attachments_redirect_post_request_instance = AttachmentsRedirectPostRequest.from_json(json)
# print the JSON string representation of the object
print(AttachmentsRedirectPostRequest.to_json())

# convert the object into a dict
attachments_redirect_post_request_dict = attachments_redirect_post_request_instance.to_dict()
# create an instance of AttachmentsRedirectPostRequest from a dict
attachments_redirect_post_request_from_dict = AttachmentsRedirectPostRequest.from_dict(attachments_redirect_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


