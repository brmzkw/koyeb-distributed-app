# RedeployRequestInfo


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deployment_group** | **str** |  | [optional] 
**sha** | **str** |  | [optional] 
**use_cache** | **bool** |  | [optional] 
**skip_build** | **bool** | If set to true, the build stage will be skipped and the image coming from the last successful build step will be used instead. The call fails if no previous successful builds happened. | [optional] 

## Example

```python
from openapi_client.models.redeploy_request_info import RedeployRequestInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RedeployRequestInfo from a JSON string
redeploy_request_info_instance = RedeployRequestInfo.from_json(json)
# print the JSON string representation of the object
print(RedeployRequestInfo.to_json())

# convert the object into a dict
redeploy_request_info_dict = redeploy_request_info_instance.to_dict()
# create an instance of RedeployRequestInfo from a dict
redeploy_request_info_from_dict = RedeployRequestInfo.from_dict(redeploy_request_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


