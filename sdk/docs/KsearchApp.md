# KsearchApp


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**organization_id** | **str** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ksearch_app import KsearchApp

# TODO update the JSON string below
json = "{}"
# create an instance of KsearchApp from a JSON string
ksearch_app_instance = KsearchApp.from_json(json)
# print the JSON string representation of the object
print(KsearchApp.to_json())

# convert the object into a dict
ksearch_app_dict = ksearch_app_instance.to_dict()
# create an instance of KsearchApp from a dict
ksearch_app_from_dict = KsearchApp.from_dict(ksearch_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


