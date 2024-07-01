# ExecCommandRequestTerminalSize


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**height** | **int** |  | [optional] 
**width** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.exec_command_request_terminal_size import ExecCommandRequestTerminalSize

# TODO update the JSON string below
json = "{}"
# create an instance of ExecCommandRequestTerminalSize from a JSON string
exec_command_request_terminal_size_instance = ExecCommandRequestTerminalSize.from_json(json)
# print the JSON string representation of the object
print(ExecCommandRequestTerminalSize.to_json())

# convert the object into a dict
exec_command_request_terminal_size_dict = exec_command_request_terminal_size_instance.to_dict()
# create an instance of ExecCommandRequestTerminalSize from a dict
exec_command_request_terminal_size_from_dict = ExecCommandRequestTerminalSize.from_dict(exec_command_request_terminal_size_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


