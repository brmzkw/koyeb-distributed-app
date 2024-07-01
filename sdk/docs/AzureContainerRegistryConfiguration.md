# AzureContainerRegistryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**registry_name** | **str** |  | [optional] 
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.azure_container_registry_configuration import AzureContainerRegistryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of AzureContainerRegistryConfiguration from a JSON string
azure_container_registry_configuration_instance = AzureContainerRegistryConfiguration.from_json(json)
# print the JSON string representation of the object
print(AzureContainerRegistryConfiguration.to_json())

# convert the object into a dict
azure_container_registry_configuration_dict = azure_container_registry_configuration_instance.to_dict()
# create an instance of AzureContainerRegistryConfiguration from a dict
azure_container_registry_configuration_from_dict = AzureContainerRegistryConfiguration.from_dict(azure_container_registry_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


