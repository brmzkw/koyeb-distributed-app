# ListRegionalDeploymentEventsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**events** | [**List[RegionalDeploymentEvent]**](RegionalDeploymentEvent.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.list_regional_deployment_events_reply import ListRegionalDeploymentEventsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegionalDeploymentEventsReply from a JSON string
list_regional_deployment_events_reply_instance = ListRegionalDeploymentEventsReply.from_json(json)
# print the JSON string representation of the object
print(ListRegionalDeploymentEventsReply.to_json())

# convert the object into a dict
list_regional_deployment_events_reply_dict = list_regional_deployment_events_reply_instance.to_dict()
# create an instance of ListRegionalDeploymentEventsReply from a dict
list_regional_deployment_events_reply_from_dict = ListRegionalDeploymentEventsReply.from_dict(list_regional_deployment_events_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


