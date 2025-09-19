# OauthClientsUpdateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the OAuth client. | 
**name** | **str** | Name of the OAuth client. | [optional] 
**description** | **str** | A short description of this OAuth client. | [optional] 
**developer_name** | **str** | The name of the developer who created this OAuth client. | [optional] 
**developer_url** | **str** | The URL of the developer who created this OAuth client. | [optional] 
**avatar_url** | **str** | A URL pointing to an image representing the OAuth client. | [optional] 
**redirect_uris** | **List[str]** | List of redirect URIs for the OAuth client. | [optional] 
**published** | **bool** | Whether the OAuth client is available to other workspaces. | [optional] 

## Example

```python
from outline_openapi.models.oauth_clients_update_request import OauthClientsUpdateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientsUpdateRequest from a JSON string
oauth_clients_update_request_instance = OauthClientsUpdateRequest.from_json(json)
# print the JSON string representation of the object
print(OauthClientsUpdateRequest.to_json())

# convert the object into a dict
oauth_clients_update_request_dict = oauth_clients_update_request_instance.to_dict()
# create an instance of OauthClientsUpdateRequest from a dict
oauth_clients_update_request_from_dict = OauthClientsUpdateRequest.from_dict(oauth_clients_update_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


