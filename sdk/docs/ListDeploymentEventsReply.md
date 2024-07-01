# ListDeploymentEventsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[DeploymentEvent]**](DeploymentEvent.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_deployment_events_reply import ListDeploymentEventsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeploymentEventsReply from a JSON string
list_deployment_events_reply_instance = ListDeploymentEventsReply.from_json(json)
# print the JSON string representation of the object
print(ListDeploymentEventsReply.to_json())

# convert the object into a dict
list_deployment_events_reply_dict = list_deployment_events_reply_instance.to_dict()
# create an instance of ListDeploymentEventsReply from a dict
list_deployment_events_reply_from_dict = ListDeploymentEventsReply.from_dict(list_deployment_events_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


