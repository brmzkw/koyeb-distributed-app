# DeletePersistentVolumeReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | [**PersistentVolume**](PersistentVolume.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_persistent_volume_reply import DeletePersistentVolumeReply

# TODO update the JSON string below
json = "{}"
# create an instance of DeletePersistentVolumeReply from a JSON string
delete_persistent_volume_reply_instance = DeletePersistentVolumeReply.from_json(json)
# print the JSON string representation of the object
print(DeletePersistentVolumeReply.to_json())

# convert the object into a dict
delete_persistent_volume_reply_dict = delete_persistent_volume_reply_instance.to_dict()
# create an instance of DeletePersistentVolumeReply from a dict
delete_persistent_volume_reply_from_dict = DeletePersistentVolumeReply.from_dict(delete_persistent_volume_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


