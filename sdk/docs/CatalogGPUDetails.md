# CatalogGPUDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**count** | **int** |  | [optional] 
**brand** | **str** |  | [optional] 
**memory** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.catalog_gpu_details import CatalogGPUDetails

# TODO update the JSON string below
json = "{}"
# create an instance of CatalogGPUDetails from a JSON string
catalog_gpu_details_instance = CatalogGPUDetails.from_json(json)
# print the JSON string representation of the object
print(CatalogGPUDetails.to_json())

# convert the object into a dict
catalog_gpu_details_dict = catalog_gpu_details_instance.to_dict()
# create an instance of CatalogGPUDetails from a dict
catalog_gpu_details_from_dict = CatalogGPUDetails.from_dict(catalog_gpu_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


