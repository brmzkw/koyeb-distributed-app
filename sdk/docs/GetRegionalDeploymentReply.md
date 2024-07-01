# GetRegionalDeploymentReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regional_deployment** | [**RegionalDeployment**](RegionalDeployment.md) |  | [optional] 

## Example

```python
from openapi_client.models.get_regional_deployment_reply import GetRegionalDeploymentReply

# TODO update the JSON string below
json = "{}"
# create an instance of GetRegionalDeploymentReply from a JSON string
get_regional_deployment_reply_instance = GetRegionalDeploymentReply.from_json(json)
# print the JSON string representation of the object
print(GetRegionalDeploymentReply.to_json())

# convert the object into a dict
get_regional_deployment_reply_dict = get_regional_deployment_reply_instance.to_dict()
# create an instance of GetRegionalDeploymentReply from a dict
get_regional_deployment_reply_from_dict = GetRegionalDeploymentReply.from_dict(get_regional_deployment_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


