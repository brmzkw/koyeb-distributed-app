# openapi_client.ProfileApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accept_organization_invitation**](ProfileApi.md#accept_organization_invitation) | **POST** /v1/account/organization_invitations/{id}/accept | 
[**decline_organization_invitation**](ProfileApi.md#decline_organization_invitation) | **POST** /v1/account/organization_invitations/{id}/decline | 
[**get_current_organization**](ProfileApi.md#get_current_organization) | **GET** /v1/account/organization | 
[**get_current_user**](ProfileApi.md#get_current_user) | **GET** /v1/account/profile | 
[**get_o_auth_options**](ProfileApi.md#get_o_auth_options) | **GET** /v1/account/oauth | Get OAuth Providers
[**get_user_organization_invitation**](ProfileApi.md#get_user_organization_invitation) | **GET** /v1/account/organization_invitations/{id} | 
[**list_user_organization_invitations**](ProfileApi.md#list_user_organization_invitations) | **GET** /v1/account/organization_invitations | 
[**o_auth_callback**](ProfileApi.md#o_auth_callback) | **POST** /v1/account/oauth | Authenticate using OAuth
[**resend_email_validation**](ProfileApi.md#resend_email_validation) | **POST** /v1/account/resend_validation | 
[**reset_password**](ProfileApi.md#reset_password) | **POST** /v1/account/reset_password | 
[**signup**](ProfileApi.md#signup) | **POST** /v1/account/signup | 
[**update_password**](ProfileApi.md#update_password) | **POST** /v1/account/update_password | 
[**update_user**](ProfileApi.md#update_user) | **PUT** /v1/account/profile | 
[**update_user2**](ProfileApi.md#update_user2) | **PATCH** /v1/account/profile | 
[**validate**](ProfileApi.md#validate) | **POST** /v1/account/validate/{id} | 


# **accept_organization_invitation**
> AcceptOrganizationInvitationReply accept_organization_invitation(id, body)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.accept_organization_invitation_reply import AcceptOrganizationInvitationReply
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
    api_instance = openapi_client.ProfileApi(api_client)
    id = 'id_example' # str | The id of the organization invitation to accept
    body = None # object | 

    try:
        api_response = api_instance.accept_organization_invitation(id, body)
        print("The response of ProfileApi->accept_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->accept_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the organization invitation to accept | 
 **body** | **object**|  | 

### Return type

[**AcceptOrganizationInvitationReply**](AcceptOrganizationInvitationReply.md)

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

# **decline_organization_invitation**
> DeclineOrganizationInvitationReply decline_organization_invitation(id, body)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.decline_organization_invitation_reply import DeclineOrganizationInvitationReply
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
    api_instance = openapi_client.ProfileApi(api_client)
    id = 'id_example' # str | The id of the organization invitation to decline
    body = None # object | 

    try:
        api_response = api_instance.decline_organization_invitation(id, body)
        print("The response of ProfileApi->decline_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->decline_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the organization invitation to decline | 
 **body** | **object**|  | 

### Return type

[**DeclineOrganizationInvitationReply**](DeclineOrganizationInvitationReply.md)

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

# **get_current_organization**
> GetOrganizationReply get_current_organization()



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
    api_instance = openapi_client.ProfileApi(api_client)

    try:
        api_response = api_instance.get_current_organization()
        print("The response of ProfileApi->get_current_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_current_organization: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

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

# **get_current_user**
> UserReply get_current_user()



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.user_reply import UserReply
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
    api_instance = openapi_client.ProfileApi(api_client)

    try:
        api_response = api_instance.get_current_user()
        print("The response of ProfileApi->get_current_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_current_user: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**UserReply**](UserReply.md)

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

# **get_o_auth_options**
> GetOAuthOptionsReply get_o_auth_options(action=action, metadata=metadata)

Get OAuth Providers

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_o_auth_options_reply import GetOAuthOptionsReply
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
    api_instance = openapi_client.ProfileApi(api_client)
    action = 'signin' # str | Which authentication flow is being initiated (optional) (default to 'signin')
    metadata = 'metadata_example' # str | A small (limited to 400 characters) string of arbitrary metadata which will be encoded in the state (optional)

    try:
        # Get OAuth Providers
        api_response = api_instance.get_o_auth_options(action=action, metadata=metadata)
        print("The response of ProfileApi->get_o_auth_options:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_o_auth_options: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **action** | **str**| Which authentication flow is being initiated | [optional] [default to &#39;signin&#39;]
 **metadata** | **str**| A small (limited to 400 characters) string of arbitrary metadata which will be encoded in the state | [optional] 

### Return type

[**GetOAuthOptionsReply**](GetOAuthOptionsReply.md)

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

# **get_user_organization_invitation**
> GetUserOrganizationInvitationReply get_user_organization_invitation(id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_user_organization_invitation_reply import GetUserOrganizationInvitationReply
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
    api_instance = openapi_client.ProfileApi(api_client)
    id = 'id_example' # str | The id of the organization invitation to get

    try:
        api_response = api_instance.get_user_organization_invitation(id)
        print("The response of ProfileApi->get_user_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->get_user_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the organization invitation to get | 

### Return type

[**GetUserOrganizationInvitationReply**](GetUserOrganizationInvitationReply.md)

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

# **list_user_organization_invitations**
> ListUserOrganizationInvitationsReply list_user_organization_invitations(limit=limit, offset=offset, statuses=statuses)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_user_organization_invitations_reply import ListUserOrganizationInvitationsReply
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
    api_instance = openapi_client.ProfileApi(api_client)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    statuses = ['statuses_example'] # List[str] | (Optional) Filter on organization invitation statuses (optional)

    try:
        api_response = api_instance.list_user_organization_invitations(limit=limit, offset=offset, statuses=statuses)
        print("The response of ProfileApi->list_user_organization_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->list_user_organization_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **statuses** | [**List[str]**](str.md)| (Optional) Filter on organization invitation statuses | [optional] 

### Return type

[**ListUserOrganizationInvitationsReply**](ListUserOrganizationInvitationsReply.md)

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

# **o_auth_callback**
> OAuthCallbackReply o_auth_callback(body, seon_fp=seon_fp)

Authenticate using OAuth

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.o_auth_callback_reply import OAuthCallbackReply
from openapi_client.models.o_auth_callback_request import OAuthCallbackRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    body = openapi_client.OAuthCallbackRequest() # OAuthCallbackRequest | 
    seon_fp = 'seon_fp_example' # str | Seon Fingerprint (optional)

    try:
        # Authenticate using OAuth
        api_response = api_instance.o_auth_callback(body, seon_fp=seon_fp)
        print("The response of ProfileApi->o_auth_callback:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->o_auth_callback: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**OAuthCallbackRequest**](OAuthCallbackRequest.md)|  | 
 **seon_fp** | **str**| Seon Fingerprint | [optional] 

### Return type

[**OAuthCallbackReply**](OAuthCallbackReply.md)

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

# **resend_email_validation**
> object resend_email_validation(body)



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
    api_instance = openapi_client.ProfileApi(api_client)
    body = None # object | 

    try:
        api_response = api_instance.resend_email_validation(body)
        print("The response of ProfileApi->resend_email_validation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->resend_email_validation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | **object**|  | 

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

# **reset_password**
> object reset_password(body)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.reset_password_request import ResetPasswordRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    body = openapi_client.ResetPasswordRequest() # ResetPasswordRequest | 

    try:
        api_response = api_instance.reset_password(body)
        print("The response of ProfileApi->reset_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->reset_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**ResetPasswordRequest**](ResetPasswordRequest.md)|  | 

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

# **signup**
> LoginReply signup(body, seon_fp=seon_fp)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.create_account_request import CreateAccountRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    body = openapi_client.CreateAccountRequest() # CreateAccountRequest | Create new account
    seon_fp = 'seon_fp_example' # str | Seon Fingerprint (optional)

    try:
        api_response = api_instance.signup(body, seon_fp=seon_fp)
        print("The response of ProfileApi->signup:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->signup: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateAccountRequest**](CreateAccountRequest.md)| Create new account | 
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

# **update_password**
> LoginReply update_password(body, seon_fp=seon_fp)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.login_reply import LoginReply
from openapi_client.models.update_password_request import UpdatePasswordRequest
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
    api_instance = openapi_client.ProfileApi(api_client)
    body = openapi_client.UpdatePasswordRequest() # UpdatePasswordRequest | 
    seon_fp = 'seon_fp_example' # str | Seon Fingerprint (optional)

    try:
        api_response = api_instance.update_password(body, seon_fp=seon_fp)
        print("The response of ProfileApi->update_password:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->update_password: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdatePasswordRequest**](UpdatePasswordRequest.md)|  | 
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

# **update_user**
> UserReply update_user(user, update_mask=update_mask)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.update_user_request_user_update_body import UpdateUserRequestUserUpdateBody
from openapi_client.models.user_reply import UserReply
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
    api_instance = openapi_client.ProfileApi(api_client)
    user = openapi_client.UpdateUserRequestUserUpdateBody() # UpdateUserRequestUserUpdateBody | 
    update_mask = 'update_mask_example' # str |  (optional)

    try:
        api_response = api_instance.update_user(user, update_mask=update_mask)
        print("The response of ProfileApi->update_user:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->update_user: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UpdateUserRequestUserUpdateBody**](UpdateUserRequestUserUpdateBody.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**UserReply**](UserReply.md)

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

# **update_user2**
> UserReply update_user2(user, update_mask=update_mask)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.update_user_request_user_update_body import UpdateUserRequestUserUpdateBody
from openapi_client.models.user_reply import UserReply
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
    api_instance = openapi_client.ProfileApi(api_client)
    user = openapi_client.UpdateUserRequestUserUpdateBody() # UpdateUserRequestUserUpdateBody | 
    update_mask = 'update_mask_example' # str |  (optional)

    try:
        api_response = api_instance.update_user2(user, update_mask=update_mask)
        print("The response of ProfileApi->update_user2:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->update_user2: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **user** | [**UpdateUserRequestUserUpdateBody**](UpdateUserRequestUserUpdateBody.md)|  | 
 **update_mask** | **str**|  | [optional] 

### Return type

[**UserReply**](UserReply.md)

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

# **validate**
> LoginReply validate(id, seon_fp=seon_fp)



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
    api_instance = openapi_client.ProfileApi(api_client)
    id = 'id_example' # str | 
    seon_fp = 'seon_fp_example' # str | Seon Fingerprint (optional)

    try:
        api_response = api_instance.validate(id, seon_fp=seon_fp)
        print("The response of ProfileApi->validate:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ProfileApi->validate: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 
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

