# DeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trigger** | [**TriggerDeploymentMetadata**](TriggerDeploymentMetadata.md) |  | [optional] 
**database** | [**DatabaseDeploymentMetadata**](DatabaseDeploymentMetadata.md) |  | [optional] 
**git** | [**GitDeploymentMetadata**](GitDeploymentMetadata.md) |  | [optional] 
**archive** | [**ArchiveDeploymentMetadata**](ArchiveDeploymentMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_metadata import DeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentMetadata from a JSON string
deployment_metadata_instance = DeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(DeploymentMetadata.to_json())

# convert the object into a dict
deployment_metadata_dict = deployment_metadata_instance.to_dict()
# create an instance of DeploymentMetadata from a dict
deployment_metadata_from_dict = DeploymentMetadata.from_dict(deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


