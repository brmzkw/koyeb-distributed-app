# GetOrganizationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_organization_reply import GetOrganizationReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationReply from a JSON string
get_organization_reply_instance = GetOrganizationReply.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationReply.to_json())

# convert the object into a dict
get_organization_reply_dict = get_organization_reply_instance.to_dict()
# create an instance of GetOrganizationReply from a dict
get_organization_reply_from_dict = GetOrganizationReply.from_dict(get_organization_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


