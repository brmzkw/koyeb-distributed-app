# Domain


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**status** | [**DomainStatus**](DomainStatus.md) |  | [optional] 
**type** | [**DomainType**](DomainType.md) |  | [optional] 
**app_id** | **str** |  | [optional] 
**deployment_group** | **str** |  | [optional] 
**verified_at** | **datetime** |  | [optional] 
**intended_cname** | **str** |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**version** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.domain import Domain

# TODO update the JSON string below
json = "{}"
# create an instance of Domain from a JSON string
domain_instance = Domain.from_json(json)
# print the JSON string representation of the object
print(Domain.to_json())

# convert the object into a dict
domain_dict = domain_instance.to_dict()
# create an instance of Domain from a dict
domain_from_dict = Domain.from_dict(domain_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


