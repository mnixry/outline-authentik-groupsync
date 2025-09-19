# outline_openapi.OAuthClientsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**oauth_clients_create**](OAuthClientsApi.md#oauth_clients_create) | **POST** /oauthClients.create | Create an OAuth client
[**oauth_clients_delete**](OAuthClientsApi.md#oauth_clients_delete) | **POST** /oauthClients.delete | Delete an OAuth client
[**oauth_clients_info**](OAuthClientsApi.md#oauth_clients_info) | **POST** /oauthClients.info | Retrieve an OAuth client
[**oauth_clients_list**](OAuthClientsApi.md#oauth_clients_list) | **POST** /oauthClients.list | List accessible OAuth clients
[**oauth_clients_rotate_secret**](OAuthClientsApi.md#oauth_clients_rotate_secret) | **POST** /oauthClients.rotate_secret | Rotate the secret for an OAuth client
[**oauth_clients_update**](OAuthClientsApi.md#oauth_clients_update) | **POST** /oauthClients.update | Update an OAuth client


# **oauth_clients_create**
> OauthClientsInfo200Response oauth_clients_create(oauth_clients_create_request=oauth_clients_create_request)

Create an OAuth client

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.oauth_clients_create_request import OauthClientsCreateRequest
from outline_openapi.models.oauth_clients_info200_response import OauthClientsInfo200Response
from outline_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = outline_openapi.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): BearerAuth
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.OAuthClientsApi(api_client)
    oauth_clients_create_request = outline_openapi.OauthClientsCreateRequest() # OauthClientsCreateRequest |  (optional)

    try:
        # Create an OAuth client
        api_response = await api_instance.oauth_clients_create(oauth_clients_create_request=oauth_clients_create_request)
        print("The response of OAuthClientsApi->oauth_clients_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->oauth_clients_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_clients_create_request** | [**OauthClientsCreateRequest**](OauthClientsCreateRequest.md)|  | [optional] 

### Return type

[**OauthClientsInfo200Response**](OauthClientsInfo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_clients_delete**
> AttachmentsDelete200Response oauth_clients_delete(oauth_clients_rotate_secret_request=oauth_clients_rotate_secret_request)

Delete an OAuth client

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.oauth_clients_rotate_secret_request import OauthClientsRotateSecretRequest
from outline_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = outline_openapi.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): BearerAuth
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.OAuthClientsApi(api_client)
    oauth_clients_rotate_secret_request = outline_openapi.OauthClientsRotateSecretRequest() # OauthClientsRotateSecretRequest |  (optional)

    try:
        # Delete an OAuth client
        api_response = await api_instance.oauth_clients_delete(oauth_clients_rotate_secret_request=oauth_clients_rotate_secret_request)
        print("The response of OAuthClientsApi->oauth_clients_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->oauth_clients_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_clients_rotate_secret_request** | [**OauthClientsRotateSecretRequest**](OauthClientsRotateSecretRequest.md)|  | [optional] 

### Return type

[**AttachmentsDelete200Response**](AttachmentsDelete200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_clients_info**
> OauthClientsInfo200Response oauth_clients_info(oauth_clients_info_request=oauth_clients_info_request)

Retrieve an OAuth client

To retrieve information about an OAuth client you must pass either an `id` or a `clientId`.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.oauth_clients_info200_response import OauthClientsInfo200Response
from outline_openapi.models.oauth_clients_info_request import OauthClientsInfoRequest
from outline_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = outline_openapi.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): BearerAuth
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.OAuthClientsApi(api_client)
    oauth_clients_info_request = outline_openapi.OauthClientsInfoRequest() # OauthClientsInfoRequest |  (optional)

    try:
        # Retrieve an OAuth client
        api_response = await api_instance.oauth_clients_info(oauth_clients_info_request=oauth_clients_info_request)
        print("The response of OAuthClientsApi->oauth_clients_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->oauth_clients_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_clients_info_request** | [**OauthClientsInfoRequest**](OauthClientsInfoRequest.md)|  | [optional] 

### Return type

[**OauthClientsInfo200Response**](OauthClientsInfo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_clients_list**
> OauthClientsList200Response oauth_clients_list()

List accessible OAuth clients

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.oauth_clients_list200_response import OauthClientsList200Response
from outline_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = outline_openapi.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): BearerAuth
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.OAuthClientsApi(api_client)

    try:
        # List accessible OAuth clients
        api_response = await api_instance.oauth_clients_list()
        print("The response of OAuthClientsApi->oauth_clients_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->oauth_clients_list: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**OauthClientsList200Response**](OauthClientsList200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_clients_rotate_secret**
> OauthClientsInfo200Response oauth_clients_rotate_secret(oauth_clients_rotate_secret_request=oauth_clients_rotate_secret_request)

Rotate the secret for an OAuth client

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.oauth_clients_info200_response import OauthClientsInfo200Response
from outline_openapi.models.oauth_clients_rotate_secret_request import OauthClientsRotateSecretRequest
from outline_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = outline_openapi.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): BearerAuth
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.OAuthClientsApi(api_client)
    oauth_clients_rotate_secret_request = outline_openapi.OauthClientsRotateSecretRequest() # OauthClientsRotateSecretRequest |  (optional)

    try:
        # Rotate the secret for an OAuth client
        api_response = await api_instance.oauth_clients_rotate_secret(oauth_clients_rotate_secret_request=oauth_clients_rotate_secret_request)
        print("The response of OAuthClientsApi->oauth_clients_rotate_secret:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->oauth_clients_rotate_secret: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_clients_rotate_secret_request** | [**OauthClientsRotateSecretRequest**](OauthClientsRotateSecretRequest.md)|  | [optional] 

### Return type

[**OauthClientsInfo200Response**](OauthClientsInfo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **oauth_clients_update**
> OauthClientsInfo200Response oauth_clients_update(oauth_clients_update_request=oauth_clients_update_request)

Update an OAuth client

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.oauth_clients_info200_response import OauthClientsInfo200Response
from outline_openapi.models.oauth_clients_update_request import OauthClientsUpdateRequest
from outline_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = outline_openapi.Configuration(
    host = "https://app.getoutline.com/api"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

configuration.access_token = os.environ["ACCESS_TOKEN"]

# Configure Bearer authorization (JWT): BearerAuth
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.OAuthClientsApi(api_client)
    oauth_clients_update_request = outline_openapi.OauthClientsUpdateRequest() # OauthClientsUpdateRequest |  (optional)

    try:
        # Update an OAuth client
        api_response = await api_instance.oauth_clients_update(oauth_clients_update_request=oauth_clients_update_request)
        print("The response of OAuthClientsApi->oauth_clients_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OAuthClientsApi->oauth_clients_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **oauth_clients_update_request** | [**OauthClientsUpdateRequest**](OauthClientsUpdateRequest.md)|  | [optional] 

### Return type

[**OauthClientsInfo200Response**](OauthClientsInfo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

