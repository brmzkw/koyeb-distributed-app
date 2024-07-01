# UpdatePersistentVolumeRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**max_size** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.update_persistent_volume_request import UpdatePersistentVolumeRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdatePersistentVolumeRequest from a JSON string
update_persistent_volume_request_instance = UpdatePersistentVolumeRequest.from_json(json)
# print the JSON string representation of the object
print(UpdatePersistentVolumeRequest.to_json())

# convert the object into a dict
update_persistent_volume_request_dict = update_persistent_volume_request_instance.to_dict()
# create an instance of UpdatePersistentVolumeRequest from a dict
update_persistent_volume_request_from_dict = UpdatePersistentVolumeRequest.from_dict(update_persistent_volume_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


