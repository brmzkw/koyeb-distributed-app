# openapi_client.BillingApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**has_unpaid_invoices**](BillingApi.md#has_unpaid_invoices) | **GET** /v1/billing/has_unpaid_invoices | Experimental: Has unpaid invoices
[**manage**](BillingApi.md#manage) | **GET** /v1/billing/manage | 
[**next_invoice**](BillingApi.md#next_invoice) | **GET** /v1/billing/next_invoice | Experimental: Fetch next invoice


# **has_unpaid_invoices**
> HasUnpaidInvoicesReply has_unpaid_invoices()

Experimental: Has unpaid invoices

WARNING: Please don't use the following method. Koyeb doesn't guarantee backwards compatible breaking change and reserve the right to completely drop it without notice. USE AT YOUR OWN RISK.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.has_unpaid_invoices_reply import HasUnpaidInvoicesReply
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
    api_instance = openapi_client.BillingApi(api_client)

    try:
        # Experimental: Has unpaid invoices
        api_response = api_instance.has_unpaid_invoices()
        print("The response of BillingApi->has_unpaid_invoices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->has_unpaid_invoices: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**HasUnpaidInvoicesReply**](HasUnpaidInvoicesReply.md)

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

# **manage**
> ManageReply manage()



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.manage_reply import ManageReply
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
    api_instance = openapi_client.BillingApi(api_client)

    try:
        api_response = api_instance.manage()
        print("The response of BillingApi->manage:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->manage: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**ManageReply**](ManageReply.md)

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

# **next_invoice**
> NextInvoiceReply next_invoice()

Experimental: Fetch next invoice

WARNING: Please don't use the following method. Koyeb doesn't guarantee backwards compatible breaking change and reserve the right to completely drop it without notice. USE AT YOUR OWN RISK.

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.next_invoice_reply import NextInvoiceReply
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
    api_instance = openapi_client.BillingApi(api_client)

    try:
        # Experimental: Fetch next invoice
        api_response = api_instance.next_invoice()
        print("The response of BillingApi->next_invoice:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BillingApi->next_invoice: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**NextInvoiceReply**](NextInvoiceReply.md)

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

