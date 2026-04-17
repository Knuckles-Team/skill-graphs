##  PydanticUseDefault [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticUseDefault)
Bases:
An exception to signal that standard validation either failed or should be skipped, and the default value should be used instead.
This warning can be raised in custom valiation functions to redirect the flow of validation.
Example
```
from pydantic_core import PydanticUseDefault
from datetime import datetime
from pydantic import BaseModel, field_validator


class Event(BaseModel):
    name: str = 'meeting'
    time: datetime

    @field_validator('name', mode='plain')
    def name_must_be_present(cls, v) -> str:
        if not v or not isinstance(v, str):
            raise PydanticUseDefault()
        return v


event1 = Event(name='party', time=datetime(2024, 1, 1, 12, 0, 0))
print(repr(event1))
# > Event(name='party', time=datetime.datetime(2024, 1, 1, 12, 0))
event2 = Event(time=datetime(2024, 1, 1, 12, 0, 0))
print(repr(event2))
# > Event(name='meeting', time=datetime.datetime(2024, 1, 1, 12, 0))

```

For an additional example, see the [validating partial json data](https://docs.pydantic.dev/latest/concepts/json/#partial-json-parsing) section of the Pydantic documentation.
