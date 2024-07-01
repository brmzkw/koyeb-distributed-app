# CreateCredential


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**description** | **str** |  | [optional] 
**type** | [**CredentialType**](CredentialType.md) |  | [optional] 
**organization_id** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.create_credential import CreateCredential

# TODO update the JSON string below
json = "{}"
# create an instance of CreateCredential from a JSON string
create_credential_instance = CreateCredential.from_json(json)
# print the JSON string representation of the object
print(CreateCredential.to_json())

# convert the object into a dict
create_credential_dict = create_credential_instance.to_dict()
# create an instance of CreateCredential from a dict
create_credential_from_dict = CreateCredential.from_dict(create_credential_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


