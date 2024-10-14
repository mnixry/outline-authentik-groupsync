# NavigationNode


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for the document. | [optional] 
**title** | **str** |  | [optional] 
**url** | **str** |  | [optional] 
**children** | [**List[NavigationNode]**](NavigationNode.md) |  | [optional] 

## Example

```python
from outline_openapi.models.navigation_node import NavigationNode

# TODO update the JSON string below
json = "{}"
# create an instance of NavigationNode from a JSON string
navigation_node_instance = NavigationNode.from_json(json)
# print the JSON string representation of the object
print(NavigationNode.to_json())

# convert the object into a dict
navigation_node_dict = navigation_node_instance.to_dict()
# create an instance of NavigationNode from a dict
navigation_node_from_dict = NavigationNode.from_dict(navigation_node_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


