# DockerSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**image** | **str** |  | [optional] 
**command** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**image_registry_secret** | **str** |  | [optional] 
**entrypoint** | **List[str]** |  | [optional] 
**privileged** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.docker_source import DockerSource

# TODO update the JSON string below
json = "{}"
# create an instance of DockerSource from a JSON string
docker_source_instance = DockerSource.from_json(json)
# print the JSON string representation of the object
print(DockerSource.to_json())

# convert the object into a dict
docker_source_dict = docker_source_instance.to_dict()
# create an instance of DockerSource from a dict
docker_source_from_dict = DockerSource.from_dict(docker_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


