# CollectionsMemberships200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**CollectionsAddUser200ResponseData**](CollectionsAddUser200ResponseData.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_memberships200_response import CollectionsMemberships200Response

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsMemberships200Response from a JSON string
collections_memberships200_response_instance = CollectionsMemberships200Response.from_json(json)
# print the JSON string representation of the object
print(CollectionsMemberships200Response.to_json())

# convert the object into a dict
collections_memberships200_response_dict = collections_memberships200_response_instance.to_dict()
# create an instance of CollectionsMemberships200Response from a dict
collections_memberships200_response_from_dict = CollectionsMemberships200Response.from_dict(collections_memberships200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


