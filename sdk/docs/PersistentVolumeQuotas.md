# PersistentVolumeQuotas


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_total_size** | **int** | MaxTotalSize for all volumes on a region (in Gigabyte / GB). | [optional] 
**max_volume_size** | **int** | MaxVolumeSize for one volume (in Gigabyte / GB). | [optional] 
**max_per_instance_size** | **int** | MaxPerInstanceSize for all volumes on an instance (in Gigabyte / GB). | [optional] 

## Example

```python
from openapi_client.models.persistent_volume_quotas import PersistentVolumeQuotas

# TODO update the JSON string below
json = "{}"
# create an instance of PersistentVolumeQuotas from a JSON string
persistent_volume_quotas_instance = PersistentVolumeQuotas.from_json(json)
# print the JSON string representation of the object
print(PersistentVolumeQuotas.to_json())

# convert the object into a dict
persistent_volume_quotas_dict = persistent_volume_quotas_instance.to_dict()
# create an instance of PersistentVolumeQuotas from a dict
persistent_volume_quotas_from_dict = PersistentVolumeQuotas.from_dict(persistent_volume_quotas_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


