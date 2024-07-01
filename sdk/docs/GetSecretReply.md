# GetSecretReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | [**Secret**](Secret.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_secret_reply import GetSecretReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetSecretReply from a JSON string
get_secret_reply_instance = GetSecretReply.from_json(json)
# print the JSON string representation of the object
print(GetSecretReply.to_json())

# convert the object into a dict
get_secret_reply_dict = get_secret_reply_instance.to_dict()
# create an instance of GetSecretReply from a dict
get_secret_reply_from_dict = GetSecretReply.from_dict(get_secret_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)

