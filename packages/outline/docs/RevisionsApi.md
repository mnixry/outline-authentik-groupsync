# outline_openapi.RevisionsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**revisions_info**](RevisionsApi.md#revisions_info) | **POST** /revisions.info | Retrieve a revision
[**revisions_list**](RevisionsApi.md#revisions_list) | **POST** /revisions.list | List all revisions


# **revisions_info**
> RevisionsInfo200Response revisions_info(revisions_info_request=revisions_info_request)

Retrieve a revision

A revision is a snapshot of a document at a specific point in time. This endpoint allows you to retrieve a specific version of a document by its unique identifier.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.revisions_info200_response import RevisionsInfo200Response
from outline_openapi.models.revisions_info_request import RevisionsInfoRequest
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
    api_instance = outline_openapi.RevisionsApi(api_client)
    revisions_info_request = outline_openapi.RevisionsInfoRequest() # RevisionsInfoRequest |  (optional)

    try:
        # Retrieve a revision
        api_response = await api_instance.revisions_info(revisions_info_request=revisions_info_request)
        print("The response of RevisionsApi->revisions_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevisionsApi->revisions_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revisions_info_request** | [**RevisionsInfoRequest**](RevisionsInfoRequest.md)|  | [optional] 

### Return type

[**RevisionsInfo200Response**](RevisionsInfo200Response.md)

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

# **revisions_list**
> RevisionsList200Response revisions_list(revisions_list_request=revisions_list_request)

List all revisions

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.revisions_list200_response import RevisionsList200Response
from outline_openapi.models.revisions_list_request import RevisionsListRequest
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
    api_instance = outline_openapi.RevisionsApi(api_client)
    revisions_list_request = outline_openapi.RevisionsListRequest() # RevisionsListRequest |  (optional)

    try:
        # List all revisions
        api_response = await api_instance.revisions_list(revisions_list_request=revisions_list_request)
        print("The response of RevisionsApi->revisions_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RevisionsApi->revisions_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **revisions_list_request** | [**RevisionsListRequest**](RevisionsListRequest.md)|  | [optional] 

### Return type

[**RevisionsList200Response**](RevisionsList200Response.md)

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

