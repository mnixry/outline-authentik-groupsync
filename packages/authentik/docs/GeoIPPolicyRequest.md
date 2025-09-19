# GeoIPPolicyRequest

GeoIP Policy Serializer

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | 
**execution_logging** | **bool** | When this option is enabled, all executions of this policy will be logged. By default, only execution errors are logged. | [optional] 
**asns** | **List[int]** |  | [optional] 
**countries** | [**List[CountryCodeEnum]**](CountryCodeEnum.md) |  | 
**check_history_distance** | **bool** |  | [optional] 
**history_max_distance_km** | **int** |  | [optional] 
**distance_tolerance_km** | **int** |  | [optional] 
**history_login_count** | **int** |  | [optional] 
**check_impossible_travel** | **bool** |  | [optional] 
**impossible_tolerance_km** | **int** |  | [optional] 

## Example

```python
from authentik_openapi.models.geo_ip_policy_request import GeoIPPolicyRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GeoIPPolicyRequest from a JSON string
geo_ip_policy_request_instance = GeoIPPolicyRequest.from_json(json)
# print the JSON string representation of the object
print(GeoIPPolicyRequest.to_json())

# convert the object into a dict
geo_ip_policy_request_dict = geo_ip_policy_request_instance.to_dict()
# create an instance of GeoIPPolicyRequest from a dict
geo_ip_policy_request_from_dict = GeoIPPolicyRequest.from_dict(geo_ip_policy_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


