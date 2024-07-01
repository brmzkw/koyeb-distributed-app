# ServiceListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**type** | [**ServiceType**](ServiceType.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**status** | [**ServiceStatus**](ServiceStatus.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**version** | **str** |  | [optional] 
**state** | [**ServiceState**](ServiceState.md) |  | [optional] 
**active_deployment_id** | **str** |  | [optional] 
**latest_deployment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.service_list_item import ServiceListItem

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceListItem from a JSON string
service_list_item_instance = ServiceListItem.from_json(json)
# print the JSON string representation of the object
print(ServiceListItem.to_json())

# convert the object into a dict
service_list_item_dict = service_list_item_instance.to_dict()
# create an instance of ServiceListItem from a dict
service_list_item_from_dict = ServiceListItem.from_dict(service_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


