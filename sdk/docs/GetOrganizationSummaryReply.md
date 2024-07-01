# GetOrganizationSummaryReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**OrganizationSummary**](OrganizationSummary.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_organization_summary_reply import GetOrganizationSummaryReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationSummaryReply from a JSON string
get_organization_summary_reply_instance = GetOrganizationSummaryReply.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationSummaryReply.to_json())

# convert the object into a dict
get_organization_summary_reply_dict = get_organization_summary_reply_instance.to_dict()
# create an instance of GetOrganizationSummaryReply from a dict
get_organization_summary_reply_from_dict = GetOrganizationSummaryReply.from_dict(get_organization_summary_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


