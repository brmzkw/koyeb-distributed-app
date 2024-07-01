# RegionalDeploymentListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**region** | **str** |  | [optional] 
**status** | [**RegionalDeploymentStatus**](RegionalDeploymentStatus.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**definition** | [**RegionalDeploymentDefinition**](RegionalDeploymentDefinition.md) |  | [optional] 
**use_kuma_v2** | **bool** |  | [optional] 
**use_kata** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.regional_deployment_list_item import RegionalDeploymentListItem

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalDeploymentListItem from a JSON string
regional_deployment_list_item_instance = RegionalDeploymentListItem.from_json(json)
# print the JSON string representation of the object
print(RegionalDeploymentListItem.to_json())

# convert the object into a dict
regional_deployment_list_item_dict = regional_deployment_list_item_instance.to_dict()
# create an instance of RegionalDeploymentListItem from a dict
regional_deployment_list_item_from_dict = RegionalDeploymentListItem.from_dict(regional_deployment_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


