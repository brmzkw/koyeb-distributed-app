# DatabaseDeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neon_postgres** | [**NeonPostgresDatabaseDeploymentMetadata**](NeonPostgresDatabaseDeploymentMetadata.md) |  | [optional] 

## Example

```python
from openapi_client.models.database_deployment_metadata import DatabaseDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseDeploymentMetadata from a JSON string
database_deployment_metadata_instance = DatabaseDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(DatabaseDeploymentMetadata.to_json())

# convert the object into a dict
database_deployment_metadata_dict = database_deployment_metadata_instance.to_dict()
# create an instance of DatabaseDeploymentMetadata from a dict
database_deployment_metadata_from_dict = DatabaseDeploymentMetadata.from_dict(database_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


