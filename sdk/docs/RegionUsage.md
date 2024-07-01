# RegionUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**Dict[str, InstanceUsage]**](InstanceUsage.md) |  | [optional] 

## Example

```python
from openapi_client.models.region_usage import RegionUsage

# TODO update the JSON string below
json = "{}"
# create an instance of RegionUsage from a JSON string
region_usage_instance = RegionUsage.from_json(json)
# print the JSON string representation of the object
print(RegionUsage.to_json())

# convert the object into a dict
region_usage_dict = region_usage_instance.to_dict()
# create an instance of RegionUsage from a dict
region_usage_from_dict = RegionUsage.from_dict(region_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


