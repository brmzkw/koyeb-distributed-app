# RemoveOrganizationMemberReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member** | [**OrganizationMember**](OrganizationMember.md) |  | [optional] 

## Example

```python
from openapi_client.models.remove_organization_member_reply import RemoveOrganizationMemberReply

# TODO update the JSON string below
json = "{}"
# create an instance of RemoveOrganizationMemberReply from a JSON string
remove_organization_member_reply_instance = RemoveOrganizationMemberReply.from_json(json)
# print the JSON string representation of the object
print(RemoveOrganizationMemberReply.to_json())

# convert the object into a dict
remove_organization_member_reply_dict = remove_organization_member_reply_instance.to_dict()
# create an instance of RemoveOrganizationMemberReply from a dict
remove_organization_member_reply_from_dict = RemoveOrganizationMemberReply.from_dict(remove_organization_member_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


