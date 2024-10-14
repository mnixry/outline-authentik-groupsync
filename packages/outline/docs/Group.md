# Group


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**name** | **str** | The name of this group. | [optional] 
**member_count** | **float** | The number of users that are members of the group | [optional] [readonly] 
**created_at** | **datetime** | The date and time that this object was created | [optional] [readonly] 
**updated_at** | **datetime** | The date and time that this object was last changed | [optional] [readonly] 

## Example

```python
from outline_openapi.models.group import Group

# TODO update the JSON string below
json = "{}"
# create an instance of Group from a JSON string
group_instance = Group.from_json(json)
# print the JSON string representation of the object
print(Group.to_json())

# convert the object into a dict
group_dict = group_instance.to_dict()
# create an instance of Group from a dict
group_from_dict = Group.from_dict(group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


