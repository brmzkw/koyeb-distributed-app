# GithubInstallationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_name** | **str** |  | [optional] 
**app_id** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.github_installation_reply import GithubInstallationReply

# TODO update the JSON string below
json = "{}"
# create an instance of GithubInstallationReply from a JSON string
github_installation_reply_instance = GithubInstallationReply.from_json(json)
# print the JSON string representation of the object
print(GithubInstallationReply.to_json())

# convert the object into a dict
github_installation_reply_dict = github_installation_reply_instance.to_dict()
# create an instance of GithubInstallationReply from a dict
github_installation_reply_from_dict = GithubInstallationReply.from_dict(github_installation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


