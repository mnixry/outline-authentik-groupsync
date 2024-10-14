# CollectionsCreatePost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Collection**](Collection.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_create_post200_response import CollectionsCreatePost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsCreatePost200Response from a JSON string
collections_create_post200_response_instance = CollectionsCreatePost200Response.from_json(json)
# print the JSON string representation of the object
print(CollectionsCreatePost200Response.to_json())

# convert the object into a dict
collections_create_post200_response_dict = collections_create_post200_response_instance.to_dict()
# create an instance of CollectionsCreatePost200Response from a dict
collections_create_post200_response_from_dict = CollectionsCreatePost200Response.from_dict(collections_create_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


