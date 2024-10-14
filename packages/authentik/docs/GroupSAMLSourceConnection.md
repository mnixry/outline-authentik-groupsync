# GroupSAMLSourceConnection

OAuth Group-Source connection Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **int** |  | [readonly] 
**group** | **str** |  | [readonly] 
**source** | [**Source**](Source.md) |  | [readonly] 
**identifier** | **str** |  | [readonly] 
**created** | **datetime** |  | [readonly] 

## Example

```python
from authentik_openapi.models.group_saml_source_connection import GroupSAMLSourceConnection

# TODO update the JSON string below
json = "{}"
# create an instance of GroupSAMLSourceConnection from a JSON string
group_saml_source_connection_instance = GroupSAMLSourceConnection.from_json(json)
# print the JSON string representation of the object
print(GroupSAMLSourceConnection.to_json())

# convert the object into a dict
group_saml_source_connection_dict = group_saml_source_connection_instance.to_dict()
# create an instance of GroupSAMLSourceConnection from a dict
group_saml_source_connection_from_dict = GroupSAMLSourceConnection.from_dict(group_saml_source_connection_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


