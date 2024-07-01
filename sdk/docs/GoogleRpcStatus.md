# GoogleRpcStatus


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** |  | [optional] 
**message** | **str** |  | [optional] 
**details** | [**List[GoogleProtobufAny]**](GoogleProtobufAny.md) |  | [optional] 

## Example

```python
from openapi_client.models.google_rpc_status import GoogleRpcStatus

# TODO update the JSON string below
json = "{}"
# create an instance of GoogleRpcStatus from a JSON string
google_rpc_status_instance = GoogleRpcStatus.from_json(json)
# print the JSON string representation of the object
print(GoogleRpcStatus.to_json())

# convert the object into a dict
google_rpc_status_dict = google_rpc_status_instance.to_dict()
# create an instance of GoogleRpcStatus from a dict
google_rpc_status_from_dict = GoogleRpcStatus.from_dict(google_rpc_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


