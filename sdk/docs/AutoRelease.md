# AutoRelease


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[AutoReleaseGroup]**](AutoReleaseGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.auto_release import AutoRelease

# TODO update the JSON string below
json = "{}"
# create an instance of AutoRelease from a JSON string
auto_release_instance = AutoRelease.from_json(json)
# print the JSON string representation of the object
print(AutoRelease.to_json())

# convert the object into a dict
auto_release_dict = auto_release_instance.to_dict()
# create an instance of AutoRelease from a dict
auto_release_from_dict = AutoRelease.from_dict(auto_release_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


