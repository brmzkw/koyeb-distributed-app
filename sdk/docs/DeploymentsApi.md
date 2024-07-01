# openapi_client.DeploymentsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**cancel_deployment**](DeploymentsApi.md#cancel_deployment) | **POST** /v1/deployments/{id}/cancel | Cancel Deployment
[**get_deployment**](DeploymentsApi.md#get_deployment) | **GET** /v1/deployments/{id} | Get Deployment
[**list_deployment_events**](DeploymentsApi.md#list_deployment_events) | **GET** /v1/deployment_events | List Deployment events
[**list_deployments**](DeploymentsApi.md#list_deployments) | **GET** /v1/deployments | List Deployments


# **cancel_deployment**
> object cancel_deployment(id)

Cancel Deployment

Deployment cancellation is allowed for the following status:  - pending  - provisioning  - scheduled

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
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
    api_instance = openapi_client.DeploymentsApi(api_client)
    id = 'id_example' # str | The id of the deployment to cancel.

    try:
        # Cancel Deployment
        api_response = api_instance.cancel_deployment(id)
        print("The response of DeploymentsApi->cancel_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->cancel_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment to cancel. | 

### Return type

**object**

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

# **get_deployment**
> GetDeploymentReply get_deployment(id)

Get Deployment

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_deployment_reply import GetDeploymentReply
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
    api_instance = openapi_client.DeploymentsApi(api_client)
    id = 'id_example' # str | The id of the deployment

    try:
        # Get Deployment
        api_response = api_instance.get_deployment(id)
        print("The response of DeploymentsApi->get_deployment:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->get_deployment: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the deployment | 

### Return type

[**GetDeploymentReply**](GetDeploymentReply.md)

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

# **list_deployment_events**
> ListDeploymentEventsReply list_deployment_events(deployment_id=deployment_id, types=types, limit=limit, offset=offset, order=order)

List Deployment events

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_deployment_events_reply import ListDeploymentEventsReply
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
    api_instance = openapi_client.DeploymentsApi(api_client)
    deployment_id = 'deployment_id_example' # str | (Optional) Filter on deployment id (optional)
    types = ['types_example'] # List[str] | (Optional) Filter on deployment event types (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    order = 'order_example' # str | (Optional) Sorts the list in the ascending or the descending order (optional)

    try:
        # List Deployment events
        api_response = api_instance.list_deployment_events(deployment_id=deployment_id, types=types, limit=limit, offset=offset, order=order)
        print("The response of DeploymentsApi->list_deployment_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->list_deployment_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **deployment_id** | **str**| (Optional) Filter on deployment id | [optional] 
 **types** | [**List[str]**](str.md)| (Optional) Filter on deployment event types | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **order** | **str**| (Optional) Sorts the list in the ascending or the descending order | [optional] 

### Return type

[**ListDeploymentEventsReply**](ListDeploymentEventsReply.md)

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

# **list_deployments**
> ListDeploymentsReply list_deployments(app_id=app_id, service_id=service_id, limit=limit, offset=offset, statuses=statuses)

List Deployments

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_deployments_reply import ListDeploymentsReply
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
    api_instance = openapi_client.DeploymentsApi(api_client)
    app_id = 'app_id_example' # str | (Optional) Filter on application id (optional)
    service_id = 'service_id_example' # str | (Optional) Filter on service id (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    statuses = ['statuses_example'] # List[str] | (Optional) Filter on statuses (optional)

    try:
        # List Deployments
        api_response = api_instance.list_deployments(app_id=app_id, service_id=service_id, limit=limit, offset=offset, statuses=statuses)
        print("The response of DeploymentsApi->list_deployments:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DeploymentsApi->list_deployments: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| (Optional) Filter on application id | [optional] 
 **service_id** | **str**| (Optional) Filter on service id | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **statuses** | [**List[str]**](str.md)| (Optional) Filter on statuses | [optional] 

### Return type

[**ListDeploymentsReply**](ListDeploymentsReply.md)

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

