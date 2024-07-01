# KsearchUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**github_user** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.ksearch_user import KsearchUser

# TODO update the JSON string below
json = "{}"
# create an instance of KsearchUser from a JSON string
ksearch_user_instance = KsearchUser.from_json(json)
# print the JSON string representation of the object
print(KsearchUser.to_json())

# convert the object into a dict
ksearch_user_dict = ksearch_user_instance.to_dict()
# create an instance of KsearchUser from a dict
ksearch_user_from_dict = KsearchUser.from_dict(ksearch_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


