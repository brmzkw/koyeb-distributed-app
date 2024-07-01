# openapi_client.UsagesApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_organization_usage**](UsagesApi.md#get_organization_usage) | **GET** /v1/usages | Get organization usage
[**get_organization_usage_details**](UsagesApi.md#get_organization_usage_details) | **GET** /v1/usages/details | Get organization usage details


# **get_organization_usage**
> GetOrganizationUsageReply get_organization_usage(starting_time=starting_time, ending_time=ending_time)

Get organization usage

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_organization_usage_reply import GetOrganizationUsageReply
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
    api_instance = openapi_client.UsagesApi(api_client)
    starting_time = '2013-10-20T19:20:30+01:00' # datetime | The starting time of the period to get data from (optional)
    ending_time = '2013-10-20T19:20:30+01:00' # datetime | The ending time of the period to get data from (optional)

    try:
        # Get organization usage
        api_response = api_instance.get_organization_usage(starting_time=starting_time, ending_time=ending_time)
        print("The response of UsagesApi->get_organization_usage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsagesApi->get_organization_usage: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_time** | **datetime**| The starting time of the period to get data from | [optional] 
 **ending_time** | **datetime**| The ending time of the period to get data from | [optional] 

### Return type

[**GetOrganizationUsageReply**](GetOrganizationUsageReply.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_organization_usage_details**
> GetOrganizationUsageDetailsReply get_organization_usage_details(starting_time=starting_time, ending_time=ending_time, limit=limit, offset=offset, order=order, accept=accept)

Get organization usage details

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_organization_usage_details_reply import GetOrganizationUsageDetailsReply
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
    api_instance = openapi_client.UsagesApi(api_client)
    starting_time = '2013-10-20T19:20:30+01:00' # datetime | The starting time of the period to get data from (optional)
    ending_time = '2013-10-20T19:20:30+01:00' # datetime | The ending time of the period to get data from (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    order = 'order_example' # str | (Optional) Sorts the list in the ascending or the descending order (optional)
    accept = 'accept_example' # str | If defined with the value 'text/csv', a csv file is returned (optional)

    try:
        # Get organization usage details
        api_response = api_instance.get_organization_usage_details(starting_time=starting_time, ending_time=ending_time, limit=limit, offset=offset, order=order, accept=accept)
        print("The response of UsagesApi->get_organization_usage_details:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling UsagesApi->get_organization_usage_details: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **starting_time** | **datetime**| The starting time of the period to get data from | [optional] 
 **ending_time** | **datetime**| The ending time of the period to get data from | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **order** | **str**| (Optional) Sorts the list in the ascending or the descending order | [optional] 
 **accept** | **str**| If defined with the value &#39;text/csv&#39;, a csv file is returned | [optional] 

### Return type

[**GetOrganizationUsageDetailsReply**](GetOrganizationUsageDetailsReply.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: */*

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | A successful response. |  -  |
**0** | An unexpected error response. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

