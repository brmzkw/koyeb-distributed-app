# OAuthProvider


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.o_auth_provider import OAuthProvider

# TODO update the JSON string below
json = "{}"
# create an instance of OAuthProvider from a JSON string
o_auth_provider_instance = OAuthProvider.from_json(json)
# print the JSON string representation of the object
print(OAuthProvider.to_json())

# convert the object into a dict
o_auth_provider_dict = o_auth_provider_instance.to_dict()
# create an instance of OAuthProvider from a dict
o_auth_provider_from_dict = OAuthProvider.from_dict(o_auth_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


