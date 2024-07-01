# RegionListItem


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**coordinates** | **List[str]** |  | [optional] 
**status** | **str** |  | [optional] 
**instances** | **List[str]** |  | [optional] 
**datacenters** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.region_list_item import RegionListItem

# TODO update the JSON string below
json = "{}"
# create an instance of RegionListItem from a JSON string
region_list_item_instance = RegionListItem.from_json(json)
# print the JSON string representation of the object
print(RegionListItem.to_json())

# convert the object into a dict
region_list_item_dict = region_list_item_instance.to_dict()
# create an instance of RegionListItem from a dict
region_list_item_from_dict = RegionListItem.from_dict(region_list_item_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


