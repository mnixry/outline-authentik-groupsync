# PaginatedGroupKerberosSourceConnectionList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[GroupKerberosSourceConnection]**](GroupKerberosSourceConnection.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.paginated_group_kerberos_source_connection_list import PaginatedGroupKerberosSourceConnectionList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedGroupKerberosSourceConnectionList from a JSON string
paginated_group_kerberos_source_connection_list_instance = PaginatedGroupKerberosSourceConnectionList.from_json(json)
# print the JSON string representation of the object
print(PaginatedGroupKerberosSourceConnectionList.to_json())

# convert the object into a dict
paginated_group_kerberos_source_connection_list_dict = paginated_group_kerberos_source_connection_list_instance.to_dict()
# create an instance of PaginatedGroupKerberosSourceConnectionList from a dict
paginated_group_kerberos_source_connection_list_from_dict = PaginatedGroupKerberosSourceConnectionList.from_dict(paginated_group_kerberos_source_connection_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


