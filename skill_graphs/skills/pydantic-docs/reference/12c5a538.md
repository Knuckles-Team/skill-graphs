##  `multiple_argument_values`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#multiple_argument_values)
This error is raised when you provide multiple values for a single argument while calling a function decorated with `validate_call`:
```
from pydantic import ValidationError, validate_call


@validate_call
def foo(a: int):
    return a


try:
    foo(1, a=2)
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'multiple_argument_values'

```
