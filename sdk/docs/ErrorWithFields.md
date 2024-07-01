# ErrorWithFields


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**status** | **int** |  | [optional] 
**code** | **str** |  | [optional] 
**message** | **str** |  | [optional] 
**fields** | [**List[ErrorField]**](ErrorField.md) |  | [optional] 

## Example

```python
from openapi_client.models.error_with_fields import ErrorWithFields

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorWithFields from a JSON string
error_with_fields_instance = ErrorWithFields.from_json(json)
# print the JSON string representation of the object
print(ErrorWithFields.to_json())

# convert the object into a dict
error_with_fields_dict = error_with_fields_instance.to_dict()
# create an instance of ErrorWithFields from a dict
error_with_fields_from_dict = ErrorWithFields.from_dict(error_with_fields_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


