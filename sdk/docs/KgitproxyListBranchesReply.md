# KgitproxyListBranchesReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**branches** | [**List[KgitproxyBranch]**](KgitproxyBranch.md) | The collection of branches. | [optional] 
**limit** | **int** | The limit in the request. | [optional] 
**offset** | **int** | The offset in the request. | [optional] 
**count** | **int** | The total number of items. | [optional] 

## Example

```python
from openapi_client.models.kgitproxy_list_branches_reply import KgitproxyListBranchesReply

# TODO update the JSON string below
json = "{}"
# create an instance of KgitproxyListBranchesReply from a JSON string
kgitproxy_list_branches_reply_instance = KgitproxyListBranchesReply.from_json(json)
# print the JSON string representation of the object
print(KgitproxyListBranchesReply.to_json())

# convert the object into a dict
kgitproxy_list_branches_reply_dict = kgitproxy_list_branches_reply_instance.to_dict()
# create an instance of KgitproxyListBranchesReply from a dict
kgitproxy_list_branches_reply_from_dict = KgitproxyListBranchesReply.from_dict(kgitproxy_list_branches_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


