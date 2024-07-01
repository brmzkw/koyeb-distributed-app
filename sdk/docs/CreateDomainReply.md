# CreateDomainReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domain** | [**Domain**](Domain.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_domain_reply import CreateDomainReply

# TODO update the JSON string below
json = "{}"
# create an instance of CreateDomainReply from a JSON string
create_domain_reply_instance = CreateDomainReply.from_json(json)
# print the JSON string representation of the object
print(CreateDomainReply.to_json())

# convert the object into a dict
create_domain_reply_dict = create_domain_reply_instance.to_dict()
# create an instance of CreateDomainReply from a dict
create_domain_reply_from_dict = CreateDomainReply.from_dict(create_domain_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


