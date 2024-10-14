# outline_openapi.RevisionsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revisions_info_post**](RevisionsApi.md#revisions_info_post) | **POST** /revisions.info | Retrieve a revision
[**revisions_list_post**](RevisionsApi.md#revisions_list_post) | **POST** /revisions.list | List all revisions


# **revisions_info_post**
> RevisionsInfoPost200Response revisions_info_post(revisions_info_post_request=revisions_info_post_request)

Retrieve a revision

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.revisions_info_post200_response import RevisionsInfoPost200Response
from outline_openapi.models.revisions_info_post_request import RevisionsInfoPostRequest
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
    api_instance = outline_openapi.RevisionsApi(api_client)
    revisions_info_post_request = outline_openapi.RevisionsInfoPostRequest() # RevisionsInfoPostRequest |  (optional)

    try:
        # Retrieve a revision
        api_response = await api_instance.revisions_info_post(revisions_info_post_request=revisions_info_post_request)
        print("The response of RevisionsApi->revisions_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevisionsApi->revisions_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revisions_info_post_request** | [**RevisionsInfoPostRequest**](RevisionsInfoPostRequest.md)|  | [optional] 

### Return type

[**RevisionsInfoPost200Response**](RevisionsInfoPost200Response.md)

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
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **revisions_list_post**
> RevisionsListPost200Response revisions_list_post(documents_viewed_post_request=documents_viewed_post_request)

List all revisions

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.revisions_list_post200_response import RevisionsListPost200Response
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
    api_instance = outline_openapi.RevisionsApi(api_client)
    documents_viewed_post_request = outline_openapi.DocumentsViewedPostRequest() # DocumentsViewedPostRequest |  (optional)

    try:
        # List all revisions
        api_response = await api_instance.revisions_list_post(documents_viewed_post_request=documents_viewed_post_request)
        print("The response of RevisionsApi->revisions_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevisionsApi->revisions_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_viewed_post_request** | [**DocumentsViewedPostRequest**](DocumentsViewedPostRequest.md)|  | [optional] 

### Return type

[**RevisionsListPost200Response**](RevisionsListPost200Response.md)

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

