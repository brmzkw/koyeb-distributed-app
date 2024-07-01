# RegionalDeploymentEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**regional_deployment_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.regional_deployment_event import RegionalDeploymentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of RegionalDeploymentEvent from a JSON string
regional_deployment_event_instance = RegionalDeploymentEvent.from_json(json)
# print the JSON string representation of the object
print(RegionalDeploymentEvent.to_json())

# convert the object into a dict
regional_deployment_event_dict = regional_deployment_event_instance.to_dict()
# create an instance of RegionalDeploymentEvent from a dict
regional_deployment_event_from_dict = RegionalDeploymentEvent.from_dict(regional_deployment_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


