# CreatePersistentVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**volume_type** | [**PersistentVolumeBackingStore**](PersistentVolumeBackingStore.md) |  | [optional] [default to PersistentVolumeBackingStore.INVALID]
**name** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**max_size** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.create_persistent_volume_request import CreatePersistentVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePersistentVolumeRequest from a JSON string
create_persistent_volume_request_instance = CreatePersistentVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(CreatePersistentVolumeRequest.to_json())

# convert the object into a dict
create_persistent_volume_request_dict = create_persistent_volume_request_instance.to_dict()
# create an instance of CreatePersistentVolumeRequest from a dict
create_persistent_volume_request_from_dict = CreatePersistentVolumeRequest.from_dict(create_persistent_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


