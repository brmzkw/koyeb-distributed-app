# DeploymentInstanceType


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_instance_type import DeploymentInstanceType

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentInstanceType from a JSON string
deployment_instance_type_instance = DeploymentInstanceType.from_json(json)
# print the JSON string representation of the object
print(DeploymentInstanceType.to_json())

# convert the object into a dict
deployment_instance_type_dict = deployment_instance_type_instance.to_dict()
# create an instance of DeploymentInstanceType from a dict
deployment_instance_type_from_dict = DeploymentInstanceType.from_dict(deployment_instance_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


