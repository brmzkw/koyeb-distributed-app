# DeploymentDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**DeploymentDefinitionType**](DeploymentDefinitionType.md) |  | [optional] 
**routes** | [**List[DeploymentRoute]**](DeploymentRoute.md) |  | [optional] 
**ports** | [**List[DeploymentPort]**](DeploymentPort.md) |  | [optional] 
**env** | [**List[DeploymentEnv]**](DeploymentEnv.md) |  | [optional] 
**regions** | **List[str]** |  | [optional] 
**scalings** | [**List[DeploymentScaling]**](DeploymentScaling.md) |  | [optional] 
**instance_types** | [**List[DeploymentInstanceType]**](DeploymentInstanceType.md) |  | [optional] 
**health_checks** | [**List[DeploymentHealthCheck]**](DeploymentHealthCheck.md) |  | [optional] 
**volumes** | [**List[DeploymentVolume]**](DeploymentVolume.md) |  | [optional] 
**skip_cache** | **bool** |  | [optional] 
**docker** | [**DockerSource**](DockerSource.md) |  | [optional] 
**git** | [**GitSource**](GitSource.md) |  | [optional] 
**database** | [**DatabaseSource**](DatabaseSource.md) |  | [optional] 
**archive** | [**ArchiveSource**](ArchiveSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_definition import DeploymentDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentDefinition from a JSON string
deployment_definition_instance = DeploymentDefinition.from_json(json)
# print the JSON string representation of the object
print(DeploymentDefinition.to_json())

# convert the object into a dict
deployment_definition_dict = deployment_definition_instance.to_dict()
# create an instance of DeploymentDefinition from a dict
deployment_definition_from_dict = DeploymentDefinition.from_dict(deployment_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


