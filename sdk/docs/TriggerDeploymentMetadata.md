# TriggerDeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**type** | [**TriggerDeploymentMetadataTriggerType**](TriggerDeploymentMetadataTriggerType.md) |  | [optional] [default to TriggerDeploymentMetadataTriggerType.UNKNOWN_TYPE]
**actor** | [**TriggerDeploymentMetadataActorType**](TriggerDeploymentMetadataActorType.md) |  | [optional] [default to TriggerDeploymentMetadataActorType.UNKNOWN_ACTOR]
**git** | [**TriggerGitDeploymentMetadata**](TriggerGitDeploymentMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.trigger_deployment_metadata import TriggerDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of TriggerDeploymentMetadata from a JSON string
trigger_deployment_metadata_instance = TriggerDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(TriggerDeploymentMetadata.to_json())

# convert the object into a dict
trigger_deployment_metadata_dict = trigger_deployment_metadata_instance.to_dict()
# create an instance of TriggerDeploymentMetadata from a dict
trigger_deployment_metadata_from_dict = TriggerDeploymentMetadata.from_dict(trigger_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


