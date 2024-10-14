# Invite


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The full name of the user being invited | [optional] 
**email** | **str** | The email address to invite | [optional] 
**role** | [**UserRole**](UserRole.md) |  | [optional] 

## Example

```python
from outline_openapi.models.invite import Invite

# TODO update the JSON string below
json = "{}"
# create an instance of Invite from a JSON string
invite_instance = Invite.from_json(json)
# print the JSON string representation of the object
print(Invite.to_json())

# convert the object into a dict
invite_dict = invite_instance.to_dict()
# create an instance of Invite from a dict
invite_from_dict = Invite.from_dict(invite_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


