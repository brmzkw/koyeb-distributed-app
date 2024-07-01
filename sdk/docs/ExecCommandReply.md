# ExecCommandReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stdout** | [**ExecCommandIO**](ExecCommandIO.md) |  | [optional] 
**stderr** | [**ExecCommandIO**](ExecCommandIO.md) |  | [optional] 
**exited** | **bool** |  | [optional] 
**exit_code** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.exec_command_reply import ExecCommandReply

# TODO update the JSON string below
json = "{}"
# create an instance of ExecCommandReply from a JSON string
exec_command_reply_instance = ExecCommandReply.from_json(json)
# print the JSON string representation of the object
print(ExecCommandReply.to_json())

# convert the object into a dict
exec_command_reply_dict = exec_command_reply_instance.to_dict()
# create an instance of ExecCommandReply from a dict
exec_command_reply_from_dict = ExecCommandReply.from_dict(exec_command_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


