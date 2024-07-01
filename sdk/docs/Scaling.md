# Scaling


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min** | **int** |  | [optional] 
**max** | **int** |  | [optional] 
**targets** | [**List[DeploymentScalingTarget]**](DeploymentScalingTarget.md) |  | [optional] 

## Example

```python
from openapi_client.models.scaling import Scaling

# TODO update the JSON string below
json = "{}"
# create an instance of Scaling from a JSON string
scaling_instance = Scaling.from_json(json)
# print the JSON string representation of the object
print(Scaling.to_json())

# convert the object into a dict
scaling_dict = scaling_instance.to_dict()
# create an instance of Scaling from a dict
scaling_from_dict = Scaling.from_dict(scaling_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


