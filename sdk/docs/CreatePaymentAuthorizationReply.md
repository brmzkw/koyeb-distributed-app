# CreatePaymentAuthorizationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_method** | [**PaymentMethod**](PaymentMethod.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_payment_authorization_reply import CreatePaymentAuthorizationReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreatePaymentAuthorizationReply from a JSON string
create_payment_authorization_reply_instance = CreatePaymentAuthorizationReply.from_json(json)
# print the JSON string representation of the object
print(CreatePaymentAuthorizationReply.to_json())

# convert the object into a dict
create_payment_authorization_reply_dict = create_payment_authorization_reply_instance.to_dict()
# create an instance of CreatePaymentAuthorizationReply from a dict
create_payment_authorization_reply_from_dict = CreatePaymentAuthorizationReply.from_dict(create_payment_authorization_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


