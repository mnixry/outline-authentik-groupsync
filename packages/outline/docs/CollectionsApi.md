# outline_openapi.CollectionsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**collections_add_group**](CollectionsApi.md#collections_add_group) | **POST** /collections.add_group | Add a group to a collection
[**collections_add_user**](CollectionsApi.md#collections_add_user) | **POST** /collections.add_user | Add a collection user
[**collections_create**](CollectionsApi.md#collections_create) | **POST** /collections.create | Create a collection
[**collections_delete**](CollectionsApi.md#collections_delete) | **POST** /collections.delete | Delete a collection
[**collections_documents**](CollectionsApi.md#collections_documents) | **POST** /collections.documents | Retrieve a collections document structure
[**collections_export**](CollectionsApi.md#collections_export) | **POST** /collections.export | Export a collection
[**collections_export_all**](CollectionsApi.md#collections_export_all) | **POST** /collections.export_all | Export all collections
[**collections_group_memberships**](CollectionsApi.md#collections_group_memberships) | **POST** /collections.group_memberships | List all collection group members
[**collections_info**](CollectionsApi.md#collections_info) | **POST** /collections.info | Retrieve a collection
[**collections_list**](CollectionsApi.md#collections_list) | **POST** /collections.list | List all collections
[**collections_memberships**](CollectionsApi.md#collections_memberships) | **POST** /collections.memberships | List all collection memberships
[**collections_remove_group**](CollectionsApi.md#collections_remove_group) | **POST** /collections.remove_group | Remove a collection group
[**collections_remove_user**](CollectionsApi.md#collections_remove_user) | **POST** /collections.remove_user | Remove a collection user
[**collections_update**](CollectionsApi.md#collections_update) | **POST** /collections.update | Update a collection


# **collections_add_group**
> CollectionsAddGroup200Response collections_add_group(collections_add_group_request=collections_add_group_request)

Add a group to a collection

This method allows you to give all members in a group access to a collection.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_add_group200_response import CollectionsAddGroup200Response
from outline_openapi.models.collections_add_group_request import CollectionsAddGroupRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_add_group_request = outline_openapi.CollectionsAddGroupRequest() # CollectionsAddGroupRequest |  (optional)

    try:
        # Add a group to a collection
        api_response = await api_instance.collections_add_group(collections_add_group_request=collections_add_group_request)
        print("The response of CollectionsApi->collections_add_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_add_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_add_group_request** | [**CollectionsAddGroupRequest**](CollectionsAddGroupRequest.md)|  | [optional] 

### Return type

[**CollectionsAddGroup200Response**](CollectionsAddGroup200Response.md)

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

# **collections_add_user**
> CollectionsAddUser200Response collections_add_user(collections_add_user_request=collections_add_user_request)

Add a collection user

This method allows you to add a user membership to the specified collection.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_add_user200_response import CollectionsAddUser200Response
from outline_openapi.models.collections_add_user_request import CollectionsAddUserRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_add_user_request = outline_openapi.CollectionsAddUserRequest() # CollectionsAddUserRequest |  (optional)

    try:
        # Add a collection user
        api_response = await api_instance.collections_add_user(collections_add_user_request=collections_add_user_request)
        print("The response of CollectionsApi->collections_add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_add_user_request** | [**CollectionsAddUserRequest**](CollectionsAddUserRequest.md)|  | [optional] 

### Return type

[**CollectionsAddUser200Response**](CollectionsAddUser200Response.md)

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

# **collections_create**
> CollectionsInfo200Response collections_create(collections_create_request=collections_create_request)

Create a collection

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_create_request import CollectionsCreateRequest
from outline_openapi.models.collections_info200_response import CollectionsInfo200Response
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_create_request = outline_openapi.CollectionsCreateRequest() # CollectionsCreateRequest |  (optional)

    try:
        # Create a collection
        api_response = await api_instance.collections_create(collections_create_request=collections_create_request)
        print("The response of CollectionsApi->collections_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_create_request** | [**CollectionsCreateRequest**](CollectionsCreateRequest.md)|  | [optional] 

### Return type

[**CollectionsInfo200Response**](CollectionsInfo200Response.md)

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

# **collections_delete**
> AttachmentsDelete200Response collections_delete(collections_delete_request=collections_delete_request)

Delete a collection

Delete a collection and all of its documents. This action can’t be undone so please be careful.

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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_delete_request = outline_openapi.CollectionsDeleteRequest() # CollectionsDeleteRequest |  (optional)

    try:
        # Delete a collection
        api_response = await api_instance.collections_delete(collections_delete_request=collections_delete_request)
        print("The response of CollectionsApi->collections_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_delete: %s\n" % e)
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

# **collections_documents**
> CollectionsDocuments200Response collections_documents(collections_info_request=collections_info_request)

Retrieve a collections document structure

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_documents200_response import CollectionsDocuments200Response
from outline_openapi.models.collections_info_request import CollectionsInfoRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_info_request = outline_openapi.CollectionsInfoRequest() # CollectionsInfoRequest |  (optional)

    try:
        # Retrieve a collections document structure
        api_response = await api_instance.collections_documents(collections_info_request=collections_info_request)
        print("The response of CollectionsApi->collections_documents:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_documents: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_info_request** | [**CollectionsInfoRequest**](CollectionsInfoRequest.md)|  | [optional] 

### Return type

[**CollectionsDocuments200Response**](CollectionsDocuments200Response.md)

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

# **collections_export**
> CollectionsExport200Response collections_export(collections_export_request=collections_export_request)

Export a collection

Triggers a bulk export of the collection in markdown format and their attachments. If documents are nested then they will be nested in folders inside the zip file. The endpoint returns a `FileOperation` that can be queried to track the progress of the export and get the url for the final file.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_export200_response import CollectionsExport200Response
from outline_openapi.models.collections_export_request import CollectionsExportRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_export_request = outline_openapi.CollectionsExportRequest() # CollectionsExportRequest |  (optional)

    try:
        # Export a collection
        api_response = await api_instance.collections_export(collections_export_request=collections_export_request)
        print("The response of CollectionsApi->collections_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_export_request** | [**CollectionsExportRequest**](CollectionsExportRequest.md)|  | [optional] 

### Return type

[**CollectionsExport200Response**](CollectionsExport200Response.md)

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

# **collections_export_all**
> CollectionsExport200Response collections_export_all(collections_export_all_request=collections_export_all_request)

Export all collections

Triggers a bulk export of all documents in and their attachments. The endpoint returns a `FileOperation` that can be queried through the fileOperations endpoint to track the progress of the export and get the url for the final file.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_export200_response import CollectionsExport200Response
from outline_openapi.models.collections_export_all_request import CollectionsExportAllRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_export_all_request = outline_openapi.CollectionsExportAllRequest() # CollectionsExportAllRequest |  (optional)

    try:
        # Export all collections
        api_response = await api_instance.collections_export_all(collections_export_all_request=collections_export_all_request)
        print("The response of CollectionsApi->collections_export_all:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_export_all: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_export_all_request** | [**CollectionsExportAllRequest**](CollectionsExportAllRequest.md)|  | [optional] 

### Return type

[**CollectionsExport200Response**](CollectionsExport200Response.md)

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

# **collections_group_memberships**
> CollectionsGroupMemberships200Response collections_group_memberships(collections_group_memberships_request=collections_group_memberships_request)

List all collection group members

This method allows you to list a collections group memberships. This is the list of groups that have been given access to the collection.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_group_memberships200_response import CollectionsGroupMemberships200Response
from outline_openapi.models.collections_group_memberships_request import CollectionsGroupMembershipsRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_group_memberships_request = outline_openapi.CollectionsGroupMembershipsRequest() # CollectionsGroupMembershipsRequest |  (optional)

    try:
        # List all collection group members
        api_response = await api_instance.collections_group_memberships(collections_group_memberships_request=collections_group_memberships_request)
        print("The response of CollectionsApi->collections_group_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_group_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_group_memberships_request** | [**CollectionsGroupMembershipsRequest**](CollectionsGroupMembershipsRequest.md)|  | [optional] 

### Return type

[**CollectionsGroupMemberships200Response**](CollectionsGroupMemberships200Response.md)

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

# **collections_info**
> CollectionsInfo200Response collections_info(collections_info_request=collections_info_request)

Retrieve a collection

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_info200_response import CollectionsInfo200Response
from outline_openapi.models.collections_info_request import CollectionsInfoRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_info_request = outline_openapi.CollectionsInfoRequest() # CollectionsInfoRequest |  (optional)

    try:
        # Retrieve a collection
        api_response = await api_instance.collections_info(collections_info_request=collections_info_request)
        print("The response of CollectionsApi->collections_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_info_request** | [**CollectionsInfoRequest**](CollectionsInfoRequest.md)|  | [optional] 

### Return type

[**CollectionsInfo200Response**](CollectionsInfo200Response.md)

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

# **collections_list**
> CollectionsList200Response collections_list(collections_list_request=collections_list_request)

List all collections

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_list200_response import CollectionsList200Response
from outline_openapi.models.collections_list_request import CollectionsListRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_list_request = outline_openapi.CollectionsListRequest() # CollectionsListRequest |  (optional)

    try:
        # List all collections
        api_response = await api_instance.collections_list(collections_list_request=collections_list_request)
        print("The response of CollectionsApi->collections_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_list_request** | [**CollectionsListRequest**](CollectionsListRequest.md)|  | [optional] 

### Return type

[**CollectionsList200Response**](CollectionsList200Response.md)

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

# **collections_memberships**
> CollectionsMemberships200Response collections_memberships(collections_memberships_request=collections_memberships_request)

List all collection memberships

This method allows you to list a collections individual memberships. It's important to note that memberships returned from this endpoint do not include group memberships.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_memberships200_response import CollectionsMemberships200Response
from outline_openapi.models.collections_memberships_request import CollectionsMembershipsRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_memberships_request = outline_openapi.CollectionsMembershipsRequest() # CollectionsMembershipsRequest |  (optional)

    try:
        # List all collection memberships
        api_response = await api_instance.collections_memberships(collections_memberships_request=collections_memberships_request)
        print("The response of CollectionsApi->collections_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_memberships_request** | [**CollectionsMembershipsRequest**](CollectionsMembershipsRequest.md)|  | [optional] 

### Return type

[**CollectionsMemberships200Response**](CollectionsMemberships200Response.md)

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

# **collections_remove_group**
> AttachmentsDelete200Response collections_remove_group(collections_remove_group_request=collections_remove_group_request)

Remove a collection group

This method allows you to revoke all members in a group access to a collection. Note that members of the group may still retain access through other groups or individual memberships.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.collections_remove_group_request import CollectionsRemoveGroupRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_remove_group_request = outline_openapi.CollectionsRemoveGroupRequest() # CollectionsRemoveGroupRequest |  (optional)

    try:
        # Remove a collection group
        api_response = await api_instance.collections_remove_group(collections_remove_group_request=collections_remove_group_request)
        print("The response of CollectionsApi->collections_remove_group:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_remove_group: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_remove_group_request** | [**CollectionsRemoveGroupRequest**](CollectionsRemoveGroupRequest.md)|  | [optional] 

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

# **collections_remove_user**
> AttachmentsDelete200Response collections_remove_user(collections_remove_user_request=collections_remove_user_request)

Remove a collection user

This method allows you to remove a user from the specified collection.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.collections_remove_user_request import CollectionsRemoveUserRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_remove_user_request = outline_openapi.CollectionsRemoveUserRequest() # CollectionsRemoveUserRequest |  (optional)

    try:
        # Remove a collection user
        api_response = await api_instance.collections_remove_user(collections_remove_user_request=collections_remove_user_request)
        print("The response of CollectionsApi->collections_remove_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_remove_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_remove_user_request** | [**CollectionsRemoveUserRequest**](CollectionsRemoveUserRequest.md)|  | [optional] 

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

# **collections_update**
> CollectionsInfo200Response collections_update(collections_update_request=collections_update_request)

Update a collection

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_info200_response import CollectionsInfo200Response
from outline_openapi.models.collections_update_request import CollectionsUpdateRequest
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
    api_instance = outline_openapi.CollectionsApi(api_client)
    collections_update_request = outline_openapi.CollectionsUpdateRequest() # CollectionsUpdateRequest |  (optional)

    try:
        # Update a collection
        api_response = await api_instance.collections_update(collections_update_request=collections_update_request)
        print("The response of CollectionsApi->collections_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CollectionsApi->collections_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_update_request** | [**CollectionsUpdateRequest**](CollectionsUpdateRequest.md)|  | [optional] 

### Return type

[**CollectionsInfo200Response**](CollectionsInfo200Response.md)

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

