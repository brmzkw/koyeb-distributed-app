# openapi_client.InstancesApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**exec_command**](InstancesApi.md#exec_command) | **GET** /v1/streams/instances/exec | Exec Command
[**get_instance**](InstancesApi.md#get_instance) | **GET** /v1/instances/{id} | Get Instance
[**list_instance_events**](InstancesApi.md#list_instance_events) | **GET** /v1/instance_events | List Instance events
[**list_instances**](InstancesApi.md#list_instances) | **GET** /v1/instances | List Instances


# **exec_command**
> StreamResultOfExecCommandReply exec_command(id=id, body_command=body_command, body_tty_size_height=body_tty_size_height, body_tty_size_width=body_tty_size_width, body_stdin_data=body_stdin_data, body_stdin_close=body_stdin_close, body_disable_tty=body_disable_tty, id_type=id_type)

Exec Command

This endpoint opens a websocket. Once open, all frames going through the websocket should be formatted in JSON. Input frames should match the format specified below. Output frames will match the response schema.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.stream_result_of_exec_command_reply import StreamResultOfExecCommandReply
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
    api_instance = openapi_client.InstancesApi(api_client)
    id = 'id_example' # str | ID of the resource to exec on. (optional)
    body_command = ['body_command_example'] # List[str] | Command to exec. Mandatory in the first frame sent (optional)
    body_tty_size_height = 56 # int |  (optional)
    body_tty_size_width = 56 # int |  (optional)
    body_stdin_data = None # bytearray | Data is base64 encoded (optional)
    body_stdin_close = True # bool | Indicate last data frame (optional)
    body_disable_tty = True # bool | Disable TTY. It's enough to specify it in the first frame (optional)
    id_type = 'INVALID' # str | When specified, it is used to determine if the kind of resource the id refers to. If missing, defaults to the instance id. (optional) (default to 'INVALID')

    try:
        # Exec Command
        api_response = api_instance.exec_command(id=id, body_command=body_command, body_tty_size_height=body_tty_size_height, body_tty_size_width=body_tty_size_width, body_stdin_data=body_stdin_data, body_stdin_close=body_stdin_close, body_disable_tty=body_disable_tty, id_type=id_type)
        print("The response of InstancesApi->exec_command:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->exec_command: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| ID of the resource to exec on. | [optional] 
 **body_command** | [**List[str]**](str.md)| Command to exec. Mandatory in the first frame sent | [optional] 
 **body_tty_size_height** | **int**|  | [optional] 
 **body_tty_size_width** | **int**|  | [optional] 
 **body_stdin_data** | **bytearray**| Data is base64 encoded | [optional] 
 **body_stdin_close** | **bool**| Indicate last data frame | [optional] 
 **body_disable_tty** | **bool**| Disable TTY. It&#39;s enough to specify it in the first frame | [optional] 
 **id_type** | **str**| When specified, it is used to determine if the kind of resource the id refers to. If missing, defaults to the instance id. | [optional] [default to &#39;INVALID&#39;]

### Return type

[**StreamResultOfExecCommandReply**](StreamResultOfExecCommandReply.md)

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

# **get_instance**
> GetInstanceReply get_instance(id)

Get Instance

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_instance_reply import GetInstanceReply
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
    api_instance = openapi_client.InstancesApi(api_client)
    id = 'id_example' # str | The id of the instance

    try:
        # Get Instance
        api_response = api_instance.get_instance(id)
        print("The response of InstancesApi->get_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->get_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the instance | 

### Return type

[**GetInstanceReply**](GetInstanceReply.md)

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

# **list_instance_events**
> ListInstanceEventsReply list_instance_events(instance_ids=instance_ids, types=types, limit=limit, offset=offset, order=order)

List Instance events

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_instance_events_reply import ListInstanceEventsReply
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
    api_instance = openapi_client.InstancesApi(api_client)
    instance_ids = ['instance_ids_example'] # List[str] | (Optional) Filter on list of instance id (optional)
    types = ['types_example'] # List[str] | (Optional) Filter on instance event types (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    order = 'order_example' # str | (Optional) Sorts the list in the ascending or the descending order (optional)

    try:
        # List Instance events
        api_response = api_instance.list_instance_events(instance_ids=instance_ids, types=types, limit=limit, offset=offset, order=order)
        print("The response of InstancesApi->list_instance_events:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->list_instance_events: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **instance_ids** | [**List[str]**](str.md)| (Optional) Filter on list of instance id | [optional] 
 **types** | [**List[str]**](str.md)| (Optional) Filter on instance event types | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **order** | **str**| (Optional) Sorts the list in the ascending or the descending order | [optional] 

### Return type

[**ListInstanceEventsReply**](ListInstanceEventsReply.md)

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

# **list_instances**
> ListInstancesReply list_instances(app_id=app_id, service_id=service_id, deployment_id=deployment_id, regional_deployment_id=regional_deployment_id, allocation_id=allocation_id, replica_index=replica_index, statuses=statuses, limit=limit, offset=offset, order=order, starting_time=starting_time, ending_time=ending_time)

List Instances

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_instances_reply import ListInstancesReply
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
    api_instance = openapi_client.InstancesApi(api_client)
    app_id = 'app_id_example' # str | (Optional) Filter on application id (optional)
    service_id = 'service_id_example' # str | (Optional) Filter on service id (optional)
    deployment_id = 'deployment_id_example' # str | (Optional) Filter on deployment id (optional)
    regional_deployment_id = 'regional_deployment_id_example' # str | (Optional) Filter on regional deployment id (optional)
    allocation_id = 'allocation_id_example' # str | (Optional) Filter on allocation id (optional)
    replica_index = 'replica_index_example' # str | (Optional) Filter on replica index (optional)
    statuses = ['statuses_example'] # List[str] | (Optional) Filter on instance statuses (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    order = 'order_example' # str | (Optional) Sorts the list in the ascending or the descending order (optional)
    starting_time = '2013-10-20T19:20:30+01:00' # datetime | (Optional) The starting time of the period of running instance (optional)
    ending_time = '2013-10-20T19:20:30+01:00' # datetime | (Optional) The ending time of the period of running instance (optional)

    try:
        # List Instances
        api_response = api_instance.list_instances(app_id=app_id, service_id=service_id, deployment_id=deployment_id, regional_deployment_id=regional_deployment_id, allocation_id=allocation_id, replica_index=replica_index, statuses=statuses, limit=limit, offset=offset, order=order, starting_time=starting_time, ending_time=ending_time)
        print("The response of InstancesApi->list_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling InstancesApi->list_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **app_id** | **str**| (Optional) Filter on application id | [optional] 
 **service_id** | **str**| (Optional) Filter on service id | [optional] 
 **deployment_id** | **str**| (Optional) Filter on deployment id | [optional] 
 **regional_deployment_id** | **str**| (Optional) Filter on regional deployment id | [optional] 
 **allocation_id** | **str**| (Optional) Filter on allocation id | [optional] 
 **replica_index** | **str**| (Optional) Filter on replica index | [optional] 
 **statuses** | [**List[str]**](str.md)| (Optional) Filter on instance statuses | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **order** | **str**| (Optional) Sorts the list in the ascending or the descending order | [optional] 
 **starting_time** | **datetime**| (Optional) The starting time of the period of running instance | [optional] 
 **ending_time** | **datetime**| (Optional) The ending time of the period of running instance | [optional] 

### Return type

[**ListInstancesReply**](ListInstancesReply.md)

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

