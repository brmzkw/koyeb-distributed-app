# UsageDetails


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization_id** | **str** |  | [optional] 
**instance_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**app_name** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**service_name** | **str** |  | [optional] 
**regional_deployment_id** | **str** |  | [optional] 
**region** | **str** |  | [optional] 
**deployment_id** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**duration_seconds** | **int** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 

## Example

```python
from openapi_client.models.usage_details import UsageDetails

# TODO update the JSON string below
json = "{}"
# create an instance of UsageDetails from a JSON string
usage_details_instance = UsageDetails.from_json(json)
# print the JSON string representation of the object
print(UsageDetails.to_json())

# convert the object into a dict
usage_details_dict = usage_details_instance.to_dict()
# create an instance of UsageDetails from a dict
usage_details_from_dict = UsageDetails.from_dict(usage_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


