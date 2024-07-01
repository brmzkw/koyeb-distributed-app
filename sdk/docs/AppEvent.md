# AppEvent


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**when** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**metadata** | **object** |  | [optional] 

## Example

```python
from openapi_client.models.app_event import AppEvent

# TODO update the JSON string below
json = "{}"
# create an instance of AppEvent from a JSON string
app_event_instance = AppEvent.from_json(json)
# print the JSON string representation of the object
print(AppEvent.to_json())

# convert the object into a dict
app_event_dict = app_event_instance.to_dict()
# create an instance of AppEvent from a dict
app_event_from_dict = AppEvent.from_dict(app_event_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


