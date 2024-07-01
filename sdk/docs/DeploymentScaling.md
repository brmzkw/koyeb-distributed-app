# DeploymentScaling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **List[str]** |  | [optional] 
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**targets** | [**List[DeploymentScalingTarget]**](DeploymentScalingTarget.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_scaling import DeploymentScaling

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentScaling from a JSON string
deployment_scaling_instance = DeploymentScaling.from_json(json)
# print the JSON string representation of the object
print(DeploymentScaling.to_json())

# convert the object into a dict
deployment_scaling_dict = deployment_scaling_instance.to_dict()
# create an instance of DeploymentScaling from a dict
deployment_scaling_from_dict = DeploymentScaling.from_dict(deployment_scaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


