# outline_openapi.EventsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_list_post**](EventsApi.md#events_list_post) | **POST** /events.list | List all events


# **events_list_post**
> EventsListPost200Response events_list_post(events_list_post_request=events_list_post_request)

List all events

Events are an audit trail of important events that happen in the knowledge base.

### Example

* Bearer (JWT) Authentication (http):

```python
import outline_openapi
from outline_openapi.models.events_list_post200_response import EventsListPost200Response
from outline_openapi.models.events_list_post_request import EventsListPostRequest
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
    api_instance = outline_openapi.EventsApi(api_client)
    events_list_post_request = outline_openapi.EventsListPostRequest() # EventsListPostRequest |  (optional)

    try:
        # List all events
        api_response = await api_instance.events_list_post(events_list_post_request=events_list_post_request)
        print("The response of EventsApi->events_list_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_list_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_list_post_request** | [**EventsListPostRequest**](EventsListPostRequest.md)|  | [optional] 

### Return type

[**EventsListPost200Response**](EventsListPost200Response.md)

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

