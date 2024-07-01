# GetDeploymentReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment** | [**Deployment**](Deployment.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_deployment_reply import GetDeploymentReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetDeploymentReply from a JSON string
get_deployment_reply_instance = GetDeploymentReply.from_json(json)
# print the JSON string representation of the object
print(GetDeploymentReply.to_json())

# convert the object into a dict
get_deployment_reply_dict = get_deployment_reply_instance.to_dict()
# create an instance of GetDeploymentReply from a dict
get_deployment_reply_from_dict = GetDeploymentReply.from_dict(get_deployment_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


