# UpdateOrganizationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_organization_reply import UpdateOrganizationReply

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateOrganizationReply from a JSON string
update_organization_reply_instance = UpdateOrganizationReply.from_json(json)
# print the JSON string representation of the object
print(UpdateOrganizationReply.to_json())

# convert the object into a dict
update_organization_reply_dict = update_organization_reply_instance.to_dict()
# create an instance of UpdateOrganizationReply from a dict
update_organization_reply_from_dict = UpdateOrganizationReply.from_dict(update_organization_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


