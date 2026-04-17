##  `missing_argument`[¶](https://docs.pydantic.dev/latest/errors/validation_errors/#missing_argument)
This error is raised when a required positional-or-keyword argument is not passed to a function decorated with `validate_call`:
```
from pydantic import ValidationError, validate_call


@validate_call
def foo(a: int):
    return a


try:
    foo()
except ValidationError as exc:
    print(repr(exc.errors()[0]['type']))
    #> 'missing_argument'

```
