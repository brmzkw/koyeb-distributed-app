# ListServiceEventsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[ServiceEvent]**](ServiceEvent.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_service_events_reply import ListServiceEventsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListServiceEventsReply from a JSON string
list_service_events_reply_instance = ListServiceEventsReply.from_json(json)
# print the JSON string representation of the object
print(ListServiceEventsReply.to_json())

# convert the object into a dict
list_service_events_reply_dict = list_service_events_reply_instance.to_dict()
# create an instance of ListServiceEventsReply from a dict
list_service_events_reply_from_dict = ListServiceEventsReply.from_dict(list_service_events_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


