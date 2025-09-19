# OauthClientsInfo200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**OAuthClient**](OAuthClient.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 

## Example

```python
from outline_openapi.models.oauth_clients_info200_response import OauthClientsInfo200Response

# TODO update the JSON string below
json = "{}"
# create an instance of OauthClientsInfo200Response from a JSON string
oauth_clients_info200_response_instance = OauthClientsInfo200Response.from_json(json)
# print the JSON string representation of the object
print(OauthClientsInfo200Response.to_json())

# convert the object into a dict
oauth_clients_info200_response_dict = oauth_clients_info200_response_instance.to_dict()
# create an instance of OauthClientsInfo200Response from a dict
oauth_clients_info200_response_from_dict = OauthClientsInfo200Response.from_dict(oauth_clients_info200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


