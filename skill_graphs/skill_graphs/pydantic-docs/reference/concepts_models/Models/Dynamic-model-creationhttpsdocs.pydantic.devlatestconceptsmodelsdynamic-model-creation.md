## Dynamic model creation[¶](https://docs.pydantic.dev/latest/concepts/models/#dynamic-model-creation)
API Documentation
[`pydantic.main.create_model`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.create_model)

There are some occasions where it is desirable to create a model using runtime information to specify the fields. Pydantic provides the [`create_model()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.create_model) function to allow models to be created dynamically:
```
from pydantic import BaseModel, create_model

DynamicFoobarModel = create_model('DynamicFoobarModel', foo=str, bar=(int, 123))

# Equivalent to:


class StaticFoobarModel(BaseModel):
    foo: str
    bar: int = 123

```

Field definitions are specified as keyword arguments, and should either be:
  * A single element, representing the type annotation of the field.
  * A two-tuple, the first element being the type and the second element the assigned value (either a default or the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function).


Here is a more advanced example:
```
from typing import Annotated

from pydantic import BaseModel, Field, PrivateAttr, create_model

DynamicModel = create_model(
    'DynamicModel',
    foo=(str, Field(alias='FOO')),
    bar=Annotated[str, Field(description='Bar field')],
    _private=(int, PrivateAttr(default=1)),
)


class StaticModel(BaseModel):
    foo: str = Field(alias='FOO')
    bar: Annotated[str, Field(description='Bar field')]
    _private: int = PrivateAttr(default=1)

```

The special keyword arguments `__config__` and `__base__` can be used to customize the new model. This includes extending a base model with extra fields.
```
from pydantic import BaseModel, create_model


class FooModel(BaseModel):
    foo: str
    bar: int = 123


BarModel = create_model(
    'BarModel',
    apple=(str, 'russet'),
    banana=(str, 'yellow'),
    __base__=FooModel,
)
print(BarModel)
#> <class '__main__.BarModel'>
print(BarModel.model_fields.keys())
#> dict_keys(['foo', 'bar', 'apple', 'banana'])

```

You can also add validators by passing a dictionary to the `__validators__` argument.
```
from pydantic import ValidationError, create_model, field_validator


def alphanum(cls, v):
    assert v.isalnum(), 'must be alphanumeric'
    return v


validators = {
    'username_validator': field_validator('username')(alphanum)  [](https://docs.pydantic.dev/latest/concepts/models/#__code_39_annotation_1)
}

UserModel = create_model(
    'UserModel', username=(str, ...), __validators__=validators
)

user = UserModel(username='scolvin')
print(user)
#> username='scolvin'

try:
    UserModel(username='scolvi%n')
except ValidationError as e:
    print(e)
    """
    1 validation error for UserModel
    username
      Assertion failed, must be alphanumeric [type=assertion_error, input_value='scolvi%n', input_type=str]
    """

```

Note
To pickle a dynamically created model:
  * the model must be defined globally
  * the `__module__` argument must be provided


Warning
This function may execute arbitrary code contained in field annotations, if string references need to be evaluated.
See
See also: the [dynamic model example](https://docs.pydantic.dev/latest/examples/dynamic_models/), providing guidelines to derive an optional model from another one.
