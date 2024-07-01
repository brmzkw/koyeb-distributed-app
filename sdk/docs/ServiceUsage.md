# ServiceUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**regions** | [**Dict[str, RegionUsage]**](RegionUsage.md) |  | [optional] 

## Example

```python
from openapi_client.models.service_usage import ServiceUsage

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceUsage from a JSON string
service_usage_instance = ServiceUsage.from_json(json)
# print the JSON string representation of the object
print(ServiceUsage.to_json())

# convert the object into a dict
service_usage_dict = service_usage_instance.to_dict()
# create an instance of ServiceUsage from a dict
service_usage_from_dict = ServiceUsage.from_dict(service_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


