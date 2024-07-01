# DatabaseSource


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**neon_postgres** | [**NeonPostgresDatabase**](NeonPostgresDatabase.md) |  | [optional] 

## Example

```python
from openapi_client.models.database_source import DatabaseSource

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseSource from a JSON string
database_source_instance = DatabaseSource.from_json(json)
# print the JSON string representation of the object
print(DatabaseSource.to_json())

# convert the object into a dict
database_source_dict = database_source_instance.to_dict()
# create an instance of DatabaseSource from a dict
database_source_from_dict = DatabaseSource.from_dict(database_source_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


