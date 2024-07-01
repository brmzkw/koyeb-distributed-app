# GithubInstallationCallbackRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**installation_id** | **str** |  | [optional] 
**setup_action** | **str** |  | [optional] 
**state** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.github_installation_callback_request import GithubInstallationCallbackRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubInstallationCallbackRequest from a JSON string
github_installation_callback_request_instance = GithubInstallationCallbackRequest.from_json(json)
# print the JSON string representation of the object
print(GithubInstallationCallbackRequest.to_json())

# convert the object into a dict
github_installation_callback_request_dict = github_installation_callback_request_instance.to_dict()
# create an instance of GithubInstallationCallbackRequest from a dict
github_installation_callback_request_from_dict = GithubInstallationCallbackRequest.from_dict(github_installation_callback_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


