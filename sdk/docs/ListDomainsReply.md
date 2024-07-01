# ListDomainsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**domains** | [**List[Domain]**](Domain.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_domains_reply import ListDomainsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListDomainsReply from a JSON string
list_domains_reply_instance = ListDomainsReply.from_json(json)
# print the JSON string representation of the object
print(ListDomainsReply.to_json())

# convert the object into a dict
list_domains_reply_dict = list_domains_reply_instance.to_dict()
# create an instance of ListDomainsReply from a dict
list_domains_reply_from_dict = ListDomainsReply.from_dict(list_domains_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


