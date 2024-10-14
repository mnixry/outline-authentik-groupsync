# SharesListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Share]**](Share.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.shares_list_post200_response import SharesListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SharesListPost200Response from a JSON string
shares_list_post200_response_instance = SharesListPost200Response.from_json(json)
# print the JSON string representation of the object
print(SharesListPost200Response.to_json())

# convert the object into a dict
shares_list_post200_response_dict = shares_list_post200_response_instance.to_dict()
# create an instance of SharesListPost200Response from a dict
shares_list_post200_response_from_dict = SharesListPost200Response.from_dict(shares_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


