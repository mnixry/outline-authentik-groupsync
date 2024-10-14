# Share


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**document_title** | **str** | Title of the shared document. | [optional] [readonly] 
**document_url** | **str** | URL of the original document. | [optional] [readonly] 
**url** | **str** | URL of the publicly shared document. | [optional] [readonly] 
**published** | **bool** | If true the share can be loaded without a user account. | [optional] 
**include_child_documents** | **bool** | If to also give permission to view documents nested beneath this one. | [optional] 
**created_at** | **datetime** | Date and time when this share was created | [optional] [readonly] 
**created_by** | [**User**](User.md) |  | [optional] 
**updated_at** | **datetime** | Date and time when this share was edited | [optional] [readonly] 
**last_accessed_at** | **datetime** | Date and time when this share was last viewed | [optional] [readonly] 

## Example

```python
from outline_openapi.models.share import Share

# TODO update the JSON string below
json = "{}"
# create an instance of Share from a JSON string
share_instance = Share.from_json(json)
# print the JSON string representation of the object
print(Share.to_json())

# convert the object into a dict
share_dict = share_instance.to_dict()
# create an instance of Share from a dict
share_from_dict = Share.from_dict(share_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


