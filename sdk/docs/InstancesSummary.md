# InstancesSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**by_type** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.instances_summary import InstancesSummary

# TODO update the JSON string below
json = "{}"
# create an instance of InstancesSummary from a JSON string
instances_summary_instance = InstancesSummary.from_json(json)
# print the JSON string representation of the object
print(InstancesSummary.to_json())

# convert the object into a dict
instances_summary_dict = instances_summary_instance.to_dict()
# create an instance of InstancesSummary from a dict
instances_summary_from_dict = InstancesSummary.from_dict(instances_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


