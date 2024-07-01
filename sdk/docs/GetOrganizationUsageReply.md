# GetOrganizationUsageReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage** | [**Usage**](Usage.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_organization_usage_reply import GetOrganizationUsageReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationUsageReply from a JSON string
get_organization_usage_reply_instance = GetOrganizationUsageReply.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationUsageReply.to_json())

# convert the object into a dict
get_organization_usage_reply_dict = get_organization_usage_reply_instance.to_dict()
# create an instance of GetOrganizationUsageReply from a dict
get_organization_usage_reply_from_dict = GetOrganizationUsageReply.from_dict(get_organization_usage_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


