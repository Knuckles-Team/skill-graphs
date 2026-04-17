## Rebuilding model schema[¶](https://docs.pydantic.dev/latest/concepts/models/#rebuilding-model-schema)
When you define a model class in your code, Pydantic will analyze the body of the class to collect a variety of information required to perform validation and serialization, gathered in a core schema. Notably, the model's type annotations are evaluated to understand the valid types for each field (more information can be found in the [Architecture](https://docs.pydantic.dev/latest/internals/architecture/) documentation). However, it might be the case that annotations refer to symbols not defined when the model class is being created. To circumvent this issue, the [`model_rebuild()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild) method can be used:
```
from pydantic import BaseModel, PydanticUserError


class Foo(BaseModel):
    x: 'Bar'  [](https://docs.pydantic.dev/latest/concepts/models/#__code_12_annotation_1)


try:
    Foo.model_json_schema()
except PydanticUserError as e:
    print(e)
    """
    `Foo` is not fully defined; you should define `Bar`, then call `Foo.model_rebuild()`.

    For further information visit https://errors.pydantic.dev/2/u/class-not-fully-defined
    """


class Bar(BaseModel):
    pass


Foo.model_rebuild()
print(Foo.model_json_schema())
"""
{
    '$defs': {'Bar': {'properties': {}, 'title': 'Bar', 'type': 'object'}},
    'properties': {'x': {'$ref': '#/$defs/Bar'}},
    'required': ['x'],
    'title': 'Foo',
    'type': 'object',
}
"""

```

Pydantic tries to determine when this is necessary automatically and error if it wasn't done, but you may want to call [`model_rebuild()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild) proactively when dealing with recursive models or generics.
In V2, [`model_rebuild()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild) replaced `update_forward_refs()` from V1. There are some slight differences with the new behavior. The biggest change is that when calling [`model_rebuild()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild) on the outermost model, it builds a core schema used for validation of the whole model (nested models and all), so all types at all levels need to be ready before [`model_rebuild()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_rebuild) is called.
