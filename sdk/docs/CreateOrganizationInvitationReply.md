# CreateOrganizationInvitationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitation** | [**OrganizationInvitation**](OrganizationInvitation.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_organization_invitation_reply import CreateOrganizationInvitationReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationInvitationReply from a JSON string
create_organization_invitation_reply_instance = CreateOrganizationInvitationReply.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationInvitationReply.to_json())

# convert the object into a dict
create_organization_invitation_reply_dict = create_organization_invitation_reply_instance.to_dict()
# create an instance of CreateOrganizationInvitationReply from a dict
create_organization_invitation_reply_from_dict = CreateOrganizationInvitationReply.from_dict(create_organization_invitation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


