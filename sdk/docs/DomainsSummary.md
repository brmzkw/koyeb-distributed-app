# DomainsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**by_status** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.domains_summary import DomainsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of DomainsSummary from a JSON string
domains_summary_instance = DomainsSummary.from_json(json)
# print the JSON string representation of the object
print(DomainsSummary.to_json())

# convert the object into a dict
domains_summary_dict = domains_summary_instance.to_dict()
# create an instance of DomainsSummary from a dict
domains_summary_from_dict = DomainsSummary.from_dict(domains_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


