# SharesInfoPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the share. | [optional] 
**document_id** | **str** | Unique identifier for a document. One of id or documentId must be provided. | [optional] 

## Example

```python
from outline_openapi.models.shares_info_post_request import SharesInfoPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharesInfoPostRequest from a JSON string
shares_info_post_request_instance = SharesInfoPostRequest.from_json(json)
# print the JSON string representation of the object
print(SharesInfoPostRequest.to_json())

# convert the object into a dict
shares_info_post_request_dict = shares_info_post_request_instance.to_dict()
# create an instance of SharesInfoPostRequest from a dict
shares_info_post_request_from_dict = SharesInfoPostRequest.from_dict(shares_info_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


