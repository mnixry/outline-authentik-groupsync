# outline_openapi.EventsApi

All URIs are relative to *https://app.getoutline.com/api*

Method | HTTP request | Description
------------- | ------------- | -------------
[**events_list**](EventsApi.md#events_list) | **POST** /events.list | List all events


# **events_list**
> EventsList200Response events_list(events_list_request=events_list_request)

List all events

Events are an audit trail of important events that happen in the knowledge base.

### Example

* OAuth Authentication (OAuth2):
* Bearer (JWT) Authentication (BearerAuth):

```python
import outline_openapi
from outline_openapi.models.events_list200_response import EventsList200Response
from outline_openapi.models.events_list_request import EventsListRequest
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
    api_instance = outline_openapi.EventsApi(api_client)
    events_list_request = outline_openapi.EventsListRequest() # EventsListRequest |  (optional)

    try:
        # List all events
        api_response = await api_instance.events_list(events_list_request=events_list_request)
        print("The response of EventsApi->events_list:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling EventsApi->events_list: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **events_list_request** | [**EventsListRequest**](EventsListRequest.md)|  | [optional] 

### Return type

[**EventsList200Response**](EventsList200Response.md)

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

