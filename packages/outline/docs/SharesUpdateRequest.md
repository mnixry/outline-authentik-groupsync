# SharesUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | 
**published** | **bool** |  | 

## Example

```python
from outline_openapi.models.shares_update_request import SharesUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharesUpdateRequest from a JSON string
shares_update_request_instance = SharesUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(SharesUpdateRequest.to_json())

# convert the object into a dict
shares_update_request_dict = shares_update_request_instance.to_dict()
# create an instance of SharesUpdateRequest from a dict
shares_update_request_from_dict = SharesUpdateRequest.from_dict(shares_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


