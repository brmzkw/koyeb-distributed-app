# DeploymentEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**deployment_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_event import DeploymentEvent

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentEvent from a JSON string
deployment_event_instance = DeploymentEvent.from_json(json)
# print the JSON string representation of the object
print(DeploymentEvent.to_json())

# convert the object into a dict
deployment_event_dict = deployment_event_instance.to_dict()
# create an instance of DeploymentEvent from a dict
deployment_event_from_dict = DeploymentEvent.from_dict(deployment_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


