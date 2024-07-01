# AutocompleteReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | **List[str]** |  | [optional] 
**user_env** | **List[str]** |  | [optional] 
**system_env** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.autocomplete_reply import AutocompleteReply

# TODO update the JSON string below
json = "{}"
# create an instance of AutocompleteReply from a JSON string
autocomplete_reply_instance = AutocompleteReply.from_json(json)
# print the JSON string representation of the object
print(AutocompleteReply.to_json())

# convert the object into a dict
autocomplete_reply_dict = autocomplete_reply_instance.to_dict()
# create an instance of AutocompleteReply from a dict
autocomplete_reply_from_dict = AutocompleteReply.from_dict(autocomplete_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


