# UpdateService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**definition** | [**DeploymentDefinition**](DeploymentDefinition.md) |  | [optional] 
**metadata** | [**DeploymentMetadata**](DeploymentMetadata.md) |  | [optional] 
**skip_build** | **bool** | If set to true, the build stage will be skipped and the image coming from the last successful build step will be used instead. The call fails if no previous successful builds happened. | [optional] 
**save_only** | **bool** |  | [optional] 

## Example

```python
from openapi_client.models.update_service import UpdateService

# TODO update the JSON string below
json = "{}"
# create an instance of UpdateService from a JSON string
update_service_instance = UpdateService.from_json(json)
# print the JSON string representation of the object
print(UpdateService.to_json())

# convert the object into a dict
update_service_dict = update_service_instance.to_dict()
# create an instance of UpdateService from a dict
update_service_from_dict = UpdateService.from_dict(update_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


