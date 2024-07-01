# ArchiveDeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_provisioned_deployment_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.archive_deployment_metadata import ArchiveDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of ArchiveDeploymentMetadata from a JSON string
archive_deployment_metadata_instance = ArchiveDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(ArchiveDeploymentMetadata.to_json())

# convert the object into a dict
archive_deployment_metadata_dict = archive_deployment_metadata_instance.to_dict()
# create an instance of ArchiveDeploymentMetadata from a dict
archive_deployment_metadata_from_dict = ArchiveDeploymentMetadata.from_dict(archive_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


