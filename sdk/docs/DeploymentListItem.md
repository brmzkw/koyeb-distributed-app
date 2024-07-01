# DeploymentListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**allocated_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**succeeded_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**parent_id** | **str** |  | [optional] 
**child_id** | **str** |  | [optional] 
**status** | [**DeploymentStatus**](DeploymentStatus.md) |  | [optional] 
**metadata** | [**DeploymentMetadata**](DeploymentMetadata.md) |  | [optional] 
**definition** | [**DeploymentDefinition**](DeploymentDefinition.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**provisioning_info** | [**DeploymentProvisioningInfo**](DeploymentProvisioningInfo.md) |  | [optional] 
**database_info** | [**DeploymentDatabaseInfo**](DeploymentDatabaseInfo.md) |  | [optional] 
**version** | **str** |  | [optional] 
**deployment_group** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_list_item import DeploymentListItem

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentListItem from a JSON string
deployment_list_item_instance = DeploymentListItem.from_json(json)
# print the JSON string representation of the object
print(DeploymentListItem.to_json())

# convert the object into a dict
deployment_list_item_dict = deployment_list_item_instance.to_dict()
# create an instance of DeploymentListItem from a dict
deployment_list_item_from_dict = DeploymentListItem.from_dict(deployment_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


