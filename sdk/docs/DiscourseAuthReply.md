# DiscourseAuthReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sso** | **str** |  | [optional] 
**sig** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.discourse_auth_reply import DiscourseAuthReply

# TODO update the JSON string below
json = "{}"
# create an instance of DiscourseAuthReply from a JSON string
discourse_auth_reply_instance = DiscourseAuthReply.from_json(json)
# print the JSON string representation of the object
print(DiscourseAuthReply.to_json())

# convert the object into a dict
discourse_auth_reply_dict = discourse_auth_reply_instance.to_dict()
# create an instance of DiscourseAuthReply from a dict
discourse_auth_reply_from_dict = DiscourseAuthReply.from_dict(discourse_auth_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


