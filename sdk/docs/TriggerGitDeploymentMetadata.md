# TriggerGitDeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**provider** | [**TriggerGitDeploymentMetadataProvider**](TriggerGitDeploymentMetadataProvider.md) |  | [optional] [default to TriggerGitDeploymentMetadataProvider.UNKNOWN]
**repository** | **str** |  | [optional] 
**branch** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**sender_username** | **str** |  | [optional] 
**sender_avatar_url** | **str** |  | [optional] 
**sender_profile_url** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.trigger_git_deployment_metadata import TriggerGitDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerGitDeploymentMetadata from a JSON string
trigger_git_deployment_metadata_instance = TriggerGitDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(TriggerGitDeploymentMetadata.to_json())

# convert the object into a dict
trigger_git_deployment_metadata_dict = trigger_git_deployment_metadata_instance.to_dict()
# create an instance of TriggerGitDeploymentMetadata from a dict
trigger_git_deployment_metadata_from_dict = TriggerGitDeploymentMetadata.from_dict(trigger_git_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


