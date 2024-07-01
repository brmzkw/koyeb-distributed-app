# DiscourseAuthRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**payload** | **str** |  | [optional] 
**sig** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.discourse_auth_request import DiscourseAuthRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DiscourseAuthRequest from a JSON string
discourse_auth_request_instance = DiscourseAuthRequest.from_json(json)
# print the JSON string representation of the object
print(DiscourseAuthRequest.to_json())

# convert the object into a dict
discourse_auth_request_dict = discourse_auth_request_instance.to_dict()
# create an instance of DiscourseAuthRequest from a dict
discourse_auth_request_from_dict = DiscourseAuthRequest.from_dict(discourse_auth_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


