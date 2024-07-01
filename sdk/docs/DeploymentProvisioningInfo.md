# DeploymentProvisioningInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sha** | **str** | The git sha for this build (we resolve the reference at the start of the build). | [optional] 
**image** | **str** | The docker image built as a result of this build. | [optional] 
**stages** | [**List[DeploymentProvisioningInfoStage]**](DeploymentProvisioningInfoStage.md) | Some info about the build. | [optional] 

## Example

```python
from openapi_client.models.deployment_provisioning_info import DeploymentProvisioningInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentProvisioningInfo from a JSON string
deployment_provisioning_info_instance = DeploymentProvisioningInfo.from_json(json)
# print the JSON string representation of the object
print(DeploymentProvisioningInfo.to_json())

# convert the object into a dict
deployment_provisioning_info_dict = deployment_provisioning_info_instance.to_dict()
# create an instance of DeploymentProvisioningInfo from a dict
deployment_provisioning_info_from_dict = DeploymentProvisioningInfo.from_dict(deployment_provisioning_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


