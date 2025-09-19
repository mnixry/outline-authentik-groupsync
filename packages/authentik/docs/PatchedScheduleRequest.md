# PatchedScheduleRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rel_obj_id** | **str** |  | [optional] 
**crontab** | **str** | When to schedule tasks | [optional] 
**paused** | **bool** | Pause this schedule | [optional] 

## Example

```python
from authentik_openapi.models.patched_schedule_request import PatchedScheduleRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedScheduleRequest from a JSON string
patched_schedule_request_instance = PatchedScheduleRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedScheduleRequest.to_json())

# convert the object into a dict
patched_schedule_request_dict = patched_schedule_request_instance.to_dict()
# create an instance of PatchedScheduleRequest from a dict
patched_schedule_request_from_dict = PatchedScheduleRequest.from_dict(patched_schedule_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


