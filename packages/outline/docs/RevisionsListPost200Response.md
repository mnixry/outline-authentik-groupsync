# RevisionsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Revision]**](Revision.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.revisions_list_post200_response import RevisionsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of RevisionsListPost200Response from a JSON string
revisions_list_post200_response_instance = RevisionsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(RevisionsListPost200Response.to_json())

# convert the object into a dict
revisions_list_post200_response_dict = revisions_list_post200_response_instance.to_dict()
# create an instance of RevisionsListPost200Response from a dict
revisions_list_post200_response_from_dict = RevisionsListPost200Response.from_dict(revisions_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


