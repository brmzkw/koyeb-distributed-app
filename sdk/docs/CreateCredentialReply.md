# CreateCredentialReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credential** | [**Credential**](Credential.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_credential_reply import CreateCredentialReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredentialReply from a JSON string
create_credential_reply_instance = CreateCredentialReply.from_json(json)
# print the JSON string representation of the object
print(CreateCredentialReply.to_json())

# convert the object into a dict
create_credential_reply_dict = create_credential_reply_instance.to_dict()
# create an instance of CreateCredentialReply from a dict
create_credential_reply_from_dict = CreateCredentialReply.from_dict(create_credential_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


