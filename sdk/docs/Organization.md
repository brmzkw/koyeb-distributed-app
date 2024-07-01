# Organization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**address1** | **str** |  | [optional] 
**address2** | **str** |  | [optional] 
**city** | **str** |  | [optional] 
**postal_code** | **str** |  | [optional] 
**state** | **str** |  | [optional] 
**country** | **str** |  | [optional] 
**company** | **bool** |  | [optional] 
**vat_number** | **str** |  | [optional] 
**billing_name** | **str** |  | [optional] 
**billing_email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**plan_updated_at** | **datetime** |  | [optional] 
**has_payment_method** | **bool** |  | [optional] 
**subscription_id** | **str** |  | [optional] 
**current_subscription_id** | **str** |  | [optional] 
**latest_subscription_id** | **str** |  | [optional] 
**signup_qualification** | **object** |  | [optional] 
**status** | [**OrganizationStatus**](OrganizationStatus.md) |  | [optional] 
**status_message** | [**OrganizationDetailedStatus**](OrganizationDetailedStatus.md) |  | [optional] 
**deactivation_reason** | [**OrganizationDeactivationReason**](OrganizationDeactivationReason.md) |  | [optional] 
**verified** | **bool** |  | [optional] 
**qualifies_for_hobby23** | **bool** |  | [optional] 
**reprocess_after** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.organization import Organization

# TODO update the JSON string below
json = "{}"
# create an instance of Organization from a JSON string
organization_instance = Organization.from_json(json)
# print the JSON string representation of the object
print(Organization.to_json())

# convert the object into a dict
organization_dict = organization_instance.to_dict()
# create an instance of Organization from a dict
organization_from_dict = Organization.from_dict(organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


