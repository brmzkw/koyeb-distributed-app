# ListAppsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**apps** | [**List[AppListItem]**](AppListItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_apps_reply import ListAppsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListAppsReply from a JSON string
list_apps_reply_instance = ListAppsReply.from_json(json)
# print the JSON string representation of the object
print(ListAppsReply.to_json())

# convert the object into a dict
list_apps_reply_dict = list_apps_reply_instance.to_dict()
# create an instance of ListAppsReply from a dict
list_apps_reply_from_dict = ListAppsReply.from_dict(list_apps_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


