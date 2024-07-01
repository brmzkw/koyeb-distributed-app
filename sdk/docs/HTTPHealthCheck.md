# HTTPHealthCheck


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**path** | **str** |  | [optional] 
**method** | **str** |  | [optional] 
**headers** | [**List[HTTPHeader]**](HTTPHeader.md) |  | [optional] 

## Example

```python
from openapi_client.models.http_health_check import HTTPHealthCheck

# TODO update the JSON string below
json = "{}"
# create an instance of HTTPHealthCheck from a JSON string
http_health_check_instance = HTTPHealthCheck.from_json(json)
# print the JSON string representation of the object
print(HTTPHealthCheck.to_json())

# convert the object into a dict
http_health_check_dict = http_health_check_instance.to_dict()
# create an instance of HTTPHealthCheck from a dict
http_health_check_from_dict = HTTPHealthCheck.from_dict(http_health_check_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


