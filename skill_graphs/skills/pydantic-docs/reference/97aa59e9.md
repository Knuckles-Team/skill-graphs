## Migration guide[¶](https://docs.pydantic.dev/latest/migration/#migration-guide)
The following sections provide details on the most important changes in Pydantic V2.
### Changes to `pydantic.BaseModel`[¶](https://docs.pydantic.dev/latest/migration/#changes-to-pydanticbasemodel)
Various method names have been changed; all non-deprecated `BaseModel` methods now have names matching either the format `model_.*` or `__.*pydantic.*__`. Where possible, we have retained the deprecated methods with their old names to help ease migration, but calling them will emit `DeprecationWarning`s.
Pydantic V1 | Pydantic V2
---|---
`__fields__` | `model_fields`
`__private_attributes__` | `__pydantic_private__`
`__validators__` | `__pydantic_validator__`
`construct()` | `model_construct()`
`copy()` | `model_copy()`
`dict()` | `model_dump()`
`json_schema()` | `model_json_schema()`
`json()` | `model_dump_json()`
`parse_obj()` | `model_validate()`
`update_forward_refs()` | `model_rebuild()`
  * Some of the built-in data-loading functionality has been slated for removal. In particular, `parse_raw` and `parse_file` are now deprecated. In Pydantic V2, `model_validate_json` works like `parse_raw`. Otherwise, you should load the data and then pass it to `model_validate`.
  * The `from_orm` method has been deprecated; you can now just use `model_validate` (equivalent to `parse_obj` from Pydantic V1) to achieve something similar, as long as you've set `from_attributes=True` in the model config.
  * The `__eq__` method has changed for models.
    * Models can only be equal to other `BaseModel` instances.
    * For two model instances to be equal, they must have the same:
      * Type (or, in the case of generic models, non-parametrized generic origin type)
      * Field values
      * Extra values (only relevant when `model_config['extra'] == 'allow'`)
      * Private attribute values; models with different values of private attributes are no longer equal.
      * Models are no longer equal to the dicts containing their data.
      * Non-generic models of different types are never equal.
      * Generic models with different origin types are never equal. We don't require _exact_ type equality so that, for example, instances of `MyGenericModel[Any]` could be equal to instances of `MyGenericModel[int]`.
  * We have replaced the use of the `__root__` field to specify a "custom root model" with a new type called [`RootModel`](https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types) which is intended to replace the functionality of using a field called `__root__` in Pydantic V1. Note, `RootModel` types no longer support the `arbitrary_types_allowed` config setting. See
  * We have significantly expanded Pydantic's capabilities related to customizing serialization. In particular, we have added the [`@field_serializer`](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.field_serializer), [`@model_serializer`](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.model_serializer), and [`@computed_field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.computed_field) decorators, which each address various shortcomings from Pydantic V1.
    * See [Custom serializers](https://docs.pydantic.dev/latest/concepts/serialization/#serializers) for the usage docs of these new decorators.
    * Due to performance overhead and implementation complexity, we have now deprecated support for specifying `json_encoders` in the model config. This functionality was originally added for the purpose of achieving custom serialization logic, and we think the new serialization decorators are a better choice in most common scenarios.
  * We have changed the behavior related to serializing subclasses of models when they occur as nested fields in a parent model. In V1, we would always include all fields from the subclass instance. In V2, when we dump a model, we only include the fields that are defined on the annotated type of the field. This helps prevent some accidental security bugs. You can read more about this (including how to opt out of this behavior) in the [relevant section](https://docs.pydantic.dev/latest/concepts/serialization/#subclasses-of-model-like-types) of the model exporting docs.
  * `GetterDict` has been removed as it was just an implementation detail of `orm_mode`, which has been removed.
  * In many cases, arguments passed to the constructor will be **copied** in order to perform validation and, where necessary, coercion (see the [documentation](https://docs.pydantic.dev/latest/concepts/models/#attribute-copies)). This is notable in the case of passing mutable objects as arguments to a constructor.
  * The `.json()` method is deprecated, and attempting to use this deprecated method with arguments such as `indent` or `ensure_ascii` may lead to confusing errors. For best results, switch to V2's equivalent, `model_dump_json()`. If you'd still like to use said arguments, you can use
  * JSON serialization of non-string key values is generally done with `str(key)`, leading to some changes in behavior such as the following:


```
from typing import Optional

from pydantic import BaseModel as V2BaseModel
from pydantic.v1 import BaseModel as V1BaseModel


class V1Model(V1BaseModel):
    a: dict[Optional[str], int]


class V2Model(V2BaseModel):
    a: dict[Optional[str], int]


v1_model = V1Model(a={None: 123})
v2_model = V2Model(a={None: 123})

# V1
print(v1_model.json())
#> {"a": {"null": 123}}

# V2
print(v2_model.model_dump_json())
#> {"a":{"None":123}}

```

  * `model_dump_json()` results are compacted in order to save space, and don't always exactly match that of `json.dumps()` output. That being said, you can easily modify the separators used in `json.dumps()` results in order to align the two outputs:


```
import json

from pydantic import BaseModel as V2BaseModel
from pydantic.v1 import BaseModel as V1BaseModel


class V1Model(V1BaseModel):
    a: list[str]


class V2Model(V2BaseModel):
    a: list[str]


v1_model = V1Model(a=['fancy', 'sushi'])
v2_model = V2Model(a=['fancy', 'sushi'])

# V1
print(v1_model.json())
#> {"a": ["fancy", "sushi"]}

# V2
print(v2_model.model_dump_json())
#> {"a":["fancy","sushi"]}

# Plain json.dumps
print(json.dumps(v2_model.model_dump()))
#> {"a": ["fancy", "sushi"]}

# Modified json.dumps
print(json.dumps(v2_model.model_dump(), separators=(',', ':')))
#> {"a":["fancy","sushi"]}

```

### Changes to `pydantic.generics.GenericModel`[¶](https://docs.pydantic.dev/latest/migration/#changes-to-pydanticgenericsgenericmodel)
The `pydantic.generics.GenericModel` class is no longer necessary, and has been removed. Instead, you can now create generic `BaseModel` subclasses by just adding `Generic` as a parent class on a `BaseModel` subclass directly. This looks like `class MyGenericModel(BaseModel, Generic[T]): ...`.
Mixing of V1 and V2 models is not supported which means that type parameters of such generic `BaseModel` (V2) cannot be V1 models.
While it may not raise an error, we strongly advise against using _parametrized_ generics in `isinstance` checks.
  * For example, you should not do `isinstance(my_model, MyGenericModel[int])`. However, it is fine to do `isinstance(my_model, MyGenericModel)`. (Note that for standard generics, it would raise an error to do a subclass check with a parameterized generic.)
  * If you need to perform `isinstance` checks against parametrized generics, you can do this by subclassing the parametrized generic class. This looks like `class MyIntModel(MyGenericModel[int]): ...` and `isinstance(my_model, MyIntModel)`.


Find more information in the [Generic models](https://docs.pydantic.dev/latest/concepts/models/#generic-models) documentation.
### Changes to `pydantic.Field`[¶](https://docs.pydantic.dev/latest/migration/#changes-to-pydanticfield)
`Field` no longer supports arbitrary keyword arguments to be added to the JSON schema. Instead, any extra data you want to add to the JSON schema should be passed as a dictionary to the `json_schema_extra` keyword argument.
In Pydantic V1, the `alias` property returns the field's name when no alias is set. In Pydantic V2, this behavior has changed to return `None` when no alias is set.
The following properties have been removed from or changed in `Field`:
  * `const`
  * `min_items` (use `min_length` instead)
  * `max_items` (use `max_length` instead)
  * `unique_items`
  * `allow_mutation` (use `frozen` instead)
  * `regex` (use `pattern` instead)
  * `final` (use the


Field constraints are no longer automatically pushed down to the parameters of generics. For example, you can no longer validate every element of a list matches a regex by providing `my_list: list[str] = Field(pattern=".*")`. Instead, use `str` itself: `my_list: list[Annotated[str, Field(pattern=".*")]]`
### Changes to dataclasses[¶](https://docs.pydantic.dev/latest/migration/#changes-to-dataclasses)
Pydantic [dataclasses](https://docs.pydantic.dev/latest/concepts/dataclasses/) continue to be useful for enabling the data validation on standard dataclasses without having to subclass `BaseModel`. Pydantic V2 introduces the following changes to this dataclass behavior:
  * When used as fields, dataclasses (Pydantic or vanilla) no longer accept tuples as validation inputs; dicts should be used instead.
  * The `__post_init__` in Pydantic dataclasses will now be called _after_ validation, rather than before.
    * As a result, the `__post_init_post_parse__` method would have become redundant, so has been removed.
  * Pydantic no longer supports `extra='allow'` for Pydantic dataclasses, where extra fields passed to the initializer would be stored as extra attributes on the dataclass. `extra='ignore'` is still supported for the purpose of ignoring unexpected fields while parsing data, they just won't be stored on the instance.
  * Pydantic dataclasses no longer have an attribute `__pydantic_model__`, and no longer use an underlying `BaseModel` to perform validation or provide other functionality.
    * To perform validation, generate a JSON schema, or make use of any other functionality that may have required `__pydantic_model__` in V1, you should now wrap the dataclass with a [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) ([discussed more below](https://docs.pydantic.dev/latest/migration/#introduction-of-typeadapter)) and make use of its methods.
  * In Pydantic V1, if you used a vanilla (i.e., non-Pydantic) dataclass as a field, the config of the parent type would be used as though it was the config for the dataclass itself as well. In Pydantic V2, this is no longer the case.
    * In Pydantic V2, to override the config (like you would with `model_config` on a `BaseModel`), you can use the `config` parameter on the `@dataclass` decorator. See [Dataclass Config](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config) for examples.


### Changes to config[¶](https://docs.pydantic.dev/latest/migration/#changes-to-config)
  * In Pydantic V2, to specify config on a model, you should set a class attribute called `model_config` to be a dict with the key/value pairs you want to be used as the config. The Pydantic V1 behavior to create a class called `Config` in the namespace of the parent `BaseModel` subclass is now deprecated.
  * When subclassing a model, the `model_config` attribute is inherited. This is helpful in the case where you'd like to use a base class with a given configuration for many models. Note, if you inherit from multiple `BaseModel` subclasses, like `class MyModel(Model1, Model2)`, the non-default settings in the `model_config` attribute from the two models will be merged, and for any settings defined in both, those from `Model2` will override those from `Model1`.
  * The following config settings have been removed:
    * `allow_mutation` — this has been removed. You should be able to use [frozen](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) equivalently (inverse of current use).
    * `error_msg_templates`
    * `fields` — this was the source of various bugs, so has been removed. You should be able to use `Annotated` on fields to modify them as desired.
    * `getter_dict` — `orm_mode` has been removed, and this implementation detail is no longer necessary.
    * `smart_union` - the default `union_mode` in Pydantic V2 is `'smart'`.
    * `underscore_attrs_are_private` — the Pydantic V2 behavior is now the same as if this was always set to `True` in Pydantic V1.
    * `json_loads`
    * `json_dumps`
    * `copy_on_model_validation`
    * `post_init_call`
  * The following config settings have been renamed:
    * `allow_population_by_field_name` → `populate_by_name` (or `validate_by_name` starting in v2.11)
    * `anystr_lower` → `str_to_lower`
    * `anystr_strip_whitespace` → `str_strip_whitespace`
    * `anystr_upper` → `str_to_upper`
    * `keep_untouched` → `ignored_types`
    * `max_anystr_length` → `str_max_length`
    * `min_anystr_length` → `str_min_length`
    * `orm_mode` → `from_attributes`
    * `schema_extra` → `json_schema_extra`
    * `validate_all` → `validate_default`


See the [`ConfigDict` API reference](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict) for more details.
### Changes to validators[¶](https://docs.pydantic.dev/latest/migration/#changes-to-validators)
####  `@validator` and `@root_validator` are deprecated[¶](https://docs.pydantic.dev/latest/migration/#validator-and-root_validator-are-deprecated)
  * `@validator` has been deprecated, and should be replaced with [`@field_validator`](https://docs.pydantic.dev/latest/concepts/validators/), which provides various new features and improvements.
    * The new `@field_validator` decorator does not have the `each_item` keyword argument; validators you want to apply to items within a generic container should be added by annotating the type argument. See [validators in Annotated metadata](https://docs.pydantic.dev/latest/concepts/types/#using-the-annotated-pattern) for details. This looks like `list[Annotated[int, Field(ge=0)]]`
    * Even if you keep using the deprecated `@validator` decorator, you can no longer add the `field` or `config` arguments to the signature of validator functions. If you need access to these, you'll need to migrate to `@field_validator` — see the [next section](https://docs.pydantic.dev/latest/migration/#changes-to-validators-allowed-signatures) for more details.
    * If you use the `always=True` keyword argument to a validator function, note that standard validators for the annotated type will _also_ be applied even to defaults, not just the custom validators. For example, despite the fact that the validator below will never error, the following code raises a `ValidationError`:


Note
To avoid this, you can use the `validate_default` argument in the `Field` function. When set to `True`, it mimics the behavior of `always=True` in Pydantic v1. However, the new way of using `validate_default` is encouraged as it provides more flexibility and control.
```
from pydantic import BaseModel, validator


class Model(BaseModel):
    x: str = 1

    @validator('x', always=True)
    @classmethod
    def validate_x(cls, v):
        return v


Model()

```

  * `@root_validator` has been deprecated, and should be replaced with [`@model_validator`](https://docs.pydantic.dev/latest/api/functional_validators/#pydantic.functional_validators.model_validator), which also provides new features and improvements. Be aware that the allowed signatures have changed (see the [relevant documentation](https://docs.pydantic.dev/latest/concepts/validators/#model-validators)).
    * Under some circumstances (such as assignment when `model_config['validate_assignment'] is True`), the `@model_validator` decorator will receive an instance of the model, not a dict of values. You may need to be careful to handle this case.
    * Even if you keep using the deprecated `@root_validator` decorator, due to refactors in validation logic, you can no longer run with `skip_on_failure=False` (which is the default value of this keyword argument, so must be set explicitly to `True`).


#### Changes to `@validator`'s allowed signatures[¶](https://docs.pydantic.dev/latest/migration/#changes-to-validators-allowed-signatures)
In Pydantic V1, functions wrapped by `@validator` could receive keyword arguments with metadata about what was being validated. Some of these arguments have been removed from `@field_validator` in Pydantic V2:
  * `config`: Pydantic V2's config is now a dictionary instead of a class, which means this argument is no longer backwards compatible. If you need to access the configuration you should migrate to `@field_validator` and use `info.config`.
  * `field`: this argument used to be a `ModelField` object, which was a quasi-internal class that no longer exists in Pydantic V2. Most of this information can still be accessed by using the field name from `info.field_name` to index into `cls.model_fields`


```
from pydantic import BaseModel, ValidationInfo, field_validator


class Model(BaseModel):
    x: int

    @field_validator('x')
    def val_x(cls, v: int, info: ValidationInfo) -> int:
        assert info.config is not None
        print(info.config.get('title'))
        #> Model
        print(cls.model_fields[info.field_name].is_required())
        #> True
        return v


Model(x=1)

```

####  `TypeError` is no longer converted to `ValidationError` in validators[¶](https://docs.pydantic.dev/latest/migration/#typeerror-is-no-longer-converted-to-validationerror-in-validators)
Previously, when raising a `TypeError` within a validator function, that error would be wrapped into a `ValidationError` and, in some cases (such as with FastAPI), these errors might be displayed to end users. This led to a variety of undesirable behavior — for example, calling a function with the wrong signature might produce a user-facing `ValidationError`.
However, in Pydantic V2, when a `TypeError` is raised in a validator, it is no longer converted into a `ValidationError`:
```
import pytest

from pydantic import BaseModel, field_validator


class Model(BaseModel):
    x: int

    @field_validator('x')
    def val_x(cls, v: int) -> int:
        return str.lower(v)  # raises a TypeError


with pytest.raises(TypeError):
    Model(x=1)

```

This applies to all validation decorators.
#### Validator behavior changes[¶](https://docs.pydantic.dev/latest/migration/#validator-behavior-changes)
Pydantic V2 includes some changes to type coercion. For example:
  * coercing `int`, `float`, and `Decimal` values to strings is now optional and disabled by default, see [Coerce Numbers to Strings](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.coerce_numbers_to_str).
  * iterable of pairs is no longer coerced to a dict.


See the [Conversion table](https://docs.pydantic.dev/latest/concepts/conversion_table/) for details on Pydantic V2 type coercion defaults.
#### The `allow_reuse` keyword argument is no longer necessary[¶](https://docs.pydantic.dev/latest/migration/#the-allow_reuse-keyword-argument-is-no-longer-necessary)
Previously, Pydantic tracked "reused" functions in decorators as this was a common source of mistakes. We did this by comparing the function's fully qualified name (module name + function name), which could result in false positives. The `allow_reuse` keyword argument could be used to disable this when it was intentional.
Our approach to detecting repeatedly defined functions has been overhauled to only error for redefinition within a single class, reducing false positives and bringing the behavior more in line with the errors that type checkers and linters would give for defining a method with the same name multiple times in a single class definition.
In nearly all cases, if you were using `allow_reuse=True`, you should be able to simply delete that keyword argument and have things keep working as expected.
####  `@validate_arguments` has been renamed to `@validate_call`[¶](https://docs.pydantic.dev/latest/migration/#validate_arguments-has-been-renamed-to-validate_call)
In Pydantic V2, the `@validate_arguments` decorator has been renamed to `@validate_call`.
In Pydantic V1, the decorated function had various attributes added, such as `raw_function`, and `validate` (which could be used to validate arguments without actually calling the decorated function). Due to limited use of these attributes, and performance-oriented changes in implementation, we have not preserved this functionality in `@validate_call`.
### Input types are not preserved[¶](https://docs.pydantic.dev/latest/migration/#input-types-are-not-preserved)
In Pydantic V1 we made great efforts to preserve the types of all field inputs for generic collections when they were proper subtypes of the field annotations. For example, given the annotation `Mapping[str, int]` if you passed in a `collection.Counter()` you'd get a `collection.Counter()` as the value.
Supporting this behavior in V2 would have negative performance implications for the general case (we'd have to check types every time) and would add a lot of complexity to validation. Further, even in V1 this behavior was inconsistent and partially broken: it did not work for many types (`str`, `UUID`, etc.), and for generic collections it's impossible to re-build the original input correctly without a lot of special casing (consider `ChainMap`; rebuilding the input is necessary because we need to replace values after validation, e.g. if coercing strings to ints).
In Pydantic V2 we no longer attempt to preserve the input type in all cases; instead, we only promise that the output type will match the type annotations.
Going back to the `Mapping` example, we promise the output will be a valid `Mapping`, and in practice it will be a plain `dict`:
```
from collections.abc import Mapping

from pydantic import TypeAdapter


class MyDict(dict):
    pass


ta = TypeAdapter(Mapping[str, int])
v = ta.validate_python(MyDict())
print(type(v))
#> <class 'dict'>

```

If you want the output type to be a specific type, consider annotating it as such or implementing a custom validator:
```
from collections.abc import Mapping
from typing import Annotated, Any, TypeVar

from pydantic import (
    TypeAdapter,
    ValidationInfo,
    ValidatorFunctionWrapHandler,
    WrapValidator,
)


def restore_input_type(
    value: Any, handler: ValidatorFunctionWrapHandler, _info: ValidationInfo
) -> Any:
    return type(value)(handler(value))


T = TypeVar('T')
PreserveType = Annotated[T, WrapValidator(restore_input_type)]


ta = TypeAdapter(PreserveType[Mapping[str, int]])


class MyDict(dict):
    pass


v = ta.validate_python(MyDict())
assert type(v) is MyDict

```

While we don't promise to preserve input types everywhere, we _do_ preserve them for subclasses of `BaseModel`, and for dataclasses:
```
import pydantic.dataclasses
from pydantic import BaseModel


class InnerModel(BaseModel):
    x: int


class OuterModel(BaseModel):
    inner: InnerModel


class SubInnerModel(InnerModel):
    y: int


m = OuterModel(inner=SubInnerModel(x=1, y=2))
print(m)
#> inner=SubInnerModel(x=1, y=2)


@pydantic.dataclasses.dataclass
class InnerDataclass:
    x: int


@pydantic.dataclasses.dataclass
class SubInnerDataclass(InnerDataclass):
    y: int


@pydantic.dataclasses.dataclass
class OuterDataclass:
    inner: InnerDataclass


d = OuterDataclass(inner=SubInnerDataclass(x=1, y=2))
print(d)
#> OuterDataclass(inner=SubInnerDataclass(x=1, y=2))

```

### Changes to Handling of Standard Types[¶](https://docs.pydantic.dev/latest/migration/#changes-to-handling-of-standard-types)
#### Dicts[¶](https://docs.pydantic.dev/latest/migration/#dicts)
Iterables of pairs (which include empty iterables) no longer pass validation for fields of type `dict`.
#### Unions[¶](https://docs.pydantic.dev/latest/migration/#unions)
While union types will still attempt validation of each choice from left to right, they now preserve the type of the input whenever possible, even if the correct type is not the first choice for which the input would pass validation. As a demonstration, consider the following example:
[Python 3.9 and above](https://docs.pydantic.dev/latest/migration/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/migration/#__tabbed_2_2)
```
from typing import Union

from pydantic import BaseModel


class Model(BaseModel):
    x: Union[int, str]


print(Model(x='1'))
#> x='1'

```

```
from pydantic import BaseModel


class Model(BaseModel):
    x: int | str


print(Model(x='1'))
#> x='1'

```

In Pydantic V1, the printed result would have been `x=1`, since the value would pass validation as an `int`. In Pydantic V2, we recognize that the value is an instance of one of the cases and short-circuit the standard union validation.
To revert to the non-short-circuiting left-to-right behavior of V1, annotate the union with `Field(union_mode='left_to_right')`. See [Union Mode](https://docs.pydantic.dev/latest/concepts/unions/#union-modes) for more details.
#### Required, optional, and nullable fields[¶](https://docs.pydantic.dev/latest/migration/#required-optional-and-nullable-fields)
Pydantic V2 changes some of the logic for specifying whether a field annotated as `Optional` is required (i.e., has no default value) or not (i.e., has a default value of `None` or any other value of the corresponding type), and now more closely matches the behavior of `dataclasses`. Similarly, fields annotated as `Any` no longer have a default value of `None`.
The following table describes the behavior of field annotations in V2:
State | Field Definition
---|---
Required, cannot be `None` | `f1: str`
Not required, cannot be `None`, is `'abc'` by default | `f2: str = 'abc'`
Required, can be `None` | `f3: Optional[str]`
Not required, can be `None`, is `None` by default | `f4: Optional[str] = None`
Not required, can be `None`, is `'abc'` by default | `f5: Optional[str] = 'abc'`
Required, can be any type (including `None`) | `f6: Any`
Not required, can be any type (including `None`) | `f7: Any = None`
Note
A field annotated as `typing.Optional[T]` will be required, and will allow for a value of `None`. It does not mean that the field has a default value of `None`. _(This is a breaking change from V1.)_
Note
Any default value if provided makes a field not required.
Here is a code example demonstrating the above:
[Python 3.9 and above](https://docs.pydantic.dev/latest/migration/#__tabbed_3_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/migration/#__tabbed_3_2)
```
from typing import Optional

from pydantic import BaseModel, ValidationError


class Foo(BaseModel):
    f1: str  # required, cannot be None
    f2: Optional[str]  # required, can be None - same as str | None
    f3: Optional[str] = None  # not required, can be None
    f4: str = 'Foobar'  # not required, but cannot be None


try:
    Foo(f1=None, f2=None, f4='b')
except ValidationError as e:
    print(e)
    """
    1 validation error for Foo
    f1
      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
    """

```

```
from pydantic import BaseModel, ValidationError


class Foo(BaseModel):
    f1: str  # required, cannot be None
    f2: str | None  # required, can be None - same as str | None
    f3: str | None = None  # not required, can be None
    f4: str = 'Foobar'  # not required, but cannot be None


try:
    Foo(f1=None, f2=None, f4='b')
except ValidationError as e:
    print(e)
    """
    1 validation error for Foo
    f1
      Input should be a valid string [type=string_type, input_value=None, input_type=NoneType]
    """

```

#### Patterns / regex on strings[¶](https://docs.pydantic.dev/latest/migration/#patterns-regex-on-strings)
Pydantic V1 used Python's regex library. Pydantic V2 uses the Rust
If you still want to use Python's regex library, you can use the [`regex_engine`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.regex_engine) config setting.
### Type conversion from floats to integers[¶](https://docs.pydantic.dev/latest/migration/#type-conversion-from-floats-to-integers)
In V1, whenever a field was annotated as `int`, any float value would be accepted, which could lead to a potential data loss if the float value contains a non-zero decimal part. In V2, type conversion from floats to integers is only allowed if the decimal part is zero:
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: int


print(Model(x=10.0))
#> x=10
try:
    Model(x=10.2)
except ValidationError as err:
    print(err)
    """
    1 validation error for Model
    x
      Input should be a valid integer, got a number with a fractional part [type=int_from_float, input_value=10.2, input_type=float]
    """

```

### Introduction of `TypeAdapter`[¶](https://docs.pydantic.dev/latest/migration/#introduction-of-typeadapter)
Pydantic V1 had weak support for validating or serializing non-`BaseModel` types.
To work with them, you had to either create a "root" model or use the utility functions in `pydantic.tools` (namely, `parse_obj_as` and `schema_of`).
In Pydantic V2 this is _a lot_ easier: the [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) class lets you create an object with methods for validating, serializing, and producing JSON schemas for arbitrary types. This serves as a complete replacement for `parse_obj_as` and `schema_of` (which are now deprecated), and also covers some of the use cases of "root" models. ([`RootModel`](https://docs.pydantic.dev/latest/concepts/models/#rootmodel-and-custom-root-types), [discussed above](https://docs.pydantic.dev/latest/migration/#changes-to-pydanticbasemodel), covers the others.)
```
from pydantic import TypeAdapter

adapter = TypeAdapter(list[int])
assert adapter.validate_python(['1', '2', '3']) == [1, 2, 3]
print(adapter.json_schema())
#> {'items': {'type': 'integer'}, 'type': 'array'}

```

Due to limitations of inferring generic types with common type checkers, to get proper typing in some scenarios, you may need to explicitly specify the generic parameter:
```
from pydantic import TypeAdapter

adapter = TypeAdapter[str | int](str | int)
...

```

See [Type Adapter](https://docs.pydantic.dev/latest/concepts/type_adapter/) for more information.
### Defining custom types[¶](https://docs.pydantic.dev/latest/migration/#defining-custom-types)
We have completely overhauled the way custom types are defined in pydantic.
We have exposed hooks for generating both `pydantic-core` and JSON schemas, allowing you to get all the performance benefits of Pydantic V2 even when using your own custom types.
We have also introduced ways to use
The main changes are:
  * `__get_validators__` should be replaced with `__get_pydantic_core_schema__`. See [Custom Data Types](https://docs.pydantic.dev/latest/concepts/types/#customizing_validation_with_get_pydantic_core_schema) for more information.
  * `__modify_schema__` becomes `__get_pydantic_json_schema__`. See [JSON Schema Customization](https://docs.pydantic.dev/latest/concepts/json_schema/#customizing-json-schema) for more information.


Additionally, you can use `__get_pydantic_core_schema__` and `__get_pydantic_json_schema__` functions of a type by annotating it, rather than modifying the type itself. This provides a powerful and flexible mechanism for integrating third-party types with Pydantic, and in some cases may help you remove hacks from Pydantic V1 introduced to work around the limitations for custom types.
See [Custom Data Types](https://docs.pydantic.dev/latest/concepts/types/#custom-types) for more information.
### Changes to JSON schema generation[¶](https://docs.pydantic.dev/latest/migration/#changes-to-json-schema-generation)
We received many requests over the years to make changes to the JSON schemas that pydantic generates.
In Pydantic V2, we have tried to address many of the common requests:
  * The JSON schema for `Optional` fields now indicates that the value `null` is allowed.
  * The `Decimal` type is now exposed in JSON schema (and serialized) as a string.
  * The JSON schema no longer preserves namedtuples as namedtuples.
  * The JSON schema we generate by default now targets draft 2020-12 (with some OpenAPI extensions).
  * When they differ, you can now specify if you want the JSON schema representing the inputs to validation, or the outputs from serialization.


However, there have been many reasonable requests over the years for changes which we have not chosen to implement.
In Pydantic V1, even if you were willing to implement changes yourself, it was very difficult because the JSON schema generation process involved various recursive function calls; to override one, you'd have to copy and modify the whole implementation.
In Pydantic V2, one of our design goals was to make it easier to customize JSON schema generation. To this end, we have introduced the class [`GenerateJsonSchema`](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema), which implements the translation of a type's pydantic-core schema into a JSON schema. By design, this class breaks the JSON schema generation process into smaller methods that can be easily overridden in subclasses to modify the "global" approach to generating JSON schema.
The various methods that can be used to produce JSON schema (such as `BaseModel.model_json_schema` or `TypeAdapter.json_schema`) accept a keyword argument `schema_generator: type[GenerateJsonSchema] = GenerateJsonSchema`, and you can pass your custom subclass to these methods in order to use your own approach to generating JSON schema.
Hopefully this means that if you disagree with any of the choices we've made, or if you are reliant on behaviors in Pydantic V1 that have changed in Pydantic V2, you can use a custom `schema_generator`, modifying the `GenerateJsonSchema` class as necessary for your application.
###  `BaseSettings` has moved to `pydantic-settings`[¶](https://docs.pydantic.dev/latest/migration/#basesettings-has-moved-to-pydantic-settings)
[`BaseSettings`](https://docs.pydantic.dev/latest/api/pydantic_settings/#pydantic_settings.BaseSettings), the base object for Pydantic [settings management](https://docs.pydantic.dev/latest/concepts/pydantic_settings/), has been moved to a separate package,
Also, the `parse_env_var` classmethod has been removed. So, you need to [customise settings sources](https://docs.pydantic.dev/latest/concepts/pydantic_settings/#customise-settings-sources) to have your own parsing function.
### Color and Payment Card Numbers moved to `pydantic-extra-types`[¶](https://docs.pydantic.dev/latest/migration/#color-and-payment-card-numbers-moved-to-pydantic-extra-types)
The following special-use types have been moved to the
  * [Color Types](https://docs.pydantic.dev/latest/api/pydantic_extra_types_color/)
  * [Payment Card Numbers](https://docs.pydantic.dev/latest/api/pydantic_extra_types_payment/)


### Url and Dsn types in `pydantic.networks` no longer inherit from `str`[¶](https://docs.pydantic.dev/latest/migration/#url-and-dsn-types-in-pydanticnetworks-no-longer-inherit-from-str)
In Pydantic V1 the [`AnyUrl`](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl) type inherited from `str`, and all the other `Url` and `Dsn` types inherited from these. In Pydantic V2 these types are built on two new `Url` and `MultiHostUrl` classes using `Annotated`.
Inheriting from `str` had upsides and downsides, and for V2 we decided it would be better to remove this. To use these types in APIs which expect `str` you'll now need to convert them (with `str(url)`).
Pydantic V2 uses Rust's `Url` types append slashes to the validated version if no path is included, even if a slash is not specified in the argument to a `Url` type constructor. See the example below for this behavior:
```
from pydantic import AnyUrl

assert str(AnyUrl(url='https://google.com')) == 'https://google.com/'
assert str(AnyUrl(url='https://google.com/')) == 'https://google.com/'
assert str(AnyUrl(url='https://google.com/api')) == 'https://google.com/api'
assert str(AnyUrl(url='https://google.com/api/')) == 'https://google.com/api/'

```

If you still want to use the old behavior without the appended slash, take a look at this
### Constrained types[¶](https://docs.pydantic.dev/latest/migration/#constrained-types)
The `Constrained*` classes were _removed_ , and you should replace them by `Annotated[<type>, Field(...)]`, for example:
```
from pydantic import BaseModel, ConstrainedInt


class MyInt(ConstrainedInt):
    ge = 0


class Model(BaseModel):
    x: MyInt

```

...becomes:
```
from typing import Annotated

from pydantic import BaseModel, Field

MyInt = Annotated[int, Field(ge=0)]


class Model(BaseModel):
    x: MyInt

```

Read more about it in the [Composing types via `Annotated`](https://docs.pydantic.dev/latest/concepts/types/#using-the-annotated-pattern) docs.
For `ConstrainedStr` you can use [`StringConstraints`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StringConstraints) instead.
### Mypy plugins[¶](https://docs.pydantic.dev/latest/migration/#mypy-plugins)
Pydantic V2 contains a `pydantic.mypy`.
When using [V1 features](https://docs.pydantic.dev/latest/migration/#continue-using-pydantic-v1-features) the `pydantic.v1.mypy` plugin might need to also be enabled.
To configure the mypy plugins:
[`mypy.ini`](https://docs.pydantic.dev/latest/migration/#__tabbed_4_1)[`pyproject.toml`](https://docs.pydantic.dev/latest/migration/#__tabbed_4_2)
```
[mypy]
plugins = pydantic.mypy, pydantic.v1.mypy  # include `.v1.mypy` if required.

```

```
[tool.mypy]
plugins = [
    "pydantic.mypy",
    "pydantic.v1.mypy",  # include `.v1.mypy` if required.
]

```
