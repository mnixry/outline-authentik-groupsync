# SharesListRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**query** | **str** | Filter to shared documents matching a search query | [optional] 

## Example

```python
from outline_openapi.models.shares_list_request import SharesListRequest

# TODO update the JSON string below
json = "{}"
# create an instance of SharesListRequest from a JSON string
shares_list_request_instance = SharesListRequest.from_json(json)
# print the JSON string representation of the object
print(SharesListRequest.to_json())

# convert the object into a dict
shares_list_request_dict = shares_list_request_instance.to_dict()
# create an instance of SharesListRequest from a dict
shares_list_request_from_dict = SharesListRequest.from_dict(shares_list_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


