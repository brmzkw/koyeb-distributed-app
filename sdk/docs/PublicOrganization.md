# PublicOrganization


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**plan** | [**Plan**](Plan.md) |  | [optional] 
**status** | [**OrganizationStatus**](OrganizationStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.public_organization import PublicOrganization

# TODO update the JSON string below
json = "{}"
# create an instance of PublicOrganization from a JSON string
public_organization_instance = PublicOrganization.from_json(json)
# print the JSON string representation of the object
print(PublicOrganization.to_json())

# convert the object into a dict
public_organization_dict = public_organization_instance.to_dict()
# create an instance of PublicOrganization from a dict
public_organization_from_dict = PublicOrganization.from_dict(public_organization_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


