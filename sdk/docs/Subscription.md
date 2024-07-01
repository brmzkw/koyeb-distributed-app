# Subscription


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**version** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**stripe_subscription_id** | **str** |  | [optional] 
**status** | [**SubscriptionStatus**](SubscriptionStatus.md) |  | [optional] [default to SubscriptionStatus.INVALID]
**messages** | **List[str]** |  | [optional] 
**has_pending_update** | **bool** |  | [optional] 
**stripe_pending_invoice_id** | **str** |  | [optional] 
**terminate_at** | **datetime** |  | [optional] 
**canceled_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**current_period_start** | **datetime** |  | [optional] 
**current_period_end** | **datetime** |  | [optional] 
**currency** | **str** |  | [optional] 
**amount_payable** | **str** |  | [optional] 
**amount_paid** | **str** |  | [optional] 
**amount_remaining** | **str** |  | [optional] 
**payment_failure** | [**SubscriptionPaymentFailure**](SubscriptionPaymentFailure.md) |  | [optional] 

## Example

```python
from openapi_client.models.subscription import Subscription

# TODO update the JSON string below
json = "{}"
# create an instance of Subscription from a JSON string
subscription_instance = Subscription.from_json(json)
# print the JSON string representation of the object
print(Subscription.to_json())

# convert the object into a dict
subscription_dict = subscription_instance.to_dict()
# create an instance of Subscription from a dict
subscription_from_dict = Subscription.from_dict(subscription_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


