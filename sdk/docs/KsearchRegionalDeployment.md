# KsearchRegionalDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ksearch_regional_deployment import KsearchRegionalDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of KsearchRegionalDeployment from a JSON string
ksearch_regional_deployment_instance = KsearchRegionalDeployment.from_json(json)
# print the JSON string representation of the object
print(KsearchRegionalDeployment.to_json())

# convert the object into a dict
ksearch_regional_deployment_dict = ksearch_regional_deployment_instance.to_dict()
# create an instance of KsearchRegionalDeployment from a dict
ksearch_regional_deployment_from_dict = KsearchRegionalDeployment.from_dict(ksearch_regional_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


