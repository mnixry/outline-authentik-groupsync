# Event


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**name** | **str** |  | [optional] [readonly] 
**model_id** | **str** | Identifier for the object this event is associated with when it is not one of document, collection, or user. | [optional] [readonly] 
**actor_id** | **str** | The user that performed the action. | [optional] [readonly] 
**actor_ip_address** | **str** | The ip address the action was performed from. This field is only returned when the &#x60;auditLog&#x60; boolean is true. | [optional] [readonly] 
**collection_id** | **str** | Identifier for the associated collection, if any | [optional] [readonly] 
**document_id** | **str** | Identifier for the associated document, if any | [optional] [readonly] 
**created_at** | **datetime** | The date and time that this event was created | [optional] [readonly] 
**data** | **object** | Additional unstructured data associated with the event | [optional] [readonly] 
**actor** | [**User**](User.md) |  | [optional] 

## Example

```python
from outline_openapi.models.event import Event

# TODO update the JSON string below
json = "{}"
# create an instance of Event from a JSON string
event_instance = Event.from_json(json)
# print the JSON string representation of the object
print(Event.to_json())

# convert the object into a dict
event_dict = event_instance.to_dict()
# create an instance of Event from a dict
event_from_dict = Event.from_dict(event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


