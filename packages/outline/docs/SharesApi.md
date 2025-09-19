# outline_openapi.SharesApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**shares_create**](SharesApi.md#shares_create) | **POST** /shares.create | Create a share
[**shares_info**](SharesApi.md#shares_info) | **POST** /shares.info | Retrieve a share object
[**shares_list**](SharesApi.md#shares_list) | **POST** /shares.list | List all shares
[**shares_revoke**](SharesApi.md#shares_revoke) | **POST** /shares.revoke | Revoke a share
[**shares_update**](SharesApi.md#shares_update) | **POST** /shares.update | Update a share


# **shares_create**
> SharesInfo200Response shares_create(shares_create_request=shares_create_request)

Create a share

Creates a new share link that can be used by to access a document. If you request multiple shares for the same document with the same API key, the same share object will be returned. By default all shares are unpublished.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.shares_create_request import SharesCreateRequest
from outline_openapi.models.shares_info200_response import SharesInfo200Response
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
    api_instance = outline_openapi.SharesApi(api_client)
    shares_create_request = outline_openapi.SharesCreateRequest() # SharesCreateRequest |  (optional)

    try:
        # Create a share
        api_response = await api_instance.shares_create(shares_create_request=shares_create_request)
        print("The response of SharesApi->shares_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_create_request** | [**SharesCreateRequest**](SharesCreateRequest.md)|  | [optional] 

### Return type

[**SharesInfo200Response**](SharesInfo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

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
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_info**
> SharesInfo200Response shares_info(shares_info_request=shares_info_request)

Retrieve a share object

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.shares_info200_response import SharesInfo200Response
from outline_openapi.models.shares_info_request import SharesInfoRequest
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
    api_instance = outline_openapi.SharesApi(api_client)
    shares_info_request = outline_openapi.SharesInfoRequest() # SharesInfoRequest |  (optional)

    try:
        # Retrieve a share object
        api_response = await api_instance.shares_info(shares_info_request=shares_info_request)
        print("The response of SharesApi->shares_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_info_request** | [**SharesInfoRequest**](SharesInfoRequest.md)|  | [optional] 

### Return type

[**SharesInfo200Response**](SharesInfo200Response.md)

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

# **shares_list**
> SharesList200Response shares_list(shares_list_request=shares_list_request)

List all shares

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.shares_list200_response import SharesList200Response
from outline_openapi.models.shares_list_request import SharesListRequest
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
    api_instance = outline_openapi.SharesApi(api_client)
    shares_list_request = outline_openapi.SharesListRequest() # SharesListRequest |  (optional)

    try:
        # List all shares
        api_response = await api_instance.shares_list(shares_list_request=shares_list_request)
        print("The response of SharesApi->shares_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_list_request** | [**SharesListRequest**](SharesListRequest.md)|  | [optional] 

### Return type

[**SharesList200Response**](SharesList200Response.md)

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

# **shares_revoke**
> AttachmentsDelete200Response shares_revoke(collections_delete_request=collections_delete_request)

Revoke a share

Makes the share link inactive so that it can no longer be used to access the document.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.collections_delete_request import CollectionsDeleteRequest
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
    api_instance = outline_openapi.SharesApi(api_client)
    collections_delete_request = outline_openapi.CollectionsDeleteRequest() # CollectionsDeleteRequest |  (optional)

    try:
        # Revoke a share
        api_response = await api_instance.shares_revoke(collections_delete_request=collections_delete_request)
        print("The response of SharesApi->shares_revoke:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_revoke: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_delete_request** | [**CollectionsDeleteRequest**](CollectionsDeleteRequest.md)|  | [optional] 

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
**400** | The request failed one or more validations. |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **shares_update**
> SharesInfo200Response shares_update(shares_update_request=shares_update_request)

Update a share

Allows changing an existing share's published status, which removes authentication and makes it available to anyone with the link.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.shares_info200_response import SharesInfo200Response
from outline_openapi.models.shares_update_request import SharesUpdateRequest
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
    api_instance = outline_openapi.SharesApi(api_client)
    shares_update_request = outline_openapi.SharesUpdateRequest() # SharesUpdateRequest |  (optional)

    try:
        # Update a share
        api_response = await api_instance.shares_update(shares_update_request=shares_update_request)
        print("The response of SharesApi->shares_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling SharesApi->shares_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **shares_update_request** | [**SharesUpdateRequest**](SharesUpdateRequest.md)|  | [optional] 

### Return type

[**SharesInfo200Response**](SharesInfo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

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
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

