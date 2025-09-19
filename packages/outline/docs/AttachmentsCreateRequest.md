# AttachmentsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**document_id** | **str** | Identifier for the associated document, if any. | [optional] 
**content_type** | **str** |  | 
**size** | **float** | Size of the file attachment in bytes. | 

## Example

```python
from outline_openapi.models.attachments_create_request import AttachmentsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsCreateRequest from a JSON string
attachments_create_request_instance = AttachmentsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(AttachmentsCreateRequest.to_json())

# convert the object into a dict
attachments_create_request_dict = attachments_create_request_instance.to_dict()
# create an instance of AttachmentsCreateRequest from a dict
attachments_create_request_from_dict = AttachmentsCreateRequest.from_dict(attachments_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


