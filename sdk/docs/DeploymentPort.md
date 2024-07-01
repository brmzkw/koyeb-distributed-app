# DeploymentPort


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**protocol** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_port import DeploymentPort

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentPort from a JSON string
deployment_port_instance = DeploymentPort.from_json(json)
# print the JSON string representation of the object
print(DeploymentPort.to_json())

# convert the object into a dict
deployment_port_dict = deployment_port_instance.to_dict()
# create an instance of DeploymentPort from a dict
deployment_port_from_dict = DeploymentPort.from_dict(deployment_port_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


