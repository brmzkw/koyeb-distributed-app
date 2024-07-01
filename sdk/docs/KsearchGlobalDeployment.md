# KsearchGlobalDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ksearch_global_deployment import KsearchGlobalDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of KsearchGlobalDeployment from a JSON string
ksearch_global_deployment_instance = KsearchGlobalDeployment.from_json(json)
# print the JSON string representation of the object
print(KsearchGlobalDeployment.to_json())

# convert the object into a dict
ksearch_global_deployment_dict = ksearch_global_deployment_instance.to_dict()
# create an instance of KsearchGlobalDeployment from a dict
ksearch_global_deployment_from_dict = KsearchGlobalDeployment.from_dict(ksearch_global_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


