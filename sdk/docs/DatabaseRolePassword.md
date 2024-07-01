# DatabaseRolePassword


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**username** | **str** |  | [optional] 
**password** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.database_role_password import DatabaseRolePassword

# TODO update the JSON string below
json = "{}"
# create an instance of DatabaseRolePassword from a JSON string
database_role_password_instance = DatabaseRolePassword.from_json(json)
# print the JSON string representation of the object
print(DatabaseRolePassword.to_json())

# convert the object into a dict
database_role_password_dict = database_role_password_instance.to_dict()
# create an instance of DatabaseRolePassword from a dict
database_role_password_from_dict = DatabaseRolePassword.from_dict(database_role_password_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


