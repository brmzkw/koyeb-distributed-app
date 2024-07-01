# UpdateOrganizationPlanReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_organization_plan_reply import UpdateOrganizationPlanReply

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationPlanReply from a JSON string
update_organization_plan_reply_instance = UpdateOrganizationPlanReply.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationPlanReply.to_json())

# convert the object into a dict
update_organization_plan_reply_dict = update_organization_plan_reply_instance.to_dict()
# create an instance of UpdateOrganizationPlanReply from a dict
update_organization_plan_reply_from_dict = UpdateOrganizationPlanReply.from_dict(update_organization_plan_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


