# outline_openapi.FileOperationsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**file_operations_delete_post**](FileOperationsApi.md#file_operations_delete_post) | **POST** /fileOperations.delete | Delete a file operation
[**file_operations_info_post**](FileOperationsApi.md#file_operations_info_post) | **POST** /fileOperations.info | Retrieve a file operation
[**file_operations_list_post**](FileOperationsApi.md#file_operations_list_post) | **POST** /fileOperations.list | List all file operations
[**file_operations_redirect_post**](FileOperationsApi.md#file_operations_redirect_post) | **POST** /fileOperations.redirect | Retrieve the file


# **file_operations_delete_post**
> AttachmentsDeletePost200Response file_operations_delete_post(file_operations_info_post_request=file_operations_info_post_request)

Delete a file operation

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.file_operations_info_post_request import FileOperationsInfoPostRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    file_operations_info_post_request = outline_openapi.FileOperationsInfoPostRequest() # FileOperationsInfoPostRequest |  (optional)

    try:
        # Delete a file operation
        api_response = await api_instance.file_operations_delete_post(file_operations_info_post_request=file_operations_info_post_request)
        print("The response of FileOperationsApi->file_operations_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->file_operations_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_operations_info_post_request** | [**FileOperationsInfoPostRequest**](FileOperationsInfoPostRequest.md)|  | [optional] 

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
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **file_operations_info_post**
> FileOperationsInfoPost200Response file_operations_info_post(file_operations_info_post_request=file_operations_info_post_request)

Retrieve a file operation

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.file_operations_info_post200_response import FileOperationsInfoPost200Response
from outline_openapi.models.file_operations_info_post_request import FileOperationsInfoPostRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    file_operations_info_post_request = outline_openapi.FileOperationsInfoPostRequest() # FileOperationsInfoPostRequest |  (optional)

    try:
        # Retrieve a file operation
        api_response = await api_instance.file_operations_info_post(file_operations_info_post_request=file_operations_info_post_request)
        print("The response of FileOperationsApi->file_operations_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->file_operations_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_operations_info_post_request** | [**FileOperationsInfoPostRequest**](FileOperationsInfoPostRequest.md)|  | [optional] 

### Return type

[**FileOperationsInfoPost200Response**](FileOperationsInfoPost200Response.md)

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

# **file_operations_list_post**
> FileOperationsListPost200Response file_operations_list_post(file_operations_list_post_request=file_operations_list_post_request)

List all file operations

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.file_operations_list_post200_response import FileOperationsListPost200Response
from outline_openapi.models.file_operations_list_post_request import FileOperationsListPostRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    file_operations_list_post_request = outline_openapi.FileOperationsListPostRequest() # FileOperationsListPostRequest |  (optional)

    try:
        # List all file operations
        api_response = await api_instance.file_operations_list_post(file_operations_list_post_request=file_operations_list_post_request)
        print("The response of FileOperationsApi->file_operations_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->file_operations_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_operations_list_post_request** | [**FileOperationsListPostRequest**](FileOperationsListPostRequest.md)|  | [optional] 

### Return type

[**FileOperationsListPost200Response**](FileOperationsListPost200Response.md)

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

# **file_operations_redirect_post**
> bytearray file_operations_redirect_post(file_operations_info_post_request=file_operations_info_post_request)

Retrieve the file

Load the resulting file from where it is stored based on the id. A temporary, signed url with embedded credentials is generated on demand.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.file_operations_info_post_request import FileOperationsInfoPostRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    file_operations_info_post_request = outline_openapi.FileOperationsInfoPostRequest() # FileOperationsInfoPostRequest |  (optional)

    try:
        # Retrieve the file
        api_response = await api_instance.file_operations_redirect_post(file_operations_info_post_request=file_operations_info_post_request)
        print("The response of FileOperationsApi->file_operations_redirect_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->file_operations_redirect_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file_operations_info_post_request** | [**FileOperationsInfoPostRequest**](FileOperationsInfoPostRequest.md)|  | [optional] 

### Return type

**bytearray**

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/octet-stream, application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

