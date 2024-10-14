# outline_openapi.DocumentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_add_user_post**](DocumentsApi.md#documents_add_user_post) | **POST** /documents.add_user | Add a document user
[**documents_answer_question_post**](DocumentsApi.md#documents_answer_question_post) | **POST** /documents.answerQuestion | Query documents with natural language
[**documents_archive_post**](DocumentsApi.md#documents_archive_post) | **POST** /documents.archive | Archive a document
[**documents_create_post**](DocumentsApi.md#documents_create_post) | **POST** /documents.create | Create a document
[**documents_delete_post**](DocumentsApi.md#documents_delete_post) | **POST** /documents.delete | Delete a document
[**documents_drafts_post**](DocumentsApi.md#documents_drafts_post) | **POST** /documents.drafts | List all draft documents
[**documents_export_post**](DocumentsApi.md#documents_export_post) | **POST** /documents.export | Export a document as markdown
[**documents_import_post**](DocumentsApi.md#documents_import_post) | **POST** /documents.import | Import a file as a document
[**documents_info_post**](DocumentsApi.md#documents_info_post) | **POST** /documents.info | Retrieve a document
[**documents_list_post**](DocumentsApi.md#documents_list_post) | **POST** /documents.list | List all documents
[**documents_memberships_post**](DocumentsApi.md#documents_memberships_post) | **POST** /documents.memberships | List document memberships
[**documents_move_post**](DocumentsApi.md#documents_move_post) | **POST** /documents.move | Move a document
[**documents_remove_user_post**](DocumentsApi.md#documents_remove_user_post) | **POST** /documents.remove_user | Remove a document user
[**documents_restore_post**](DocumentsApi.md#documents_restore_post) | **POST** /documents.restore | Restore a document
[**documents_search_post**](DocumentsApi.md#documents_search_post) | **POST** /documents.search | Search all documents
[**documents_star_post**](DocumentsApi.md#documents_star_post) | **POST** /documents.star | Star a document
[**documents_templatize_post**](DocumentsApi.md#documents_templatize_post) | **POST** /documents.templatize | Create a template from a document
[**documents_unpublish_post**](DocumentsApi.md#documents_unpublish_post) | **POST** /documents.unpublish | Unpublish a document
[**documents_unstar_post**](DocumentsApi.md#documents_unstar_post) | **POST** /documents.unstar | Unstar a document
[**documents_update_post**](DocumentsApi.md#documents_update_post) | **POST** /documents.update | Update a document
[**documents_users_post**](DocumentsApi.md#documents_users_post) | **POST** /documents.users | List document users
[**documents_viewed_post**](DocumentsApi.md#documents_viewed_post) | **POST** /documents.viewed | List all recently viewed documents


# **documents_add_user_post**
> CollectionsAddUserPost200Response documents_add_user_post(documents_add_user_post_request=documents_add_user_post_request)

Add a document user

This method allows you to add a user membership to the specified document.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_add_user_post200_response import CollectionsAddUserPost200Response
from outline_openapi.models.documents_add_user_post_request import DocumentsAddUserPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_add_user_post_request = outline_openapi.DocumentsAddUserPostRequest() # DocumentsAddUserPostRequest |  (optional)

    try:
        # Add a document user
        api_response = await api_instance.documents_add_user_post(documents_add_user_post_request=documents_add_user_post_request)
        print("The response of DocumentsApi->documents_add_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_add_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_add_user_post_request** | [**DocumentsAddUserPostRequest**](DocumentsAddUserPostRequest.md)|  | [optional] 

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

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_answer_question_post**
> DocumentsAnswerQuestionPost200Response documents_answer_question_post(documents_answer_question_post_request=documents_answer_question_post_request)

Query documents with natural language

This method allows asking direct questions of your documents – where possible an answer will be provided. Search results will be restricted to those accessible by the current access token. Note that \"AI answers\" must be enabled for the workspace.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_answer_question_post200_response import DocumentsAnswerQuestionPost200Response
from outline_openapi.models.documents_answer_question_post_request import DocumentsAnswerQuestionPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_answer_question_post_request = outline_openapi.DocumentsAnswerQuestionPostRequest() # DocumentsAnswerQuestionPostRequest |  (optional)

    try:
        # Query documents with natural language
        api_response = await api_instance.documents_answer_question_post(documents_answer_question_post_request=documents_answer_question_post_request)
        print("The response of DocumentsApi->documents_answer_question_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_answer_question_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_answer_question_post_request** | [**DocumentsAnswerQuestionPostRequest**](DocumentsAnswerQuestionPostRequest.md)|  | [optional] 

### Return type

[**DocumentsAnswerQuestionPost200Response**](DocumentsAnswerQuestionPost200Response.md)

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

# **documents_archive_post**
> DocumentsCreatePost200Response documents_archive_post(documents_star_post_request=documents_star_post_request)

Archive a document

Archiving a document allows outdated information to be moved out of sight whilst retaining the ability to optionally search and restore it later.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response
from outline_openapi.models.documents_star_post_request import DocumentsStarPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_star_post_request = outline_openapi.DocumentsStarPostRequest() # DocumentsStarPostRequest |  (optional)

    try:
        # Archive a document
        api_response = await api_instance.documents_archive_post(documents_star_post_request=documents_star_post_request)
        print("The response of DocumentsApi->documents_archive_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_archive_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_star_post_request** | [**DocumentsStarPostRequest**](DocumentsStarPostRequest.md)|  | [optional] 

### Return type

[**DocumentsCreatePost200Response**](DocumentsCreatePost200Response.md)

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

# **documents_create_post**
> DocumentsCreatePost200Response documents_create_post(documents_create_post_request=documents_create_post_request)

Create a document

This method allows you to create or publish a new document. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response
from outline_openapi.models.documents_create_post_request import DocumentsCreatePostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_create_post_request = outline_openapi.DocumentsCreatePostRequest() # DocumentsCreatePostRequest |  (optional)

    try:
        # Create a document
        api_response = await api_instance.documents_create_post(documents_create_post_request=documents_create_post_request)
        print("The response of DocumentsApi->documents_create_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_create_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_create_post_request** | [**DocumentsCreatePostRequest**](DocumentsCreatePostRequest.md)|  | [optional] 

### Return type

[**DocumentsCreatePost200Response**](DocumentsCreatePost200Response.md)

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

# **documents_delete_post**
> AttachmentsDeletePost200Response documents_delete_post(documents_delete_post_request=documents_delete_post_request)

Delete a document

Deleting a document moves it to the trash. If not restored within 30 days it is permenantly deleted.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.documents_delete_post_request import DocumentsDeletePostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_delete_post_request = outline_openapi.DocumentsDeletePostRequest() # DocumentsDeletePostRequest |  (optional)

    try:
        # Delete a document
        api_response = await api_instance.documents_delete_post(documents_delete_post_request=documents_delete_post_request)
        print("The response of DocumentsApi->documents_delete_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_delete_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_delete_post_request** | [**DocumentsDeletePostRequest**](DocumentsDeletePostRequest.md)|  | [optional] 

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

# **documents_drafts_post**
> CommentsListPost200Response documents_drafts_post(documents_drafts_post_request=documents_drafts_post_request)

List all draft documents

This method will list all draft documents belonging to the current user.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.comments_list_post200_response import CommentsListPost200Response
from outline_openapi.models.documents_drafts_post_request import DocumentsDraftsPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_drafts_post_request = outline_openapi.DocumentsDraftsPostRequest() # DocumentsDraftsPostRequest |  (optional)

    try:
        # List all draft documents
        api_response = await api_instance.documents_drafts_post(documents_drafts_post_request=documents_drafts_post_request)
        print("The response of DocumentsApi->documents_drafts_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_drafts_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_drafts_post_request** | [**DocumentsDraftsPostRequest**](DocumentsDraftsPostRequest.md)|  | [optional] 

### Return type

[**CommentsListPost200Response**](CommentsListPost200Response.md)

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

# **documents_export_post**
> DocumentsExportPost200Response documents_export_post(documents_export_post_request=documents_export_post_request)

Export a document as markdown

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_export_post200_response import DocumentsExportPost200Response
from outline_openapi.models.documents_export_post_request import DocumentsExportPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_export_post_request = outline_openapi.DocumentsExportPostRequest() # DocumentsExportPostRequest |  (optional)

    try:
        # Export a document as markdown
        api_response = await api_instance.documents_export_post(documents_export_post_request=documents_export_post_request)
        print("The response of DocumentsApi->documents_export_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_export_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_export_post_request** | [**DocumentsExportPostRequest**](DocumentsExportPostRequest.md)|  | [optional] 

### Return type

[**DocumentsExportPost200Response**](DocumentsExportPost200Response.md)

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

# **documents_import_post**
> DocumentsInfoPost200Response documents_import_post(file=file, collection_id=collection_id, parent_document_id=parent_document_id, template=template, publish=publish)

Import a file as a document

This method allows you to create a new document by importing an existing file. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_info_post200_response import DocumentsInfoPost200Response
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    file = None # object | Only plain text, markdown, docx, and html format are supported. (optional)
    collection_id = 'collection_id_example' # str |  (optional)
    parent_document_id = 'parent_document_id_example' # str |  (optional)
    template = True # bool |  (optional)
    publish = True # bool |  (optional)

    try:
        # Import a file as a document
        api_response = await api_instance.documents_import_post(file=file, collection_id=collection_id, parent_document_id=parent_document_id, template=template, publish=publish)
        print("The response of DocumentsApi->documents_import_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_import_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**object**](object.md)| Only plain text, markdown, docx, and html format are supported. | [optional] 
 **collection_id** | **str**|  | [optional] 
 **parent_document_id** | **str**|  | [optional] 
 **template** | **bool**|  | [optional] 
 **publish** | **bool**|  | [optional] 

### Return type

[**DocumentsInfoPost200Response**](DocumentsInfoPost200Response.md)

### Authorization

[http](../README.md#http)

### HTTP request headers

 - **Content-Type**: multipart/form-data
 - **Accept**: application/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | OK |  -  |
**401** | The API key is missing or otherwise invalid. |  -  |
**403** | The current API key is not authorized to perform this action. |  -  |
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_info_post**
> DocumentsInfoPost200Response documents_info_post(documents_info_post_request=documents_info_post_request)

Retrieve a document

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_info_post200_response import DocumentsInfoPost200Response
from outline_openapi.models.documents_info_post_request import DocumentsInfoPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_info_post_request = outline_openapi.DocumentsInfoPostRequest() # DocumentsInfoPostRequest |  (optional)

    try:
        # Retrieve a document
        api_response = await api_instance.documents_info_post(documents_info_post_request=documents_info_post_request)
        print("The response of DocumentsApi->documents_info_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_info_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_info_post_request** | [**DocumentsInfoPostRequest**](DocumentsInfoPostRequest.md)|  | [optional] 

### Return type

[**DocumentsInfoPost200Response**](DocumentsInfoPost200Response.md)

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

# **documents_list_post**
> CommentsListPost200Response documents_list_post(documents_list_post_request=documents_list_post_request)

List all documents

This method will list all published documents and draft documents belonging to the current user.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.comments_list_post200_response import CommentsListPost200Response
from outline_openapi.models.documents_list_post_request import DocumentsListPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_list_post_request = outline_openapi.DocumentsListPostRequest() # DocumentsListPostRequest |  (optional)

    try:
        # List all documents
        api_response = await api_instance.documents_list_post(documents_list_post_request=documents_list_post_request)
        print("The response of DocumentsApi->documents_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_list_post_request** | [**DocumentsListPostRequest**](DocumentsListPostRequest.md)|  | [optional] 

### Return type

[**CommentsListPost200Response**](CommentsListPost200Response.md)

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

# **documents_memberships_post**
> CollectionsMembershipsPost200Response documents_memberships_post(documents_memberships_post_request=documents_memberships_post_request)

List document memberships

Users with direct membership to a document. To list all users with access to a document use `documents.users`.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_memberships_post200_response import CollectionsMembershipsPost200Response
from outline_openapi.models.documents_memberships_post_request import DocumentsMembershipsPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_memberships_post_request = outline_openapi.DocumentsMembershipsPostRequest() # DocumentsMembershipsPostRequest |  (optional)

    try:
        # List document memberships
        api_response = await api_instance.documents_memberships_post(documents_memberships_post_request=documents_memberships_post_request)
        print("The response of DocumentsApi->documents_memberships_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_memberships_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_memberships_post_request** | [**DocumentsMembershipsPostRequest**](DocumentsMembershipsPostRequest.md)|  | [optional] 

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
**404** | The specified resource was not found. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_move_post**
> DocumentsMovePost200Response documents_move_post(documents_move_post_request=documents_move_post_request)

Move a document

Move a document to a new location or collection. If no parent document is provided, the document will be moved to the collection root.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_move_post200_response import DocumentsMovePost200Response
from outline_openapi.models.documents_move_post_request import DocumentsMovePostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_move_post_request = outline_openapi.DocumentsMovePostRequest() # DocumentsMovePostRequest |  (optional)

    try:
        # Move a document
        api_response = await api_instance.documents_move_post(documents_move_post_request=documents_move_post_request)
        print("The response of DocumentsApi->documents_move_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_move_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_move_post_request** | [**DocumentsMovePostRequest**](DocumentsMovePostRequest.md)|  | [optional] 

### Return type

[**DocumentsMovePost200Response**](DocumentsMovePost200Response.md)

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

# **documents_remove_user_post**
> AttachmentsDeletePost200Response documents_remove_user_post(documents_remove_user_post_request=documents_remove_user_post_request)

Remove a document user

This method allows you to remove a user membership from the specified document.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.attachments_delete_post200_response import AttachmentsDeletePost200Response
from outline_openapi.models.documents_remove_user_post_request import DocumentsRemoveUserPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_remove_user_post_request = outline_openapi.DocumentsRemoveUserPostRequest() # DocumentsRemoveUserPostRequest |  (optional)

    try:
        # Remove a document user
        api_response = await api_instance.documents_remove_user_post(documents_remove_user_post_request=documents_remove_user_post_request)
        print("The response of DocumentsApi->documents_remove_user_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_remove_user_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_remove_user_post_request** | [**DocumentsRemoveUserPostRequest**](DocumentsRemoveUserPostRequest.md)|  | [optional] 

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

# **documents_restore_post**
> DocumentsCreatePost200Response documents_restore_post(documents_restore_post_request=documents_restore_post_request)

Restore a document

If a document has been archived or deleted, it can be restored. Optionally a revision can be passed to restore the document to a previous point in time.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response
from outline_openapi.models.documents_restore_post_request import DocumentsRestorePostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_restore_post_request = outline_openapi.DocumentsRestorePostRequest() # DocumentsRestorePostRequest |  (optional)

    try:
        # Restore a document
        api_response = await api_instance.documents_restore_post(documents_restore_post_request=documents_restore_post_request)
        print("The response of DocumentsApi->documents_restore_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_restore_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_restore_post_request** | [**DocumentsRestorePostRequest**](DocumentsRestorePostRequest.md)|  | [optional] 

### Return type

[**DocumentsCreatePost200Response**](DocumentsCreatePost200Response.md)

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

# **documents_search_post**
> DocumentsSearchPost200Response documents_search_post(documents_search_post_request=documents_search_post_request)

Search all documents

This methods allows you to search your teams documents with keywords. Note that search results will be restricted to those accessible by the current access token.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_search_post200_response import DocumentsSearchPost200Response
from outline_openapi.models.documents_search_post_request import DocumentsSearchPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_search_post_request = outline_openapi.DocumentsSearchPostRequest() # DocumentsSearchPostRequest |  (optional)

    try:
        # Search all documents
        api_response = await api_instance.documents_search_post(documents_search_post_request=documents_search_post_request)
        print("The response of DocumentsApi->documents_search_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_search_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_search_post_request** | [**DocumentsSearchPostRequest**](DocumentsSearchPostRequest.md)|  | [optional] 

### Return type

[**DocumentsSearchPost200Response**](DocumentsSearchPost200Response.md)

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

# **documents_star_post**
> DocumentsStarPost200Response documents_star_post(documents_star_post_request=documents_star_post_request)

Star a document

Starring a document gives it extra priority in the UI and makes it easier to find important information later.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_star_post200_response import DocumentsStarPost200Response
from outline_openapi.models.documents_star_post_request import DocumentsStarPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_star_post_request = outline_openapi.DocumentsStarPostRequest() # DocumentsStarPostRequest |  (optional)

    try:
        # Star a document
        api_response = await api_instance.documents_star_post(documents_star_post_request=documents_star_post_request)
        print("The response of DocumentsApi->documents_star_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_star_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_star_post_request** | [**DocumentsStarPostRequest**](DocumentsStarPostRequest.md)|  | [optional] 

### Return type

[**DocumentsStarPost200Response**](DocumentsStarPost200Response.md)

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

# **documents_templatize_post**
> DocumentsCreatePost200Response documents_templatize_post(collections_delete_post_request=collections_delete_post_request)

Create a template from a document

This method allows you to createa new template using an existing document as the basis

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.collections_delete_post_request import CollectionsDeletePostRequest
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    collections_delete_post_request = outline_openapi.CollectionsDeletePostRequest() # CollectionsDeletePostRequest |  (optional)

    try:
        # Create a template from a document
        api_response = await api_instance.documents_templatize_post(collections_delete_post_request=collections_delete_post_request)
        print("The response of DocumentsApi->documents_templatize_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_templatize_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_delete_post_request** | [**CollectionsDeletePostRequest**](CollectionsDeletePostRequest.md)|  | [optional] 

### Return type

[**DocumentsCreatePost200Response**](DocumentsCreatePost200Response.md)

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

# **documents_unpublish_post**
> DocumentsCreatePost200Response documents_unpublish_post(documents_star_post_request=documents_star_post_request)

Unpublish a document

Unpublishing a document moves it back to a draft status and out of the collection.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response
from outline_openapi.models.documents_star_post_request import DocumentsStarPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_star_post_request = outline_openapi.DocumentsStarPostRequest() # DocumentsStarPostRequest |  (optional)

    try:
        # Unpublish a document
        api_response = await api_instance.documents_unpublish_post(documents_star_post_request=documents_star_post_request)
        print("The response of DocumentsApi->documents_unpublish_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_unpublish_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_star_post_request** | [**DocumentsStarPostRequest**](DocumentsStarPostRequest.md)|  | [optional] 

### Return type

[**DocumentsCreatePost200Response**](DocumentsCreatePost200Response.md)

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

# **documents_unstar_post**
> DocumentsStarPost200Response documents_unstar_post(documents_star_post_request=documents_star_post_request)

Unstar a document

Starring a document gives it extra priority in the UI and makes it easier to find important information later.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_star_post200_response import DocumentsStarPost200Response
from outline_openapi.models.documents_star_post_request import DocumentsStarPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_star_post_request = outline_openapi.DocumentsStarPostRequest() # DocumentsStarPostRequest |  (optional)

    try:
        # Unstar a document
        api_response = await api_instance.documents_unstar_post(documents_star_post_request=documents_star_post_request)
        print("The response of DocumentsApi->documents_unstar_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_unstar_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_star_post_request** | [**DocumentsStarPostRequest**](DocumentsStarPostRequest.md)|  | [optional] 

### Return type

[**DocumentsStarPost200Response**](DocumentsStarPost200Response.md)

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

# **documents_update_post**
> DocumentsCreatePost200Response documents_update_post(documents_update_post_request=documents_update_post_request)

Update a document

This method allows you to modify an already created document

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_create_post200_response import DocumentsCreatePost200Response
from outline_openapi.models.documents_update_post_request import DocumentsUpdatePostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_update_post_request = outline_openapi.DocumentsUpdatePostRequest() # DocumentsUpdatePostRequest |  (optional)

    try:
        # Update a document
        api_response = await api_instance.documents_update_post(documents_update_post_request=documents_update_post_request)
        print("The response of DocumentsApi->documents_update_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_update_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_update_post_request** | [**DocumentsUpdatePostRequest**](DocumentsUpdatePostRequest.md)|  | [optional] 

### Return type

[**DocumentsCreatePost200Response**](DocumentsCreatePost200Response.md)

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

# **documents_users_post**
> DocumentsUsersPost200Response documents_users_post(documents_users_post_request=documents_users_post_request)

List document users

All users with access to a document. To list only users with direct membership to the document use `documents.memberships`

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.documents_users_post200_response import DocumentsUsersPost200Response
from outline_openapi.models.documents_users_post_request import DocumentsUsersPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_users_post_request = outline_openapi.DocumentsUsersPostRequest() # DocumentsUsersPostRequest |  (optional)

    try:
        # List document users
        api_response = await api_instance.documents_users_post(documents_users_post_request=documents_users_post_request)
        print("The response of DocumentsApi->documents_users_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_users_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_users_post_request** | [**DocumentsUsersPostRequest**](DocumentsUsersPostRequest.md)|  | [optional] 

### Return type

[**DocumentsUsersPost200Response**](DocumentsUsersPost200Response.md)

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

# **documents_viewed_post**
> CommentsListPost200Response documents_viewed_post(documents_viewed_post_request=documents_viewed_post_request)

List all recently viewed documents

This method will list all documents recently viewed by the current user.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.comments_list_post200_response import CommentsListPost200Response
from outline_openapi.models.documents_viewed_post_request import DocumentsViewedPostRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_viewed_post_request = outline_openapi.DocumentsViewedPostRequest() # DocumentsViewedPostRequest |  (optional)

    try:
        # List all recently viewed documents
        api_response = await api_instance.documents_viewed_post(documents_viewed_post_request=documents_viewed_post_request)
        print("The response of DocumentsApi->documents_viewed_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_viewed_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_viewed_post_request** | [**DocumentsViewedPostRequest**](DocumentsViewedPostRequest.md)|  | [optional] 

### Return type

[**CommentsListPost200Response**](CommentsListPost200Response.md)

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

