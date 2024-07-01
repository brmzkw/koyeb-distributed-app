# GitDeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_provisioned_deployment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.git_deployment_metadata import GitDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of GitDeploymentMetadata from a JSON string
git_deployment_metadata_instance = GitDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(GitDeploymentMetadata.to_json())

# convert the object into a dict
git_deployment_metadata_dict = git_deployment_metadata_instance.to_dict()
# create an instance of GitDeploymentMetadata from a dict
git_deployment_metadata_from_dict = GitDeploymentMetadata.from_dict(git_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


