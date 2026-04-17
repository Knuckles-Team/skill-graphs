##  `unexpected_keyword_argument`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#unexpected_keyword_argument)
This error is raised when you provide a value by keyword for a positional-only argument while calling a function decorated with `validate_call`:
```
from pydantic import ValidationError, validate_call


@validate_call
def foo(a: int, /):
    return a


try:
    foo(a=2)
except ValidationError as exc:
    print(repr(exc.errors()[1]['type']))
    #> 'unexpected_keyword_argument'

```

It is also raised when using pydantic.dataclasses and `extra=forbid`:
```
from pydantic import TypeAdapter, ValidationError
from pydantic.dataclasses import dataclass


@dataclass(config={'extra': 'forbid'})
class Foo:
    bar: int


try:
    TypeAdapter(Foo).validate_python({'bar': 1, 'foobar': 2})
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'unexpected_keyword_argument'

```
