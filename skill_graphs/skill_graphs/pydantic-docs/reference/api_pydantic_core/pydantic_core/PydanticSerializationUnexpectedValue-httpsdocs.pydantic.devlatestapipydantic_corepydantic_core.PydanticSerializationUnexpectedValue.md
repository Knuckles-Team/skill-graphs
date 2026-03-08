##  PydanticSerializationUnexpectedValue [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationUnexpectedValue)
```
PydanticSerializationUnexpectedValue(message: )

```

Bases:
An error raised when an unexpected value is encountered during serialization.
This error is often caught and coerced into a warning, as `pydantic-core` generally makes a best attempt at serializing values, in contrast with validation where errors are eagerly raised.
Example
```
from pydantic import BaseModel, field_serializer
from pydantic_core import PydanticSerializationUnexpectedValue

class BasicPoint(BaseModel):
    x: int
    y: int

    @field_serializer('*')
    def serialize(self, v):
        if not isinstance(v, int):
            raise PydanticSerializationUnexpectedValue(f'Expected type `int`, got {type(v)} with value {v}')
        return v

point = BasicPoint(x=1, y=2)
# some sort of mutation
point.x = 'a'

print(point.model_dump())
'''
UserWarning: Pydantic serializer warnings:
PydanticSerializationUnexpectedValue(Expected type `int`, got <class 'str'> with value a)
return self.__pydantic_serializer__.to_python(
{'x': 'a', 'y': 2}
'''

```

This is often used internally in `pydantic-core` when unexpected types are encountered during serialization, but it can also be used by users in custom serializers, as seen above.
Parameters:
Name | Type | Description | Default
---|---|---|---
`message` |  |  The message associated with the unexpected value. |  _required_
