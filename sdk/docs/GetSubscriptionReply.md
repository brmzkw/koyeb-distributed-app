# GetSubscriptionReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**subscription** | [**Subscription**](Subscription.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_subscription_reply import GetSubscriptionReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetSubscriptionReply from a JSON string
get_subscription_reply_instance = GetSubscriptionReply.from_json(json)
# print the JSON string representation of the object
print(GetSubscriptionReply.to_json())

# convert the object into a dict
get_subscription_reply_dict = get_subscription_reply_instance.to_dict()
# create an instance of GetSubscriptionReply from a dict
get_subscription_reply_from_dict = GetSubscriptionReply.from_dict(get_subscription_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


