# openapi_client.OrganizationMembersApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_organization_members**](OrganizationMembersApi.md#list_organization_members) | **GET** /v1/organization_members | List organization members
[**remove_organization_member**](OrganizationMembersApi.md#remove_organization_member) | **DELETE** /v1/organization_members/{id} | Remove an organization member


# **list_organization_members**
> ListOrganizationMembersReply list_organization_members(limit=limit, offset=offset, organization_id=organization_id, user_id=user_id)

List organization members

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.list_organization_members_reply import ListOrganizationMembersReply
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
    api_instance = openapi_client.OrganizationMembersApi(api_client)
    limit = 'limit_example' # str | (Optional) The number of items to return (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return (optional)
    organization_id = 'organization_id_example' # str | (Optional) Filter for an organization (optional)
    user_id = 'user_id_example' # str | (Optional) Filter for an user (optional)

    try:
        # List organization members
        api_response = api_instance.list_organization_members(limit=limit, offset=offset, organization_id=organization_id, user_id=user_id)
        print("The response of OrganizationMembersApi->list_organization_members:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationMembersApi->list_organization_members: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **limit** | **str**| (Optional) The number of items to return | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return | [optional] 
 **organization_id** | **str**| (Optional) Filter for an organization | [optional] 
 **user_id** | **str**| (Optional) Filter for an user | [optional] 

### Return type

[**ListOrganizationMembersReply**](ListOrganizationMembersReply.md)

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

# **remove_organization_member**
> RemoveOrganizationMemberReply remove_organization_member(id)

Remove an organization member

### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.remove_organization_member_reply import RemoveOrganizationMemberReply
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
    api_instance = openapi_client.OrganizationMembersApi(api_client)
    id = 'id_example' # str | 

    try:
        # Remove an organization member
        api_response = api_instance.remove_organization_member(id)
        print("The response of OrganizationMembersApi->remove_organization_member:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling OrganizationMembersApi->remove_organization_member: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

[**RemoveOrganizationMemberReply**](RemoveOrganizationMemberReply.md)

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

