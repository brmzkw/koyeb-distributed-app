# OrganizationMember


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**user_id** | **str** |  | [optional] 
**joined_at** | **datetime** |  | [optional] 
**role** | [**UserRoleRole**](UserRoleRole.md) |  | [optional] [default to UserRoleRole.INVALID]
**status** | [**OrganizationMemberStatus**](OrganizationMemberStatus.md) |  | [optional] [default to OrganizationMemberStatus.INVALID]
**user** | [**PublicUser**](PublicUser.md) |  | [optional] 
**organization** | [**PublicOrganization**](PublicOrganization.md) |  | [optional] 

## Example

```python
from openapi_client.models.organization_member import OrganizationMember

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationMember from a JSON string
organization_member_instance = OrganizationMember.from_json(json)
# print the JSON string representation of the object
print(OrganizationMember.to_json())

# convert the object into a dict
organization_member_dict = organization_member_instance.to_dict()
# create an instance of OrganizationMember from a dict
organization_member_from_dict = OrganizationMember.from_dict(organization_member_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


