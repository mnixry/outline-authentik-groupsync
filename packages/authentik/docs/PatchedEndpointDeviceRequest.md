# PatchedEndpointDeviceRequest

Serializer for Endpoint authenticator devices

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pk** | **str** |  | [optional] 
**name** | **str** | The human-readable name of this device. | [optional] 

## Example

```python
from authentik_openapi.models.patched_endpoint_device_request import PatchedEndpointDeviceRequest

# TODO update the JSON string below
json = "{}"
# create an instance of PatchedEndpointDeviceRequest from a JSON string
patched_endpoint_device_request_instance = PatchedEndpointDeviceRequest.from_json(json)
# print the JSON string representation of the object
print(PatchedEndpointDeviceRequest.to_json())

# convert the object into a dict
patched_endpoint_device_request_dict = patched_endpoint_device_request_instance.to_dict()
# create an instance of PatchedEndpointDeviceRequest from a dict
patched_endpoint_device_request_from_dict = PatchedEndpointDeviceRequest.from_dict(patched_endpoint_device_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


