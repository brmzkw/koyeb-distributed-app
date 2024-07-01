# GithubInstallationRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | **str** |  | [optional] 

## Example

```python
from openapi_client.models.github_installation_request import GithubInstallationRequest

# TODO update the JSON string below
json = "{}"
# create an instance of GithubInstallationRequest from a JSON string
github_installation_request_instance = GithubInstallationRequest.from_json(json)
# print the JSON string representation of the object
print(GithubInstallationRequest.to_json())

# convert the object into a dict
github_installation_request_dict = github_installation_request_instance.to_dict()
# create an instance of GithubInstallationRequest from a dict
github_installation_request_from_dict = GithubInstallationRequest.from_dict(github_installation_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


