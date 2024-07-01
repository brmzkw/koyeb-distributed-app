# CreateService


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **str** |  | [optional] 
**definition** | [**DeploymentDefinition**](DeploymentDefinition.md) |  | [optional] 

## Example

```python
from openapi_client.models.create_service import CreateService

# TODO update the JSON string below
json = "{}"
# create an instance of CreateService from a JSON string
create_service_instance = CreateService.from_json(json)
# print the JSON string representation of the object
print(CreateService.to_json())

# convert the object into a dict
create_service_dict = create_service_instance.to_dict()
# create an instance of CreateService from a dict
create_service_from_dict = CreateService.from_dict(create_service_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


