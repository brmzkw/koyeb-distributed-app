# AppUsage


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**services** | [**List[ServiceUsage]**](ServiceUsage.md) |  | [optional] 

## Example

```python
from openapi_client.models.app_usage import AppUsage

# TODO update the JSON string below
json = "{}"
# create an instance of AppUsage from a JSON string
app_usage_instance = AppUsage.from_json(json)
# print the JSON string representation of the object
print(AppUsage.to_json())

# convert the object into a dict
app_usage_dict = app_usage_instance.to_dict()
# create an instance of AppUsage from a dict
app_usage_from_dict = AppUsage.from_dict(app_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


