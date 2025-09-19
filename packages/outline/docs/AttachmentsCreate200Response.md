# AttachmentsCreate200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**AttachmentsCreate200ResponseData**](AttachmentsCreate200ResponseData.md) |  | [optional] 

## Example

```python
from outline_openapi.models.attachments_create200_response import AttachmentsCreate200Response

# TODO update the JSON string below
json = "{}"
# create an instance of AttachmentsCreate200Response from a JSON string
attachments_create200_response_instance = AttachmentsCreate200Response.from_json(json)
# print the JSON string representation of the object
print(AttachmentsCreate200Response.to_json())

# convert the object into a dict
attachments_create200_response_dict = attachments_create200_response_instance.to_dict()
# create an instance of AttachmentsCreate200Response from a dict
attachments_create200_response_from_dict = AttachmentsCreate200Response.from_dict(attachments_create200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


