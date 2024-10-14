# PolicyAbilities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**create** | **bool** |  | [optional] 
**read** | **bool** |  | [optional] 
**update** | **bool** |  | [optional] 
**delete** | **bool** |  | [optional] 
**restore** | **bool** |  | [optional] 
**star** | **bool** |  | [optional] 
**unstar** | **bool** |  | [optional] 
**share** | **bool** |  | [optional] 
**download** | **bool** |  | [optional] 
**pin** | **bool** |  | [optional] 
**unpin** | **bool** |  | [optional] 
**move** | **bool** |  | [optional] 
**archive** | **bool** |  | [optional] 
**unarchive** | **bool** |  | [optional] 
**create_child_document** | **bool** |  | [optional] 

## Example

```python
from outline_openapi.models.policy_abilities import PolicyAbilities

# TODO update the JSON string below
json = "{}"
# create an instance of PolicyAbilities from a JSON string
policy_abilities_instance = PolicyAbilities.from_json(json)
# print the JSON string representation of the object
print(PolicyAbilities.to_json())

# convert the object into a dict
policy_abilities_dict = policy_abilities_instance.to_dict()
# create an instance of PolicyAbilities from a dict
policy_abilities_from_dict = PolicyAbilities.from_dict(policy_abilities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


