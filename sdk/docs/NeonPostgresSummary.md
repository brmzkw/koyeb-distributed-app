# NeonPostgresSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**by_instance_type** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.neon_postgres_summary import NeonPostgresSummary

# TODO update the JSON string below
json = "{}"
# create an instance of NeonPostgresSummary from a JSON string
neon_postgres_summary_instance = NeonPostgresSummary.from_json(json)
# print the JSON string representation of the object
print(NeonPostgresSummary.to_json())

# convert the object into a dict
neon_postgres_summary_dict = neon_postgres_summary_instance.to_dict()
# create an instance of NeonPostgresSummary from a dict
neon_postgres_summary_from_dict = NeonPostgresSummary.from_dict(neon_postgres_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


