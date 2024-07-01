# openapi_client.CredentialsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_credential**](CredentialsApi.md#create_credential) | **POST** /v1/credentials | Create credential
[**delete_credential**](CredentialsApi.md#delete_credential) | **DELETE** /v1/credentials/{id} | Delete credential
[**get_credential**](CredentialsApi.md#get_credential) | **GET** /v1/credentials/{id} | Get credential
[**list_credentials**](CredentialsApi.md#list_credentials) | **GET** /v1/credentials | List credentials
[**update_credential**](CredentialsApi.md#update_credential) | **PUT** /v1/credentials/{id} | Update credential
[**update_credential2**](CredentialsApi.md#update_credential2) | **PATCH** /v1/credentials/{id} | Update credential


# **create_credential**
> CreateCredentialReply create_credential(credential)

Create credential

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.create_credential import CreateCredential
from openapi_client.models.create_credential_reply import CreateCredentialReply
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
    api_instance = openapi_client.CredentialsApi(api_client)
    credential = openapi_client.CreateCredential() # CreateCredential | 

    try:
        # Create credential
        api_response = api_instance.create_credential(credential)
        print("The response of CredentialsApi->create_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->create_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **credential** | [**CreateCredential**](CreateCredential.md)|  | 

### Return type

[**CreateCredentialReply**](CreateCredentialReply.md)

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

# **delete_credential**
> object delete_credential(id)

Delete credential

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
    api_instance = openapi_client.CredentialsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete credential
        api_response = api_instance.delete_credential(id)
        print("The response of CredentialsApi->delete_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->delete_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

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

# **get_credential**
> GetCredentialReply get_credential(id)

Get credential

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_credential_reply import GetCredentialReply
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
    api_instance = openapi_client.CredentialsApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get credential
        api_response = api_instance.get_credential(id)
        print("The response of CredentialsApi->get_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->get_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetCredentialReply**](GetCredentialReply.md)

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

# **list_credentials**
> ListCredentialsReply list_credentials(type=type, name=name, organization_id=organization_id, user_id=user_id, limit=limit, offset=offset)

List credentials

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_credentials_reply import ListCredentialsReply
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
    api_instance = openapi_client.CredentialsApi(api_client)
    type = 'INVALID' # str | (Optional) A filter for type (optional) (default to 'INVALID')
    name = 'name_example' # str | (Optional) A filter for name (optional)
    organization_id = 'organization_id_example' # str | (Optional) Filter for an organization (optional)
    user_id = 'user_id_example' # str | (Optional) Filter for an user (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)

    try:
        # List credentials
        api_response = api_instance.list_credentials(type=type, name=name, organization_id=organization_id, user_id=user_id, limit=limit, offset=offset)
        print("The response of CredentialsApi->list_credentials:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->list_credentials: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **type** | **str**| (Optional) A filter for type | [optional] [default to &#39;INVALID&#39;]
 **name** | **str**| (Optional) A filter for name | [optional] 
 **organization_id** | **str**| (Optional) Filter for an organization | [optional] 
 **user_id** | **str**| (Optional) Filter for an user | [optional] 
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 

### Return type

[**ListCredentialsReply**](ListCredentialsReply.md)

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

# **update_credential**
> UpdateCredentialReply update_credential(id, credential, update_mask=update_mask)

Update credential

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.credential import Credential
from openapi_client.models.update_credential_reply import UpdateCredentialReply
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
    api_instance = openapi_client.CredentialsApi(api_client)
    id = 'id_example' # str | 
    credential = openapi_client.Credential() # Credential | 
    update_mask = 'update_mask_example' # str |  (optional)

    try:
        # Update credential
        api_response = api_instance.update_credential(id, credential, update_mask=update_mask)
        print("The response of CredentialsApi->update_credential:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_credential: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **credential** | [**Credential**](Credential.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**UpdateCredentialReply**](UpdateCredentialReply.md)

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

# **update_credential2**
> UpdateCredentialReply update_credential2(id, credential, update_mask=update_mask)

Update credential

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.credential import Credential
from openapi_client.models.update_credential_reply import UpdateCredentialReply
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
    api_instance = openapi_client.CredentialsApi(api_client)
    id = 'id_example' # str | 
    credential = openapi_client.Credential() # Credential | 
    update_mask = 'update_mask_example' # str |  (optional)

    try:
        # Update credential
        api_response = api_instance.update_credential2(id, credential, update_mask=update_mask)
        print("The response of CredentialsApi->update_credential2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling CredentialsApi->update_credential2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **credential** | [**Credential**](Credential.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**UpdateCredentialReply**](UpdateCredentialReply.md)

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

