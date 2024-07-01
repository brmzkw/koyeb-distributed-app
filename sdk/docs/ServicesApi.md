# openapi_client.ServicesApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**autocomplete**](ServicesApi.md#autocomplete) | **POST** /v1/services-autocomplete | Generate autocomplete definition for a service
[**create_service**](ServicesApi.md#create_service) | **POST** /v1/services | Create Service
[**delete_service**](ServicesApi.md#delete_service) | **DELETE** /v1/services/{id} | Delete Service
[**get_service**](ServicesApi.md#get_service) | **GET** /v1/services/{id} | Get Service
[**list_service_events**](ServicesApi.md#list_service_events) | **GET** /v1/service_events | List Service events
[**list_services**](ServicesApi.md#list_services) | **GET** /v1/services | List Services
[**pause_service**](ServicesApi.md#pause_service) | **POST** /v1/services/{id}/pause | Pause Service
[**re_deploy**](ServicesApi.md#re_deploy) | **POST** /v1/services/{id}/redeploy | ReDeploy Service
[**resume_service**](ServicesApi.md#resume_service) | **POST** /v1/services/{id}/resume | Resume Service
[**update_service**](ServicesApi.md#update_service) | **PUT** /v1/services/{id} | Update Service
[**update_service2**](ServicesApi.md#update_service2) | **PATCH** /v1/services/{id} | Update Service


# **autocomplete**
> AutocompleteReply autocomplete(body)

Generate autocomplete definition for a service

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.autocomplete_reply import AutocompleteReply
from openapi_client.models.autocomplete_request import AutocompleteRequest
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
    api_instance = openapi_client.ServicesApi(api_client)
    body = openapi_client.AutocompleteRequest() # AutocompleteRequest | 

    try:
        # Generate autocomplete definition for a service
        api_response = api_instance.autocomplete(body)
        print("The response of ServicesApi->autocomplete:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->autocomplete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**AutocompleteRequest**](AutocompleteRequest.md)|  | 

### Return type

[**AutocompleteReply**](AutocompleteReply.md)

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

# **create_service**
> CreateServiceReply create_service(service, dry_run=dry_run)

Create Service

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.create_service import CreateService
from openapi_client.models.create_service_reply import CreateServiceReply
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
    api_instance = openapi_client.ServicesApi(api_client)
    service = openapi_client.CreateService() # CreateService | 
    dry_run = True # bool | If set only run validation (optional)

    try:
        # Create Service
        api_response = api_instance.create_service(service, dry_run=dry_run)
        print("The response of ServicesApi->create_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->create_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | [**CreateService**](CreateService.md)|  | 
 **dry_run** | **bool**| If set only run validation | [optional] 

### Return type

[**CreateServiceReply**](CreateServiceReply.md)

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

# **delete_service**
> object delete_service(id)

Delete Service

Service deletion is allowed for all status.

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
    api_instance = openapi_client.ServicesApi(api_client)
    id = 'id_example' # str | The id of the entity to delete

    try:
        # Delete Service
        api_response = api_instance.delete_service(id)
        print("The response of ServicesApi->delete_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->delete_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the entity to delete | 

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

# **get_service**
> GetServiceReply get_service(id)

Get Service

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_service_reply import GetServiceReply
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
    api_instance = openapi_client.ServicesApi(api_client)
    id = 'id_example' # str | The id of the Service

    try:
        # Get Service
        api_response = api_instance.get_service(id)
        print("The response of ServicesApi->get_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->get_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the Service | 

### Return type

[**GetServiceReply**](GetServiceReply.md)

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

# **list_service_events**
> ListServiceEventsReply list_service_events(service_id=service_id, types=types, limit=limit, offset=offset, order=order)

List Service events

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_service_events_reply import ListServiceEventsReply
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
    api_instance = openapi_client.ServicesApi(api_client)
    service_id = 'service_id_example' # str | (Optional) Filter on service id (optional)
    types = ['types_example'] # List[str] | (Optional) Filter on service event types (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    order = 'order_example' # str | (Optional) Sorts the list in the ascending or the descending order (optional)

    try:
        # List Service events
        api_response = api_instance.list_service_events(service_id=service_id, types=types, limit=limit, offset=offset, order=order)
        print("The response of ServicesApi->list_service_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_service_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service_id** | **str**| (Optional) Filter on service id | [optional] 
 **types** | [**List[str]**](str.md)| (Optional) Filter on service event types | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **order** | **str**| (Optional) Sorts the list in the ascending or the descending order | [optional] 

### Return type

[**ListServiceEventsReply**](ListServiceEventsReply.md)

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

# **list_services**
> ListServicesReply list_services(app_id=app_id, limit=limit, offset=offset, name=name, types=types)

List Services

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_services_reply import ListServicesReply
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
    api_instance = openapi_client.ServicesApi(api_client)
    app_id = 'app_id_example' # str | (Optional) The id of the app (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    name = 'name_example' # str | (Optional) A filter for name (optional)
    types = ['types_example'] # List[str] | (Optional) Filter on service types (optional)

    try:
        # List Services
        api_response = api_instance.list_services(app_id=app_id, limit=limit, offset=offset, name=name, types=types)
        print("The response of ServicesApi->list_services:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->list_services: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| (Optional) The id of the app | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **name** | **str**| (Optional) A filter for name | [optional] 
 **types** | [**List[str]**](str.md)| (Optional) Filter on service types | [optional] 

### Return type

[**ListServicesReply**](ListServicesReply.md)

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

# **pause_service**
> object pause_service(id)

Pause Service

Service pause action is allowed for the following status:  - starting  - healthy  - degraded  - unhealthy  - resuming

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
    api_instance = openapi_client.ServicesApi(api_client)
    id = 'id_example' # str | The id of the service to pause.

    try:
        # Pause Service
        api_response = api_instance.pause_service(id)
        print("The response of ServicesApi->pause_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->pause_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the service to pause. | 

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

# **re_deploy**
> RedeployReply re_deploy(id, info)

ReDeploy Service

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.redeploy_reply import RedeployReply
from openapi_client.models.redeploy_request_info import RedeployRequestInfo
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
    api_instance = openapi_client.ServicesApi(api_client)
    id = 'id_example' # str | 
    info = openapi_client.RedeployRequestInfo() # RedeployRequestInfo | 

    try:
        # ReDeploy Service
        api_response = api_instance.re_deploy(id, info)
        print("The response of ServicesApi->re_deploy:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->re_deploy: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **info** | [**RedeployRequestInfo**](RedeployRequestInfo.md)|  | 

### Return type

[**RedeployReply**](RedeployReply.md)

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

# **resume_service**
> object resume_service(id)

Resume Service

Service resume action is allowed for the following status:  - paused

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
    api_instance = openapi_client.ServicesApi(api_client)
    id = 'id_example' # str | The id of the service to pause.

    try:
        # Resume Service
        api_response = api_instance.resume_service(id)
        print("The response of ServicesApi->resume_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->resume_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the service to pause. | 

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

# **update_service**
> UpdateServiceReply update_service(id, service, dry_run=dry_run)

Update Service

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.update_service import UpdateService
from openapi_client.models.update_service_reply import UpdateServiceReply
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
    api_instance = openapi_client.ServicesApi(api_client)
    id = 'id_example' # str | The id of the entity to update
    service = openapi_client.UpdateService() # UpdateService | 
    dry_run = True # bool | If set, run validation and check that the service exists (optional)

    try:
        # Update Service
        api_response = api_instance.update_service(id, service, dry_run=dry_run)
        print("The response of ServicesApi->update_service:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the entity to update | 
 **service** | [**UpdateService**](UpdateService.md)|  | 
 **dry_run** | **bool**| If set, run validation and check that the service exists | [optional] 

### Return type

[**UpdateServiceReply**](UpdateServiceReply.md)

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

# **update_service2**
> UpdateServiceReply update_service2(id, service, dry_run=dry_run)

Update Service

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.update_service import UpdateService
from openapi_client.models.update_service_reply import UpdateServiceReply
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
    api_instance = openapi_client.ServicesApi(api_client)
    id = 'id_example' # str | The id of the entity to update
    service = openapi_client.UpdateService() # UpdateService | 
    dry_run = True # bool | If set, run validation and check that the service exists (optional)

    try:
        # Update Service
        api_response = api_instance.update_service2(id, service, dry_run=dry_run)
        print("The response of ServicesApi->update_service2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ServicesApi->update_service2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the entity to update | 
 **service** | [**UpdateService**](UpdateService.md)|  | 
 **dry_run** | **bool**| If set, run validation and check that the service exists | [optional] 

### Return type

[**UpdateServiceReply**](UpdateServiceReply.md)

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

