# openapi_client.RegionalDeploymentsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_regional_deployment**](RegionalDeploymentsApi.md#get_regional_deployment) | **GET** /v1/regional_deployments/{id} | Experimental: Get regional deployment Use at your own risk
[**list_regional_deployment_events**](RegionalDeploymentsApi.md#list_regional_deployment_events) | **GET** /v1/regional_deployment_events | List Regional Deployment events
[**list_regional_deployments**](RegionalDeploymentsApi.md#list_regional_deployments) | **GET** /v1/regional_deployments | Experimental: List regional deployments Use at your own risk


# **get_regional_deployment**
> GetRegionalDeploymentReply get_regional_deployment(id)

Experimental: Get regional deployment Use at your own risk

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_regional_deployment_reply import GetRegionalDeploymentReply
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
    api_instance = openapi_client.RegionalDeploymentsApi(api_client)
    id = 'id_example' # str | The id of the regional deployment

    try:
        # Experimental: Get regional deployment Use at your own risk
        api_response = api_instance.get_regional_deployment(id)
        print("The response of RegionalDeploymentsApi->get_regional_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalDeploymentsApi->get_regional_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the regional deployment | 

### Return type

[**GetRegionalDeploymentReply**](GetRegionalDeploymentReply.md)

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

# **list_regional_deployment_events**
> ListRegionalDeploymentEventsReply list_regional_deployment_events(regional_deployment_id=regional_deployment_id, types=types, limit=limit, offset=offset, order=order)

List Regional Deployment events

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_regional_deployment_events_reply import ListRegionalDeploymentEventsReply
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
    api_instance = openapi_client.RegionalDeploymentsApi(api_client)
    regional_deployment_id = 'regional_deployment_id_example' # str | (Optional) Filter on regional deployment id (optional)
    types = ['types_example'] # List[str] | (Optional) Filter on regional deployment event types (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    order = 'order_example' # str | (Optional) Sorts the list in the ascending or the descending order (optional)

    try:
        # List Regional Deployment events
        api_response = api_instance.list_regional_deployment_events(regional_deployment_id=regional_deployment_id, types=types, limit=limit, offset=offset, order=order)
        print("The response of RegionalDeploymentsApi->list_regional_deployment_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalDeploymentsApi->list_regional_deployment_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **regional_deployment_id** | **str**| (Optional) Filter on regional deployment id | [optional] 
 **types** | [**List[str]**](str.md)| (Optional) Filter on regional deployment event types | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **order** | **str**| (Optional) Sorts the list in the ascending or the descending order | [optional] 

### Return type

[**ListRegionalDeploymentEventsReply**](ListRegionalDeploymentEventsReply.md)

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

# **list_regional_deployments**
> ListRegionalDeploymentsReply list_regional_deployments(deployment_id=deployment_id, limit=limit, offset=offset)

Experimental: List regional deployments Use at your own risk

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_regional_deployments_reply import ListRegionalDeploymentsReply
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
    api_instance = openapi_client.RegionalDeploymentsApi(api_client)
    deployment_id = 'deployment_id_example' # str | (Optional) Filter on deployment id (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)

    try:
        # Experimental: List regional deployments Use at your own risk
        api_response = api_instance.list_regional_deployments(deployment_id=deployment_id, limit=limit, offset=offset)
        print("The response of RegionalDeploymentsApi->list_regional_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RegionalDeploymentsApi->list_regional_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| (Optional) Filter on deployment id | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 

### Return type

[**ListRegionalDeploymentsReply**](ListRegionalDeploymentsReply.md)

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

