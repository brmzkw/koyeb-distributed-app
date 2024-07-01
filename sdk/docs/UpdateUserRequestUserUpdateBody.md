# UpdateUserRequestUserUpdateBody


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** |  | [optional] 
**email** | **str** |  | [optional] 
**current_password** | **str** |  | [optional] 
**password** | **str** |  | [optional] 
**newsletter_subscribed** | **bool** |  | [optional] 
**name** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.update_user_request_user_update_body import UpdateUserRequestUserUpdateBody

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateUserRequestUserUpdateBody from a JSON string
update_user_request_user_update_body_instance = UpdateUserRequestUserUpdateBody.from_json(json)
# print the JSON string representation of the object
print(UpdateUserRequestUserUpdateBody.to_json())

# convert the object into a dict
update_user_request_user_update_body_dict = update_user_request_user_update_body_instance.to_dict()
# create an instance of UpdateUserRequestUserUpdateBody from a dict
update_user_request_user_update_body_from_dict = UpdateUserRequestUserUpdateBody.from_dict(update_user_request_user_update_body_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


