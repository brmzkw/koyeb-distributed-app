# ListOrganizationMembersReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**members** | [**List[OrganizationMember]**](OrganizationMember.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_organization_members_reply import ListOrganizationMembersReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListOrganizationMembersReply from a JSON string
list_organization_members_reply_instance = ListOrganizationMembersReply.from_json(json)
# print the JSON string representation of the object
print(ListOrganizationMembersReply.to_json())

# convert the object into a dict
list_organization_members_reply_dict = list_organization_members_reply_instance.to_dict()
# create an instance of ListOrganizationMembersReply from a dict
list_organization_members_reply_from_dict = ListOrganizationMembersReply.from_dict(list_organization_members_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


