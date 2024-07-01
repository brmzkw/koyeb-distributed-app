# CatalogInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**vcpu** | **int** | The number of cpus. Deprecated. Use vcpu_shares instead. | [optional] 
**memory** | **str** |  | [optional] 
**disk** | **str** |  | [optional] 
**price_hourly** | **str** |  | [optional] 
**price_monthly** | **str** |  | [optional] 
**regions** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**require_plan** | **List[str]** |  | [optional] 
**vcpu_shares** | **float** | The number of vcpu shares reserved for the instance. | [optional] 
**display_name** | **str** |  | [optional] 
**aliases** | **List[str]** |  | [optional] 
**type** | **str** |  | [optional] 
**gpu** | [**CatalogGPUDetails**](CatalogGPUDetails.md) |  | [optional] 
**service_types** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.catalog_instance import CatalogInstance

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogInstance from a JSON string
catalog_instance_instance = CatalogInstance.from_json(json)
# print the JSON string representation of the object
print(CatalogInstance.to_json())

# convert the object into a dict
catalog_instance_dict = catalog_instance_instance.to_dict()
# create an instance of CatalogInstance from a dict
catalog_instance_from_dict = CatalogInstance.from_dict(catalog_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


