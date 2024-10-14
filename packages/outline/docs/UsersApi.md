# outline_openapi.UsersApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**users_activate_post**](UsersApi.md#users_activate_post) | **POST** /users.activate | Activate a user
[**users_delete_post**](UsersApi.md#users_delete_post) | **POST** /users.delete | Delete a user
[**users_info_post**](UsersApi.md#users_info_post) | **POST** /users.info | Retrieve a user
[**users_invite_post**](UsersApi.md#users_invite_post) | **POST** /users.invite | Invite users
[**users_list_post**](UsersApi.md#users_list_post) | **POST** /users.list | List all users
[**users_suspend_post**](UsersApi.md#users_suspend_post) | **POST** /users.suspend | Suspend a user
[**users_update_post**](UsersApi.md#users_update_post) | **POST** /users.update | Update a user
[**users_update_role_post**](UsersApi.md#users_update_role_post) | **POST** /users.update_role | Change a users role


# **users_activate_post**
> UsersInfoPost200Response users_activate_post(users_info_post_request=users_info_post_request)

Activate a user

Activating a previously suspended user allows them to signin again. Users that are activated will cause billing totals to be re-calculated in the hosted version.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_info_post_request = outline_openapi.UsersInfoPostRequest() # UsersInfoPostRequest |  (optional)

    try:
        # Activate a user
        api_response = await api_instance.users_activate_post(users_info_post_request=users_info_post_request)
        print("The response of UsersApi->users_activate_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_activate_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_info_post_request** | [**UsersInfoPostRequest**](UsersInfoPostRequest.md)|  | [optional] 

### Return type

[**UsersInfoPost200Response**](UsersInfoPost200Response.md)

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

# **users_delete_post**
> AttachmentsDeletePost200Response users_delete_post(users_info_post_request=users_info_post_request)

Delete a user

Deleting a user removes the object entirely. In almost every circumstance it is preferable to suspend a user, as a deleted user can be recreated by signing in with SSO again.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_info_post_request = outline_openapi.UsersInfoPostRequest() # UsersInfoPostRequest |  (optional)

    try:
        # Delete a user
        api_response = await api_instance.users_delete_post(users_info_post_request=users_info_post_request)
        print("The response of UsersApi->users_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_info_post_request** | [**UsersInfoPostRequest**](UsersInfoPostRequest.md)|  | [optional] 

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

# **users_info_post**
> UsersInfoPost200Response users_info_post(users_info_post_request=users_info_post_request)

Retrieve a user

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_info_post_request = outline_openapi.UsersInfoPostRequest() # UsersInfoPostRequest |  (optional)

    try:
        # Retrieve a user
        api_response = await api_instance.users_info_post(users_info_post_request=users_info_post_request)
        print("The response of UsersApi->users_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_info_post_request** | [**UsersInfoPostRequest**](UsersInfoPostRequest.md)|  | [optional] 

### Return type

[**UsersInfoPost200Response**](UsersInfoPost200Response.md)

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

# **users_invite_post**
> UsersInvitePost200Response users_invite_post(users_invite_post_request=users_invite_post_request)

Invite users

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.users_invite_post200_response import UsersInvitePost200Response
from outline_openapi.models.users_invite_post_request import UsersInvitePostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_invite_post_request = outline_openapi.UsersInvitePostRequest() # UsersInvitePostRequest |  (optional)

    try:
        # Invite users
        api_response = await api_instance.users_invite_post(users_invite_post_request=users_invite_post_request)
        print("The response of UsersApi->users_invite_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_invite_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_invite_post_request** | [**UsersInvitePostRequest**](UsersInvitePostRequest.md)|  | [optional] 

### Return type

[**UsersInvitePost200Response**](UsersInvitePost200Response.md)

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

# **users_list_post**
> UsersListPost200Response users_list_post(users_list_post_request=users_list_post_request)

List all users

List and filter all the users in the team

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.users_list_post200_response import UsersListPost200Response
from outline_openapi.models.users_list_post_request import UsersListPostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_list_post_request = outline_openapi.UsersListPostRequest() # UsersListPostRequest |  (optional)

    try:
        # List all users
        api_response = await api_instance.users_list_post(users_list_post_request=users_list_post_request)
        print("The response of UsersApi->users_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_list_post_request** | [**UsersListPostRequest**](UsersListPostRequest.md)|  | [optional] 

### Return type

[**UsersListPost200Response**](UsersListPost200Response.md)

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

# **users_suspend_post**
> UsersInfoPost200Response users_suspend_post(users_info_post_request=users_info_post_request)

Suspend a user

Suspending a user prevents the user from signing in. Users that are suspended are also not counted against billing totals in the hosted version.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_info_post_request import UsersInfoPostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_info_post_request = outline_openapi.UsersInfoPostRequest() # UsersInfoPostRequest |  (optional)

    try:
        # Suspend a user
        api_response = await api_instance.users_suspend_post(users_info_post_request=users_info_post_request)
        print("The response of UsersApi->users_suspend_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_suspend_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_info_post_request** | [**UsersInfoPostRequest**](UsersInfoPostRequest.md)|  | [optional] 

### Return type

[**UsersInfoPost200Response**](UsersInfoPost200Response.md)

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

# **users_update_post**
> UsersInfoPost200Response users_update_post(users_update_post_request=users_update_post_request)

Update a user

Update a users name or avatar. If no `id` is passed then the user associated with the authentication will be updated by default.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_update_post_request import UsersUpdatePostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_update_post_request = outline_openapi.UsersUpdatePostRequest() # UsersUpdatePostRequest |  (optional)

    try:
        # Update a user
        api_response = await api_instance.users_update_post(users_update_post_request=users_update_post_request)
        print("The response of UsersApi->users_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_update_post_request** | [**UsersUpdatePostRequest**](UsersUpdatePostRequest.md)|  | [optional] 

### Return type

[**UsersInfoPost200Response**](UsersInfoPost200Response.md)

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

# **users_update_role_post**
> UsersInfoPost200Response users_update_role_post(users_update_role_post_request=users_update_role_post_request)

Change a users role

Change the role of a user, only available to admin authorization.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.users_info_post200_response import UsersInfoPost200Response
from outline_openapi.models.users_update_role_post_request import UsersUpdateRolePostRequest
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
    api_instance = outline_openapi.UsersApi(api_client)
    users_update_role_post_request = outline_openapi.UsersUpdateRolePostRequest() # UsersUpdateRolePostRequest |  (optional)

    try:
        # Change a users role
        api_response = await api_instance.users_update_role_post(users_update_role_post_request=users_update_role_post_request)
        print("The response of UsersApi->users_update_role_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsersApi->users_update_role_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **users_update_role_post_request** | [**UsersUpdateRolePostRequest**](UsersUpdateRolePostRequest.md)|  | [optional] 

### Return type

[**UsersInfoPost200Response**](UsersInfoPost200Response.md)

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

