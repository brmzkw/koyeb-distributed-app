# DockerHubRegistryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.docker_hub_registry_configuration import DockerHubRegistryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DockerHubRegistryConfiguration from a JSON string
docker_hub_registry_configuration_instance = DockerHubRegistryConfiguration.from_json(json)
# print the JSON string representation of the object
print(DockerHubRegistryConfiguration.to_json())

# convert the object into a dict
docker_hub_registry_configuration_dict = docker_hub_registry_configuration_instance.to_dict()
# create an instance of DockerHubRegistryConfiguration from a dict
docker_hub_registry_configuration_from_dict = DockerHubRegistryConfiguration.from_dict(docker_hub_registry_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


