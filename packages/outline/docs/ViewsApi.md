# outline_openapi.ViewsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**views_create_post**](ViewsApi.md#views_create_post) | **POST** /views.create | Create a view
[**views_list_post**](ViewsApi.md#views_list_post) | **POST** /views.list | List all views


# **views_create_post**
> ViewsCreatePost200Response views_create_post(shares_create_post_request=shares_create_post_request)

Create a view

Creates a new view for a document. This is documented in the interests of thoroughness however it is recommended that views are not created from outside of the Outline UI.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.shares_create_post_request import SharesCreatePostRequest
from outline_openapi.models.views_create_post200_response import ViewsCreatePost200Response
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
    api_instance = outline_openapi.ViewsApi(api_client)
    shares_create_post_request = outline_openapi.SharesCreatePostRequest() # SharesCreatePostRequest |  (optional)

    try:
        # Create a view
        api_response = await api_instance.views_create_post(shares_create_post_request=shares_create_post_request)
        print("The response of ViewsApi->views_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->views_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_create_post_request** | [**SharesCreatePostRequest**](SharesCreatePostRequest.md)|  | [optional] 

### Return type

[**ViewsCreatePost200Response**](ViewsCreatePost200Response.md)

### Authorization

[http](../README.md#http)

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

# **views_list_post**
> ViewsListPost200Response views_list_post(shares_create_post_request=shares_create_post_request)

List all views

List all users that have viewed a document and the overall view count.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.shares_create_post_request import SharesCreatePostRequest
from outline_openapi.models.views_list_post200_response import ViewsListPost200Response
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
    api_instance = outline_openapi.ViewsApi(api_client)
    shares_create_post_request = outline_openapi.SharesCreatePostRequest() # SharesCreatePostRequest |  (optional)

    try:
        # List all views
        api_response = await api_instance.views_list_post(shares_create_post_request=shares_create_post_request)
        print("The response of ViewsApi->views_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ViewsApi->views_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_create_post_request** | [**SharesCreatePostRequest**](SharesCreatePostRequest.md)|  | [optional] 

### Return type

[**ViewsListPost200Response**](ViewsListPost200Response.md)

### Authorization

[http](../README.md#http)

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

