# KgitproxyBranch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**repository_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**is_default** | **bool** |  | [optional] 
**is_protected** | **bool** |  | [optional] 
**provider** | [**KgitproxyRepositoryProvider**](KgitproxyRepositoryProvider.md) |  | [optional] 

## Example

```python
from openapi_client.models.kgitproxy_branch import KgitproxyBranch

# TODO update the JSON string below
json = "{}"
# create an instance of KgitproxyBranch from a JSON string
kgitproxy_branch_instance = KgitproxyBranch.from_json(json)
# print the JSON string representation of the object
print(KgitproxyBranch.to_json())

# convert the object into a dict
kgitproxy_branch_dict = kgitproxy_branch_instance.to_dict()
# create an instance of KgitproxyBranch from a dict
kgitproxy_branch_from_dict = KgitproxyBranch.from_dict(kgitproxy_branch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


