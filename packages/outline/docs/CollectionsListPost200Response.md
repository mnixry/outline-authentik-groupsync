# CollectionsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Collection]**](Collection.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_list_post200_response import CollectionsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsListPost200Response from a JSON string
collections_list_post200_response_instance = CollectionsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(CollectionsListPost200Response.to_json())

# convert the object into a dict
collections_list_post200_response_dict = collections_list_post200_response_instance.to_dict()
# create an instance of CollectionsListPost200Response from a dict
collections_list_post200_response_from_dict = CollectionsListPost200Response.from_dict(collections_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


