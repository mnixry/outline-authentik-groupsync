# SharesUpdatePostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**published** | **bool** |  | 

## Example

```python
from outline_openapi.models.shares_update_post_request import SharesUpdatePostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharesUpdatePostRequest from a JSON string
shares_update_post_request_instance = SharesUpdatePostRequest.from_json(json)
# print the JSON string representation of the object
print(SharesUpdatePostRequest.to_json())

# convert the object into a dict
shares_update_post_request_dict = shares_update_post_request_instance.to_dict()
# create an instance of SharesUpdatePostRequest from a dict
shares_update_post_request_from_dict = SharesUpdatePostRequest.from_dict(shares_update_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


