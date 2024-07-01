# User


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**two_factor_authentication** | **bool** |  | [optional] 
**last_login** | **datetime** |  | [optional] 
**last_login_ip** | **str** |  | [optional] 
**updated_at** | **datetime** |  | [optional] 
**created_at** | **datetime** |  | [optional] 
**newsletter_subscribed** | **bool** |  | [optional] 
**github_id** | **str** |  | [optional] 
**github_user** | **str** |  | [optional] 
**flags** | [**List[UserFlags]**](UserFlags.md) |  | [optional] 
**name** | **str** |  | [optional] 
**email_validated** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.user import User

# TODO update the JSON string below
json = "{}"
# create an instance of User from a JSON string
user_instance = User.from_json(json)
# print the JSON string representation of the object
print(User.to_json())

# convert the object into a dict
user_dict = user_instance.to_dict()
# create an instance of User from a dict
user_from_dict = User.from_dict(user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


