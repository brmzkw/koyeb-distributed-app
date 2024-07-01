# openapi_client.LogsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**tail_logs**](LogsApi.md#tail_logs) | **GET** /v1/streams/logs/tail | Tails logs


# **tail_logs**
> StreamResultOfLogEntry tail_logs(type=type, app_id=app_id, service_id=service_id, deployment_id=deployment_id, regional_deployment_id=regional_deployment_id, instance_id=instance_id, stream=stream, start=start, limit=limit)

Tails logs

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.stream_result_of_log_entry import StreamResultOfLogEntry
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
    api_instance = openapi_client.LogsApi(api_client)
    type = 'type_example' # str |  (optional)
    app_id = 'app_id_example' # str |  (optional)
    service_id = 'service_id_example' # str |  (optional)
    deployment_id = 'deployment_id_example' # str |  (optional)
    regional_deployment_id = 'regional_deployment_id_example' # str |  (optional)
    instance_id = 'instance_id_example' # str |  (optional)
    stream = 'stream_example' # str |  (optional)
    start = 'start_example' # str |  (optional)
    limit = 'limit_example' # str |  (optional)

    try:
        # Tails logs
        api_response = api_instance.tail_logs(type=type, app_id=app_id, service_id=service_id, deployment_id=deployment_id, regional_deployment_id=regional_deployment_id, instance_id=instance_id, stream=stream, start=start, limit=limit)
        print("The response of LogsApi->tail_logs:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling LogsApi->tail_logs: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**|  | [optional] 
 **app_id** | **str**|  | [optional] 
 **service_id** | **str**|  | [optional] 
 **deployment_id** | **str**|  | [optional] 
 **regional_deployment_id** | **str**|  | [optional] 
 **instance_id** | **str**|  | [optional] 
 **stream** | **str**|  | [optional] 
 **start** | **str**|  | [optional] 
 **limit** | **str**|  | [optional] 

### Return type

[**StreamResultOfLogEntry**](StreamResultOfLogEntry.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response.(streaming responses) |  -  |
**400** | Validation error |  -  |
**401** | Returned when the token is not valid. |  -  |
**403** | Returned when the user does not have permission to access the resource. |  -  |
**404** | Returned when the resource does not exist. |  -  |
**500** | Returned in case of server error. |  -  |
**503** | Service is unavailable. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

