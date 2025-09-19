# PaginatedTenantList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Tenant]**](Tenant.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.paginated_tenant_list import PaginatedTenantList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTenantList from a JSON string
paginated_tenant_list_instance = PaginatedTenantList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTenantList.to_json())

# convert the object into a dict
paginated_tenant_list_dict = paginated_tenant_list_instance.to_dict()
# create an instance of PaginatedTenantList from a dict
paginated_tenant_list_from_dict = PaginatedTenantList.from_dict(paginated_tenant_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


