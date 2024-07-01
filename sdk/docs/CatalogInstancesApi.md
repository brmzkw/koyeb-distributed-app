# openapi_client.CatalogInstancesApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_catalog_instance**](CatalogInstancesApi.md#get_catalog_instance) | **GET** /v1/catalog/instances/{id} | Get Instance
[**list_catalog_instances**](CatalogInstancesApi.md#list_catalog_instances) | **GET** /v1/catalog/instances | List Instance


# **get_catalog_instance**
> GetCatalogInstanceReply get_catalog_instance(id)

Get Instance

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_catalog_instance_reply import GetCatalogInstanceReply
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
    api_instance = openapi_client.CatalogInstancesApi(api_client)
    id = 'id_example' # str | The name of the instance

    try:
        # Get Instance
        api_response = api_instance.get_catalog_instance(id)
        print("The response of CatalogInstancesApi->get_catalog_instance:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogInstancesApi->get_catalog_instance: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of the instance | 

### Return type

[**GetCatalogInstanceReply**](GetCatalogInstanceReply.md)

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

# **list_catalog_instances**
> ListCatalogInstancesReply list_catalog_instances(limit=limit, offset=offset, id=id)

List Instance

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_catalog_instances_reply import ListCatalogInstancesReply
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
    api_instance = openapi_client.CatalogInstancesApi(api_client)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    id = 'id_example' # str | (Optional) A filter for instances (optional)

    try:
        # List Instance
        api_response = api_instance.list_catalog_instances(limit=limit, offset=offset, id=id)
        print("The response of CatalogInstancesApi->list_catalog_instances:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogInstancesApi->list_catalog_instances: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **id** | **str**| (Optional) A filter for instances | [optional] 

### Return type

[**ListCatalogInstancesReply**](ListCatalogInstancesReply.md)

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

