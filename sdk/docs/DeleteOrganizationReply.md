# DeleteOrganizationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from openapi_client.models.delete_organization_reply import DeleteOrganizationReply

# TODO update the JSON string below
json = "{}"
# create an instance of DeleteOrganizationReply from a JSON string
delete_organization_reply_instance = DeleteOrganizationReply.from_json(json)
# print the JSON string representation of the object
print(DeleteOrganizationReply.to_json())

# convert the object into a dict
delete_organization_reply_dict = delete_organization_reply_instance.to_dict()
# create an instance of DeleteOrganizationReply from a dict
delete_organization_reply_from_dict = DeleteOrganizationReply.from_dict(delete_organization_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


