## Error handling[¶](https://docs.pydantic.dev/latest/concepts/models/#error-handling)
Pydantic will raise a [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) exception whenever it finds an error in the data it's validating.
A single exception will be raised regardless of the number of errors found, and that validation error will contain information about all of the errors and how they happened.
See [Error Handling](https://docs.pydantic.dev/latest/errors/errors/) for details on standard and custom errors.
As a demonstration:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    list_of_ints: list[int]
    a_float: float


data = {
    'list_of_ints': ['1', 2, 'bad'],
    'a_float': 'not a float',
}

try:
    Model(**data)
except ValidationError as e:
    print(e)
    """
    2 validation errors for Model
    list_of_ints.2
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='bad', input_type=str]
    a_float
      Input should be a valid number, unable to parse string as a number [type=float_parsing, input_value='not a float', input_type=str]
    """

```
