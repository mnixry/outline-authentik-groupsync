# OauthClientsRotateSecretRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the OAuth client. | 

## Example

```python
from outline_openapi.models.oauth_clients_rotate_secret_request import OauthClientsRotateSecretRequest

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientsRotateSecretRequest from a JSON string
oauth_clients_rotate_secret_request_instance = OauthClientsRotateSecretRequest.from_json(json)
# print the JSON string representation of the object
print(OauthClientsRotateSecretRequest.to_json())

# convert the object into a dict
oauth_clients_rotate_secret_request_dict = oauth_clients_rotate_secret_request_instance.to_dict()
# create an instance of OauthClientsRotateSecretRequest from a dict
oauth_clients_rotate_secret_request_from_dict = OauthClientsRotateSecretRequest.from_dict(oauth_clients_rotate_secret_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


