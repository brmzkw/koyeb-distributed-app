# OrganizationInvitation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**role** | [**UserRoleRole**](UserRoleRole.md) |  | [optional] [default to UserRoleRole.INVALID]
**status** | [**OrganizationInvitationStatus**](OrganizationInvitationStatus.md) |  | [optional] [default to OrganizationInvitationStatus.INVALID]
**expires_at** | **datetime** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**organization** | [**PublicOrganization**](PublicOrganization.md) |  | [optional] 
**invitee_id** | **str** |  | [optional] 
**invitee** | [**PublicUser**](PublicUser.md) |  | [optional] 
**inviter_id** | **str** |  | [optional] 
**inviter** | [**PublicUser**](PublicUser.md) |  | [optional] 

## Example

```python
from openapi_client.models.organization_invitation import OrganizationInvitation

# TODO update the JSON string below
json = "{}"
# create an instance of OrganizationInvitation from a JSON string
organization_invitation_instance = OrganizationInvitation.from_json(json)
# print the JSON string representation of the object
print(OrganizationInvitation.to_json())

# convert the object into a dict
organization_invitation_dict = organization_invitation_instance.to_dict()
# create an instance of OrganizationInvitation from a dict
organization_invitation_from_dict = OrganizationInvitation.from_dict(organization_invitation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


