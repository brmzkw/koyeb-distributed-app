# DeploymentDatabaseInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neon_postgres** | [**DeploymentNeonPostgresDatabaseInfo**](DeploymentNeonPostgresDatabaseInfo.md) |  | [optional] 

## Example

```python
from openapi_client.models.deployment_database_info import DeploymentDatabaseInfo

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentDatabaseInfo from a JSON string
deployment_database_info_instance = DeploymentDatabaseInfo.from_json(json)
# print the JSON string representation of the object
print(DeploymentDatabaseInfo.to_json())

# convert the object into a dict
deployment_database_info_dict = deployment_database_info_instance.to_dict()
# create an instance of DeploymentDatabaseInfo from a dict
deployment_database_info_from_dict = DeploymentDatabaseInfo.from_dict(deployment_database_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


