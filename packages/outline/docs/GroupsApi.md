# outline_openapi.GroupsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**groups_add_user**](GroupsApi.md#groups_add_user) | **POST** /groups.add_user | Add a group member
[**groups_create**](GroupsApi.md#groups_create) | **POST** /groups.create | Create a group
[**groups_delete**](GroupsApi.md#groups_delete) | **POST** /groups.delete | Delete a group
[**groups_info**](GroupsApi.md#groups_info) | **POST** /groups.info | Retrieve a group
[**groups_list**](GroupsApi.md#groups_list) | **POST** /groups.list | List all groups
[**groups_memberships**](GroupsApi.md#groups_memberships) | **POST** /groups.memberships | List all group members
[**groups_remove_user**](GroupsApi.md#groups_remove_user) | **POST** /groups.remove_user | Remove a group member
[**groups_update**](GroupsApi.md#groups_update) | **POST** /groups.update | Update a group


# **groups_add_user**
> GroupsAddUser200Response groups_add_user(groups_add_user_request=groups_add_user_request)

Add a group member

This method allows you to add a user to the specified group.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.groups_add_user200_response import GroupsAddUser200Response
from outline_openapi.models.groups_add_user_request import GroupsAddUserRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_add_user_request = outline_openapi.GroupsAddUserRequest() # GroupsAddUserRequest |  (optional)

    try:
        # Add a group member
        api_response = await api_instance.groups_add_user(groups_add_user_request=groups_add_user_request)
        print("The response of GroupsApi->groups_add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_add_user_request** | [**GroupsAddUserRequest**](GroupsAddUserRequest.md)|  | [optional] 

### Return type

[**GroupsAddUser200Response**](GroupsAddUser200Response.md)

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

# **groups_create**
> GroupsInfo200Response groups_create(groups_create_request=groups_create_request)

Create a group

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.groups_create_request import GroupsCreateRequest
from outline_openapi.models.groups_info200_response import GroupsInfo200Response
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_create_request = outline_openapi.GroupsCreateRequest() # GroupsCreateRequest |  (optional)

    try:
        # Create a group
        api_response = await api_instance.groups_create(groups_create_request=groups_create_request)
        print("The response of GroupsApi->groups_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_create_request** | [**GroupsCreateRequest**](GroupsCreateRequest.md)|  | [optional] 

### Return type

[**GroupsInfo200Response**](GroupsInfo200Response.md)

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

# **groups_delete**
> AttachmentsDelete200Response groups_delete(collections_delete_request=collections_delete_request)

Delete a group

Deleting a group will cause all of its members to lose access to any collections the group has previously been added to. This action can’t be undone so please be careful.

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
    api_instance = outline_openapi.GroupsApi(api_client)
    collections_delete_request = outline_openapi.CollectionsDeleteRequest() # CollectionsDeleteRequest |  (optional)

    try:
        # Delete a group
        api_response = await api_instance.groups_delete(collections_delete_request=collections_delete_request)
        print("The response of GroupsApi->groups_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_delete: %s\n" % e)
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

# **groups_info**
> GroupsInfo200Response groups_info(groups_info_request=groups_info_request)

Retrieve a group

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.groups_info200_response import GroupsInfo200Response
from outline_openapi.models.groups_info_request import GroupsInfoRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_info_request = outline_openapi.GroupsInfoRequest() # GroupsInfoRequest |  (optional)

    try:
        # Retrieve a group
        api_response = await api_instance.groups_info(groups_info_request=groups_info_request)
        print("The response of GroupsApi->groups_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_info_request** | [**GroupsInfoRequest**](GroupsInfoRequest.md)|  | [optional] 

### Return type

[**GroupsInfo200Response**](GroupsInfo200Response.md)

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

# **groups_list**
> GroupsList200Response groups_list(groups_list_request=groups_list_request)

List all groups

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.groups_list200_response import GroupsList200Response
from outline_openapi.models.groups_list_request import GroupsListRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_list_request = outline_openapi.GroupsListRequest() # GroupsListRequest |  (optional)

    try:
        # List all groups
        api_response = await api_instance.groups_list(groups_list_request=groups_list_request)
        print("The response of GroupsApi->groups_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_list_request** | [**GroupsListRequest**](GroupsListRequest.md)|  | [optional] 

### Return type

[**GroupsList200Response**](GroupsList200Response.md)

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

# **groups_memberships**
> GroupsMemberships200Response groups_memberships(groups_memberships_request=groups_memberships_request)

List all group members

List and filter all the members in a group.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.groups_memberships200_response import GroupsMemberships200Response
from outline_openapi.models.groups_memberships_request import GroupsMembershipsRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_memberships_request = outline_openapi.GroupsMembershipsRequest() # GroupsMembershipsRequest |  (optional)

    try:
        # List all group members
        api_response = await api_instance.groups_memberships(groups_memberships_request=groups_memberships_request)
        print("The response of GroupsApi->groups_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_memberships_request** | [**GroupsMembershipsRequest**](GroupsMembershipsRequest.md)|  | [optional] 

### Return type

[**GroupsMemberships200Response**](GroupsMemberships200Response.md)

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

# **groups_remove_user**
> GroupsRemoveUser200Response groups_remove_user(collections_remove_user_request=collections_remove_user_request)

Remove a group member

This method allows you to remove a user from the group.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_remove_user_request import CollectionsRemoveUserRequest
from outline_openapi.models.groups_remove_user200_response import GroupsRemoveUser200Response
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
    api_instance = outline_openapi.GroupsApi(api_client)
    collections_remove_user_request = outline_openapi.CollectionsRemoveUserRequest() # CollectionsRemoveUserRequest |  (optional)

    try:
        # Remove a group member
        api_response = await api_instance.groups_remove_user(collections_remove_user_request=collections_remove_user_request)
        print("The response of GroupsApi->groups_remove_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_remove_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_remove_user_request** | [**CollectionsRemoveUserRequest**](CollectionsRemoveUserRequest.md)|  | [optional] 

### Return type

[**GroupsRemoveUser200Response**](GroupsRemoveUser200Response.md)

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

# **groups_update**
> GroupsInfo200Response groups_update(groups_update_request=groups_update_request)

Update a group

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.groups_info200_response import GroupsInfo200Response
from outline_openapi.models.groups_update_request import GroupsUpdateRequest
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
    api_instance = outline_openapi.GroupsApi(api_client)
    groups_update_request = outline_openapi.GroupsUpdateRequest() # GroupsUpdateRequest |  (optional)

    try:
        # Update a group
        api_response = await api_instance.groups_update(groups_update_request=groups_update_request)
        print("The response of GroupsApi->groups_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling GroupsApi->groups_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **groups_update_request** | [**GroupsUpdateRequest**](GroupsUpdateRequest.md)|  | [optional] 

### Return type

[**GroupsInfo200Response**](GroupsInfo200Response.md)

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

