# KsearchSearchReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organizations** | [**List[KsearchOrganization]**](KsearchOrganization.md) |  | [optional] 
**users** | [**List[KsearchUser]**](KsearchUser.md) |  | [optional] 
**apps** | [**List[KsearchApp]**](KsearchApp.md) |  | [optional] 
**services** | [**List[KsearchService]**](KsearchService.md) |  | [optional] 
**global_deployments** | [**List[KsearchGlobalDeployment]**](KsearchGlobalDeployment.md) |  | [optional] 
**regional_deployments** | [**List[KsearchRegionalDeployment]**](KsearchRegionalDeployment.md) |  | [optional] 
**instances** | [**List[KsearchInstance]**](KsearchInstance.md) |  | [optional] 

## Example

```python
from openapi_client.models.ksearch_search_reply import KsearchSearchReply

# TODO update the JSON string below
json = "{}"
# create an instance of KsearchSearchReply from a JSON string
ksearch_search_reply_instance = KsearchSearchReply.from_json(json)
# print the JSON string representation of the object
print(KsearchSearchReply.to_json())

# convert the object into a dict
ksearch_search_reply_dict = ksearch_search_reply_instance.to_dict()
# create an instance of KsearchSearchReply from a dict
ksearch_search_reply_from_dict = KsearchSearchReply.from_dict(ksearch_search_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


