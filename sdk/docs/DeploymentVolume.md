# DeploymentVolume


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**path** | **str** |  | [optional] 
**replica_index** | **int** |  | [optional] 
**scopes** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_volume import DeploymentVolume

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentVolume from a JSON string
deployment_volume_instance = DeploymentVolume.from_json(json)
# print the JSON string representation of the object
print(DeploymentVolume.to_json())

# convert the object into a dict
deployment_volume_dict = deployment_volume_instance.to_dict()
# create an instance of DeploymentVolume from a dict
deployment_volume_from_dict = DeploymentVolume.from_dict(deployment_volume_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


