# RegionalDeploymentDefinition


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**RegionalDeploymentDefinitionType**](RegionalDeploymentDefinitionType.md) |  | [optional] [default to RegionalDeploymentDefinitionType.INVALID]
**routes** | [**List[Route]**](Route.md) |  | [optional] 
**ports** | [**List[Port]**](Port.md) |  | [optional] 
**env** | [**List[Env]**](Env.md) |  | [optional] 
**region** | **str** |  | [optional] 
**scaling** | [**Scaling**](Scaling.md) |  | [optional] 
**instance_type** | **str** |  | [optional] 
**deployment_group** | **str** |  | [optional] 
**health_checks** | [**List[DeploymentHealthCheck]**](DeploymentHealthCheck.md) |  | [optional] 
**volumes** | [**List[RegionalDeploymentVolume]**](RegionalDeploymentVolume.md) |  | [optional] 
**skip_cache** | **bool** |  | [optional] 
**use_kuma_v2** | **bool** |  | [optional] 
**docker** | [**DockerSource**](DockerSource.md) |  | [optional] 
**git** | [**GitSource**](GitSource.md) |  | [optional] 
**archive** | [**ArchiveSource**](ArchiveSource.md) |  | [optional] 

## Example

```python
from openapi_client.models.regional_deployment_definition import RegionalDeploymentDefinition

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalDeploymentDefinition from a JSON string
regional_deployment_definition_instance = RegionalDeploymentDefinition.from_json(json)
# print the JSON string representation of the object
print(RegionalDeploymentDefinition.to_json())

# convert the object into a dict
regional_deployment_definition_dict = regional_deployment_definition_instance.to_dict()
# create an instance of RegionalDeploymentDefinition from a dict
regional_deployment_definition_from_dict = RegionalDeploymentDefinition.from_dict(regional_deployment_definition_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


