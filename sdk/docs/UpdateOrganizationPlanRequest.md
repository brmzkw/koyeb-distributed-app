# UpdateOrganizationPlanRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**plan** | [**Plan**](Plan.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_organization_plan_request import UpdateOrganizationPlanRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationPlanRequest from a JSON string
update_organization_plan_request_instance = UpdateOrganizationPlanRequest.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationPlanRequest.to_json())

# convert the object into a dict
update_organization_plan_request_dict = update_organization_plan_request_instance.to_dict()
# create an instance of UpdateOrganizationPlanRequest from a dict
update_organization_plan_request_from_dict = UpdateOrganizationPlanRequest.from_dict(update_organization_plan_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


