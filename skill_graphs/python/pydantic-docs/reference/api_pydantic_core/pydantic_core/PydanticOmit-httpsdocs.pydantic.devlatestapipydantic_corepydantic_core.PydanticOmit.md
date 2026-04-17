##  PydanticOmit [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticOmit)
Bases:
An exception to signal that a field should be omitted from a generated result.
This could span from omitting a field from a JSON Schema to omitting a field from a serialized result. Upcoming: more robust support for using PydanticOmit in custom serializers is still in development. Right now, this is primarily used in the JSON Schema generation process.
Example
```
from typing import Callable

from pydantic_core import PydanticOmit

from pydantic import BaseModel
from pydantic.json_schema import GenerateJsonSchema, JsonSchemaValue


class MyGenerateJsonSchema(GenerateJsonSchema):
    def handle_invalid_for_json_schema(self, schema, error_info) -> JsonSchemaValue:
        raise PydanticOmit


class Predicate(BaseModel):
    name: str = 'no-op'
    func: Callable = lambda x: x


instance_example = Predicate()

validation_schema = instance_example.model_json_schema(schema_generator=MyGenerateJsonSchema, mode='validation')
print(validation_schema)
'''
{'properties': {'name': {'default': 'no-op', 'title': 'Name', 'type': 'string'}}, 'title': 'Predicate', 'type': 'object'}
'''

```

For a more in depth example / explanation, see the [customizing JSON schema](https://docs.pydantic.dev/latest/concepts/json_schema/#customizing-the-json-schema-generation-process) docs.
