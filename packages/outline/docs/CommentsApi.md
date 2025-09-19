# outline_openapi.CommentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_create**](CommentsApi.md#comments_create) | **POST** /comments.create | Create a comment
[**comments_delete**](CommentsApi.md#comments_delete) | **POST** /comments.delete | Delete a comment
[**comments_info**](CommentsApi.md#comments_info) | **POST** /comments.info | Retrieve a comment
[**comments_list**](CommentsApi.md#comments_list) | **POST** /comments.list | List all comments
[**comments_update**](CommentsApi.md#comments_update) | **POST** /comments.update | Update a comment


# **comments_create**
> CommentsCreate200Response comments_create(comments_create_request=comments_create_request)

Create a comment

Add a comment or reply to a document, either `data` or `text` is required.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.comments_create200_response import CommentsCreate200Response
from outline_openapi.models.comments_create_request import CommentsCreateRequest
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
    api_instance = outline_openapi.CommentsApi(api_client)
    comments_create_request = outline_openapi.CommentsCreateRequest() # CommentsCreateRequest |  (optional)

    try:
        # Create a comment
        api_response = await api_instance.comments_create(comments_create_request=comments_create_request)
        print("The response of CommentsApi->comments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_create_request** | [**CommentsCreateRequest**](CommentsCreateRequest.md)|  | [optional] 

### Return type

[**CommentsCreate200Response**](CommentsCreate200Response.md)

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

# **comments_delete**
> AttachmentsDelete200Response comments_delete(collections_delete_request=collections_delete_request)

Delete a comment

Deletes a comment. If the comment is a top-level comment, all its children will be deleted as well.

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
    api_instance = outline_openapi.CommentsApi(api_client)
    collections_delete_request = outline_openapi.CollectionsDeleteRequest() # CollectionsDeleteRequest |  (optional)

    try:
        # Delete a comment
        api_response = await api_instance.comments_delete(collections_delete_request=collections_delete_request)
        print("The response of CommentsApi->comments_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_delete: %s\n" % e)
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
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_info**
> CommentsInfo200Response comments_info(comments_info_request=comments_info_request)

Retrieve a comment

Retrieve a comment

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.comments_info200_response import CommentsInfo200Response
from outline_openapi.models.comments_info_request import CommentsInfoRequest
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
    api_instance = outline_openapi.CommentsApi(api_client)
    comments_info_request = outline_openapi.CommentsInfoRequest() # CommentsInfoRequest |  (optional)

    try:
        # Retrieve a comment
        api_response = await api_instance.comments_info(comments_info_request=comments_info_request)
        print("The response of CommentsApi->comments_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_info_request** | [**CommentsInfoRequest**](CommentsInfoRequest.md)|  | [optional] 

### Return type

[**CommentsInfo200Response**](CommentsInfo200Response.md)

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

# **comments_list**
> CommentsList200Response comments_list(comments_list_request=comments_list_request)

List all comments

This method will list all comments matching the given properties.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.comments_list200_response import CommentsList200Response
from outline_openapi.models.comments_list_request import CommentsListRequest
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
    api_instance = outline_openapi.CommentsApi(api_client)
    comments_list_request = outline_openapi.CommentsListRequest() # CommentsListRequest |  (optional)

    try:
        # List all comments
        api_response = await api_instance.comments_list(comments_list_request=comments_list_request)
        print("The response of CommentsApi->comments_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_list_request** | [**CommentsListRequest**](CommentsListRequest.md)|  | [optional] 

### Return type

[**CommentsList200Response**](CommentsList200Response.md)

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

# **comments_update**
> CommentsInfo200Response comments_update(comments_update_request=comments_update_request)

Update a comment

Update a comment

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.comments_info200_response import CommentsInfo200Response
from outline_openapi.models.comments_update_request import CommentsUpdateRequest
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
    api_instance = outline_openapi.CommentsApi(api_client)
    comments_update_request = outline_openapi.CommentsUpdateRequest() # CommentsUpdateRequest |  (optional)

    try:
        # Update a comment
        api_response = await api_instance.comments_update(comments_update_request=comments_update_request)
        print("The response of CommentsApi->comments_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CommentsApi->comments_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **comments_update_request** | [**CommentsUpdateRequest**](CommentsUpdateRequest.md)|  | [optional] 

### Return type

[**CommentsInfo200Response**](CommentsInfo200Response.md)

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

