# ResendOrganizationInvitationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation** | [**OrganizationInvitation**](OrganizationInvitation.md) |  | [optional] 

## Example

```python
from openapi_client.models.resend_organization_invitation_reply import ResendOrganizationInvitationReply

# TODO update the JSON string below
json = "{}"
# create an instance of ResendOrganizationInvitationReply from a JSON string
resend_organization_invitation_reply_instance = ResendOrganizationInvitationReply.from_json(json)
# print the JSON string representation of the object
print(ResendOrganizationInvitationReply.to_json())

# convert the object into a dict
resend_organization_invitation_reply_dict = resend_organization_invitation_reply_instance.to_dict()
# create an instance of ResendOrganizationInvitationReply from a dict
resend_organization_invitation_reply_from_dict = ResendOrganizationInvitationReply.from_dict(resend_organization_invitation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


