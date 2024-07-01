# GetOAuthOptionsReply

A list of providers which you can use for single sign-on.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**oauth_providers** | [**List[OAuthProvider]**](OAuthProvider.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_o_auth_options_reply import GetOAuthOptionsReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetOAuthOptionsReply from a JSON string
get_o_auth_options_reply_instance = GetOAuthOptionsReply.from_json(json)
# print the JSON string representation of the object
print(GetOAuthOptionsReply.to_json())

# convert the object into a dict
get_o_auth_options_reply_dict = get_o_auth_options_reply_instance.to_dict()
# create an instance of GetOAuthOptionsReply from a dict
get_o_auth_options_reply_from_dict = GetOAuthOptionsReply.from_dict(get_o_auth_options_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


