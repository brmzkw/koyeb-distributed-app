# DeploymentNeonPostgresDatabaseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_time_seconds** | **str** |  | [optional] 
**compute_time_seconds** | **str** |  | [optional] 
**written_data_bytes** | **str** |  | [optional] 
**data_transfer_bytes** | **str** |  | [optional] 
**data_storage_bytes_hour** | **str** |  | [optional] 
**server_host** | **str** |  | [optional] 
**server_port** | **int** |  | [optional] 
**endpoint_state** | **str** |  | [optional] 
**endpoint_last_active** | **datetime** |  | [optional] 
**default_branch_id** | **str** |  | [optional] 
**default_branch_name** | **str** |  | [optional] 
**default_branch_state** | **str** |  | [optional] 
**default_branch_logical_size** | **str** |  | [optional] 
**roles** | [**List[DeploymentNeonPostgresDatabaseInfoRole]**](DeploymentNeonPostgresDatabaseInfoRole.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_neon_postgres_database_info import DeploymentNeonPostgresDatabaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentNeonPostgresDatabaseInfo from a JSON string
deployment_neon_postgres_database_info_instance = DeploymentNeonPostgresDatabaseInfo.from_json(json)
# print the JSON string representation of the object
print(DeploymentNeonPostgresDatabaseInfo.to_json())

# convert the object into a dict
deployment_neon_postgres_database_info_dict = deployment_neon_postgres_database_info_instance.to_dict()
# create an instance of DeploymentNeonPostgresDatabaseInfo from a dict
deployment_neon_postgres_database_info_from_dict = DeploymentNeonPostgresDatabaseInfo.from_dict(deployment_neon_postgres_database_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


