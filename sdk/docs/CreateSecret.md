# CreateSecret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**type** | [**SecretType**](SecretType.md) |  | [optional] [default to SecretType.SIMPLE]
**value** | **str** |  | [optional] 
**docker_hub_registry** | [**DockerHubRegistryConfiguration**](DockerHubRegistryConfiguration.md) |  | [optional] 
**private_registry** | [**PrivateRegistryConfiguration**](PrivateRegistryConfiguration.md) |  | [optional] 
**digital_ocean_registry** | [**DigitalOceanRegistryConfiguration**](DigitalOceanRegistryConfiguration.md) |  | [optional] 
**github_registry** | [**GitHubRegistryConfiguration**](GitHubRegistryConfiguration.md) |  | [optional] 
**gitlab_registry** | [**GitLabRegistryConfiguration**](GitLabRegistryConfiguration.md) |  | [optional] 
**gcp_container_registry** | [**GCPContainerRegistryConfiguration**](GCPContainerRegistryConfiguration.md) |  | [optional] 
**azure_container_registry** | [**AzureContainerRegistryConfiguration**](AzureContainerRegistryConfiguration.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_secret import CreateSecret

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecret from a JSON string
create_secret_instance = CreateSecret.from_json(json)
# print the JSON string representation of the object
print(CreateSecret.to_json())

# convert the object into a dict
create_secret_dict = create_secret_instance.to_dict()
# create an instance of CreateSecret from a dict
create_secret_from_dict = CreateSecret.from_dict(create_secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


