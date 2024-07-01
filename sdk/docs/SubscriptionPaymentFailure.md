# SubscriptionPaymentFailure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failed_at** | **datetime** |  | [optional] 
**next_attempt** | **datetime** |  | [optional] 
**attempt_count** | **str** |  | [optional] 
**error_code** | **str** |  | [optional] 
**error_reason** | **str** |  | [optional] 
**error_type** | **str** |  | [optional] 
**error_message** | **str** |  | [optional] 
**payment_method_required** | **bool** |  | [optional] 
**redirect_url** | **str** |  | [optional] 
**stripe_sdk** | [**SubscriptionPaymentFailureStripeSDK**](SubscriptionPaymentFailureStripeSDK.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscription_payment_failure import SubscriptionPaymentFailure

# TODO update the JSON string below
json = "{}"
# create an instance of SubscriptionPaymentFailure from a JSON string
subscription_payment_failure_instance = SubscriptionPaymentFailure.from_json(json)
# print the JSON string representation of the object
print(SubscriptionPaymentFailure.to_json())

# convert the object into a dict
subscription_payment_failure_dict = subscription_payment_failure_instance.to_dict()
# create an instance of SubscriptionPaymentFailure from a dict
subscription_payment_failure_from_dict = SubscriptionPaymentFailure.from_dict(subscription_payment_failure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


