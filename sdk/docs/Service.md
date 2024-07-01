# Service


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**succeeded_at** | **datetime** |  | [optional] 
**paused_at** | **datetime** |  | [optional] 
**resumed_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ServiceType**](ServiceType.md) |  | [optional] [default to ServiceType.INVALID_TYPE]
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**status** | [**ServiceStatus**](ServiceStatus.md) |  | [optional] [default to ServiceStatus.STARTING]
**messages** | **List[str]** |  | [optional] 
**version** | **str** |  | [optional] 
**active_deployment_id** | **str** |  | [optional] 
**latest_deployment_id** | **str** |  | [optional] 
**last_provisioned_deployment_id** | **str** |  | [optional] 
**state** | [**ServiceState**](ServiceState.md) |  | [optional] 

## Example

```python
from openapi_client.models.service import Service

# TODO update the JSON string below
json = "{}"
# create an instance of Service from a JSON string
service_instance = Service.from_json(json)
# print the JSON string representation of the object
print(Service.to_json())

# convert the object into a dict
service_dict = service_instance.to_dict()
# create an instance of Service from a dict
service_from_dict = Service.from_dict(service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


