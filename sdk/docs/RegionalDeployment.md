# RegionalDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**scheduled_at** | **datetime** |  | [optional] 
**allocated_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**succeeded_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**child_id** | **str** |  | [optional] 
**status** | [**RegionalDeploymentStatus**](RegionalDeploymentStatus.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**definition** | [**RegionalDeploymentDefinition**](RegionalDeploymentDefinition.md) |  | [optional] 
**datacenters** | **List[str]** |  | [optional] 
**metadata** | **object** |  | [optional] 
**provisioning_info** | [**DeploymentProvisioningInfo**](DeploymentProvisioningInfo.md) |  | [optional] 
**role** | [**RegionalDeploymentRole**](RegionalDeploymentRole.md) |  | [optional] 
**use_kuma_v2** | **bool** |  | [optional] 
**use_kata** | **bool** |  | [optional] 
**version** | **str** |  | [optional] 
**deployment_group** | **str** |  | [optional] 
**deployment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.regional_deployment import RegionalDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalDeployment from a JSON string
regional_deployment_instance = RegionalDeployment.from_json(json)
# print the JSON string representation of the object
print(RegionalDeployment.to_json())

# convert the object into a dict
regional_deployment_dict = regional_deployment_instance.to_dict()
# create an instance of RegionalDeployment from a dict
regional_deployment_from_dict = RegionalDeployment.from_dict(regional_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


