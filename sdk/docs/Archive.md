# Archive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The archive id, that can be referenced when creating or updating a service. | [optional] 
**organization_id** | **str** | Organization owning the archive. | [optional] 
**upload_url** | **str** | The URL where to upload the archive. This URL is signed and can only be used to upload the archive until &#x60;valid_until&#x60;. | [optional] 
**size** | **str** | The provisioned space for the archive. | [optional] 
**created_at** | **datetime** | Date of creation of the archive. | [optional] 
**deleted_at** | **datetime** | This field is automatically set by Koyeb when the archive is garbage collected. | [optional] 

## Example

```python
from openapi_client.models.archive import Archive

# TODO update the JSON string below
json = "{}"
# create an instance of Archive from a JSON string
archive_instance = Archive.from_json(json)
# print the JSON string representation of the object
print(Archive.to_json())

# convert the object into a dict
archive_dict = archive_instance.to_dict()
# create an instance of Archive from a dict
archive_from_dict = Archive.from_dict(archive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


