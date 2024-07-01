# DeploymentRoute


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**port** | **int** |  | [optional] 
**path** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.deployment_route import DeploymentRoute

# TODO update the JSON string below
json = "{}"
# create an instance of DeploymentRoute from a JSON string
deployment_route_instance = DeploymentRoute.from_json(json)
# print the JSON string representation of the object
print(DeploymentRoute.to_json())

# convert the object into a dict
deployment_route_dict = deployment_route_instance.to_dict()
# create an instance of DeploymentRoute from a dict
deployment_route_from_dict = DeploymentRoute.from_dict(deployment_route_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


