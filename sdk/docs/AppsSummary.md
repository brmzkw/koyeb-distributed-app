# AppsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**by_status** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.apps_summary import AppsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AppsSummary from a JSON string
apps_summary_instance = AppsSummary.from_json(json)
# print the JSON string representation of the object
print(AppsSummary.to_json())

# convert the object into a dict
apps_summary_dict = apps_summary_instance.to_dict()
# create an instance of AppsSummary from a dict
apps_summary_from_dict = AppsSummary.from_dict(apps_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


