# openapi_client.CatalogRegionsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_region**](CatalogRegionsApi.md#get_region) | **GET** /v1/catalog/regions/{id} | Get Region
[**list_regions**](CatalogRegionsApi.md#list_regions) | **GET** /v1/catalog/regions | List Region


# **get_region**
> GetRegionReply get_region(id)

Get Region

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_region_reply import GetRegionReply
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
    api_instance = openapi_client.CatalogRegionsApi(api_client)
    id = 'id_example' # str | The name of the region

    try:
        # Get Region
        api_response = api_instance.get_region(id)
        print("The response of CatalogRegionsApi->get_region:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogRegionsApi->get_region: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The name of the region | 

### Return type

[**GetRegionReply**](GetRegionReply.md)

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

# **list_regions**
> ListRegionsReply list_regions(limit=limit, offset=offset, id=id)

List Region

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_regions_reply import ListRegionsReply
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
    api_instance = openapi_client.CatalogRegionsApi(api_client)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    id = 'id_example' # str | (Optional) A filter for regions (optional)

    try:
        # List Region
        api_response = api_instance.list_regions(limit=limit, offset=offset, id=id)
        print("The response of CatalogRegionsApi->list_regions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogRegionsApi->list_regions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **id** | **str**| (Optional) A filter for regions | [optional] 

### Return type

[**ListRegionsReply**](ListRegionsReply.md)

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

