# NeonPostgresDatabase


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**pg_version** | **int** |  | [optional] 
**region** | **str** |  | [optional] 
**instance_type** | **str** |  | [optional] 
**roles** | [**List[NeonPostgresDatabaseNeonRole]**](NeonPostgresDatabaseNeonRole.md) |  | [optional] 
**databases** | [**List[NeonPostgresDatabaseNeonDatabase]**](NeonPostgresDatabaseNeonDatabase.md) |  | [optional] 

## Example

```python
from openapi_client.models.neon_postgres_database import NeonPostgresDatabase

# TODO update the JSON string below
json = "{}"
# create an instance of NeonPostgresDatabase from a JSON string
neon_postgres_database_instance = NeonPostgresDatabase.from_json(json)
# print the JSON string representation of the object
print(NeonPostgresDatabase.to_json())

# convert the object into a dict
neon_postgres_database_dict = neon_postgres_database_instance.to_dict()
# create an instance of NeonPostgresDatabase from a dict
neon_postgres_database_from_dict = NeonPostgresDatabase.from_dict(neon_postgres_database_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


