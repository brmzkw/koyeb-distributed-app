# GetPersistentVolumeReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | [**PersistentVolume**](PersistentVolume.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_persistent_volume_reply import GetPersistentVolumeReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetPersistentVolumeReply from a JSON string
get_persistent_volume_reply_instance = GetPersistentVolumeReply.from_json(json)
# print the JSON string representation of the object
print(GetPersistentVolumeReply.to_json())

# convert the object into a dict
get_persistent_volume_reply_dict = get_persistent_volume_reply_instance.to_dict()
# create an instance of GetPersistentVolumeReply from a dict
get_persistent_volume_reply_from_dict = GetPersistentVolumeReply.from_dict(get_persistent_volume_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


