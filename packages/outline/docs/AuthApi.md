# outline_openapi.AuthApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_config_post**](AuthApi.md#auth_config_post) | **POST** /auth.config | Retrieve auth config
[**auth_info_post**](AuthApi.md#auth_info_post) | **POST** /auth.info | Retrieve auth


# **auth_config_post**
> AuthConfigPost200Response auth_config_post()

Retrieve auth config

Retrieve authentication options

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.auth_config_post200_response import AuthConfigPost200Response
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

# Configure Bearer authorization (JWT): http
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.AuthApi(api_client)

    try:
        # Retrieve auth config
        api_response = await api_instance.auth_config_post()
        print("The response of AuthApi->auth_config_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_config_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthConfigPost200Response**](AuthConfigPost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_info_post**
> AuthInfoPost200Response auth_info_post()

Retrieve auth

Retrieve authentication details for the current API key

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.auth_info_post200_response import AuthInfoPost200Response
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

# Configure Bearer authorization (JWT): http
configuration = outline_openapi.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.AuthApi(api_client)

    try:
        # Retrieve auth
        api_response = await api_instance.auth_info_post()
        print("The response of AuthApi->auth_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_info_post: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthInfoPost200Response**](AuthInfoPost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

