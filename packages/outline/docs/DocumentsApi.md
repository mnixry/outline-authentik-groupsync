# outline_openapi.DocumentsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**documents_add_user**](DocumentsApi.md#documents_add_user) | **POST** /documents.add_user | Add a document user
[**documents_answerquestion**](DocumentsApi.md#documents_answerquestion) | **POST** /documents.answerQuestion | Query documents with natural language
[**documents_archive**](DocumentsApi.md#documents_archive) | **POST** /documents.archive | Archive a document
[**documents_create**](DocumentsApi.md#documents_create) | **POST** /documents.create | Create a document
[**documents_delete**](DocumentsApi.md#documents_delete) | **POST** /documents.delete | Delete a document
[**documents_drafts**](DocumentsApi.md#documents_drafts) | **POST** /documents.drafts | List all draft documents
[**documents_export**](DocumentsApi.md#documents_export) | **POST** /documents.export | Export a document as markdown
[**documents_import**](DocumentsApi.md#documents_import) | **POST** /documents.import | Import a file as a document
[**documents_info**](DocumentsApi.md#documents_info) | **POST** /documents.info | Retrieve a document
[**documents_list**](DocumentsApi.md#documents_list) | **POST** /documents.list | List all documents
[**documents_memberships**](DocumentsApi.md#documents_memberships) | **POST** /documents.memberships | List document memberships
[**documents_move**](DocumentsApi.md#documents_move) | **POST** /documents.move | Move a document
[**documents_remove_user**](DocumentsApi.md#documents_remove_user) | **POST** /documents.remove_user | Remove a document user
[**documents_restore**](DocumentsApi.md#documents_restore) | **POST** /documents.restore | Restore a document
[**documents_search**](DocumentsApi.md#documents_search) | **POST** /documents.search | Search all documents
[**documents_templatize**](DocumentsApi.md#documents_templatize) | **POST** /documents.templatize | Create a template from a document
[**documents_unpublish**](DocumentsApi.md#documents_unpublish) | **POST** /documents.unpublish | Unpublish a document
[**documents_update**](DocumentsApi.md#documents_update) | **POST** /documents.update | Update a document
[**documents_users**](DocumentsApi.md#documents_users) | **POST** /documents.users | List document users
[**documents_viewed**](DocumentsApi.md#documents_viewed) | **POST** /documents.viewed | List all recently viewed documents


# **documents_add_user**
> CollectionsAddUser200Response documents_add_user(documents_add_user_request=documents_add_user_request)

Add a document user

This method allows you to add a user membership to the specified document.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_add_user200_response import CollectionsAddUser200Response
from outline_openapi.models.documents_add_user_request import DocumentsAddUserRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_add_user_request = outline_openapi.DocumentsAddUserRequest() # DocumentsAddUserRequest |  (optional)

    try:
        # Add a document user
        api_response = await api_instance.documents_add_user(documents_add_user_request=documents_add_user_request)
        print("The response of DocumentsApi->documents_add_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_add_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_add_user_request** | [**DocumentsAddUserRequest**](DocumentsAddUserRequest.md)|  | [optional] 

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

# **documents_answerquestion**
> DocumentsAnswerquestion200Response documents_answerquestion(documents_answerquestion_request=documents_answerquestion_request)

Query documents with natural language

This method allows asking direct questions of your documents – where possible an answer will be provided. Search results will be restricted to those accessible by the current access token. Note that "AI answers" must be enabled for the workspace.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_answerquestion200_response import DocumentsAnswerquestion200Response
from outline_openapi.models.documents_answerquestion_request import DocumentsAnswerquestionRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_answerquestion_request = outline_openapi.DocumentsAnswerquestionRequest() # DocumentsAnswerquestionRequest |  (optional)

    try:
        # Query documents with natural language
        api_response = await api_instance.documents_answerquestion(documents_answerquestion_request=documents_answerquestion_request)
        print("The response of DocumentsApi->documents_answerquestion:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_answerquestion: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_answerquestion_request** | [**DocumentsAnswerquestionRequest**](DocumentsAnswerquestionRequest.md)|  | [optional] 

### Return type

[**DocumentsAnswerquestion200Response**](DocumentsAnswerquestion200Response.md)

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

# **documents_archive**
> DocumentsInfo200Response documents_archive(documents_unpublish_request=documents_unpublish_request)

Archive a document

Archiving a document allows outdated information to be moved out of sight whilst retaining the ability to optionally search and restore it later.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
from outline_openapi.models.documents_unpublish_request import DocumentsUnpublishRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_unpublish_request = outline_openapi.DocumentsUnpublishRequest() # DocumentsUnpublishRequest |  (optional)

    try:
        # Archive a document
        api_response = await api_instance.documents_archive(documents_unpublish_request=documents_unpublish_request)
        print("The response of DocumentsApi->documents_archive:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_archive: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_unpublish_request** | [**DocumentsUnpublishRequest**](DocumentsUnpublishRequest.md)|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

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

# **documents_create**
> DocumentsInfo200Response documents_create(documents_create_request=documents_create_request)

Create a document

This method allows you to create or publish a new document. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_create_request import DocumentsCreateRequest
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_create_request = outline_openapi.DocumentsCreateRequest() # DocumentsCreateRequest |  (optional)

    try:
        # Create a document
        api_response = await api_instance.documents_create(documents_create_request=documents_create_request)
        print("The response of DocumentsApi->documents_create:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_create: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_create_request** | [**DocumentsCreateRequest**](DocumentsCreateRequest.md)|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

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

# **documents_delete**
> AttachmentsDelete200Response documents_delete(documents_delete_request=documents_delete_request)

Delete a document

Deleting a document moves it to the trash. If not restored within 30 days it is permenantly deleted.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.documents_delete_request import DocumentsDeleteRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_delete_request = outline_openapi.DocumentsDeleteRequest() # DocumentsDeleteRequest |  (optional)

    try:
        # Delete a document
        api_response = await api_instance.documents_delete(documents_delete_request=documents_delete_request)
        print("The response of DocumentsApi->documents_delete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_delete_request** | [**DocumentsDeleteRequest**](DocumentsDeleteRequest.md)|  | [optional] 

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

# **documents_drafts**
> DocumentsList200Response documents_drafts(documents_drafts_request=documents_drafts_request)

List all draft documents

This method will list all draft documents belonging to the current user.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_drafts_request import DocumentsDraftsRequest
from outline_openapi.models.documents_list200_response import DocumentsList200Response
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_drafts_request = outline_openapi.DocumentsDraftsRequest() # DocumentsDraftsRequest |  (optional)

    try:
        # List all draft documents
        api_response = await api_instance.documents_drafts(documents_drafts_request=documents_drafts_request)
        print("The response of DocumentsApi->documents_drafts:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_drafts: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_drafts_request** | [**DocumentsDraftsRequest**](DocumentsDraftsRequest.md)|  | [optional] 

### Return type

[**DocumentsList200Response**](DocumentsList200Response.md)

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

# **documents_export**
> DocumentsExport200Response documents_export(documents_export_request=documents_export_request)

Export a document as markdown

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_export200_response import DocumentsExport200Response
from outline_openapi.models.documents_export_request import DocumentsExportRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_export_request = outline_openapi.DocumentsExportRequest() # DocumentsExportRequest |  (optional)

    try:
        # Export a document as markdown
        api_response = await api_instance.documents_export(documents_export_request=documents_export_request)
        print("The response of DocumentsApi->documents_export:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_export: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_export_request** | [**DocumentsExportRequest**](DocumentsExportRequest.md)|  | [optional] 

### Return type

[**DocumentsExport200Response**](DocumentsExport200Response.md)

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

# **documents_import**
> DocumentsInfo200Response documents_import(file, collection_id=collection_id, parent_document_id=parent_document_id, template=template, publish=publish)

Import a file as a document

This method allows you to create a new document by importing an existing file. By default a document is set to the collection root. If you want to create a nested/child document, you should pass parentDocumentId to set the parent document.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    file = None # object | Plain text, markdown, docx, csv, tsv, and html format are supported.
    collection_id = 'collection_id_example' # str |  (optional)
    parent_document_id = 'parent_document_id_example' # str |  (optional)
    template = True # bool |  (optional)
    publish = True # bool |  (optional)

    try:
        # Import a file as a document
        api_response = await api_instance.documents_import(file, collection_id=collection_id, parent_document_id=parent_document_id, template=template, publish=publish)
        print("The response of DocumentsApi->documents_import:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_import: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **file** | [**object**](object.md)| Plain text, markdown, docx, csv, tsv, and html format are supported. | 
 **collection_id** | **str**|  | [optional] 
 **parent_document_id** | **str**|  | [optional] 
 **template** | **bool**|  | [optional] 
 **publish** | **bool**|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

### Authorization

[OAuth2](../README.md#OAuth2), [BearerAuth](../README.md#BearerAuth)

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
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_info**
> DocumentsInfo200Response documents_info(documents_info_request=documents_info_request)

Retrieve a document

Retrieve a document by its `UUID`, `urlId`, or `shareId`. At least one of these parameters must be provided.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
from outline_openapi.models.documents_info_request import DocumentsInfoRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_info_request = outline_openapi.DocumentsInfoRequest() # DocumentsInfoRequest |  (optional)

    try:
        # Retrieve a document
        api_response = await api_instance.documents_info(documents_info_request=documents_info_request)
        print("The response of DocumentsApi->documents_info:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_info: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_info_request** | [**DocumentsInfoRequest**](DocumentsInfoRequest.md)|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

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

# **documents_list**
> DocumentsList200Response documents_list(documents_list_request=documents_list_request)

List all documents

This method will list all published documents and draft documents belonging to the current user.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_list200_response import DocumentsList200Response
from outline_openapi.models.documents_list_request import DocumentsListRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_list_request = outline_openapi.DocumentsListRequest() # DocumentsListRequest |  (optional)

    try:
        # List all documents
        api_response = await api_instance.documents_list(documents_list_request=documents_list_request)
        print("The response of DocumentsApi->documents_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_list_request** | [**DocumentsListRequest**](DocumentsListRequest.md)|  | [optional] 

### Return type

[**DocumentsList200Response**](DocumentsList200Response.md)

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

# **documents_memberships**
> CollectionsMemberships200Response documents_memberships(documents_memberships_request=documents_memberships_request)

List document memberships

Users with direct membership to a document. To list all users with access to a document use `documents.users`.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_memberships200_response import CollectionsMemberships200Response
from outline_openapi.models.documents_memberships_request import DocumentsMembershipsRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_memberships_request = outline_openapi.DocumentsMembershipsRequest() # DocumentsMembershipsRequest |  (optional)

    try:
        # List document memberships
        api_response = await api_instance.documents_memberships(documents_memberships_request=documents_memberships_request)
        print("The response of DocumentsApi->documents_memberships:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_memberships: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_memberships_request** | [**DocumentsMembershipsRequest**](DocumentsMembershipsRequest.md)|  | [optional] 

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
**404** | The specified resource was not found. |  -  |
**429** | The request was rate limited. |  * Retry-After -  <br>  * RateLimit-Limit -  <br>  * RateLimit-Remaining -  <br>  * RateLimit-Reset -  <br>  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **documents_move**
> DocumentsMove200Response documents_move(documents_move_request=documents_move_request)

Move a document

Move a document to a new location or collection. If no parent document is provided, the document will be moved to the collection root.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_move200_response import DocumentsMove200Response
from outline_openapi.models.documents_move_request import DocumentsMoveRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_move_request = outline_openapi.DocumentsMoveRequest() # DocumentsMoveRequest |  (optional)

    try:
        # Move a document
        api_response = await api_instance.documents_move(documents_move_request=documents_move_request)
        print("The response of DocumentsApi->documents_move:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_move: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_move_request** | [**DocumentsMoveRequest**](DocumentsMoveRequest.md)|  | [optional] 

### Return type

[**DocumentsMove200Response**](DocumentsMove200Response.md)

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

# **documents_remove_user**
> AttachmentsDelete200Response documents_remove_user(documents_remove_user_request=documents_remove_user_request)

Remove a document user

This method allows you to remove a user membership from the specified document.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.attachments_delete200_response import AttachmentsDelete200Response
from outline_openapi.models.documents_remove_user_request import DocumentsRemoveUserRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_remove_user_request = outline_openapi.DocumentsRemoveUserRequest() # DocumentsRemoveUserRequest |  (optional)

    try:
        # Remove a document user
        api_response = await api_instance.documents_remove_user(documents_remove_user_request=documents_remove_user_request)
        print("The response of DocumentsApi->documents_remove_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_remove_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_remove_user_request** | [**DocumentsRemoveUserRequest**](DocumentsRemoveUserRequest.md)|  | [optional] 

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

# **documents_restore**
> DocumentsInfo200Response documents_restore(documents_restore_request=documents_restore_request)

Restore a document

If a document has been archived or deleted, it can be restored. Optionally a revision can be passed to restore the document to a previous point in time.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
from outline_openapi.models.documents_restore_request import DocumentsRestoreRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_restore_request = outline_openapi.DocumentsRestoreRequest() # DocumentsRestoreRequest |  (optional)

    try:
        # Restore a document
        api_response = await api_instance.documents_restore(documents_restore_request=documents_restore_request)
        print("The response of DocumentsApi->documents_restore:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_restore: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_restore_request** | [**DocumentsRestoreRequest**](DocumentsRestoreRequest.md)|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

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

# **documents_search**
> DocumentsSearch200Response documents_search(documents_search_request=documents_search_request)

Search all documents

This methods allows you to search your teams documents with keywords. Note that search results will be restricted to those accessible by the current access token.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_search200_response import DocumentsSearch200Response
from outline_openapi.models.documents_search_request import DocumentsSearchRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_search_request = outline_openapi.DocumentsSearchRequest() # DocumentsSearchRequest |  (optional)

    try:
        # Search all documents
        api_response = await api_instance.documents_search(documents_search_request=documents_search_request)
        print("The response of DocumentsApi->documents_search:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_search: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_search_request** | [**DocumentsSearchRequest**](DocumentsSearchRequest.md)|  | [optional] 

### Return type

[**DocumentsSearch200Response**](DocumentsSearch200Response.md)

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

# **documents_templatize**
> DocumentsInfo200Response documents_templatize(collections_delete_request=collections_delete_request)

Create a template from a document

This method allows you to createa new template using an existing document as the basis

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.collections_delete_request import CollectionsDeleteRequest
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    collections_delete_request = outline_openapi.CollectionsDeleteRequest() # CollectionsDeleteRequest |  (optional)

    try:
        # Create a template from a document
        api_response = await api_instance.documents_templatize(collections_delete_request=collections_delete_request)
        print("The response of DocumentsApi->documents_templatize:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_templatize: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **collections_delete_request** | [**CollectionsDeleteRequest**](CollectionsDeleteRequest.md)|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

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

# **documents_unpublish**
> DocumentsInfo200Response documents_unpublish(documents_unpublish_request=documents_unpublish_request)

Unpublish a document

Unpublishing a document moves it back to a draft status and out of the collection.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
from outline_openapi.models.documents_unpublish_request import DocumentsUnpublishRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_unpublish_request = outline_openapi.DocumentsUnpublishRequest() # DocumentsUnpublishRequest |  (optional)

    try:
        # Unpublish a document
        api_response = await api_instance.documents_unpublish(documents_unpublish_request=documents_unpublish_request)
        print("The response of DocumentsApi->documents_unpublish:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_unpublish: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_unpublish_request** | [**DocumentsUnpublishRequest**](DocumentsUnpublishRequest.md)|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

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

# **documents_update**
> DocumentsInfo200Response documents_update(documents_update_request=documents_update_request)

Update a document

This method allows you to modify an already created document

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_info200_response import DocumentsInfo200Response
from outline_openapi.models.documents_update_request import DocumentsUpdateRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_update_request = outline_openapi.DocumentsUpdateRequest() # DocumentsUpdateRequest |  (optional)

    try:
        # Update a document
        api_response = await api_instance.documents_update(documents_update_request=documents_update_request)
        print("The response of DocumentsApi->documents_update:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_update: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_update_request** | [**DocumentsUpdateRequest**](DocumentsUpdateRequest.md)|  | [optional] 

### Return type

[**DocumentsInfo200Response**](DocumentsInfo200Response.md)

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

# **documents_users**
> DocumentsUsers200Response documents_users(documents_users_request=documents_users_request)

List document users

All users with access to a document. To list only users with direct membership to the document use `documents.memberships`

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_users200_response import DocumentsUsers200Response
from outline_openapi.models.documents_users_request import DocumentsUsersRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_users_request = outline_openapi.DocumentsUsersRequest() # DocumentsUsersRequest |  (optional)

    try:
        # List document users
        api_response = await api_instance.documents_users(documents_users_request=documents_users_request)
        print("The response of DocumentsApi->documents_users:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_users: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_users_request** | [**DocumentsUsersRequest**](DocumentsUsersRequest.md)|  | [optional] 

### Return type

[**DocumentsUsers200Response**](DocumentsUsers200Response.md)

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

# **documents_viewed**
> DocumentsList200Response documents_viewed(documents_viewed_request=documents_viewed_request)

List all recently viewed documents

This method will list all documents recently viewed by the current user.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.documents_list200_response import DocumentsList200Response
from outline_openapi.models.documents_viewed_request import DocumentsViewedRequest
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
    api_instance = outline_openapi.DocumentsApi(api_client)
    documents_viewed_request = outline_openapi.DocumentsViewedRequest() # DocumentsViewedRequest |  (optional)

    try:
        # List all recently viewed documents
        api_response = await api_instance.documents_viewed(documents_viewed_request=documents_viewed_request)
        print("The response of DocumentsApi->documents_viewed:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DocumentsApi->documents_viewed: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **documents_viewed_request** | [**DocumentsViewedRequest**](DocumentsViewedRequest.md)|  | [optional] 

### Return type

[**DocumentsList200Response**](DocumentsList200Response.md)

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

