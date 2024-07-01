# GetQuotasReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**quotas** | [**Quotas**](Quotas.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_quotas_reply import GetQuotasReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetQuotasReply from a JSON string
get_quotas_reply_instance = GetQuotasReply.from_json(json)
# print the JSON string representation of the object
print(GetQuotasReply.to_json())

# convert the object into a dict
get_quotas_reply_dict = get_quotas_reply_instance.to_dict()
# create an instance of GetQuotasReply from a dict
get_quotas_reply_from_dict = GetQuotasReply.from_dict(get_quotas_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


