# EventsList200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Event]**](Event.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.events_list200_response import EventsList200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EventsList200Response from a JSON string
events_list200_response_instance = EventsList200Response.from_json(json)
# print the JSON string representation of the object
print(EventsList200Response.to_json())

# convert the object into a dict
events_list200_response_dict = events_list200_response_instance.to_dict()
# create an instance of EventsList200Response from a dict
events_list200_response_from_dict = EventsList200Response.from_dict(events_list200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


