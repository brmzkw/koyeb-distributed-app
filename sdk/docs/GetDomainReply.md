# GetDomainReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**Domain**](Domain.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_domain_reply import GetDomainReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetDomainReply from a JSON string
get_domain_reply_instance = GetDomainReply.from_json(json)
# print the JSON string representation of the object
print(GetDomainReply.to_json())

# convert the object into a dict
get_domain_reply_dict = get_domain_reply_instance.to_dict()
# create an instance of GetDomainReply from a dict
get_domain_reply_from_dict = GetDomainReply.from_dict(get_domain_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


