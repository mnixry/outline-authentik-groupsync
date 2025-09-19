# outline_openapi.AttachmentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**attachments_create**](AttachmentsApi.md#attachments_create) | **POST** /attachments.create | Create an attachment
[**attachments_delete**](AttachmentsApi.md#attachments_delete) | **POST** /attachments.delete | Delete an attachment
[**attachments_redirect**](AttachmentsApi.md#attachments_redirect) | **POST** /attachments.redirect | Retrieve an attachment


# **attachments_create**
> AttachmentsCreate200Response attachments_create(attachments_create_request=attachments_create_request)

Create an attachment

Creating an attachment object creates a database record and returns the inputs needed to generate a signed url and upload the file from the client to cloud storage.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_create200_response import AttachmentsCreate200Response
from outline_openapi.models.attachments_create_request import AttachmentsCreateRequest
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
    api_instance = outline_openapi.AttachmentsApi(api_client)
    attachments_create_request = outline_openapi.AttachmentsCreateRequest() # AttachmentsCreateRequest |  (optional)

    try:
        # Create an attachment
        api_response = await api_instance.attachments_create(attachments_create_request=attachments_create_request)
        print("The response of AttachmentsApi->attachments_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_create_request** | [**AttachmentsCreateRequest**](AttachmentsCreateRequest.md)|  | [optional] 

### Return type

[**AttachmentsCreate200Response**](AttachmentsCreate200Response.md)

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

# **attachments_delete**
> AttachmentsDelete200Response attachments_delete(attachments_redirect_request=attachments_redirect_request)

Delete an attachment

Deleting an attachment is permanant. It will not delete references or links to the attachment that may exist in your documents.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.attachments_redirect_request import AttachmentsRedirectRequest
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
    api_instance = outline_openapi.AttachmentsApi(api_client)
    attachments_redirect_request = outline_openapi.AttachmentsRedirectRequest() # AttachmentsRedirectRequest |  (optional)

    try:
        # Delete an attachment
        api_response = await api_instance.attachments_delete(attachments_redirect_request=attachments_redirect_request)
        print("The response of AttachmentsApi->attachments_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_redirect_request** | [**AttachmentsRedirectRequest**](AttachmentsRedirectRequest.md)|  | [optional] 

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

# **attachments_redirect**
> attachments_redirect(attachments_redirect_request=attachments_redirect_request)

Retrieve an attachment

Load an attachment from where it is stored based on the id. If the attachment is private then a temporary, signed url with embedded credentials is generated on demand.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_redirect_request import AttachmentsRedirectRequest
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
    api_instance = outline_openapi.AttachmentsApi(api_client)
    attachments_redirect_request = outline_openapi.AttachmentsRedirectRequest() # AttachmentsRedirectRequest |  (optional)

    try:
        # Retrieve an attachment
        await api_instance.attachments_redirect(attachments_redirect_request=attachments_redirect_request)
    except Exception as e:
        print("Exception when calling AttachmentsApi->attachments_redirect: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **attachments_redirect_request** | [**AttachmentsRedirectRequest**](AttachmentsRedirectRequest.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: Not defined

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**302** | The url for the attachment |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

