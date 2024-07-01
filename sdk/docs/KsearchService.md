# KsearchService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ksearch_service import KsearchService

# TODO update the JSON string below
json = "{}"
# create an instance of KsearchService from a JSON string
ksearch_service_instance = KsearchService.from_json(json)
# print the JSON string representation of the object
print(KsearchService.to_json())

# convert the object into a dict
ksearch_service_dict = ksearch_service_instance.to_dict()
# create an instance of KsearchService from a dict
ksearch_service_from_dict = KsearchService.from_dict(ksearch_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


