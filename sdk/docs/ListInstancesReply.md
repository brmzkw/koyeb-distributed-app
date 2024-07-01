# ListInstancesReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[InstanceListItem]**](InstanceListItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_instances_reply import ListInstancesReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListInstancesReply from a JSON string
list_instances_reply_instance = ListInstancesReply.from_json(json)
# print the JSON string representation of the object
print(ListInstancesReply.to_json())

# convert the object into a dict
list_instances_reply_dict = list_instances_reply_instance.to_dict()
# create an instance of ListInstancesReply from a dict
list_instances_reply_from_dict = ListInstancesReply.from_dict(list_instances_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


