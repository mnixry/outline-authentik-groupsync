# EventsListPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**List[Event]**](Event.md) |  | [optional] 
**pagination** | [**Pagination**](Pagination.md) |  | [optional] 

## Example

```python
from outline_openapi.models.events_list_post200_response import EventsListPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of EventsListPost200Response from a JSON string
events_list_post200_response_instance = EventsListPost200Response.from_json(json)
# print the JSON string representation of the object
print(EventsListPost200Response.to_json())

# convert the object into a dict
events_list_post200_response_dict = events_list_post200_response_instance.to_dict()
# create an instance of EventsListPost200Response from a dict
events_list_post200_response_from_dict = EventsListPost200Response.from_dict(events_list_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


