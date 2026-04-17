## Validating data[¶](https://docs.pydantic.dev/latest/concepts/models/#validating-data)
Pydantic can validate data in three different modes: _Python_ , _JSON_ and _strings_.
The _Python_ mode gets used when using:
  * The `__init__()` model constructor. Field values must be provided using keyword arguments.
  * [`model_validate()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate): data can be provided either as a dictionary, or as a model instance (by default, instances are assumed to be valid; see the [`revalidate_instances`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.revalidate_instances) setting). [Arbitrary objects](https://docs.pydantic.dev/latest/concepts/models/#arbitrary-class-instances) can also be provided if explicitly enabled.


The _JSON_ and _strings_ modes can be used with dedicated methods:
  * [`model_validate_json()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_json): data is validated as a JSON string or `bytes` object. If your incoming data is a JSON payload, this is generally considered faster (instead of manually parsing the data as a dictionary). Learn more about JSON parsing in the [JSON](https://docs.pydantic.dev/latest/concepts/json/) documentation.
  * [`model_validate_strings()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_strings): data is validated as a dictionary (can be nested) with string keys and values and validates the data in JSON mode so that said strings can be coerced into the correct types.


Compared to using the model constructor, it is possible to control several validation parameters when using the `model_validate_*()` methods ([strictness](https://docs.pydantic.dev/latest/concepts/strict_mode/), [extra data](https://docs.pydantic.dev/latest/concepts/models/#extra-data), [validation context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context), etc.).
Note
Depending on the types and model configuration involved, the _Python_ and _JSON_ modes may have different validation behavior (e.g. with [strictness](https://docs.pydantic.dev/latest/concepts/strict_mode/)). If you have data coming from a non-JSON source, but want the same validation behavior and errors you'd get from the _JSON_ mode, our recommendation for now is to either dump your data to JSON (e.g. using [`model_validate_strings()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_validate_strings) if the data takes the form of a (potentially nested) dictionary with string keys and values. Progress for this feature can be tracked in
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/models/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/models/#__tabbed_2_2)
```
from datetime import datetime
from typing import Optional

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None


m = User.model_validate({'id': 123, 'name': 'James'})
print(m)
#> id=123 name='James' signup_ts=None

try:
    m = User.model_validate_json('{"id": 123, "name": 123}')
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    name
      Input should be a valid string [type=string_type, input_value=123, input_type=int]
    """

m = User.model_validate_strings({'id': '123', 'name': 'James'})
print(m)
#> id=123 name='James' signup_ts=None

m = User.model_validate_strings(
    {'id': '123', 'name': 'James', 'signup_ts': '2024-04-01T12:00:00'}
)
print(m)
#> id=123 name='James' signup_ts=datetime.datetime(2024, 4, 1, 12, 0)

try:
    m = User.model_validate_strings(
        {'id': '123', 'name': 'James', 'signup_ts': '2024-04-01'}, strict=True
    )
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    signup_ts
      Input should be a valid datetime, invalid datetime separator, expected `T`, `t`, `_` or space [type=datetime_parsing, input_value='2024-04-01', input_type=str]
    """

```

```
from datetime import datetime

from pydantic import BaseModel, ValidationError


class User(BaseModel):
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None


m = User.model_validate({'id': 123, 'name': 'James'})
print(m)
#> id=123 name='James' signup_ts=None

try:
    m = User.model_validate_json('{"id": 123, "name": 123}')
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    name
      Input should be a valid string [type=string_type, input_value=123, input_type=int]
    """

m = User.model_validate_strings({'id': '123', 'name': 'James'})
print(m)
#> id=123 name='James' signup_ts=None

m = User.model_validate_strings(
    {'id': '123', 'name': 'James', 'signup_ts': '2024-04-01T12:00:00'}
)
print(m)
#> id=123 name='James' signup_ts=datetime.datetime(2024, 4, 1, 12, 0)

try:
    m = User.model_validate_strings(
        {'id': '123', 'name': 'James', 'signup_ts': '2024-04-01'}, strict=True
    )
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    signup_ts
      Input should be a valid datetime, invalid datetime separator, expected `T`, `t`, `_` or space [type=datetime_parsing, input_value='2024-04-01', input_type=str]
    """

```

### Creating models without validation[¶](https://docs.pydantic.dev/latest/concepts/models/#creating-models-without-validation)
Pydantic also provides the [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct) method, which allows models to be created **without validation**. This can be useful in at least a few cases:
  * when working with complex data that is already known to be valid (for performance reasons)
  * when one or more of the validator functions are non-idempotent
  * when one or more of the validator functions have side effects that you don't want to be triggered.


Warning
[`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct) does not do any validation, meaning it can create models which are invalid. **You should only ever use the[`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct) method with data which has already been validated, or that you definitely trust.**
Note
In Pydantic V2, the performance gap between validation (either with direct instantiation or the `model_validate*` methods) and [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct) has been narrowed considerably. For simple models, going with validation may even be faster. If you are using [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct) for performance reasons, you may want to profile your use case before assuming it is actually faster.
Note that for [root models](https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types), the root value can be passed to [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct) positionally, instead of using a keyword argument.
Here are some additional notes on the behavior of [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct):
  * When we say "no validation is performed" — this includes converting dictionaries to model instances. So if you have a field referring to a model type, you will need to convert the inner dictionary to a model yourself.
  * If you do not pass keyword arguments for fields with defaults, the default values will still be used.
  * For models with private attributes, the `__pydantic_private__` dictionary will be populated the same as it would be when creating the model with validation.
  * No `__init__` method from the model or any of its parent classes will be called, even when a custom `__init__` method is defined.


On [extra data](https://docs.pydantic.dev/latest/concepts/models/#extra-data) behavior with [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct)
  * For models with [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) set to `'allow'`, data not corresponding to fields will be correctly stored in the `__pydantic_extra__` dictionary and saved to the model's `__dict__` attribute.
  * For models with [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) set to `'ignore'`, data not corresponding to fields will be ignored — that is, not stored in `__pydantic_extra__` or `__dict__` on the instance.
  * Unlike when instantiating the model with validation, a call to [`model_construct()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_construct) with [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) set to `'forbid'` doesn't raise an error in the presence of data not corresponding to fields. Rather, said input data is simply ignored.


### Defining a custom `__init__()`[¶](https://docs.pydantic.dev/latest/concepts/models/#defining-a-custom-__init__)
Pydantic provides a default `__init__()` implementation for Pydantic models, that is called _only_ when using the model constructor (and not with the `model_validate_*()` methods). This implementation delegates validation to `pydantic-core`.
However, it is possible to define a custom `__init__()` on your models. In this case, it will be called unconditionally from all the [validation methods](https://docs.pydantic.dev/latest/concepts/models/#validating-data), without performing validation (and so you should call `super().__init__(**kwargs)` in your implementation).
Defining a custom `__init__()` is not recommended, as all the validation parameters ([strictness](https://docs.pydantic.dev/latest/concepts/strict_mode/), [extra data behavior](https://docs.pydantic.dev/latest/concepts/models/#extra-data), [validation context](https://docs.pydantic.dev/latest/concepts/validators/#validation-context)) will be lost. If you need to perform actions after the model was initialized, you can make use of _after_ [field](https://docs.pydantic.dev/latest/concepts/validators/#field-after-validator) or [model](https://docs.pydantic.dev/latest/concepts/validators/#model-after-validator) validators, or define a [`model_post_init()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_post_init) implementation:
```
import logging
from typing import Any

from pydantic import BaseModel


class MyModel(BaseModel):
    id: int

    def model_post_init(self, context: Any) -> None:
        logging.info("Model initialized with id %d", self.id)

```
