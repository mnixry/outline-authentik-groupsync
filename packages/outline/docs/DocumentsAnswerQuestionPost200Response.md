# DocumentsAnswerQuestionPost200Response


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**documents** | [**List[Document]**](Document.md) |  | [optional] 
**policies** | [**List[Policy]**](Policy.md) |  | [optional] 
**search** | [**SearchResult**](SearchResult.md) |  | [optional] 

## Example

```python
from outline_openapi.models.documents_answer_question_post200_response import DocumentsAnswerQuestionPost200Response

# TODO update the JSON string below
json = "{}"
# create an instance of DocumentsAnswerQuestionPost200Response from a JSON string
documents_answer_question_post200_response_instance = DocumentsAnswerQuestionPost200Response.from_json(json)
# print the JSON string representation of the object
print(DocumentsAnswerQuestionPost200Response.to_json())

# convert the object into a dict
documents_answer_question_post200_response_dict = documents_answer_question_post200_response_instance.to_dict()
# create an instance of DocumentsAnswerQuestionPost200Response from a dict
documents_answer_question_post200_response_from_dict = DocumentsAnswerQuestionPost200Response.from_dict(documents_answer_question_post200_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


