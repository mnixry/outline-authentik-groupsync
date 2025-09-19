# PaginatedTaskList


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pagination** | [**Pagination**](Pagination.md) |  | 
**results** | [**List[Task]**](Task.md) |  | 
**autocomplete** | **Dict[str, object]** |  | 

## Example

```python
from authentik_openapi.models.paginated_task_list import PaginatedTaskList

# TODO update the JSON string below
json = "{}"
# create an instance of PaginatedTaskList from a JSON string
paginated_task_list_instance = PaginatedTaskList.from_json(json)
# print the JSON string representation of the object
print(PaginatedTaskList.to_json())

# convert the object into a dict
paginated_task_list_dict = paginated_task_list_instance.to_dict()
# create an instance of PaginatedTaskList from a dict
paginated_task_list_from_dict = PaginatedTaskList.from_dict(paginated_task_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


