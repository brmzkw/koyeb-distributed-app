# GCPContainerRegistryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**keyfile_content** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.gcp_container_registry_configuration import GCPContainerRegistryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of GCPContainerRegistryConfiguration from a JSON string
gcp_container_registry_configuration_instance = GCPContainerRegistryConfiguration.from_json(json)
# print the JSON string representation of the object
print(GCPContainerRegistryConfiguration.to_json())

# convert the object into a dict
gcp_container_registry_configuration_dict = gcp_container_registry_configuration_instance.to_dict()
# create an instance of GCPContainerRegistryConfiguration from a dict
gcp_container_registry_configuration_from_dict = GCPContainerRegistryConfiguration.from_dict(gcp_container_registry_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


