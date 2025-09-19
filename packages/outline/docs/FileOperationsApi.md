# outline_openapi.FileOperationsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**fileoperations_delete**](FileOperationsApi.md#fileoperations_delete) | **POST** /fileOperations.delete | Delete a file operation
[**fileoperations_info**](FileOperationsApi.md#fileoperations_info) | **POST** /fileOperations.info | Retrieve a file operation
[**fileoperations_list**](FileOperationsApi.md#fileoperations_list) | **POST** /fileOperations.list | List all file operations
[**fileoperations_redirect**](FileOperationsApi.md#fileoperations_redirect) | **POST** /fileOperations.redirect | Retrieve the file


# **fileoperations_delete**
> AttachmentsDelete200Response fileoperations_delete(fileoperations_info_request=fileoperations_info_request)

Delete a file operation

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.fileoperations_info_request import FileoperationsInfoRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    fileoperations_info_request = outline_openapi.FileoperationsInfoRequest() # FileoperationsInfoRequest |  (optional)

    try:
        # Delete a file operation
        api_response = await api_instance.fileoperations_delete(fileoperations_info_request=fileoperations_info_request)
        print("The response of FileOperationsApi->fileoperations_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->fileoperations_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileoperations_info_request** | [**FileoperationsInfoRequest**](FileoperationsInfoRequest.md)|  | [optional] 

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

# **fileoperations_info**
> FileoperationsInfo200Response fileoperations_info(fileoperations_info_request=fileoperations_info_request)

Retrieve a file operation

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.fileoperations_info200_response import FileoperationsInfo200Response
from outline_openapi.models.fileoperations_info_request import FileoperationsInfoRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    fileoperations_info_request = outline_openapi.FileoperationsInfoRequest() # FileoperationsInfoRequest |  (optional)

    try:
        # Retrieve a file operation
        api_response = await api_instance.fileoperations_info(fileoperations_info_request=fileoperations_info_request)
        print("The response of FileOperationsApi->fileoperations_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->fileoperations_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileoperations_info_request** | [**FileoperationsInfoRequest**](FileoperationsInfoRequest.md)|  | [optional] 

### Return type

[**FileoperationsInfo200Response**](FileoperationsInfo200Response.md)

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

# **fileoperations_list**
> FileoperationsList200Response fileoperations_list(fileoperations_list_request=fileoperations_list_request)

List all file operations

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.fileoperations_list200_response import FileoperationsList200Response
from outline_openapi.models.fileoperations_list_request import FileoperationsListRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    fileoperations_list_request = outline_openapi.FileoperationsListRequest() # FileoperationsListRequest |  (optional)

    try:
        # List all file operations
        api_response = await api_instance.fileoperations_list(fileoperations_list_request=fileoperations_list_request)
        print("The response of FileOperationsApi->fileoperations_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->fileoperations_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileoperations_list_request** | [**FileoperationsListRequest**](FileoperationsListRequest.md)|  | [optional] 

### Return type

[**FileoperationsList200Response**](FileoperationsList200Response.md)

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

# **fileoperations_redirect**
> bytearray fileoperations_redirect(fileoperations_info_request=fileoperations_info_request)

Retrieve the file

Load the resulting file from where it is stored based on the id. A temporary, signed url with embedded credentials is generated on demand.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.fileoperations_info_request import FileoperationsInfoRequest
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
    api_instance = outline_openapi.FileOperationsApi(api_client)
    fileoperations_info_request = outline_openapi.FileoperationsInfoRequest() # FileoperationsInfoRequest |  (optional)

    try:
        # Retrieve the file
        api_response = await api_instance.fileoperations_redirect(fileoperations_info_request=fileoperations_info_request)
        print("The response of FileOperationsApi->fileoperations_redirect:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling FileOperationsApi->fileoperations_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **fileoperations_info_request** | [**FileoperationsInfoRequest**](FileoperationsInfoRequest.md)|  | [optional] 

### Return type

**bytearray**

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

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
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

