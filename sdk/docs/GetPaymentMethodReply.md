# GetPaymentMethodReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_payment_method_reply import GetPaymentMethodReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetPaymentMethodReply from a JSON string
get_payment_method_reply_instance = GetPaymentMethodReply.from_json(json)
# print the JSON string representation of the object
print(GetPaymentMethodReply.to_json())

# convert the object into a dict
get_payment_method_reply_dict = get_payment_method_reply_instance.to_dict()
# create an instance of GetPaymentMethodReply from a dict
get_payment_method_reply_from_dict = GetPaymentMethodReply.from_dict(get_payment_method_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


