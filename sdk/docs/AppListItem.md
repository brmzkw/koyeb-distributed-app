# AppListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**domains** | [**List[Domain]**](Domain.md) |  | [optional] 
**status** | [**AppStatus**](AppStatus.md) |  | [optional] [default to AppStatus.STARTING]
**messages** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.app_list_item import AppListItem

# TODO update the JSON string below
json = "{}"
# create an instance of AppListItem from a JSON string
app_list_item_instance = AppListItem.from_json(json)
# print the JSON string representation of the object
print(AppListItem.to_json())

# convert the object into a dict
app_list_item_dict = app_list_item_instance.to_dict()
# create an instance of AppListItem from a dict
app_list_item_from_dict = AppListItem.from_dict(app_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


