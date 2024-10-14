# EventsListPostRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**offset** | **float** |  | [optional] 
**limit** | **float** |  | [optional] 
**sort** | **str** |  | [optional] 
**direction** | **str** |  | [optional] 
**name** | **str** | Filter to a specific event, e.g. \&quot;collections.create\&quot;. Event names are in the format \&quot;objects.verb\&quot; | [optional] 
**actor_id** | **str** | Filter to events performed by the selected user | [optional] 
**document_id** | **str** | Filter to events performed in the selected document | [optional] 
**collection_id** | **str** | Filter to events performed in the selected collection | [optional] 
**audit_log** | **bool** | Whether to return detailed events suitable for an audit log. Without this flag less detailed event types will be returned. | [optional] 

## Example

```python
from outline_openapi.models.events_list_post_request import EventsListPostRequest

# TODO update the JSON string below
json = "{}"
# create an instance of EventsListPostRequest from a JSON string
events_list_post_request_instance = EventsListPostRequest.from_json(json)
# print the JSON string representation of the object
print(EventsListPostRequest.to_json())

# convert the object into a dict
events_list_post_request_dict = events_list_post_request_instance.to_dict()
# create an instance of EventsListPostRequest from a dict
events_list_post_request_from_dict = EventsListPostRequest.from_dict(events_list_post_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


