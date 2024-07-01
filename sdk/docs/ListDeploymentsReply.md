# ListDeploymentsReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployments** | [**List[DeploymentListItem]**](DeploymentListItem.md) |  | [optional] 
**limit** | **int** |  | [optional] 
**offset** | **int** |  | [optional] 
**count** | **int** |  | [optional] 

## Example

```python
from openapi_client.models.list_deployments_reply import ListDeploymentsReply

# TODO update the JSON string below
json = "{}"
# create an instance of ListDeploymentsReply from a JSON string
list_deployments_reply_instance = ListDeploymentsReply.from_json(json)
# print the JSON string representation of the object
print(ListDeploymentsReply.to_json())

# convert the object into a dict
list_deployments_reply_dict = list_deployments_reply_instance.to_dict()
# create an instance of ListDeploymentsReply from a dict
list_deployments_reply_from_dict = ListDeploymentsReply.from_dict(list_deployments_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


