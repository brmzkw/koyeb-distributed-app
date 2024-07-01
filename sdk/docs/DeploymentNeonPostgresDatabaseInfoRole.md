# DeploymentNeonPostgresDatabaseInfoRole


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**secret_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_neon_postgres_database_info_role import DeploymentNeonPostgresDatabaseInfoRole

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentNeonPostgresDatabaseInfoRole from a JSON string
deployment_neon_postgres_database_info_role_instance = DeploymentNeonPostgresDatabaseInfoRole.from_json(json)
# print the JSON string representation of the object
print(DeploymentNeonPostgresDatabaseInfoRole.to_json())

# convert the object into a dict
deployment_neon_postgres_database_info_role_dict = deployment_neon_postgres_database_info_role_instance.to_dict()
# create an instance of DeploymentNeonPostgresDatabaseInfoRole from a dict
deployment_neon_postgres_database_info_role_from_dict = DeploymentNeonPostgresDatabaseInfoRole.from_dict(deployment_neon_postgres_database_info_role_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


