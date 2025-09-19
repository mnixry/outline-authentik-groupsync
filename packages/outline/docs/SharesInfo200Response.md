# SharesInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Share**](Share.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.shares_info200_response import SharesInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of SharesInfo200Response from a JSON string
shares_info200_response_instance = SharesInfo200Response.from_json(json)
# print the JSON string representation of the object
print(SharesInfo200Response.to_json())

# convert the object into a dict
shares_info200_response_dict = shares_info200_response_instance.to_dict()
# create an instance of SharesInfo200Response from a dict
shares_info200_response_from_dict = SharesInfo200Response.from_dict(shares_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


