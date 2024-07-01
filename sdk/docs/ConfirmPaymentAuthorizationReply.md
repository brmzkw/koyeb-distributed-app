# ConfirmPaymentAuthorizationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.confirm_payment_authorization_reply import ConfirmPaymentAuthorizationReply

# TODO update the JSON string below
json = "{}"
# create an instance of ConfirmPaymentAuthorizationReply from a JSON string
confirm_payment_authorization_reply_instance = ConfirmPaymentAuthorizationReply.from_json(json)
# print the JSON string representation of the object
print(ConfirmPaymentAuthorizationReply.to_json())

# convert the object into a dict
confirm_payment_authorization_reply_dict = confirm_payment_authorization_reply_instance.to_dict()
# create an instance of ConfirmPaymentAuthorizationReply from a dict
confirm_payment_authorization_reply_from_dict = ConfirmPaymentAuthorizationReply.from_dict(confirm_payment_authorization_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


