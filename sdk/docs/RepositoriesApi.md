# openapi_client.RepositoriesApi

All URIs are relative to *https://app.koyeb.com*

Method | HTTP request | Description
------------- | ------------- | -------------
[**list_branches**](RepositoriesApi.md#list_branches) | **GET** /v1/git/branches | 
[**list_repositories**](RepositoriesApi.md#list_repositories) | **GET** /v1/git/repositories | 
[**resync_organization**](RepositoriesApi.md#resync_organization) | **POST** /v1/git/sync/organization/{organization_id} | 


# **list_branches**
> KgitproxyListBranchesReply list_branches(repository_id=repository_id, name=name, limit=limit, offset=offset)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.kgitproxy_list_branches_reply import KgitproxyListBranchesReply
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
    api_instance = openapi_client.RepositoriesApi(api_client)
    repository_id = 'repository_id_example' # str | (Optional) Filter on one repository. (optional)
    name = 'name_example' # str | (Optional) Filter on branch name using a fuzzy search. Repository filter is required to enable this filter. (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return. (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return. (optional)

    try:
        api_response = api_instance.list_branches(repository_id=repository_id, name=name, limit=limit, offset=offset)
        print("The response of RepositoriesApi->list_branches:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->list_branches: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **repository_id** | **str**| (Optional) Filter on one repository. | [optional] 
 **name** | **str**| (Optional) Filter on branch name using a fuzzy search. Repository filter is required to enable this filter. | [optional] 
 **limit** | **str**| (Optional) The number of items to return. | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return. | [optional] 

### Return type

[**KgitproxyListBranchesReply**](KgitproxyListBranchesReply.md)

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

# **list_repositories**
> KgitproxyListRepositoriesReply list_repositories(name=name, name_search_op=name_search_op, limit=limit, offset=offset)



### Example

* Api Key Authentication (Bearer):

```python
import openapi_client
from openapi_client.models.kgitproxy_list_repositories_reply import KgitproxyListRepositoriesReply
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
    api_instance = openapi_client.RepositoriesApi(api_client)
    name = 'name_example' # str | (Optional) Filter on repository name using a fuzzy search. (optional)
    name_search_op = 'name_search_op_example' # str | (Optional) Define search operation for repository name. Accept either \"fuzzy\" or \"equality\", use \"fuzzy\" by default. (optional)
    limit = 'limit_example' # str | (Optional) The number of items to return. (optional)
    offset = 'offset_example' # str | (Optional) The offset in the list of item to return. (optional)

    try:
        api_response = api_instance.list_repositories(name=name, name_search_op=name_search_op, limit=limit, offset=offset)
        print("The response of RepositoriesApi->list_repositories:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->list_repositories: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **name** | **str**| (Optional) Filter on repository name using a fuzzy search. | [optional] 
 **name_search_op** | **str**| (Optional) Define search operation for repository name. Accept either \&quot;fuzzy\&quot; or \&quot;equality\&quot;, use \&quot;fuzzy\&quot; by default. | [optional] 
 **limit** | **str**| (Optional) The number of items to return. | [optional] 
 **offset** | **str**| (Optional) The offset in the list of item to return. | [optional] 

### Return type

[**KgitproxyListRepositoriesReply**](KgitproxyListRepositoriesReply.md)

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

# **resync_organization**
> object resync_organization(organization_id)



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
    api_instance = openapi_client.RepositoriesApi(api_client)
    organization_id = 'organization_id_example' # str | 

    try:
        api_response = api_instance.resync_organization(organization_id)
        print("The response of RepositoriesApi->resync_organization:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling RepositoriesApi->resync_organization: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **organization_id** | **str**|  | 

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

