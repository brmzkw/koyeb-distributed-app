# GetCatalogInstanceReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**instance** | [**CatalogInstance**](CatalogInstance.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_catalog_instance_reply import GetCatalogInstanceReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetCatalogInstanceReply from a JSON string
get_catalog_instance_reply_instance = GetCatalogInstanceReply.from_json(json)
# print the JSON string representation of the object
print(GetCatalogInstanceReply.to_json())

# convert the object into a dict
get_catalog_instance_reply_dict = get_catalog_instance_reply_instance.to_dict()
# create an instance of GetCatalogInstanceReply from a dict
get_catalog_instance_reply_from_dict = GetCatalogInstanceReply.from_dict(get_catalog_instance_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


