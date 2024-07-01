# DeploymentScalingTarget


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**average_cpu** | [**DeploymentScalingTargetAverageCPU**](DeploymentScalingTargetAverageCPU.md) |  | [optional] 
**average_mem** | [**DeploymentScalingTargetAverageMem**](DeploymentScalingTargetAverageMem.md) |  | [optional] 
**requests_per_second** | [**DeploymentScalingTargetRequestsPerSecond**](DeploymentScalingTargetRequestsPerSecond.md) |  | [optional] 
**concurrent_requests** | [**DeploymentScalingTargetConcurrentRequests**](DeploymentScalingTargetConcurrentRequests.md) |  | [optional] 
**requests_response_time** | [**DeploymentScalingTargetRequestsResponseTime**](DeploymentScalingTargetRequestsResponseTime.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_scaling_target import DeploymentScalingTarget

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentScalingTarget from a JSON string
deployment_scaling_target_instance = DeploymentScalingTarget.from_json(json)
# print the JSON string representation of the object
print(DeploymentScalingTarget.to_json())

# convert the object into a dict
deployment_scaling_target_dict = deployment_scaling_target_instance.to_dict()
# create an instance of DeploymentScalingTarget from a dict
deployment_scaling_target_from_dict = DeploymentScalingTarget.from_dict(deployment_scaling_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


