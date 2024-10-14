# outline_openapi.GroupsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_add_user_post**](GroupsApi.md#groups_add_user_post) | **POST** /groups.add_user | Add a group member
[**groups_create_post**](GroupsApi.md#groups_create_post) | **POST** /groups.create | Create a group
[**groups_delete_post**](GroupsApi.md#groups_delete_post) | **POST** /groups.delete | Delete a group
[**groups_info_post**](GroupsApi.md#groups_info_post) | **POST** /groups.info | Retrieve a group
[**groups_list_post**](GroupsApi.md#groups_list_post) | **POST** /groups.list | List all groups
[**groups_memberships_post**](GroupsApi.md#groups_memberships_post) | **POST** /groups.memberships | List all group members
[**groups_remove_user_post**](GroupsApi.md#groups_remove_user_post) | **POST** /groups.remove_user | Remove a group member
[**groups_update_post**](GroupsApi.md#groups_update_post) | **POST** /groups.update | Update a group


# **groups_add_user_post**
> GroupsAddUserPost200Response groups_add_user_post(groups_add_user_post_request=groups_add_user_post_request)

Add a group member

This method allows you to add a user to the specified group.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.groups_add_user_post200_response import GroupsAddUserPost200Response
from outline_openapi.models.groups_add_user_post_request import GroupsAddUserPostRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_add_user_post_request = outline_openapi.GroupsAddUserPostRequest() # GroupsAddUserPostRequest |  (optional)

    try:
        # Add a group member
        api_response = await api_instance.groups_add_user_post(groups_add_user_post_request=groups_add_user_post_request)
        print("The response of GroupsApi->groups_add_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_add_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_add_user_post_request** | [**GroupsAddUserPostRequest**](GroupsAddUserPostRequest.md)|  | [optional] 

### Return type

[**GroupsAddUserPost200Response**](GroupsAddUserPost200Response.md)

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

# **groups_create_post**
> GroupsCreatePost200Response groups_create_post(groups_create_post_request=groups_create_post_request)

Create a group

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.groups_create_post200_response import GroupsCreatePost200Response
from outline_openapi.models.groups_create_post_request import GroupsCreatePostRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_create_post_request = outline_openapi.GroupsCreatePostRequest() # GroupsCreatePostRequest |  (optional)

    try:
        # Create a group
        api_response = await api_instance.groups_create_post(groups_create_post_request=groups_create_post_request)
        print("The response of GroupsApi->groups_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_create_post_request** | [**GroupsCreatePostRequest**](GroupsCreatePostRequest.md)|  | [optional] 

### Return type

[**GroupsCreatePost200Response**](GroupsCreatePost200Response.md)

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

# **groups_delete_post**
> AttachmentsDeletePost200Response groups_delete_post(collections_delete_post_request=collections_delete_post_request)

Delete a group

Deleting a group will cause all of its members to lose access to any collections the group has previously been added to. This action can’t be undone so please be careful.

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
    api_instance = outline_openapi.GroupsApi(api_client)
    collections_delete_post_request = outline_openapi.CollectionsDeletePostRequest() # CollectionsDeletePostRequest |  (optional)

    try:
        # Delete a group
        api_response = await api_instance.groups_delete_post(collections_delete_post_request=collections_delete_post_request)
        print("The response of GroupsApi->groups_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_delete_post: %s\n" % e)
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

# **groups_info_post**
> GroupsInfoPost200Response groups_info_post(groups_info_post_request=groups_info_post_request)

Retrieve a group

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.groups_info_post200_response import GroupsInfoPost200Response
from outline_openapi.models.groups_info_post_request import GroupsInfoPostRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_info_post_request = outline_openapi.GroupsInfoPostRequest() # GroupsInfoPostRequest |  (optional)

    try:
        # Retrieve a group
        api_response = await api_instance.groups_info_post(groups_info_post_request=groups_info_post_request)
        print("The response of GroupsApi->groups_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_info_post_request** | [**GroupsInfoPostRequest**](GroupsInfoPostRequest.md)|  | [optional] 

### Return type

[**GroupsInfoPost200Response**](GroupsInfoPost200Response.md)

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

# **groups_list_post**
> GroupsListPost200Response groups_list_post(documents_viewed_post_request=documents_viewed_post_request)

List all groups

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
from outline_openapi.models.groups_list_post200_response import GroupsListPost200Response
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
    api_instance = outline_openapi.GroupsApi(api_client)
    documents_viewed_post_request = outline_openapi.DocumentsViewedPostRequest() # DocumentsViewedPostRequest |  (optional)

    try:
        # List all groups
        api_response = await api_instance.groups_list_post(documents_viewed_post_request=documents_viewed_post_request)
        print("The response of GroupsApi->groups_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_viewed_post_request** | [**DocumentsViewedPostRequest**](DocumentsViewedPostRequest.md)|  | [optional] 

### Return type

[**GroupsListPost200Response**](GroupsListPost200Response.md)

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

# **groups_memberships_post**
> GroupsMembershipsPost200Response groups_memberships_post(groups_memberships_post_request=groups_memberships_post_request)

List all group members

List and filter all the members in a group.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.groups_memberships_post200_response import GroupsMembershipsPost200Response
from outline_openapi.models.groups_memberships_post_request import GroupsMembershipsPostRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_memberships_post_request = outline_openapi.GroupsMembershipsPostRequest() # GroupsMembershipsPostRequest |  (optional)

    try:
        # List all group members
        api_response = await api_instance.groups_memberships_post(groups_memberships_post_request=groups_memberships_post_request)
        print("The response of GroupsApi->groups_memberships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_memberships_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_memberships_post_request** | [**GroupsMembershipsPostRequest**](GroupsMembershipsPostRequest.md)|  | [optional] 

### Return type

[**GroupsMembershipsPost200Response**](GroupsMembershipsPost200Response.md)

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

# **groups_remove_user_post**
> GroupsRemoveUserPost200Response groups_remove_user_post(collections_remove_user_post_request=collections_remove_user_post_request)

Remove a group member

This method allows you to remove a user from the group.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_remove_user_post_request import CollectionsRemoveUserPostRequest
from outline_openapi.models.groups_remove_user_post200_response import GroupsRemoveUserPost200Response
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
    api_instance = outline_openapi.GroupsApi(api_client)
    collections_remove_user_post_request = outline_openapi.CollectionsRemoveUserPostRequest() # CollectionsRemoveUserPostRequest |  (optional)

    try:
        # Remove a group member
        api_response = await api_instance.groups_remove_user_post(collections_remove_user_post_request=collections_remove_user_post_request)
        print("The response of GroupsApi->groups_remove_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_remove_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_remove_user_post_request** | [**CollectionsRemoveUserPostRequest**](CollectionsRemoveUserPostRequest.md)|  | [optional] 

### Return type

[**GroupsRemoveUserPost200Response**](GroupsRemoveUserPost200Response.md)

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

# **groups_update_post**
> GroupsCreatePost200Response groups_update_post(groups_update_post_request=groups_update_post_request)

Update a group

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.groups_create_post200_response import GroupsCreatePost200Response
from outline_openapi.models.groups_update_post_request import GroupsUpdatePostRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_update_post_request = outline_openapi.GroupsUpdatePostRequest() # GroupsUpdatePostRequest |  (optional)

    try:
        # Update a group
        api_response = await api_instance.groups_update_post(groups_update_post_request=groups_update_post_request)
        print("The response of GroupsApi->groups_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_update_post_request** | [**GroupsUpdatePostRequest**](GroupsUpdatePostRequest.md)|  | [optional] 

### Return type

[**GroupsCreatePost200Response**](GroupsCreatePost200Response.md)

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

