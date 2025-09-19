# CollectionsInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**Collection**](Collection.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_info200_response import CollectionsInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsInfo200Response from a JSON string
collections_info200_response_instance = CollectionsInfo200Response.from_json(json)
# print the JSON string representation of the object
print(CollectionsInfo200Response.to_json())

# convert the object into a dict
collections_info200_response_dict = collections_info200_response_instance.to_dict()
# create an instance of CollectionsInfo200Response from a dict
collections_info200_response_from_dict = CollectionsInfo200Response.from_dict(collections_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


