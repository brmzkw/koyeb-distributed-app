# App


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**started_at** | **datetime** |  | [optional] 
**succeeded_at** | **datetime** |  | [optional] 
**paused_at** | **datetime** |  | [optional] 
**resumed_at** | **datetime** |  | [optional] 
**terminated_at** | **datetime** |  | [optional] 
**status** | [**AppStatus**](AppStatus.md) |  | [optional] 
**messages** | **List[str]** |  | [optional] 
**version** | **str** |  | [optional] 
**domains** | [**List[Domain]**](Domain.md) |  | [optional] 

## Example

```python
from openapi_client.models.app import App

# TODO update the JSON string below
json = "{}"
# create an instance of App from a JSON string
app_instance = App.from_json(json)
# print the JSON string representation of the object
print(App.to_json())

# convert the object into a dict
app_dict = app_instance.to_dict()
# create an instance of App from a dict
app_from_dict = App.from_dict(app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


