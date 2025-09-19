# SharesList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Share]**](Share.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.shares_list200_response import SharesList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SharesList200Response from a JSON string
shares_list200_response_instance = SharesList200Response.from_json(json)
# print the JSON string representation of the object
print(SharesList200Response.to_json())

# convert the object into a dict
shares_list200_response_dict = shares_list200_response_instance.to_dict()
# create an instance of SharesList200Response from a dict
shares_list200_response_from_dict = SharesList200Response.from_dict(shares_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


