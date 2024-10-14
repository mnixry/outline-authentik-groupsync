# outline_openapi.CollectionsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_add_group_post**](CollectionsApi.md#collections_add_group_post) | **POST** /collections.add_group | Add a group to a collection
[**collections_add_user_post**](CollectionsApi.md#collections_add_user_post) | **POST** /collections.add_user | Add a collection user
[**collections_create_post**](CollectionsApi.md#collections_create_post) | **POST** /collections.create | Create a collection
[**collections_delete_post**](CollectionsApi.md#collections_delete_post) | **POST** /collections.delete | Delete a collection
[**collections_documents_post**](CollectionsApi.md#collections_documents_post) | **POST** /collections.documents | Retrieve a collections document structure
[**collections_export_all_post**](CollectionsApi.md#collections_export_all_post) | **POST** /collections.export_all | Export all collections
[**collections_export_post**](CollectionsApi.md#collections_export_post) | **POST** /collections.export | Export a collection
[**collections_group_memberships_post**](CollectionsApi.md#collections_group_memberships_post) | **POST** /collections.group_memberships | List all collection group members
[**collections_info_post**](CollectionsApi.md#collections_info_post) | **POST** /collections.info | Retrieve a collection
[**collections_list_post**](CollectionsApi.md#collections_list_post) | **POST** /collections.list | List all collections
[**collections_memberships_post**](CollectionsApi.md#collections_memberships_post) | **POST** /collections.memberships | List all collection memberships
[**collections_remove_group_post**](CollectionsApi.md#collections_remove_group_post) | **POST** /collections.remove_group | Remove a collection group
[**collections_remove_user_post**](CollectionsApi.md#collections_remove_user_post) | **POST** /collections.remove_user | Remove a collection user
[**collections_update_post**](CollectionsApi.md#collections_update_post) | **POST** /collections.update | Update a collection


# **collections_add_group_post**
> CollectionsAddGroupPost200Response collections_add_group_post(collections_add_group_post_request=collections_add_group_post_request)

Add a group to a collection

This method allows you to give all members in a group access to a collection.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_add_group_post200_response import CollectionsAddGroupPost200Response
from outline_openapi.models.collections_add_group_post_request import CollectionsAddGroupPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_add_group_post_request = outline_openapi.CollectionsAddGroupPostRequest() # CollectionsAddGroupPostRequest |  (optional)

    try:
        # Add a group to a collection
        api_response = await api_instance.collections_add_group_post(collections_add_group_post_request=collections_add_group_post_request)
        print("The response of CollectionsApi->collections_add_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_add_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_add_group_post_request** | [**CollectionsAddGroupPostRequest**](CollectionsAddGroupPostRequest.md)|  | [optional] 

### Return type

[**CollectionsAddGroupPost200Response**](CollectionsAddGroupPost200Response.md)

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

# **collections_add_user_post**
> CollectionsAddUserPost200Response collections_add_user_post(collections_add_user_post_request=collections_add_user_post_request)

Add a collection user

This method allows you to add a user membership to the specified collection.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_add_user_post200_response import CollectionsAddUserPost200Response
from outline_openapi.models.collections_add_user_post_request import CollectionsAddUserPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_add_user_post_request = outline_openapi.CollectionsAddUserPostRequest() # CollectionsAddUserPostRequest |  (optional)

    try:
        # Add a collection user
        api_response = await api_instance.collections_add_user_post(collections_add_user_post_request=collections_add_user_post_request)
        print("The response of CollectionsApi->collections_add_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_add_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_add_user_post_request** | [**CollectionsAddUserPostRequest**](CollectionsAddUserPostRequest.md)|  | [optional] 

### Return type

[**CollectionsAddUserPost200Response**](CollectionsAddUserPost200Response.md)

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

# **collections_create_post**
> CollectionsCreatePost200Response collections_create_post(collections_create_post_request=collections_create_post_request)

Create a collection

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_create_post200_response import CollectionsCreatePost200Response
from outline_openapi.models.collections_create_post_request import CollectionsCreatePostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_create_post_request = outline_openapi.CollectionsCreatePostRequest() # CollectionsCreatePostRequest |  (optional)

    try:
        # Create a collection
        api_response = await api_instance.collections_create_post(collections_create_post_request=collections_create_post_request)
        print("The response of CollectionsApi->collections_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_create_post_request** | [**CollectionsCreatePostRequest**](CollectionsCreatePostRequest.md)|  | [optional] 

### Return type

[**CollectionsCreatePost200Response**](CollectionsCreatePost200Response.md)

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

# **collections_delete_post**
> AttachmentsDeletePost200Response collections_delete_post(collections_delete_post_request=collections_delete_post_request)

Delete a collection

Delete a collection and all of its documents. This action can’t be undone so please be careful.

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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_delete_post_request = outline_openapi.CollectionsDeletePostRequest() # CollectionsDeletePostRequest |  (optional)

    try:
        # Delete a collection
        api_response = await api_instance.collections_delete_post(collections_delete_post_request=collections_delete_post_request)
        print("The response of CollectionsApi->collections_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_delete_post: %s\n" % e)
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
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **collections_documents_post**
> CollectionsDocumentsPost200Response collections_documents_post(collections_info_post_request=collections_info_post_request)

Retrieve a collections document structure

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_documents_post200_response import CollectionsDocumentsPost200Response
from outline_openapi.models.collections_info_post_request import CollectionsInfoPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_info_post_request = outline_openapi.CollectionsInfoPostRequest() # CollectionsInfoPostRequest |  (optional)

    try:
        # Retrieve a collections document structure
        api_response = await api_instance.collections_documents_post(collections_info_post_request=collections_info_post_request)
        print("The response of CollectionsApi->collections_documents_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_documents_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_info_post_request** | [**CollectionsInfoPostRequest**](CollectionsInfoPostRequest.md)|  | [optional] 

### Return type

[**CollectionsDocumentsPost200Response**](CollectionsDocumentsPost200Response.md)

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

# **collections_export_all_post**
> CollectionsExportPost200Response collections_export_all_post(collections_export_all_post_request=collections_export_all_post_request)

Export all collections

Triggers a bulk export of all documents in and their attachments. The endpoint returns a `FileOperation` that can be queried through the fileOperations endpoint to track the progress of the export and get the url for the final file.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_export_all_post_request import CollectionsExportAllPostRequest
from outline_openapi.models.collections_export_post200_response import CollectionsExportPost200Response
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_export_all_post_request = outline_openapi.CollectionsExportAllPostRequest() # CollectionsExportAllPostRequest |  (optional)

    try:
        # Export all collections
        api_response = await api_instance.collections_export_all_post(collections_export_all_post_request=collections_export_all_post_request)
        print("The response of CollectionsApi->collections_export_all_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_export_all_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_export_all_post_request** | [**CollectionsExportAllPostRequest**](CollectionsExportAllPostRequest.md)|  | [optional] 

### Return type

[**CollectionsExportPost200Response**](CollectionsExportPost200Response.md)

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

# **collections_export_post**
> CollectionsExportPost200Response collections_export_post(collections_export_post_request=collections_export_post_request)

Export a collection

Triggers a bulk export of the collection in markdown format and their attachments. If documents are nested then they will be nested in folders inside the zip file. The endpoint returns a `FileOperation` that can be queried to track the progress of the export and get the url for the final file.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_export_post200_response import CollectionsExportPost200Response
from outline_openapi.models.collections_export_post_request import CollectionsExportPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_export_post_request = outline_openapi.CollectionsExportPostRequest() # CollectionsExportPostRequest |  (optional)

    try:
        # Export a collection
        api_response = await api_instance.collections_export_post(collections_export_post_request=collections_export_post_request)
        print("The response of CollectionsApi->collections_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_export_post_request** | [**CollectionsExportPostRequest**](CollectionsExportPostRequest.md)|  | [optional] 

### Return type

[**CollectionsExportPost200Response**](CollectionsExportPost200Response.md)

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

# **collections_group_memberships_post**
> CollectionsGroupMembershipsPost200Response collections_group_memberships_post(collections_group_memberships_post_request=collections_group_memberships_post_request)

List all collection group members

This method allows you to list a collections group memberships. This is the list of groups that have been given access to the collection.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_group_memberships_post200_response import CollectionsGroupMembershipsPost200Response
from outline_openapi.models.collections_group_memberships_post_request import CollectionsGroupMembershipsPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_group_memberships_post_request = outline_openapi.CollectionsGroupMembershipsPostRequest() # CollectionsGroupMembershipsPostRequest |  (optional)

    try:
        # List all collection group members
        api_response = await api_instance.collections_group_memberships_post(collections_group_memberships_post_request=collections_group_memberships_post_request)
        print("The response of CollectionsApi->collections_group_memberships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_group_memberships_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_group_memberships_post_request** | [**CollectionsGroupMembershipsPostRequest**](CollectionsGroupMembershipsPostRequest.md)|  | [optional] 

### Return type

[**CollectionsGroupMembershipsPost200Response**](CollectionsGroupMembershipsPost200Response.md)

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

# **collections_info_post**
> CollectionsInfoPost200Response collections_info_post(collections_info_post_request=collections_info_post_request)

Retrieve a collection

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_info_post200_response import CollectionsInfoPost200Response
from outline_openapi.models.collections_info_post_request import CollectionsInfoPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_info_post_request = outline_openapi.CollectionsInfoPostRequest() # CollectionsInfoPostRequest |  (optional)

    try:
        # Retrieve a collection
        api_response = await api_instance.collections_info_post(collections_info_post_request=collections_info_post_request)
        print("The response of CollectionsApi->collections_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_info_post_request** | [**CollectionsInfoPostRequest**](CollectionsInfoPostRequest.md)|  | [optional] 

### Return type

[**CollectionsInfoPost200Response**](CollectionsInfoPost200Response.md)

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

# **collections_list_post**
> CollectionsListPost200Response collections_list_post(pagination=pagination)

List all collections

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_list_post200_response import CollectionsListPost200Response
from outline_openapi.models.pagination import Pagination
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    pagination = outline_openapi.Pagination() # Pagination |  (optional)

    try:
        # List all collections
        api_response = await api_instance.collections_list_post(pagination=pagination)
        print("The response of CollectionsApi->collections_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **pagination** | [**Pagination**](Pagination.md)|  | [optional] 

### Return type

[**CollectionsListPost200Response**](CollectionsListPost200Response.md)

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

# **collections_memberships_post**
> CollectionsMembershipsPost200Response collections_memberships_post(collections_memberships_post_request=collections_memberships_post_request)

List all collection memberships

This method allows you to list a collections individual memberships. It's important to note that memberships returned from this endpoint do not include group memberships.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_memberships_post200_response import CollectionsMembershipsPost200Response
from outline_openapi.models.collections_memberships_post_request import CollectionsMembershipsPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_memberships_post_request = outline_openapi.CollectionsMembershipsPostRequest() # CollectionsMembershipsPostRequest |  (optional)

    try:
        # List all collection memberships
        api_response = await api_instance.collections_memberships_post(collections_memberships_post_request=collections_memberships_post_request)
        print("The response of CollectionsApi->collections_memberships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_memberships_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_memberships_post_request** | [**CollectionsMembershipsPostRequest**](CollectionsMembershipsPostRequest.md)|  | [optional] 

### Return type

[**CollectionsMembershipsPost200Response**](CollectionsMembershipsPost200Response.md)

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

# **collections_remove_group_post**
> AttachmentsDeletePost200Response collections_remove_group_post(collections_remove_group_post_request=collections_remove_group_post_request)

Remove a collection group

This method allows you to revoke all members in a group access to a collection. Note that members of the group may still retain access through other groups or individual memberships.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_remove_group_post_request import CollectionsRemoveGroupPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_remove_group_post_request = outline_openapi.CollectionsRemoveGroupPostRequest() # CollectionsRemoveGroupPostRequest |  (optional)

    try:
        # Remove a collection group
        api_response = await api_instance.collections_remove_group_post(collections_remove_group_post_request=collections_remove_group_post_request)
        print("The response of CollectionsApi->collections_remove_group_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_remove_group_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_remove_group_post_request** | [**CollectionsRemoveGroupPostRequest**](CollectionsRemoveGroupPostRequest.md)|  | [optional] 

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

# **collections_remove_user_post**
> AttachmentsDeletePost200Response collections_remove_user_post(collections_remove_user_post_request=collections_remove_user_post_request)

Remove a collection user

This method allows you to remove a user from the specified collection.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.collections_remove_user_post_request import CollectionsRemoveUserPostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_remove_user_post_request = outline_openapi.CollectionsRemoveUserPostRequest() # CollectionsRemoveUserPostRequest |  (optional)

    try:
        # Remove a collection user
        api_response = await api_instance.collections_remove_user_post(collections_remove_user_post_request=collections_remove_user_post_request)
        print("The response of CollectionsApi->collections_remove_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_remove_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_remove_user_post_request** | [**CollectionsRemoveUserPostRequest**](CollectionsRemoveUserPostRequest.md)|  | [optional] 

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

# **collections_update_post**
> CollectionsCreatePost200Response collections_update_post(collections_update_post_request=collections_update_post_request)

Update a collection

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_create_post200_response import CollectionsCreatePost200Response
from outline_openapi.models.collections_update_post_request import CollectionsUpdatePostRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_update_post_request = outline_openapi.CollectionsUpdatePostRequest() # CollectionsUpdatePostRequest |  (optional)

    try:
        # Update a collection
        api_response = await api_instance.collections_update_post(collections_update_post_request=collections_update_post_request)
        print("The response of CollectionsApi->collections_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_update_post_request** | [**CollectionsUpdatePostRequest**](CollectionsUpdatePostRequest.md)|  | [optional] 

### Return type

[**CollectionsCreatePost200Response**](CollectionsCreatePost200Response.md)

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

