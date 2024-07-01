# GitLabRegistryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.git_lab_registry_configuration import GitLabRegistryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GitLabRegistryConfiguration from a JSON string
git_lab_registry_configuration_instance = GitLabRegistryConfiguration.from_json(json)
# print the JSON string representation of the object
print(GitLabRegistryConfiguration.to_json())

# convert the object into a dict
git_lab_registry_configuration_dict = git_lab_registry_configuration_instance.to_dict()
# create an instance of GitLabRegistryConfiguration from a dict
git_lab_registry_configuration_from_dict = GitLabRegistryConfiguration.from_dict(git_lab_registry_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


