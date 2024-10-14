# Document


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the object. | [optional] [readonly] 
**collection_id** | **str** | Identifier for the associated collection. | [optional] 
**parent_document_id** | **str** | Identifier for the document this is a child of, if any. | [optional] 
**title** | **str** | The title of the document. | [optional] 
**full_width** | **bool** | Whether this document should be displayed in a full-width view. | [optional] 
**emoji** | **str** | An emoji associated with the document. | [optional] 
**text** | **str** | The text content of the document, contains markdown formatting | [optional] 
**url_id** | **str** | A short unique ID that can be used to identify the document as an alternative to the UUID | [optional] 
**collaborators** | [**List[User]**](User.md) |  | [optional] 
**pinned** | **bool** | Whether this document is pinned in the collection | [optional] 
**template** | **bool** | Whether this document is a template | [optional] 
**template_id** | **str** | Unique identifier for the template this document was created from, if any | [optional] 
**revision** | **float** | A number that is auto incrementing with every revision of the document that is saved | [optional] [readonly] 
**created_at** | **datetime** | The date and time that this object was created | [optional] [readonly] 
**created_by** | [**User**](User.md) |  | [optional] 
**updated_at** | **datetime** | The date and time that this object was last changed | [optional] [readonly] 
**updated_by** | [**User**](User.md) |  | [optional] 
**published_at** | **datetime** | The date and time that this object was published | [optional] [readonly] 
**archived_at** | **datetime** | The date and time that this object was archived | [optional] [readonly] 
**deleted_at** | **datetime** | The date and time that this object was deleted | [optional] [readonly] 

## Example

```python
from outline_openapi.models.document import Document

# TODO update the JSON string below
json = "{}"
# create an instance of Document from a JSON string
document_instance = Document.from_json(json)
# print the JSON string representation of the object
print(Document.to_json())

# convert the object into a dict
document_dict = document_instance.to_dict()
# create an instance of Document from a dict
document_from_dict = Document.from_dict(document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


