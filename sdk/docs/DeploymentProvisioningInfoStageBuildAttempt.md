# DeploymentProvisioningInfoStageBuildAttempt


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** |  | [optional] 
**status** | [**DeploymentProvisioningInfoStageStatus**](DeploymentProvisioningInfoStageStatus.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_provisioning_info_stage_build_attempt import DeploymentProvisioningInfoStageBuildAttempt

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentProvisioningInfoStageBuildAttempt from a JSON string
deployment_provisioning_info_stage_build_attempt_instance = DeploymentProvisioningInfoStageBuildAttempt.from_json(json)
# print the JSON string representation of the object
print(DeploymentProvisioningInfoStageBuildAttempt.to_json())

# convert the object into a dict
deployment_provisioning_info_stage_build_attempt_dict = deployment_provisioning_info_stage_build_attempt_instance.to_dict()
# create an instance of DeploymentProvisioningInfoStageBuildAttempt from a dict
deployment_provisioning_info_stage_build_attempt_from_dict = DeploymentProvisioningInfoStageBuildAttempt.from_dict(deployment_provisioning_info_stage_build_attempt_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


