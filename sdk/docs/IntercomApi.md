# openapi_client.IntercomApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_intercom_profile**](IntercomApi.md#get_intercom_profile) | **GET** /v1/intercom/profile | Get intercom profile


# **get_intercom_profile**
> GetIntercomProfileReply get_intercom_profile()

Get intercom profile

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_intercom_profile_reply import GetIntercomProfileReply
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
    api_instance = openapi_client.IntercomApi(api_client)

    try:
        # Get intercom profile
        api_response = api_instance.get_intercom_profile()
        print("The response of IntercomApi->get_intercom_profile:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling IntercomApi->get_intercom_profile: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetIntercomProfileReply**](GetIntercomProfileReply.md)

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

