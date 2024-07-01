# ListCatalogInstancesReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instances** | [**List[CatalogInstanceListItem]**](CatalogInstanceListItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_catalog_instances_reply import ListCatalogInstancesReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListCatalogInstancesReply from a JSON string
list_catalog_instances_reply_instance = ListCatalogInstancesReply.from_json(json)
# print the JSON string representation of the object
print(ListCatalogInstancesReply.to_json())

# convert the object into a dict
list_catalog_instances_reply_dict = list_catalog_instances_reply_instance.to_dict()
# create an instance of ListCatalogInstancesReply from a dict
list_catalog_instances_reply_from_dict = ListCatalogInstancesReply.from_dict(list_catalog_instances_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


