# ListAppEventsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[AppEvent]**](AppEvent.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_app_events_reply import ListAppEventsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListAppEventsReply from a JSON string
list_app_events_reply_instance = ListAppEventsReply.from_json(json)
# print the JSON string representation of the object
print(ListAppEventsReply.to_json())

# convert the object into a dict
list_app_events_reply_dict = list_app_events_reply_instance.to_dict()
# create an instance of ListAppEventsReply from a dict
list_app_events_reply_from_dict = ListAppEventsReply.from_dict(list_app_events_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


