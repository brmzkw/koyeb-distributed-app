# UpdatePersistentVolumeReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | [**PersistentVolume**](PersistentVolume.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_persistent_volume_reply import UpdatePersistentVolumeReply

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePersistentVolumeReply from a JSON string
update_persistent_volume_reply_instance = UpdatePersistentVolumeReply.from_json(json)
# print the JSON string representation of the object
print(UpdatePersistentVolumeReply.to_json())

# convert the object into a dict
update_persistent_volume_reply_dict = update_persistent_volume_reply_instance.to_dict()
# create an instance of UpdatePersistentVolumeReply from a dict
update_persistent_volume_reply_from_dict = UpdatePersistentVolumeReply.from_dict(update_persistent_volume_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


