# outline_openapi.StarsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**stars_create**](StarsApi.md#stars_create) | **POST** /stars.create | Create a star
[**stars_delete**](StarsApi.md#stars_delete) | **POST** /stars.delete | Delete a star
[**stars_list**](StarsApi.md#stars_list) | **POST** /stars.list | List all stars
[**stars_update**](StarsApi.md#stars_update) | **POST** /stars.update | Update a stars order in the sidebar


# **stars_create**
> StarsCreate200Response stars_create(stars_create_request=stars_create_request)

Create a star

Stars a document or collection so it appears in the users sidebar. One of either `documentId` or `collectionId` must be provided.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.stars_create200_response import StarsCreate200Response
from outline_openapi.models.stars_create_request import StarsCreateRequest
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
    api_instance = outline_openapi.StarsApi(api_client)
    stars_create_request = outline_openapi.StarsCreateRequest() # StarsCreateRequest |  (optional)

    try:
        # Create a star
        api_response = await api_instance.stars_create(stars_create_request=stars_create_request)
        print("The response of StarsApi->stars_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarsApi->stars_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stars_create_request** | [**StarsCreateRequest**](StarsCreateRequest.md)|  | [optional] 

### Return type

[**StarsCreate200Response**](StarsCreate200Response.md)

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

# **stars_delete**
> AttachmentsDelete200Response stars_delete(collections_delete_request=collections_delete_request)

Delete a star

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
    api_instance = outline_openapi.StarsApi(api_client)
    collections_delete_request = outline_openapi.CollectionsDeleteRequest() # CollectionsDeleteRequest |  (optional)

    try:
        # Delete a star
        api_response = await api_instance.stars_delete(collections_delete_request=collections_delete_request)
        print("The response of StarsApi->stars_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarsApi->stars_delete: %s\n" % e)
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

# **stars_list**
> StarsList200Response stars_list(pagination=pagination)

List all stars

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.pagination import Pagination
from outline_openapi.models.stars_list200_response import StarsList200Response
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
    api_instance = outline_openapi.StarsApi(api_client)
    pagination = outline_openapi.Pagination() # Pagination |  (optional)

    try:
        # List all stars
        api_response = await api_instance.stars_list(pagination=pagination)
        print("The response of StarsApi->stars_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarsApi->stars_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**Pagination**](Pagination.md)|  | [optional] 

### Return type

[**StarsList200Response**](StarsList200Response.md)

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

# **stars_update**
> StarsCreate200Response stars_update(stars_update_request=stars_update_request)

Update a stars order in the sidebar

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.stars_create200_response import StarsCreate200Response
from outline_openapi.models.stars_update_request import StarsUpdateRequest
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
    api_instance = outline_openapi.StarsApi(api_client)
    stars_update_request = outline_openapi.StarsUpdateRequest() # StarsUpdateRequest |  (optional)

    try:
        # Update a stars order in the sidebar
        api_response = await api_instance.stars_update(stars_update_request=stars_update_request)
        print("The response of StarsApi->stars_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StarsApi->stars_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **stars_update_request** | [**StarsUpdateRequest**](StarsUpdateRequest.md)|  | [optional] 

### Return type

[**StarsCreate200Response**](StarsCreate200Response.md)

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

