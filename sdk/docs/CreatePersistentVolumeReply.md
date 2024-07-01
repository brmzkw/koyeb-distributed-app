# CreatePersistentVolumeReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume** | [**PersistentVolume**](PersistentVolume.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_persistent_volume_reply import CreatePersistentVolumeReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersistentVolumeReply from a JSON string
create_persistent_volume_reply_instance = CreatePersistentVolumeReply.from_json(json)
# print the JSON string representation of the object
print(CreatePersistentVolumeReply.to_json())

# convert the object into a dict
create_persistent_volume_reply_dict = create_persistent_volume_reply_instance.to_dict()
# create an instance of CreatePersistentVolumeReply from a dict
create_persistent_volume_reply_from_dict = CreatePersistentVolumeReply.from_dict(create_persistent_volume_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


