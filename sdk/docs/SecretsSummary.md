# SecretsSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**by_type** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.secrets_summary import SecretsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of SecretsSummary from a JSON string
secrets_summary_instance = SecretsSummary.from_json(json)
# print the JSON string representation of the object
print(SecretsSummary.to_json())

# convert the object into a dict
secrets_summary_dict = secrets_summary_instance.to_dict()
# create an instance of SecretsSummary from a dict
secrets_summary_from_dict = SecretsSummary.from_dict(secrets_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


