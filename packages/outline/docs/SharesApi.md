# outline_openapi.SharesApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shares_create_post**](SharesApi.md#shares_create_post) | **POST** /shares.create | Create a share
[**shares_info_post**](SharesApi.md#shares_info_post) | **POST** /shares.info | Retrieve a share object
[**shares_list_post**](SharesApi.md#shares_list_post) | **POST** /shares.list | List all shares
[**shares_revoke_post**](SharesApi.md#shares_revoke_post) | **POST** /shares.revoke | Revoke a share
[**shares_update_post**](SharesApi.md#shares_update_post) | **POST** /shares.update | Update a share


# **shares_create_post**
> SharesInfoPost200Response shares_create_post(shares_create_post_request=shares_create_post_request)

Create a share

Creates a new share link that can be used by to access a document. If you request multiple shares for the same document with the same API key, the same share object will be returned. By default all shares are unpublished.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.shares_create_post_request import SharesCreatePostRequest
from outline_openapi.models.shares_info_post200_response import SharesInfoPost200Response
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
    api_instance = outline_openapi.SharesApi(api_client)
    shares_create_post_request = outline_openapi.SharesCreatePostRequest() # SharesCreatePostRequest |  (optional)

    try:
        # Create a share
        api_response = await api_instance.shares_create_post(shares_create_post_request=shares_create_post_request)
        print("The response of SharesApi->shares_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_create_post_request** | [**SharesCreatePostRequest**](SharesCreatePostRequest.md)|  | [optional] 

### Return type

[**SharesInfoPost200Response**](SharesInfoPost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The request failed one or more validations. |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_info_post**
> SharesInfoPost200Response shares_info_post(shares_info_post_request=shares_info_post_request)

Retrieve a share object

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.shares_info_post200_response import SharesInfoPost200Response
from outline_openapi.models.shares_info_post_request import SharesInfoPostRequest
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
    api_instance = outline_openapi.SharesApi(api_client)
    shares_info_post_request = outline_openapi.SharesInfoPostRequest() # SharesInfoPostRequest |  (optional)

    try:
        # Retrieve a share object
        api_response = await api_instance.shares_info_post(shares_info_post_request=shares_info_post_request)
        print("The response of SharesApi->shares_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_info_post_request** | [**SharesInfoPostRequest**](SharesInfoPostRequest.md)|  | [optional] 

### Return type

[**SharesInfoPost200Response**](SharesInfoPost200Response.md)

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

# **shares_list_post**
> SharesListPost200Response shares_list_post(documents_viewed_post_request=documents_viewed_post_request)

List all shares

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.shares_list_post200_response import SharesListPost200Response
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
    api_instance = outline_openapi.SharesApi(api_client)
    documents_viewed_post_request = outline_openapi.DocumentsViewedPostRequest() # DocumentsViewedPostRequest |  (optional)

    try:
        # List all shares
        api_response = await api_instance.shares_list_post(documents_viewed_post_request=documents_viewed_post_request)
        print("The response of SharesApi->shares_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_viewed_post_request** | [**DocumentsViewedPostRequest**](DocumentsViewedPostRequest.md)|  | [optional] 

### Return type

[**SharesListPost200Response**](SharesListPost200Response.md)

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

# **shares_revoke_post**
> AttachmentsDeletePost200Response shares_revoke_post(collections_delete_post_request=collections_delete_post_request)

Revoke a share

Makes the share link inactive so that it can no longer be used to access the document.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
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
    api_instance = outline_openapi.SharesApi(api_client)
    collections_delete_post_request = outline_openapi.CollectionsDeletePostRequest() # CollectionsDeletePostRequest |  (optional)

    try:
        # Revoke a share
        api_response = await api_instance.shares_revoke_post(collections_delete_post_request=collections_delete_post_request)
        print("The response of SharesApi->shares_revoke_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_revoke_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_delete_post_request** | [**CollectionsDeletePostRequest**](CollectionsDeletePostRequest.md)|  | [optional] 

### Return type

[**AttachmentsDeletePost200Response**](AttachmentsDeletePost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The request failed one or more validations. |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_update_post**
> SharesInfoPost200Response shares_update_post(shares_update_post_request=shares_update_post_request)

Update a share

Allows changing an existing shares published status, which removes authentication and makes it available to anyone with the link.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.shares_info_post200_response import SharesInfoPost200Response
from outline_openapi.models.shares_update_post_request import SharesUpdatePostRequest
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
    api_instance = outline_openapi.SharesApi(api_client)
    shares_update_post_request = outline_openapi.SharesUpdatePostRequest() # SharesUpdatePostRequest |  (optional)

    try:
        # Update a share
        api_response = await api_instance.shares_update_post(shares_update_post_request=shares_update_post_request)
        print("The response of SharesApi->shares_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_update_post_request** | [**SharesUpdatePostRequest**](SharesUpdatePostRequest.md)|  | [optional] 

### Return type

[**SharesInfoPost200Response**](SharesInfoPost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**400** | The request failed one or more validations. |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

