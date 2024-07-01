# ListDatacentersReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**datacenters** | [**List[DatacenterListItem]**](DatacenterListItem.md) |  | [optional] 

## Example

```python
from openapi_client.models.list_datacenters_reply import ListDatacentersReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListDatacentersReply from a JSON string
list_datacenters_reply_instance = ListDatacentersReply.from_json(json)
# print the JSON string representation of the object
print(ListDatacentersReply.to_json())

# convert the object into a dict
list_datacenters_reply_dict = list_datacenters_reply_instance.to_dict()
# create an instance of ListDatacentersReply from a dict
list_datacenters_reply_from_dict = ListDatacentersReply.from_dict(list_datacenters_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


