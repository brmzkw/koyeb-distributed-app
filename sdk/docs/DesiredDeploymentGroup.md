# DesiredDeploymentGroup


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** |  | [optional] 
**deployment_ids** | **List[str]** |  | [optional] 

## Example

```python
from openapi_client.models.desired_deployment_group import DesiredDeploymentGroup

# TODO update the JSON string below
json = "{}"
# create an instance of DesiredDeploymentGroup from a JSON string
desired_deployment_group_instance = DesiredDeploymentGroup.from_json(json)
# print the JSON string representation of the object
print(DesiredDeploymentGroup.to_json())

# convert the object into a dict
desired_deployment_group_dict = desired_deployment_group_instance.to_dict()
# create an instance of DesiredDeploymentGroup from a dict
desired_deployment_group_from_dict = DesiredDeploymentGroup.from_dict(desired_deployment_group_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


