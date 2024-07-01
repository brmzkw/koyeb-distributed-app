# openapi_client.ActivityApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_account_activities**](ActivityApi.md#get_account_activities) | **GET** /v1/account/activities | 
[**list_activities**](ActivityApi.md#list_activities) | **GET** /v1/activities | 
[**list_notifications**](ActivityApi.md#list_notifications) | **GET** /v1/notifications | 


# **get_account_activities**
> ActivityList get_account_activities(limit=limit, offset=offset)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.activity_list import ActivityList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.koyeb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.koyeb.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ActivityApi(api_client)
    limit = 'limit_example' # str |  (optional)
    offset = 'offset_example' # str |  (optional)

    try:
        api_response = api_instance.get_account_activities(limit=limit, offset=offset)
        print("The response of ActivityApi->get_account_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->get_account_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 

### Return type

[**ActivityList**](ActivityList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Validation error |  -  |
**401** | Returned when the token is not valid. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned in case of server error. |  -  |
**503** | Service is unavailable. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_activities**
> ActivityList list_activities(limit=limit, offset=offset)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.activity_list import ActivityList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.koyeb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.koyeb.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ActivityApi(api_client)
    limit = 'limit_example' # str |  (optional)
    offset = 'offset_example' # str |  (optional)

    try:
        api_response = api_instance.list_activities(limit=limit, offset=offset)
        print("The response of ActivityApi->list_activities:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->list_activities: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 

### Return type

[**ActivityList**](ActivityList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Validation error |  -  |
**401** | Returned when the token is not valid. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned in case of server error. |  -  |
**503** | Service is unavailable. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_notifications**
> NotificationList list_notifications(limit=limit, offset=offset, mark_read=mark_read, mark_seen=mark_seen, unread=unread, unseen=unseen)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.notification_list import NotificationList
from openapi_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://app.koyeb.com
# See configuration.py for a list of all supported configuration parameters.
configuration = openapi_client.Configuration(
    host = "https://app.koyeb.com"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure API key authorization: Bearer
configuration.api_key['Bearer'] = os.environ["API_KEY"]

# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['Bearer'] = 'Bearer'

# Enter a context with an instance of the API client
with openapi_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = openapi_client.ActivityApi(api_client)
    limit = 'limit_example' # str |  (optional)
    offset = 'offset_example' # str |  (optional)
    mark_read = 'mark_read_example' # str |  (optional)
    mark_seen = 'mark_seen_example' # str |  (optional)
    unread = 'unread_example' # str |  (optional)
    unseen = 'unseen_example' # str |  (optional)

    try:
        api_response = api_instance.list_notifications(limit=limit, offset=offset, mark_read=mark_read, mark_seen=mark_seen, unread=unread, unseen=unseen)
        print("The response of ActivityApi->list_notifications:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ActivityApi->list_notifications: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**|  | [optional] 
 **offset** | **str**|  | [optional] 
 **mark_read** | **str**|  | [optional] 
 **mark_seen** | **str**|  | [optional] 
 **unread** | **str**|  | [optional] 
 **unseen** | **str**|  | [optional] 

### Return type

[**NotificationList**](NotificationList.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**400** | Validation error |  -  |
**401** | Returned when the token is not valid. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned in case of server error. |  -  |
**503** | Service is unavailable. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

