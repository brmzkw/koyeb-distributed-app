# PublicUser


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**github_id** | **str** |  | [optional] 
**github_user** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.public_user import PublicUser

# TODO update the JSON string below
json = "{}"
# create an instance of PublicUser from a JSON string
public_user_instance = PublicUser.from_json(json)
# print the JSON string representation of the object
print(PublicUser.to_json())

# convert the object into a dict
public_user_dict = public_user_instance.to_dict()
# create an instance of PublicUser from a dict
public_user_from_dict = PublicUser.from_dict(public_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


