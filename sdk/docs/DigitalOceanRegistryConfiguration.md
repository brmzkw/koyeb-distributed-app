# DigitalOceanRegistryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.digital_ocean_registry_configuration import DigitalOceanRegistryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of DigitalOceanRegistryConfiguration from a JSON string
digital_ocean_registry_configuration_instance = DigitalOceanRegistryConfiguration.from_json(json)
# print the JSON string representation of the object
print(DigitalOceanRegistryConfiguration.to_json())

# convert the object into a dict
digital_ocean_registry_configuration_dict = digital_ocean_registry_configuration_instance.to_dict()
# create an instance of DigitalOceanRegistryConfiguration from a dict
digital_ocean_registry_configuration_from_dict = DigitalOceanRegistryConfiguration.from_dict(digital_ocean_registry_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


