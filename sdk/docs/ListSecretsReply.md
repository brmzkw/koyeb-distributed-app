# ListSecretsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**secrets** | [**List[Secret]**](Secret.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_secrets_reply import ListSecretsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListSecretsReply from a JSON string
list_secrets_reply_instance = ListSecretsReply.from_json(json)
# print the JSON string representation of the object
print(ListSecretsReply.to_json())

# convert the object into a dict
list_secrets_reply_dict = list_secrets_reply_instance.to_dict()
# create an instance of ListSecretsReply from a dict
list_secrets_reply_from_dict = ListSecretsReply.from_dict(list_secrets_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


