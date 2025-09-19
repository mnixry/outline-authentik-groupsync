# PatchedGroupLDAPSourceConnectionRequest

Group Source Connection

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**group** | **str** |  | [optional] 
**source** | **str** |  | [optional] 
**identifier** | **str** |  | [optional] 

## Example

```python
from authentik_openapi.models.patched_group_ldap_source_connection_request import PatchedGroupLDAPSourceConnectionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedGroupLDAPSourceConnectionRequest from a JSON string
patched_group_ldap_source_connection_request_instance = PatchedGroupLDAPSourceConnectionRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedGroupLDAPSourceConnectionRequest.to_json())

# convert the object into a dict
patched_group_ldap_source_connection_request_dict = patched_group_ldap_source_connection_request_instance.to_dict()
# create an instance of PatchedGroupLDAPSourceConnectionRequest from a dict
patched_group_ldap_source_connection_request_from_dict = PatchedGroupLDAPSourceConnectionRequest.from_dict(patched_group_ldap_source_connection_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


