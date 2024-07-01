# GetOrganizationUsageDetailsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**usage_details** | [**List[UsageDetails]**](UsageDetails.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 
**order** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.get_organization_usage_details_reply import GetOrganizationUsageDetailsReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetOrganizationUsageDetailsReply from a JSON string
get_organization_usage_details_reply_instance = GetOrganizationUsageDetailsReply.from_json(json)
# print the JSON string representation of the object
print(GetOrganizationUsageDetailsReply.to_json())

# convert the object into a dict
get_organization_usage_details_reply_dict = get_organization_usage_details_reply_instance.to_dict()
# create an instance of GetOrganizationUsageDetailsReply from a dict
get_organization_usage_details_reply_from_dict = GetOrganizationUsageDetailsReply.from_dict(get_organization_usage_details_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


