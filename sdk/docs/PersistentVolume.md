# PersistentVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**deleted_at** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**read_only** | **bool** |  | [optional] 
**max_size** | **int** |  | [optional] 
**cur_size** | **int** |  | [optional] 
**status** | [**PersistentVolumeStatus**](PersistentVolumeStatus.md) |  | [optional] 
**backing_store** | [**PersistentVolumeBackingStore**](PersistentVolumeBackingStore.md) |  | [optional] 

## Example

```python
from openapi_client.models.persistent_volume import PersistentVolume

# TODO update the JSON string below
json = "{}"
# create an instance of PersistentVolume from a JSON string
persistent_volume_instance = PersistentVolume.from_json(json)
# print the JSON string representation of the object
print(PersistentVolume.to_json())

# convert the object into a dict
persistent_volume_dict = persistent_volume_instance.to_dict()
# create an instance of PersistentVolume from a dict
persistent_volume_from_dict = PersistentVolume.from_dict(persistent_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


