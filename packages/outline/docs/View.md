# View


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**document_id** | **str** | Identifier for the associated document. | [optional] [readonly] 
**first_viewed_at** | **datetime** | When the document was first viewed by the user | [optional] [readonly] 
**last_viewed_at** | **datetime** | When the document was last viewed by the user | [optional] [readonly] 
**count** | **float** | The number of times the user has viewed the document. | [optional] [readonly] 
**user** | [**User**](User.md) |  | [optional] 

## Example

```python
from outline_openapi.models.view import View

# TODO update the JSON string below
json = "{}"
# create an instance of View from a JSON string
view_instance = View.from_json(json)
# print the JSON string representation of the object
print(View.to_json())

# convert the object into a dict
view_dict = view_instance.to_dict()
# create an instance of View from a dict
view_from_dict = View.from_dict(view_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


