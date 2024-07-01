# ListServicesReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**services** | [**List[ServiceListItem]**](ServiceListItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_services_reply import ListServicesReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListServicesReply from a JSON string
list_services_reply_instance = ListServicesReply.from_json(json)
# print the JSON string representation of the object
print(ListServicesReply.to_json())

# convert the object into a dict
list_services_reply_dict = list_services_reply_instance.to_dict()
# create an instance of ListServicesReply from a dict
list_services_reply_from_dict = ListServicesReply.from_dict(list_services_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


