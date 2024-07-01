# CreateSecretReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | [**Secret**](Secret.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_secret_reply import CreateSecretReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreateSecretReply from a JSON string
create_secret_reply_instance = CreateSecretReply.from_json(json)
# print the JSON string representation of the object
print(CreateSecretReply.to_json())

# convert the object into a dict
create_secret_reply_dict = create_secret_reply_instance.to_dict()
# create an instance of CreateSecretReply from a dict
create_secret_reply_from_dict = CreateSecretReply.from_dict(create_secret_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


