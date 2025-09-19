# outline_openapi.ViewsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**views_create**](ViewsApi.md#views_create) | **POST** /views.create | Create a view
[**views_list**](ViewsApi.md#views_list) | **POST** /views.list | List all views


# **views_create**
> ViewsCreate200Response views_create(shares_create_request=shares_create_request)

Create a view

Creates a new view for a document. This is documented in the interests of thoroughness however it is recommended that views are not created from outside of the Outline UI.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.shares_create_request import SharesCreateRequest
from outline_openapi.models.views_create200_response import ViewsCreate200Response
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
    api_instance = outline_openapi.ViewsApi(api_client)
    shares_create_request = outline_openapi.SharesCreateRequest() # SharesCreateRequest |  (optional)

    try:
        # Create a view
        api_response = await api_instance.views_create(shares_create_request=shares_create_request)
        print("The response of ViewsApi->views_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->views_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_create_request** | [**SharesCreateRequest**](SharesCreateRequest.md)|  | [optional] 

### Return type

[**ViewsCreate200Response**](ViewsCreate200Response.md)

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **views_list**
> ViewsList200Response views_list(views_list_request=views_list_request)

List all views

List all users that have viewed a document and the overall view count.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.views_list200_response import ViewsList200Response
from outline_openapi.models.views_list_request import ViewsListRequest
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
    api_instance = outline_openapi.ViewsApi(api_client)
    views_list_request = outline_openapi.ViewsListRequest() # ViewsListRequest |  (optional)

    try:
        # List all views
        api_response = await api_instance.views_list(views_list_request=views_list_request)
        print("The response of ViewsApi->views_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->views_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **views_list_request** | [**ViewsListRequest**](ViewsListRequest.md)|  | [optional] 

### Return type

[**ViewsList200Response**](ViewsList200Response.md)

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

