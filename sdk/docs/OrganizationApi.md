# openapi_client.OrganizationApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization**](OrganizationApi.md#create_organization) | **POST** /v1/organizations | Create organization
[**deactivate_organization**](OrganizationApi.md#deactivate_organization) | **POST** /v1/organizations/{id}/deactivate | Deactivate an organization
[**delete_organization**](OrganizationApi.md#delete_organization) | **DELETE** /v1/organizations/{id} | Delete an organization
[**get_github_installation**](OrganizationApi.md#get_github_installation) | **GET** /v1/github/installation | Fetch github installation configuration
[**get_organization**](OrganizationApi.md#get_organization) | **GET** /v1/organizations/{id} | Get organization
[**github_installation**](OrganizationApi.md#github_installation) | **POST** /v1/github/installation | Start github installation
[**github_installation_callback**](OrganizationApi.md#github_installation_callback) | **POST** /v1/github/installation/callback | Github callback for app installation
[**reactivate_organization**](OrganizationApi.md#reactivate_organization) | **POST** /v1/organizations/{id}/reactivate | Reactivate an organization
[**switch_organization**](OrganizationApi.md#switch_organization) | **POST** /v1/organizations/{id}/switch | Switch organization context
[**update_organization**](OrganizationApi.md#update_organization) | **PUT** /v1/organizations/{id} | Update organization
[**update_organization2**](OrganizationApi.md#update_organization2) | **PATCH** /v1/organizations/{id} | Update organization
[**update_organization_plan**](OrganizationApi.md#update_organization_plan) | **POST** /v1/organizations/{id}/plan | Update organization plan
[**upsert_signup_qualification**](OrganizationApi.md#upsert_signup_qualification) | **POST** /v1/organizations/{id}/signup_qualification | Upsert organization&#39;s signup qualification


# **create_organization**
> CreateOrganizationReply create_organization(body)

Create organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.create_organization_reply import CreateOrganizationReply
from openapi_client.models.create_organization_request import CreateOrganizationRequest
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
    api_instance = openapi_client.OrganizationApi(api_client)
    body = openapi_client.CreateOrganizationRequest() # CreateOrganizationRequest | 

    try:
        # Create organization
        api_response = api_instance.create_organization(body)
        print("The response of OrganizationApi->create_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->create_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrganizationRequest**](CreateOrganizationRequest.md)|  | 

### Return type

[**CreateOrganizationReply**](CreateOrganizationReply.md)

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

# **deactivate_organization**
> DeactivateOrganizationReply deactivate_organization(id, body)

Deactivate an organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.deactivate_organization_reply import DeactivateOrganizationReply
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Deactivate an organization
        api_response = api_instance.deactivate_organization(id, body)
        print("The response of OrganizationApi->deactivate_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->deactivate_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**DeactivateOrganizationReply**](DeactivateOrganizationReply.md)

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

# **delete_organization**
> DeleteOrganizationReply delete_organization(id)

Delete an organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.delete_organization_reply import DeleteOrganizationReply
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Delete an organization
        api_response = api_instance.delete_organization(id)
        print("The response of OrganizationApi->delete_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->delete_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**DeleteOrganizationReply**](DeleteOrganizationReply.md)

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

# **get_github_installation**
> GetGithubInstallationReply get_github_installation()

Fetch github installation configuration

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_github_installation_reply import GetGithubInstallationReply
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
    api_instance = openapi_client.OrganizationApi(api_client)

    try:
        # Fetch github installation configuration
        api_response = api_instance.get_github_installation()
        print("The response of OrganizationApi->get_github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_github_installation: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**GetGithubInstallationReply**](GetGithubInstallationReply.md)

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

# **get_organization**
> GetOrganizationReply get_organization(id)

Get organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_organization_reply import GetOrganizationReply
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 

    try:
        # Get organization
        api_response = api_instance.get_organization(id)
        print("The response of OrganizationApi->get_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->get_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**GetOrganizationReply**](GetOrganizationReply.md)

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

# **github_installation**
> GithubInstallationReply github_installation(body)

Start github installation

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.github_installation_reply import GithubInstallationReply
from openapi_client.models.github_installation_request import GithubInstallationRequest
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
    api_instance = openapi_client.OrganizationApi(api_client)
    body = openapi_client.GithubInstallationRequest() # GithubInstallationRequest | 

    try:
        # Start github installation
        api_response = api_instance.github_installation(body)
        print("The response of OrganizationApi->github_installation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->github_installation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GithubInstallationRequest**](GithubInstallationRequest.md)|  | 

### Return type

[**GithubInstallationReply**](GithubInstallationReply.md)

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

# **github_installation_callback**
> object github_installation_callback(body)

Github callback for app installation

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.github_installation_callback_request import GithubInstallationCallbackRequest
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
    api_instance = openapi_client.OrganizationApi(api_client)
    body = openapi_client.GithubInstallationCallbackRequest() # GithubInstallationCallbackRequest | 

    try:
        # Github callback for app installation
        api_response = api_instance.github_installation_callback(body)
        print("The response of OrganizationApi->github_installation_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->github_installation_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**GithubInstallationCallbackRequest**](GithubInstallationCallbackRequest.md)|  | 

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

# **reactivate_organization**
> ReactivateOrganizationReply reactivate_organization(id, body)

Reactivate an organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.reactivate_organization_reply import ReactivateOrganizationReply
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 

    try:
        # Reactivate an organization
        api_response = api_instance.reactivate_organization(id, body)
        print("The response of OrganizationApi->reactivate_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->reactivate_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 

### Return type

[**ReactivateOrganizationReply**](ReactivateOrganizationReply.md)

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

# **switch_organization**
> LoginReply switch_organization(id, body, seon_fp=seon_fp)

Switch organization context

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.login_reply import LoginReply
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = None # object | 
    seon_fp = 'seon_fp_example' # str | Seon Fingerprint (optional)

    try:
        # Switch organization context
        api_response = api_instance.switch_organization(id, body, seon_fp=seon_fp)
        print("The response of OrganizationApi->switch_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->switch_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | **object**|  | 
 **seon_fp** | **str**| Seon Fingerprint | [optional] 

### Return type

[**LoginReply**](LoginReply.md)

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

# **update_organization**
> UpdateOrganizationReply update_organization(id, organization, update_mask=update_mask)

Update organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.organization import Organization
from openapi_client.models.update_organization_reply import UpdateOrganizationReply
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    organization = openapi_client.Organization() # Organization | 
    update_mask = 'update_mask_example' # str |  (optional)

    try:
        # Update organization
        api_response = api_instance.update_organization(id, organization, update_mask=update_mask)
        print("The response of OrganizationApi->update_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organization** | [**Organization**](Organization.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**UpdateOrganizationReply**](UpdateOrganizationReply.md)

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

# **update_organization2**
> UpdateOrganizationReply update_organization2(id, organization, update_mask=update_mask)

Update organization

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.organization import Organization
from openapi_client.models.update_organization_reply import UpdateOrganizationReply
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    organization = openapi_client.Organization() # Organization | 
    update_mask = 'update_mask_example' # str |  (optional)

    try:
        # Update organization
        api_response = api_instance.update_organization2(id, organization, update_mask=update_mask)
        print("The response of OrganizationApi->update_organization2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_organization2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **organization** | [**Organization**](Organization.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**UpdateOrganizationReply**](UpdateOrganizationReply.md)

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

# **update_organization_plan**
> UpdateOrganizationPlanReply update_organization_plan(id, body)

Update organization plan

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.update_organization_plan_reply import UpdateOrganizationPlanReply
from openapi_client.models.update_organization_plan_request import UpdateOrganizationPlanRequest
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = openapi_client.UpdateOrganizationPlanRequest() # UpdateOrganizationPlanRequest | 

    try:
        # Update organization plan
        api_response = api_instance.update_organization_plan(id, body)
        print("The response of OrganizationApi->update_organization_plan:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->update_organization_plan: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UpdateOrganizationPlanRequest**](UpdateOrganizationPlanRequest.md)|  | 

### Return type

[**UpdateOrganizationPlanReply**](UpdateOrganizationPlanReply.md)

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

# **upsert_signup_qualification**
> UpsertSignupQualificationReply upsert_signup_qualification(id, body)

Upsert organization's signup qualification

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.upsert_signup_qualification_reply import UpsertSignupQualificationReply
from openapi_client.models.upsert_signup_qualification_request import UpsertSignupQualificationRequest
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
    api_instance = openapi_client.OrganizationApi(api_client)
    id = 'id_example' # str | 
    body = openapi_client.UpsertSignupQualificationRequest() # UpsertSignupQualificationRequest | 

    try:
        # Upsert organization's signup qualification
        api_response = api_instance.upsert_signup_qualification(id, body)
        print("The response of OrganizationApi->upsert_signup_qualification:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationApi->upsert_signup_qualification: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
 **body** | [**UpsertSignupQualificationRequest**](UpsertSignupQualificationRequest.md)|  | 

### Return type

[**UpsertSignupQualificationReply**](UpsertSignupQualificationReply.md)

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

