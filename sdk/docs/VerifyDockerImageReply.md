# VerifyDockerImageReply


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**success** | **bool** |  | [optional] 
**reason** | **str** |  | [optional] 
**code** | [**VerifyDockerImageReplyErrCode**](VerifyDockerImageReplyErrCode.md) |  | [optional] [default to VerifyDockerImageReplyErrCode.UNKNOWN]

## Example

```python
from openapi_client.models.verify_docker_image_reply import VerifyDockerImageReply

# TODO update the JSON string below
json = "{}"
# create an instance of VerifyDockerImageReply from a JSON string
verify_docker_image_reply_instance = VerifyDockerImageReply.from_json(json)
# print the JSON string representation of the object
print(VerifyDockerImageReply.to_json())

# convert the object into a dict
verify_docker_image_reply_dict = verify_docker_image_reply_instance.to_dict()
# create an instance of VerifyDockerImageReply from a dict
verify_docker_image_reply_from_dict = VerifyDockerImageReply.from_dict(verify_docker_image_reply_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


