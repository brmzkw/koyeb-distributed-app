# StreamResultOfExecCommandReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | [**ExecCommandReply**](ExecCommandReply.md) |  | [optional] 
**error** | [**GoogleRpcStatus**](GoogleRpcStatus.md) |  | [optional] 

## Example

```python
from openapi_client.models.stream_result_of_exec_command_reply import StreamResultOfExecCommandReply

# TODO update the JSON string below
json = "{}"
# create an instance of StreamResultOfExecCommandReply from a JSON string
stream_result_of_exec_command_reply_instance = StreamResultOfExecCommandReply.from_json(json)
# print the JSON string representation of the object
print(StreamResultOfExecCommandReply.to_json())

# convert the object into a dict
stream_result_of_exec_command_reply_dict = stream_result_of_exec_command_reply_instance.to_dict()
# create an instance of StreamResultOfExecCommandReply from a dict
stream_result_of_exec_command_reply_from_dict = StreamResultOfExecCommandReply.from_dict(stream_result_of_exec_command_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


