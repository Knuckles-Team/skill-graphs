##  `unexpected_positional_argument`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#unexpected_positional_argument)
This error is raised when you provide a positional value for a keyword-only argument while calling a function decorated with `validate_call`:
```
from pydantic import ValidationError, validate_call


@validate_call
def foo(*, a: int):
    return a


try:
    foo(2)
except ValidationError as exc:
    print(repr(exc.errors()[1]['type']))
    #> 'unexpected_positional_argument'

```
