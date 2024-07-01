# KsearchInstance


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**service_id** | **str** |  | [optional] 
**allocation_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ksearch_instance import KsearchInstance

# TODO update the JSON string below
json = "{}"
# create an instance of KsearchInstance from a JSON string
ksearch_instance_instance = KsearchInstance.from_json(json)
# print the JSON string representation of the object
print(KsearchInstance.to_json())

# convert the object into a dict
ksearch_instance_dict = ksearch_instance_instance.to_dict()
# create an instance of KsearchInstance from a dict
ksearch_instance_from_dict = KsearchInstance.from_dict(ksearch_instance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


