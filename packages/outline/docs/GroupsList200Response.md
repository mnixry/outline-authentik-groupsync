# GroupsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**GroupsList200ResponseData**](GroupsList200ResponseData.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.groups_list200_response import GroupsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of GroupsList200Response from a JSON string
groups_list200_response_instance = GroupsList200Response.from_json(json)
# print the JSON string representation of the object
print(GroupsList200Response.to_json())

# convert the object into a dict
groups_list200_response_dict = groups_list200_response_instance.to_dict()
# create an instance of GroupsList200Response from a dict
groups_list200_response_from_dict = GroupsList200Response.from_dict(groups_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


