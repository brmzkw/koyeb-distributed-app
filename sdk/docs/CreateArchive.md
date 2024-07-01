# CreateArchive


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**size** | **str** | How much space to provision for the archive, in bytes. | [optional] 

## Example

```python
from openapi_client.models.create_archive import CreateArchive

# TODO update the JSON string below
json = "{}"
# create an instance of CreateArchive from a JSON string
create_archive_instance = CreateArchive.from_json(json)
# print the JSON string representation of the object
print(CreateArchive.to_json())

# convert the object into a dict
create_archive_dict = create_archive_instance.to_dict()
# create an instance of CreateArchive from a dict
create_archive_from_dict = CreateArchive.from_dict(create_archive_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


