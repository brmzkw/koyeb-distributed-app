# ListInstanceEventsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[InstanceEvent]**](InstanceEvent.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_instance_events_reply import ListInstanceEventsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListInstanceEventsReply from a JSON string
list_instance_events_reply_instance = ListInstanceEventsReply.from_json(json)
# print the JSON string representation of the object
print(ListInstanceEventsReply.to_json())

# convert the object into a dict
list_instance_events_reply_dict = list_instance_events_reply_instance.to_dict()
# create an instance of ListInstanceEventsReply from a dict
list_instance_events_reply_from_dict = ListInstanceEventsReply.from_dict(list_instance_events_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


