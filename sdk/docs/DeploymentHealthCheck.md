# DeploymentHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grace_period** | **int** |  | [optional] 
**interval** | **int** |  | [optional] 
**restart_limit** | **int** |  | [optional] 
**timeout** | **int** |  | [optional] 
**tcp** | [**TCPHealthCheck**](TCPHealthCheck.md) |  | [optional] 
**http** | [**HTTPHealthCheck**](HTTPHealthCheck.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_health_check import DeploymentHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentHealthCheck from a JSON string
deployment_health_check_instance = DeploymentHealthCheck.from_json(json)
# print the JSON string representation of the object
print(DeploymentHealthCheck.to_json())

# convert the object into a dict
deployment_health_check_dict = deployment_health_check_instance.to_dict()
# create an instance of DeploymentHealthCheck from a dict
deployment_health_check_from_dict = DeploymentHealthCheck.from_dict(deployment_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


