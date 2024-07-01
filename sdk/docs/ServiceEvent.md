# ServiceEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.service_event import ServiceEvent

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceEvent from a JSON string
service_event_instance = ServiceEvent.from_json(json)
# print the JSON string representation of the object
print(ServiceEvent.to_json())

# convert the object into a dict
service_event_dict = service_event_instance.to_dict()
# create an instance of ServiceEvent from a dict
service_event_from_dict = ServiceEvent.from_dict(service_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


