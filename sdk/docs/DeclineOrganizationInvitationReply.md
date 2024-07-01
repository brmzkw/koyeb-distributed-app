# DeclineOrganizationInvitationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation** | [**OrganizationInvitation**](OrganizationInvitation.md) |  | [optional] 

## Example

```python
from openapi_client.models.decline_organization_invitation_reply import DeclineOrganizationInvitationReply

# TODO update the JSON string below
json = "{}"
# create an instance of DeclineOrganizationInvitationReply from a JSON string
decline_organization_invitation_reply_instance = DeclineOrganizationInvitationReply.from_json(json)
# print the JSON string representation of the object
print(DeclineOrganizationInvitationReply.to_json())

# convert the object into a dict
decline_organization_invitation_reply_dict = decline_organization_invitation_reply_instance.to_dict()
# create an instance of DeclineOrganizationInvitationReply from a dict
decline_organization_invitation_reply_from_dict = DeclineOrganizationInvitationReply.from_dict(decline_organization_invitation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


