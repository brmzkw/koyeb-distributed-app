# PrivateRegistryConfiguration


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.private_registry_configuration import PrivateRegistryConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of PrivateRegistryConfiguration from a JSON string
private_registry_configuration_instance = PrivateRegistryConfiguration.from_json(json)
# print the JSON string representation of the object
print(PrivateRegistryConfiguration.to_json())

# convert the object into a dict
private_registry_configuration_dict = private_registry_configuration_instance.to_dict()
# create an instance of PrivateRegistryConfiguration from a dict
private_registry_configuration_from_dict = PrivateRegistryConfiguration.from_dict(private_registry_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


