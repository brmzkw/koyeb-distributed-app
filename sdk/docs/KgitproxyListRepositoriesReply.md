# KgitproxyListRepositoriesReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repositories** | [**List[KgitproxyRepository]**](KgitproxyRepository.md) | The collection of repositories. | [optional] 
**limit** | **int** | The limit in the request. | [optional] 
**offset** | **int** | The offset in the request. | [optional] 
**count** | **int** | The total number of items. | [optional] 

## Example

```python
from openapi_client.models.kgitproxy_list_repositories_reply import KgitproxyListRepositoriesReply

# TODO update the JSON string below
json = "{}"
# create an instance of KgitproxyListRepositoriesReply from a JSON string
kgitproxy_list_repositories_reply_instance = KgitproxyListRepositoriesReply.from_json(json)
# print the JSON string representation of the object
print(KgitproxyListRepositoriesReply.to_json())

# convert the object into a dict
kgitproxy_list_repositories_reply_dict = kgitproxy_list_repositories_reply_instance.to_dict()
# create an instance of KgitproxyListRepositoriesReply from a dict
kgitproxy_list_repositories_reply_from_dict = KgitproxyListRepositoriesReply.from_dict(kgitproxy_list_repositories_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


