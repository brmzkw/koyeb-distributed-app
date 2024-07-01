# AcceptOrganizationInvitationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation** | [**OrganizationInvitation**](OrganizationInvitation.md) |  | [optional] 

## Example

```python
from openapi_client.models.accept_organization_invitation_reply import AcceptOrganizationInvitationReply

# TODO update the JSON string below
json = "{}"
# create an instance of AcceptOrganizationInvitationReply from a JSON string
accept_organization_invitation_reply_instance = AcceptOrganizationInvitationReply.from_json(json)
# print the JSON string representation of the object
print(AcceptOrganizationInvitationReply.to_json())

# convert the object into a dict
accept_organization_invitation_reply_dict = accept_organization_invitation_reply_instance.to_dict()
# create an instance of AcceptOrganizationInvitationReply from a dict
accept_organization_invitation_reply_from_dict = AcceptOrganizationInvitationReply.from_dict(accept_organization_invitation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


