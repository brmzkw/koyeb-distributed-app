# NeonPostgresDatabaseDeploymentMetadata


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reset_role_passwords** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.neon_postgres_database_deployment_metadata import NeonPostgresDatabaseDeploymentMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of NeonPostgresDatabaseDeploymentMetadata from a JSON string
neon_postgres_database_deployment_metadata_instance = NeonPostgresDatabaseDeploymentMetadata.from_json(json)
# print the JSON string representation of the object
print(NeonPostgresDatabaseDeploymentMetadata.to_json())

# convert the object into a dict
neon_postgres_database_deployment_metadata_dict = neon_postgres_database_deployment_metadata_instance.to_dict()
# create an instance of NeonPostgresDatabaseDeploymentMetadata from a dict
neon_postgres_database_deployment_metadata_from_dict = NeonPostgresDatabaseDeploymentMetadata.from_dict(neon_postgres_database_deployment_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


