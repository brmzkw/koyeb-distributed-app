# BuildpackBuilder


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**build_command** | **str** |  | [optional] 
**run_command** | **str** |  | [optional] 
**privileged** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.buildpack_builder import BuildpackBuilder

# TODO update the JSON string below
json = "{}"
# create an instance of BuildpackBuilder from a JSON string
buildpack_builder_instance = BuildpackBuilder.from_json(json)
# print the JSON string representation of the object
print(BuildpackBuilder.to_json())

# convert the object into a dict
buildpack_builder_dict = buildpack_builder_instance.to_dict()
# create an instance of BuildpackBuilder from a dict
buildpack_builder_from_dict = BuildpackBuilder.from_dict(buildpack_builder_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


