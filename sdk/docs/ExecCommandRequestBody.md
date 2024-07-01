# ExecCommandRequestBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**command** | **List[str]** | Command to exec. Mandatory in the first frame sent | [optional] 
**tty_size** | [**ExecCommandRequestTerminalSize**](ExecCommandRequestTerminalSize.md) |  | [optional] 
**stdin** | [**ExecCommandIO**](ExecCommandIO.md) |  | [optional] 
**disable_tty** | **bool** | Disable TTY. It&#39;s enough to specify it in the first frame | [optional] 

## Example

```python
from openapi_client.models.exec_command_request_body import ExecCommandRequestBody

# TODO update the JSON string below
json = "{}"
# create an instance of ExecCommandRequestBody from a JSON string
exec_command_request_body_instance = ExecCommandRequestBody.from_json(json)
# print the JSON string representation of the object
print(ExecCommandRequestBody.to_json())

# convert the object into a dict
exec_command_request_body_dict = exec_command_request_body_instance.to_dict()
# create an instance of ExecCommandRequestBody from a dict
exec_command_request_body_from_dict = ExecCommandRequestBody.from_dict(exec_command_request_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


