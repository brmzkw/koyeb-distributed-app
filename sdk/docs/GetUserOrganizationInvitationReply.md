# GetUserOrganizationInvitationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation** | [**OrganizationInvitation**](OrganizationInvitation.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_user_organization_invitation_reply import GetUserOrganizationInvitationReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetUserOrganizationInvitationReply from a JSON string
get_user_organization_invitation_reply_instance = GetUserOrganizationInvitationReply.from_json(json)
# print the JSON string representation of the object
print(GetUserOrganizationInvitationReply.to_json())

# convert the object into a dict
get_user_organization_invitation_reply_dict = get_user_organization_invitation_reply_instance.to_dict()
# create an instance of GetUserOrganizationInvitationReply from a dict
get_user_organization_invitation_reply_from_dict = GetUserOrganizationInvitationReply.from_dict(get_user_organization_invitation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


