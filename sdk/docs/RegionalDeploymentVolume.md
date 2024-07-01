# RegionalDeploymentVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**replica_index** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.regional_deployment_volume import RegionalDeploymentVolume

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalDeploymentVolume from a JSON string
regional_deployment_volume_instance = RegionalDeploymentVolume.from_json(json)
# print the JSON string representation of the object
print(RegionalDeploymentVolume.to_json())

# convert the object into a dict
regional_deployment_volume_dict = regional_deployment_volume_instance.to_dict()
# create an instance of RegionalDeploymentVolume from a dict
regional_deployment_volume_from_dict = RegionalDeploymentVolume.from_dict(regional_deployment_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


