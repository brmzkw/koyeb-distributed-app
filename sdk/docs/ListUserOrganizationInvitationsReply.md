# ListUserOrganizationInvitationsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**invitations** | [**List[OrganizationInvitation]**](OrganizationInvitation.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_user_organization_invitations_reply import ListUserOrganizationInvitationsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListUserOrganizationInvitationsReply from a JSON string
list_user_organization_invitations_reply_instance = ListUserOrganizationInvitationsReply.from_json(json)
# print the JSON string representation of the object
print(ListUserOrganizationInvitationsReply.to_json())

# convert the object into a dict
list_user_organization_invitations_reply_dict = list_user_organization_invitations_reply_instance.to_dict()
# create an instance of ListUserOrganizationInvitationsReply from a dict
list_user_organization_invitations_reply_from_dict = ListUserOrganizationInvitationsReply.from_dict(list_user_organization_invitations_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


