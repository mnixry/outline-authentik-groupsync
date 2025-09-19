# OauthClientsCreateRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Name of the OAuth client. | 
**description** | **str** | A short description of this OAuth client. | [optional] 
**developer_name** | **str** | The name of the developer who created this OAuth client. | [optional] 
**developer_url** | **str** | The URL of the developer who created this OAuth client. | [optional] 
**avatar_url** | **str** | A URL pointing to an image representing the OAuth client. | [optional] 
**redirect_uris** | **List[str]** | List of redirect URIs for the OAuth client. | 
**published** | **bool** | Whether the OAuth client is available to other workspaces. | [optional] 

## Example

```python
from outline_openapi.models.oauth_clients_create_request import OauthClientsCreateRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientsCreateRequest from a JSON string
oauth_clients_create_request_instance = OauthClientsCreateRequest.from_json(json)
# print the JSON string representation of the object
print(OauthClientsCreateRequest.to_json())

# convert the object into a dict
oauth_clients_create_request_dict = oauth_clients_create_request_instance.to_dict()
# create an instance of OauthClientsCreateRequest from a dict
oauth_clients_create_request_from_dict = OauthClientsCreateRequest.from_dict(oauth_clients_create_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


