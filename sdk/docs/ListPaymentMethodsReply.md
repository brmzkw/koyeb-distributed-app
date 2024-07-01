# ListPaymentMethodsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payment_methods** | [**List[PaymentMethod]**](PaymentMethod.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_payment_methods_reply import ListPaymentMethodsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListPaymentMethodsReply from a JSON string
list_payment_methods_reply_instance = ListPaymentMethodsReply.from_json(json)
# print the JSON string representation of the object
print(ListPaymentMethodsReply.to_json())

# convert the object into a dict
list_payment_methods_reply_dict = list_payment_methods_reply_instance.to_dict()
# create an instance of ListPaymentMethodsReply from a dict
list_payment_methods_reply_from_dict = ListPaymentMethodsReply.from_dict(list_payment_methods_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


