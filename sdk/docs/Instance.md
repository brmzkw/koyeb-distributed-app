# Instance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**regional_deployment_id** | **str** |  | [optional] 
**allocation_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**replica_index** | **int** |  | [optional] 
**region** | **str** |  | [optional] 
**datacenter** | **str** |  | [optional] 
**hypervisor** | **str** |  | [optional] 
**status** | [**InstanceStatus**](InstanceStatus.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**succeeded_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**xyz_deployment_id** | **str** | WARNING: Please don&#39;t use the following attribute. Koyeb doesn&#39;t guarantee backwards compatible breaking change and reserve the right to completely drop it without notice. USE AT YOUR OWN RISK. | [optional] 

## Example

```python
from openapi_client.models.instance import Instance

# TODO update the JSON string below
json = "{}"
# create an instance of Instance from a JSON string
instance_instance = Instance.from_json(json)
# print the JSON string representation of the object
print(Instance.to_json())

# convert the object into a dict
instance_dict = instance_instance.to_dict()
# create an instance of Instance from a dict
instance_from_dict = Instance.from_dict(instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


