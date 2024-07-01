# DockerBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dockerfile** | **str** |  | [optional] 
**entrypoint** | **List[str]** |  | [optional] 
**command** | **str** |  | [optional] 
**args** | **List[str]** |  | [optional] 
**target** | **str** |  | [optional] 
**privileged** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.docker_builder import DockerBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of DockerBuilder from a JSON string
docker_builder_instance = DockerBuilder.from_json(json)
# print the JSON string representation of the object
print(DockerBuilder.to_json())

# convert the object into a dict
docker_builder_dict = docker_builder_instance.to_dict()
# create an instance of DockerBuilder from a dict
docker_builder_from_dict = DockerBuilder.from_dict(docker_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


