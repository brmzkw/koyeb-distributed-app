# CreateOrganizationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_organization_reply import CreateOrganizationReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreateOrganizationReply from a JSON string
create_organization_reply_instance = CreateOrganizationReply.from_json(json)
# print the JSON string representation of the object
print(CreateOrganizationReply.to_json())

# convert the object into a dict
create_organization_reply_dict = create_organization_reply_instance.to_dict()
# create an instance of CreateOrganizationReply from a dict
create_organization_reply_from_dict = CreateOrganizationReply.from_dict(create_organization_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


