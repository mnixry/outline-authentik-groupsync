# OAuthClient


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**name** | **str** | The name of this OAuth client. | [optional] 
**description** | **str** | A short description of this OAuth client. | [optional] 
**developer_name** | **str** | The name of the developer who created this OAuth client. | [optional] 
**developer_url** | **str** | The URL of the developer who created this OAuth client. | [optional] 
**avatar_url** | **str** | A URL pointing to an image representing the OAuth client. | [optional] 
**client_id** | **str** | The client ID for the OAuth client. | [optional] [readonly] 
**client_secret** | **str** | The client secret for the OAuth client. | [optional] [readonly] 
**redirect_uris** | **List[str]** | The redirect URIs for the OAuth client. | [optional] 
**published** | **bool** | Whether the OAuth client is available to other workspaces. | [optional] 
**created_at** | **datetime** | Date and time when this OAuth client was created | [optional] [readonly] 
**updated_at** | **datetime** | Date and time when this OAuth client was updated | [optional] [readonly] 

## Example

```python
from outline_openapi.models.o_auth_client import OAuthClient

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthClient from a JSON string
o_auth_client_instance = OAuthClient.from_json(json)
# print the JSON string representation of the object
print(OAuthClient.to_json())

# convert the object into a dict
o_auth_client_dict = o_auth_client_instance.to_dict()
# create an instance of OAuthClient from a dict
o_auth_client_from_dict = OAuthClient.from_dict(o_auth_client_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


