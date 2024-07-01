# GitHubRegistryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.git_hub_registry_configuration import GitHubRegistryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GitHubRegistryConfiguration from a JSON string
git_hub_registry_configuration_instance = GitHubRegistryConfiguration.from_json(json)
# print the JSON string representation of the object
print(GitHubRegistryConfiguration.to_json())

# convert the object into a dict
git_hub_registry_configuration_dict = git_hub_registry_configuration_instance.to_dict()
# create an instance of GitHubRegistryConfiguration from a dict
git_hub_registry_configuration_from_dict = GitHubRegistryConfiguration.from_dict(git_hub_registry_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


