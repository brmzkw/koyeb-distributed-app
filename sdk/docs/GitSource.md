# GitSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**repository** | **str** | A url to a git repository (contains the provider as well) .e.g: github.com/koyeb/test. | [optional] 
**branch** | **str** |  | [optional] 
**tag** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**build_command** | **str** |  | [optional] 
**run_command** | **str** |  | [optional] 
**no_deploy_on_push** | **bool** |  | [optional] 
**workdir** | **str** |  | [optional] 
**buildpack** | [**BuildpackBuilder**](BuildpackBuilder.md) |  | [optional] 
**docker** | [**DockerBuilder**](DockerBuilder.md) |  | [optional] 

## Example

```python
from openapi_client.models.git_source import GitSource

# TODO update the JSON string below
json = "{}"
# create an instance of GitSource from a JSON string
git_source_instance = GitSource.from_json(json)
# print the JSON string representation of the object
print(GitSource.to_json())

# convert the object into a dict
git_source_dict = git_source_instance.to_dict()
# create an instance of GitSource from a dict
git_source_from_dict = GitSource.from_dict(git_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


