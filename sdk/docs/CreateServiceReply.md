# CreateServiceReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | [**Service**](Service.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_service_reply import CreateServiceReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreateServiceReply from a JSON string
create_service_reply_instance = CreateServiceReply.from_json(json)
# print the JSON string representation of the object
print(CreateServiceReply.to_json())

# convert the object into a dict
create_service_reply_dict = create_service_reply_instance.to_dict()
# create an instance of CreateServiceReply from a dict
create_service_reply_from_dict = CreateServiceReply.from_dict(create_service_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


