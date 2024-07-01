# TCPHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.tcp_health_check import TCPHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of TCPHealthCheck from a JSON string
tcp_health_check_instance = TCPHealthCheck.from_json(json)
# print the JSON string representation of the object
print(TCPHealthCheck.to_json())

# convert the object into a dict
tcp_health_check_dict = tcp_health_check_instance.to_dict()
# create an instance of TCPHealthCheck from a dict
tcp_health_check_from_dict = TCPHealthCheck.from_dict(tcp_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


