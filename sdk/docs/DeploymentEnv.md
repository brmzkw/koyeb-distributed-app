# DeploymentEnv


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scopes** | **List[str]** |  | [optional] 
**key** | **str** |  | [optional] 
**value** | **str** |  | [optional] 
**secret** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_env import DeploymentEnv

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentEnv from a JSON string
deployment_env_instance = DeploymentEnv.from_json(json)
# print the JSON string representation of the object
print(DeploymentEnv.to_json())

# convert the object into a dict
deployment_env_dict = deployment_env_instance.to_dict()
# create an instance of DeploymentEnv from a dict
deployment_env_from_dict = DeploymentEnv.from_dict(deployment_env_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


