# Secret


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**type** | [**SecretType**](SecretType.md) |  | [optional] [default to SecretType.SIMPLE]
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**value** | **str** |  | [optional] 
**docker_hub_registry** | [**DockerHubRegistryConfiguration**](DockerHubRegistryConfiguration.md) |  | [optional] 
**private_registry** | [**PrivateRegistryConfiguration**](PrivateRegistryConfiguration.md) |  | [optional] 
**digital_ocean_registry** | [**DigitalOceanRegistryConfiguration**](DigitalOceanRegistryConfiguration.md) |  | [optional] 
**github_registry** | [**GitHubRegistryConfiguration**](GitHubRegistryConfiguration.md) |  | [optional] 
**gitlab_registry** | [**GitLabRegistryConfiguration**](GitLabRegistryConfiguration.md) |  | [optional] 
**gcp_container_registry** | [**GCPContainerRegistryConfiguration**](GCPContainerRegistryConfiguration.md) |  | [optional] 
**azure_container_registry** | [**AzureContainerRegistryConfiguration**](AzureContainerRegistryConfiguration.md) |  | [optional] 
**database_role_password** | [**DatabaseRolePassword**](DatabaseRolePassword.md) |  | [optional] 

## Example

```python
from openapi_client.models.secret import Secret

# TODO update the JSON string below
json = "{}"
# create an instance of Secret from a JSON string
secret_instance = Secret.from_json(json)
# print the JSON string representation of the object
print(Secret.to_json())

# convert the object into a dict
secret_dict = secret_instance.to_dict()
# create an instance of Secret from a dict
secret_from_dict = Secret.from_dict(secret_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


