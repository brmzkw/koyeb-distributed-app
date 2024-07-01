# AutocompleteRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**DeploymentDefinition**](DeploymentDefinition.md) |  | [optional] 

## Example

```python
from openapi_client.models.autocomplete_request import AutocompleteRequest

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteRequest from a JSON string
autocomplete_request_instance = AutocompleteRequest.from_json(json)
# print the JSON string representation of the object
print(AutocompleteRequest.to_json())

# convert the object into a dict
autocomplete_request_dict = autocomplete_request_instance.to_dict()
# create an instance of AutocompleteRequest from a dict
autocomplete_request_from_dict = AutocompleteRequest.from_dict(autocomplete_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


