# DeploymentScalingTargetRequestsResponseTime


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**value** | **int** |  | [optional] 
**quantile** | **int** | The quantile to use for autoscaling. For example, set to 95 to use the 95th percentile (p95) for autoscaling.  Valid values are between 0 and 100. | [optional] 

## Example

```python
from openapi_client.models.deployment_scaling_target_requests_response_time import DeploymentScalingTargetRequestsResponseTime

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentScalingTargetRequestsResponseTime from a JSON string
deployment_scaling_target_requests_response_time_instance = DeploymentScalingTargetRequestsResponseTime.from_json(json)
# print the JSON string representation of the object
print(DeploymentScalingTargetRequestsResponseTime.to_json())

# convert the object into a dict
deployment_scaling_target_requests_response_time_dict = deployment_scaling_target_requests_response_time_instance.to_dict()
# create an instance of DeploymentScalingTargetRequestsResponseTime from a dict
deployment_scaling_target_requests_response_time_from_dict = DeploymentScalingTargetRequestsResponseTime.from_dict(deployment_scaling_target_requests_response_time_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


