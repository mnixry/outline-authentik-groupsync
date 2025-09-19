# DocumentsAnswerquestionRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**query** | **str** |  | [optional] 
**user_id** | **str** | Any documents that have not been edited by the user identifier will be filtered out | [optional] 
**collection_id** | **str** | A collection to search within | [optional] 
**document_id** | **str** | A document to search within | [optional] 
**status_filter** | **str** | Any documents that are not in the specified status will be filtered out | [optional] 
**date_filter** | **str** | Any documents that have not been updated within the specified period will be filtered out | [optional] 

## Example

```python
from outline_openapi.models.documents_answerquestion_request import DocumentsAnswerquestionRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsAnswerquestionRequest from a JSON string
documents_answerquestion_request_instance = DocumentsAnswerquestionRequest.from_json(json)
# print the JSON string representation of the object
print(DocumentsAnswerquestionRequest.to_json())

# convert the object into a dict
documents_answerquestion_request_dict = documents_answerquestion_request_instance.to_dict()
# create an instance of DocumentsAnswerquestionRequest from a dict
documents_answerquestion_request_from_dict = DocumentsAnswerquestionRequest.from_dict(documents_answerquestion_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


