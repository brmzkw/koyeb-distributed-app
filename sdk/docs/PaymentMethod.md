# PaymentMethod


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**version** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**type** | **str** |  | [optional] 
**provider** | **str** |  | [optional] 
**status** | [**PaymentMethodStatus**](PaymentMethodStatus.md) |  | [optional] [default to PaymentMethodStatus.INVALID]
**messages** | **List[str]** |  | [optional] 
**stripe_payment_method_id** | **str** |  | [optional] 
**authorization_verified_at** | **datetime** |  | [optional] 
**authorization_canceled_at** | **datetime** |  | [optional] 
**authorization_stripe_payment_intent_id** | **str** |  | [optional] 
**authorization_stripe_payment_intent_client_secret** | **str** |  | [optional] 
**card_brand** | **str** |  | [optional] 
**card_country** | **str** |  | [optional] 
**card_funding** | **str** |  | [optional] 
**card_fingerprint** | **str** |  | [optional] 
**card_last_digits** | **str** |  | [optional] 
**card_expiration_month** | **int** |  | [optional] 
**card_expiration_year** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.payment_method import PaymentMethod

# TODO update the JSON string below
json = "{}"
# create an instance of PaymentMethod from a JSON string
payment_method_instance = PaymentMethod.from_json(json)
# print the JSON string representation of the object
print(PaymentMethod.to_json())

# convert the object into a dict
payment_method_dict = payment_method_instance.to_dict()
# create an instance of PaymentMethod from a dict
payment_method_from_dict = PaymentMethod.from_dict(payment_method_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


