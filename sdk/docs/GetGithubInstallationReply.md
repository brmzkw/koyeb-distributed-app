# GetGithubInstallationReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_id** | **str** |  | [optional] 
**installation_url** | **str** |  | [optional] 
**name** | **str** |  | [optional] 
**avatar_url** | **str** |  | [optional] 
**status** | [**KgitproxyGithubInstallationStatus**](KgitproxyGithubInstallationStatus.md) |  | [optional] [default to KgitproxyGithubInstallationStatus.INVALID]
**installed_at** | **datetime** |  | [optional] 
**suspended_at** | **datetime** |  | [optional] 
**indexing_status** | [**KgitproxyIndexingStatus**](KgitproxyIndexingStatus.md) |  | [optional] [default to KgitproxyIndexingStatus.INVALID_INDEXING_STATUS]
**indexed_repositories** | **int** |  | [optional] 
**total_repositories** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.get_github_installation_reply import GetGithubInstallationReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetGithubInstallationReply from a JSON string
get_github_installation_reply_instance = GetGithubInstallationReply.from_json(json)
# print the JSON string representation of the object
print(GetGithubInstallationReply.to_json())

# convert the object into a dict
get_github_installation_reply_dict = get_github_installation_reply_instance.to_dict()
# create an instance of GetGithubInstallationReply from a dict
get_github_installation_reply_from_dict = GetGithubInstallationReply.from_dict(get_github_installation_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


