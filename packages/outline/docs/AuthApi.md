# outline_openapi.AuthApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**auth_config**](AuthApi.md#auth_config) | **POST** /auth.config | Retrieve auth config
[**auth_info**](AuthApi.md#auth_info) | **POST** /auth.info | Retrieve auth


# **auth_config**
> AuthConfig200Response auth_config()

Retrieve auth config

Retrieve authentication options

### Example


```python
import outline_openapi
from outline_openapi.models.auth_config200_response import AuthConfig200Response
from outline_openapi.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.getoutline.com/api
# See configuration.py for a list of all supported configuration parameters.
configuration = outline_openapi.Configuration(
    host = "https://app.getoutline.com/api"
)


# Enter a context with an instance of the API client
async with outline_openapi.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = outline_openapi.AuthApi(api_client)

    try:
        # Retrieve auth config
        api_response = await api_instance.auth_config()
        print("The response of AuthApi->auth_config:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_config: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthConfig200Response**](AuthConfig200Response.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **auth_info**
> AuthInfo200Response auth_info()

Retrieve auth

Retrieve authentication details for the current API key

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.auth_info200_response import AuthInfo200Response
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
    api_instance = outline_openapi.AuthApi(api_client)

    try:
        # Retrieve auth
        api_response = await api_instance.auth_info()
        print("The response of AuthApi->auth_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AuthApi->auth_info: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**AuthInfo200Response**](AuthInfo200Response.md)

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
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

