# SubscriptionPaymentFailureStripeSDK


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**client_secret_key** | **str** |  | [optional] 
**raw_json** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.subscription_payment_failure_stripe_sdk import SubscriptionPaymentFailureStripeSDK

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaymentFailureStripeSDK from a JSON string
subscription_payment_failure_stripe_sdk_instance = SubscriptionPaymentFailureStripeSDK.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPaymentFailureStripeSDK.to_json())

# convert the object into a dict
subscription_payment_failure_stripe_sdk_dict = subscription_payment_failure_stripe_sdk_instance.to_dict()
# create an instance of SubscriptionPaymentFailureStripeSDK from a dict
subscription_payment_failure_stripe_sdk_from_dict = SubscriptionPaymentFailureStripeSDK.from_dict(subscription_payment_failure_stripe_sdk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


