# ServiceSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**by_status** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.service_summary import ServiceSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ServiceSummary from a JSON string
service_summary_instance = ServiceSummary.from_json(json)
# print the JSON string representation of the object
print(ServiceSummary.to_json())

# convert the object into a dict
service_summary_dict = service_summary_instance.to_dict()
# create an instance of ServiceSummary from a dict
service_summary_from_dict = ServiceSummary.from_dict(service_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


