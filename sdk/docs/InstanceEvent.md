# InstanceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.instance_event import InstanceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of InstanceEvent from a JSON string
instance_event_instance = InstanceEvent.from_json(json)
# print the JSON string representation of the object
print(InstanceEvent.to_json())

# convert the object into a dict
instance_event_dict = instance_event_instance.to_dict()
# create an instance of InstanceEvent from a dict
instance_event_from_dict = InstanceEvent.from_dict(instance_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


