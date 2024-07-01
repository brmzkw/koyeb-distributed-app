# ArchiveSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**buildpack** | [**BuildpackBuilder**](BuildpackBuilder.md) |  | [optional] 
**docker** | [**DockerBuilder**](DockerBuilder.md) |  | [optional] 

## Example

```python
from openapi_client.models.archive_source import ArchiveSource

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveSource from a JSON string
archive_source_instance = ArchiveSource.from_json(json)
# print the JSON string representation of the object
print(ArchiveSource.to_json())

# convert the object into a dict
archive_source_dict = archive_source_instance.to_dict()
# create an instance of ArchiveSource from a dict
archive_source_from_dict = ArchiveSource.from_dict(archive_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


