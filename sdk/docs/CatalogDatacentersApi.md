# openapi_client.CatalogDatacentersApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_datacenters**](CatalogDatacentersApi.md#list_datacenters) | **GET** /v1/catalog/datacenters | List datacenters


# **list_datacenters**
> ListDatacentersReply list_datacenters()

List datacenters

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_datacenters_reply import ListDatacentersReply
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
    api_instance = openapi_client.CatalogDatacentersApi(api_client)

    try:
        # List datacenters
        api_response = api_instance.list_datacenters()
        print("The response of CatalogDatacentersApi->list_datacenters:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CatalogDatacentersApi->list_datacenters: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ListDatacentersReply**](ListDatacentersReply.md)

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

