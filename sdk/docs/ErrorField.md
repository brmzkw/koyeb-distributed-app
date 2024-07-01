# ErrorField


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**var_field** | **str** |  | [optional] 
**description** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.error_field import ErrorField

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorField from a JSON string
error_field_instance = ErrorField.from_json(json)
# print the JSON string representation of the object
print(ErrorField.to_json())

# convert the object into a dict
error_field_dict = error_field_instance.to_dict()
# create an instance of ErrorField from a dict
error_field_from_dict = ErrorField.from_dict(error_field_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


