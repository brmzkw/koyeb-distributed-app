# ListCredentialsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | [**List[Credential]**](Credential.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_credentials_reply import ListCredentialsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListCredentialsReply from a JSON string
list_credentials_reply_instance = ListCredentialsReply.from_json(json)
# print the JSON string representation of the object
print(ListCredentialsReply.to_json())

# convert the object into a dict
list_credentials_reply_dict = list_credentials_reply_instance.to_dict()
# create an instance of ListCredentialsReply from a dict
list_credentials_reply_from_dict = ListCredentialsReply.from_dict(list_credentials_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


