# MembersSummary


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**total** | **str** |  | [optional] 
**invitations_by_status** | **Dict[str, str]** |  | [optional] 

## Example

```python
from openapi_client.models.members_summary import MembersSummary

# TODO update the JSON string below
json = "{}"
# create an instance of MembersSummary from a JSON string
members_summary_instance = MembersSummary.from_json(json)
# print the JSON string representation of the object
print(MembersSummary.to_json())

# convert the object into a dict
members_summary_dict = members_summary_instance.to_dict()
# create an instance of MembersSummary from a dict
members_summary_from_dict = MembersSummary.from_dict(members_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


