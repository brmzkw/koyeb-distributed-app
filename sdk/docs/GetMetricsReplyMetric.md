# GetMetricsReplyMetric


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**labels** | **Dict[str, str]** |  | [optional] 
**samples** | [**List[Sample]**](Sample.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_metrics_reply_metric import GetMetricsReplyMetric

# TODO update the JSON string below
json = "{}"
# create an instance of GetMetricsReplyMetric from a JSON string
get_metrics_reply_metric_instance = GetMetricsReplyMetric.from_json(json)
# print the JSON string representation of the object
print(GetMetricsReplyMetric.to_json())

# convert the object into a dict
get_metrics_reply_metric_dict = get_metrics_reply_metric_instance.to_dict()
# create an instance of GetMetricsReplyMetric from a dict
get_metrics_reply_metric_from_dict = GetMetricsReplyMetric.from_dict(get_metrics_reply_metric_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


