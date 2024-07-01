# UpdateSecretReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secret** | [**Secret**](Secret.md) |  | [optional] 

## Example

```python
from openapi_client.models.update_secret_reply import UpdateSecretReply

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateSecretReply from a JSON string
update_secret_reply_instance = UpdateSecretReply.from_json(json)
# print the JSON string representation of the object
print(UpdateSecretReply.to_json())

# convert the object into a dict
update_secret_reply_dict = update_secret_reply_instance.to_dict()
# create an instance of UpdateSecretReply from a dict
update_secret_reply_from_dict = UpdateSecretReply.from_dict(update_secret_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


