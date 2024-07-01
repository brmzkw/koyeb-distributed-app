# openapi_client.OrganizationInvitationsApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_organization_invitation**](OrganizationInvitationsApi.md#create_organization_invitation) | **POST** /v1/organization_invitations | 
[**delete_organization_invitation**](OrganizationInvitationsApi.md#delete_organization_invitation) | **DELETE** /v1/organization_invitations/{id} | 
[**get_organization_invitation**](OrganizationInvitationsApi.md#get_organization_invitation) | **GET** /v1/organization_invitations/{id} | 
[**list_organization_invitations**](OrganizationInvitationsApi.md#list_organization_invitations) | **GET** /v1/organization_invitations | 
[**resend_organization_invitation**](OrganizationInvitationsApi.md#resend_organization_invitation) | **POST** /v1/organization_invitations/{id}/resend | 


# **create_organization_invitation**
> CreateOrganizationInvitationReply create_organization_invitation(body)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.create_organization_invitation_reply import CreateOrganizationInvitationReply
from openapi_client.models.create_organization_invitation_request import CreateOrganizationInvitationRequest
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
    api_instance = openapi_client.OrganizationInvitationsApi(api_client)
    body = openapi_client.CreateOrganizationInvitationRequest() # CreateOrganizationInvitationRequest | 

    try:
        api_response = api_instance.create_organization_invitation(body)
        print("The response of OrganizationInvitationsApi->create_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->create_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateOrganizationInvitationRequest**](CreateOrganizationInvitationRequest.md)|  | 

### Return type

[**CreateOrganizationInvitationReply**](CreateOrganizationInvitationReply.md)

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

# **delete_organization_invitation**
> object delete_organization_invitation(id)



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
    api_instance = openapi_client.OrganizationInvitationsApi(api_client)
    id = 'id_example' # str | The id of the organization invitation to delete

    try:
        api_response = api_instance.delete_organization_invitation(id)
        print("The response of OrganizationInvitationsApi->delete_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->delete_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the organization invitation to delete | 

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

# **get_organization_invitation**
> GetOrganizationInvitationReply get_organization_invitation(id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.get_organization_invitation_reply import GetOrganizationInvitationReply
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
    api_instance = openapi_client.OrganizationInvitationsApi(api_client)
    id = 'id_example' # str | The id of the invitation to get

    try:
        api_response = api_instance.get_organization_invitation(id)
        print("The response of OrganizationInvitationsApi->get_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->get_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the invitation to get | 

### Return type

[**GetOrganizationInvitationReply**](GetOrganizationInvitationReply.md)

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

# **list_organization_invitations**
> ListOrganizationInvitationsReply list_organization_invitations(limit=limit, offset=offset, statuses=statuses, user_id=user_id)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_organization_invitations_reply import ListOrganizationInvitationsReply
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
    api_instance = openapi_client.OrganizationInvitationsApi(api_client)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    statuses = ['statuses_example'] # List[str] | (Optional) Filter on organization invitation statuses (optional)
    user_id = 'user_id_example' # str | (Optional) Filter on invitee ID. Will match both invitations sent to that user_id and invitations sent to the email of that user_id. The only valid value is the requester's user_id (optional)

    try:
        api_response = api_instance.list_organization_invitations(limit=limit, offset=offset, statuses=statuses, user_id=user_id)
        print("The response of OrganizationInvitationsApi->list_organization_invitations:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->list_organization_invitations: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **statuses** | [**List[str]**](str.md)| (Optional) Filter on organization invitation statuses | [optional] 
 **user_id** | **str**| (Optional) Filter on invitee ID. Will match both invitations sent to that user_id and invitations sent to the email of that user_id. The only valid value is the requester&#39;s user_id | [optional] 

### Return type

[**ListOrganizationInvitationsReply**](ListOrganizationInvitationsReply.md)

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

# **resend_organization_invitation**
> ResendOrganizationInvitationReply resend_organization_invitation(id, body)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.resend_organization_invitation_reply import ResendOrganizationInvitationReply
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
    api_instance = openapi_client.OrganizationInvitationsApi(api_client)
    id = 'id_example' # str | The id of the organization invitation to resend
    body = None # object | 

    try:
        api_response = api_instance.resend_organization_invitation(id, body)
        print("The response of OrganizationInvitationsApi->resend_organization_invitation:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationInvitationsApi->resend_organization_invitation: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**| The id of the organization invitation to resend | 
 **body** | **object**|  | 

### Return type

[**ResendOrganizationInvitationReply**](ResendOrganizationInvitationReply.md)

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

