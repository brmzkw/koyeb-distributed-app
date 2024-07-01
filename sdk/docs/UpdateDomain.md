# UpdateDomain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** | To attach or detach from an app for custom domain. | [optional] 
**subdomain** | **str** | To change subdomain for auto-assigned domain. | [optional] 

## Example

```python
from openapi_client.models.update_domain import UpdateDomain

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateDomain from a JSON string
update_domain_instance = UpdateDomain.from_json(json)
# print the JSON string representation of the object
print(UpdateDomain.to_json())

# convert the object into a dict
update_domain_dict = update_domain_instance.to_dict()
# create an instance of UpdateDomain from a dict
update_domain_from_dict = UpdateDomain.from_dict(update_domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


