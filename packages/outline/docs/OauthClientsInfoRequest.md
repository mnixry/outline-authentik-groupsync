# OauthClientsInfoRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the OAuth client. | [optional] 
**client_id** | **str** | Public identifier for the OAuth client. | [optional] 

## Example

```python
from outline_openapi.models.oauth_clients_info_request import OauthClientsInfoRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientsInfoRequest from a JSON string
oauth_clients_info_request_instance = OauthClientsInfoRequest.from_json(json)
# print the JSON string representation of the object
print(OauthClientsInfoRequest.to_json())

# convert the object into a dict
oauth_clients_info_request_dict = oauth_clients_info_request_instance.to_dict()
# create an instance of OauthClientsInfoRequest from a dict
oauth_clients_info_request_from_dict = OauthClientsInfoRequest.from_dict(oauth_clients_info_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


