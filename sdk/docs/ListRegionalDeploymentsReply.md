# ListRegionalDeploymentsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**regional_deployments** | [**List[RegionalDeploymentListItem]**](RegionalDeploymentListItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_regional_deployments_reply import ListRegionalDeploymentsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListRegionalDeploymentsReply from a JSON string
list_regional_deployments_reply_instance = ListRegionalDeploymentsReply.from_json(json)
# print the JSON string representation of the object
print(ListRegionalDeploymentsReply.to_json())

# convert the object into a dict
list_regional_deployments_reply_dict = list_regional_deployments_reply_instance.to_dict()
# create an instance of ListRegionalDeploymentsReply from a dict
list_regional_deployments_reply_from_dict = ListRegionalDeploymentsReply.from_dict(list_regional_deployments_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


