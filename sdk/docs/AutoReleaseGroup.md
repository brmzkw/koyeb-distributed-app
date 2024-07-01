# AutoReleaseGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**repository** | **str** |  | [optional] 
**git_ref** | **str** |  | [optional] 
**latest_sha** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.auto_release_group import AutoReleaseGroup

# TODO update the JSON string below
json = "{}"
# create an instance of AutoReleaseGroup from a JSON string
auto_release_group_instance = AutoReleaseGroup.from_json(json)
# print the JSON string representation of the object
print(AutoReleaseGroup.to_json())

# convert the object into a dict
auto_release_group_dict = auto_release_group_instance.to_dict()
# create an instance of AutoReleaseGroup from a dict
auto_release_group_from_dict = AutoReleaseGroup.from_dict(auto_release_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


