# GetMetricsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**List[GetMetricsReplyMetric]**](GetMetricsReplyMetric.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_metrics_reply import GetMetricsReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsReply from a JSON string
get_metrics_reply_instance = GetMetricsReply.from_json(json)
# print the JSON string representation of the object
print(GetMetricsReply.to_json())

# convert the object into a dict
get_metrics_reply_dict = get_metrics_reply_instance.to_dict()
# create an instance of GetMetricsReply from a dict
get_metrics_reply_from_dict = GetMetricsReply.from_dict(get_metrics_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


