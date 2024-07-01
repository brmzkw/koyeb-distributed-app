# ListRegionsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regions** | [**List[RegionListItem]**](RegionListItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_regions_reply import ListRegionsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegionsReply from a JSON string
list_regions_reply_instance = ListRegionsReply.from_json(json)
# print the JSON string representation of the object
print(ListRegionsReply.to_json())

# convert the object into a dict
list_regions_reply_dict = list_regions_reply_instance.to_dict()
# create an instance of ListRegionsReply from a dict
list_regions_reply_from_dict = ListRegionsReply.from_dict(list_regions_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


