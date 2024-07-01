# DeactivateOrganizationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**Organization**](Organization.md) |  | [optional] 

## Example

```python
from openapi_client.models.deactivate_organization_reply import DeactivateOrganizationReply

# TODO update the JSON string below
json = "{}"
# create an instance of DeactivateOrganizationReply from a JSON string
deactivate_organization_reply_instance = DeactivateOrganizationReply.from_json(json)
# print the JSON string representation of the object
print(DeactivateOrganizationReply.to_json())

# convert the object into a dict
deactivate_organization_reply_dict = deactivate_organization_reply_instance.to_dict()
# create an instance of DeactivateOrganizationReply from a dict
deactivate_organization_reply_from_dict = DeactivateOrganizationReply.from_dict(deactivate_organization_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


