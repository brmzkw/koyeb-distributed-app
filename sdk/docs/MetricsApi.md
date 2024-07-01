# openapi_client.MetricsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_metrics**](MetricsApi.md#get_metrics) | **GET** /v1/streams/metrics | 


# **get_metrics**
> GetMetricsReply get_metrics(service_id=service_id, instance_id=instance_id, name=name, start=start, end=end, step=step)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_metrics_reply import GetMetricsReply
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
    api_instance = openapi_client.MetricsApi(api_client)
    service_id = 'service_id_example' # str | ID of the service to query instances metrics for. Ignored if instance_id is set. (optional)
    instance_id = 'instance_id_example' # str | ID of the instance to query metrics for. (optional)
    name = 'UNKNOWN' # str | Metric to query. (optional) (default to 'UNKNOWN')
    start = '2013-10-20T19:20:30+01:00' # datetime | (Optional) Defaults to an hour prior to end. (optional)
    end = '2013-10-20T19:20:30+01:00' # datetime | (Optional) Defaults to now. (optional)
    step = 'step_example' # str | (Optional) Must be a valid duration in hours (h) or minutes (m). Defaulst to 5m. (optional)

    try:
        api_response = api_instance.get_metrics(service_id=service_id, instance_id=instance_id, name=name, start=start, end=end, step=step)
        print("The response of MetricsApi->get_metrics:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling MetricsApi->get_metrics: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| ID of the service to query instances metrics for. Ignored if instance_id is set. | [optional] 
 **instance_id** | **str**| ID of the instance to query metrics for. | [optional] 
 **name** | **str**| Metric to query. | [optional] [default to &#39;UNKNOWN&#39;]
 **start** | **datetime**| (Optional) Defaults to an hour prior to end. | [optional] 
 **end** | **datetime**| (Optional) Defaults to now. | [optional] 
 **step** | **str**| (Optional) Must be a valid duration in hours (h) or minutes (m). Defaulst to 5m. | [optional] 

### Return type

[**GetMetricsReply**](GetMetricsReply.md)

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

