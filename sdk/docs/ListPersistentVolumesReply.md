# ListPersistentVolumesReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volumes** | [**List[PersistentVolume]**](PersistentVolume.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_persistent_volumes_reply import ListPersistentVolumesReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListPersistentVolumesReply from a JSON string
list_persistent_volumes_reply_instance = ListPersistentVolumesReply.from_json(json)
# print the JSON string representation of the object
print(ListPersistentVolumesReply.to_json())

# convert the object into a dict
list_persistent_volumes_reply_dict = list_persistent_volumes_reply_instance.to_dict()
# create an instance of ListPersistentVolumesReply from a dict
list_persistent_volumes_reply_from_dict = ListPersistentVolumesReply.from_dict(list_persistent_volumes_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


