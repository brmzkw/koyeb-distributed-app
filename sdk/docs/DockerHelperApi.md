# openapi_client.DockerHelperApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**verify_docker_image**](DockerHelperApi.md#verify_docker_image) | **GET** /v1/docker-helper/verify | Verify if a docker image is reachable


# **verify_docker_image**
> VerifyDockerImageReply verify_docker_image(image=image, secret_id=secret_id)

Verify if a docker image is reachable

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.verify_docker_image_reply import VerifyDockerImageReply
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
    api_instance = openapi_client.DockerHelperApi(api_client)
    image = 'image_example' # str | The full image uri to be verified (optional)
    secret_id = 'secret_id_example' # str | (Optional) the id of the secret to use to authenticate to the registry (optional)

    try:
        # Verify if a docker image is reachable
        api_response = api_instance.verify_docker_image(image=image, secret_id=secret_id)
        print("The response of DockerHelperApi->verify_docker_image:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DockerHelperApi->verify_docker_image: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **image** | **str**| The full image uri to be verified | [optional] 
 **secret_id** | **str**| (Optional) the id of the secret to use to authenticate to the registry | [optional] 

### Return type

[**VerifyDockerImageReply**](VerifyDockerImageReply.md)

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

