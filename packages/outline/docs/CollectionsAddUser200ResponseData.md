# CollectionsAddUser200ResponseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**users** | [**List[User]**](User.md) |  | [optional] 
**memberships** | [**List[Membership]**](Membership.md) |  | [optional] 

## Example

```python
from outline_openapi.models.collections_add_user200_response_data import CollectionsAddUser200ResponseData

# TODO update the JSON string below
json = "{}"
# create an instance of CollectionsAddUser200ResponseData from a JSON string
collections_add_user200_response_data_instance = CollectionsAddUser200ResponseData.from_json(json)
# print the JSON string representation of the object
print(CollectionsAddUser200ResponseData.to_json())

# convert the object into a dict
collections_add_user200_response_data_dict = collections_add_user200_response_data_instance.to_dict()
# create an instance of CollectionsAddUser200ResponseData from a dict
collections_add_user200_response_data_from_dict = CollectionsAddUser200ResponseData.from_dict(collections_add_user200_response_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


