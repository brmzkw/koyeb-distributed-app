# KgitproxyRepository


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**is_private** | **bool** |  | [optional] 
**is_disabled** | **bool** |  | [optional] 
**default_branch** | **str** |  | [optional] 
**provider** | [**KgitproxyRepositoryProvider**](KgitproxyRepositoryProvider.md) |  | [optional] 
**last_push_date** | **datetime** |  | [optional] 
**github** | [**KgitproxyGitHubRepository**](KgitproxyGitHubRepository.md) |  | [optional] 

## Example

```python
from openapi_client.models.kgitproxy_repository import KgitproxyRepository

# TODO update the JSON string below
json = "{}"
# create an instance of KgitproxyRepository from a JSON string
kgitproxy_repository_instance = KgitproxyRepository.from_json(json)
# print the JSON string representation of the object
print(KgitproxyRepository.to_json())

# convert the object into a dict
kgitproxy_repository_dict = kgitproxy_repository_instance.to_dict()
# create an instance of KgitproxyRepository from a dict
kgitproxy_repository_from_dict = KgitproxyRepository.from_dict(kgitproxy_repository_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


