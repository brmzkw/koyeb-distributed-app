# DeploymentProvisioningInfoStage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**status** | [**DeploymentProvisioningInfoStageStatus**](DeploymentProvisioningInfoStageStatus.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**finished_at** | **datetime** |  | [optional] 
**build_attempts** | [**List[DeploymentProvisioningInfoStageBuildAttempt]**](DeploymentProvisioningInfoStageBuildAttempt.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_provisioning_info_stage import DeploymentProvisioningInfoStage

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentProvisioningInfoStage from a JSON string
deployment_provisioning_info_stage_instance = DeploymentProvisioningInfoStage.from_json(json)
# print the JSON string representation of the object
print(DeploymentProvisioningInfoStage.to_json())

# convert the object into a dict
deployment_provisioning_info_stage_dict = deployment_provisioning_info_stage_instance.to_dict()
# create an instance of DeploymentProvisioningInfoStage from a dict
deployment_provisioning_info_stage_from_dict = DeploymentProvisioningInfoStage.from_dict(deployment_provisioning_info_stage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


