# DesiredDeployment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**groups** | [**List[DesiredDeploymentGroup]**](DesiredDeploymentGroup.md) |  | [optional] 

## Example

```python
from openapi_client.models.desired_deployment import DesiredDeployment

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredDeployment from a JSON string
desired_deployment_instance = DesiredDeployment.from_json(json)
# print the JSON string representation of the object
print(DesiredDeployment.to_json())

# convert the object into a dict
desired_deployment_dict = desired_deployment_instance.to_dict()
# create an instance of DesiredDeployment from a dict
desired_deployment_from_dict = DesiredDeployment.from_dict(desired_deployment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


