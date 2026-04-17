## Generic models[¶](https://docs.pydantic.dev/latest/concepts/models/#generic-models)
Pydantic supports the creation of generic models to make it easier to reuse a common model structure. Both the new
Here is an example using a generic Pydantic model to create an easily-reused HTTP response payload wrapper:
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/models/#__tabbed_3_1)[Python 3.12 and above (new syntax)](https://docs.pydantic.dev/latest/concepts/models/#__tabbed_3_2)
```
from typing import Generic, TypeVar

from pydantic import BaseModel, ValidationError

DataT = TypeVar('DataT')  [](https://docs.pydantic.dev/latest/concepts/models/#__code_20_annotation_1)


class DataModel(BaseModel):
    number: int


class Response(BaseModel, Generic[DataT]):  [](https://docs.pydantic.dev/latest/concepts/models/#__code_20_annotation_2)
    data: DataT  [](https://docs.pydantic.dev/latest/concepts/models/#__code_20_annotation_3)


print(Response[int](data=1))
#> data=1
print(Response[str](data='value'))
#> data='value'
print(Response[str](data='value').model_dump())
#> {'data': 'value'}

data = DataModel(number=1)
print(Response[DataModel](data=data).model_dump())
#> {'data': {'number': 1}}
try:
    Response[int](data='value')
except ValidationError as e:
    print(e)
    """
    1 validation error for Response[int]
    data
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='value', input_type=str]
    """

```

```
from pydantic import BaseModel, ValidationError


class DataModel(BaseModel):
    number: int


class Response[DataT](BaseModel):

[](https://docs.pydantic.dev/latest/concepts/models/#__code_21_annotation_1)
    data: DataT

[](https://docs.pydantic.dev/latest/concepts/models/#__code_21_annotation_2)


print(Response[int](data=1))
#> data=1
print(Response[str](data='value'))
#> data='value'
print(Response[str](data='value').model_dump())
#> {'data': 'value'}

data = DataModel(number=1)
print(Response[DataModel](data=data).model_dump())
#> {'data': {'number': 1}}
try:
    Response[int](data='value')
except ValidationError as e:
    print(e)
    """
    1 validation error for Response[int]
    data
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='value', input_type=str]
    """

```

  1. Declare a Pydantic model and add the list of type variables as type parameters.
  2. Use the type variables as annotations where you will want to replace them with other types.


Warning
When parametrizing a model with a concrete type, Pydantic **does not** validate that the provided type is
Any [configuration](https://docs.pydantic.dev/latest/concepts/config/), [validation](https://docs.pydantic.dev/latest/concepts/validators/) or [serialization](https://docs.pydantic.dev/latest/concepts/serialization/) logic set on the generic model will also be applied to the parametrized classes, in the same way as when inheriting from a model class. Any custom methods or attributes will also be inherited.
Generic models also integrate properly with type checkers, so you get all the type checking you would expect if you were to declare a distinct type for each parametrization.
Note
Internally, Pydantic creates subclasses of the generic model at runtime when the generic model class is parametrized. These classes are cached, so there should be minimal overhead introduced by the use of generics models.
To inherit from a generic model and preserve the fact that it is generic, the subclass must also inherit from
```
from typing import Generic, TypeVar

from pydantic import BaseModel

TypeX = TypeVar('TypeX')


class BaseClass(BaseModel, Generic[TypeX]):
    X: TypeX


class ChildClass(BaseClass[TypeX], Generic[TypeX]):
    pass


# Parametrize `TypeX` with `int`:
print(ChildClass[int](X=1))
#> X=1

```

You can also create a generic subclass of a model that partially or fully replaces the type variables in the superclass:
```
from typing import Generic, TypeVar

from pydantic import BaseModel

TypeX = TypeVar('TypeX')
TypeY = TypeVar('TypeY')
TypeZ = TypeVar('TypeZ')


class BaseClass(BaseModel, Generic[TypeX, TypeY]):
    x: TypeX
    y: TypeY


class ChildClass(BaseClass[int, TypeY], Generic[TypeY, TypeZ]):
    z: TypeZ


# Parametrize `TypeY` with `str`:
print(ChildClass[str, int](x='1', y='y', z='3'))
#> x=1 y='y' z=3

```

If the name of the concrete subclasses is important, you can also override the default name generation by overriding the [`model_parametrized_name()`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel.model_parametrized_name) method:
```
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

DataT = TypeVar('DataT')


class Response(BaseModel, Generic[DataT]):
    data: DataT

    @classmethod
    def model_parametrized_name(cls, params: tuple[type[Any], ...]) -> str:
        return f'{params[0].__name__.title()}Response'


print(repr(Response[int](data=1)))
#> IntResponse(data=1)
print(repr(Response[str](data='a')))
#> StrResponse(data='a')

```

You can use parametrized generic models as types in other models:
```
from typing import Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class ResponseModel(BaseModel, Generic[T]):
    content: T


class Product(BaseModel):
    name: str
    price: float


class Order(BaseModel):
    id: int
    product: ResponseModel[Product]


product = Product(name='Apple', price=0.5)
response = ResponseModel[Product](content=product)
order = Order(id=1, product=response)
print(repr(order))
"""
Order(id=1, product=ResponseModel[Product](content=Product(name='Apple', price=0.5)))
"""

```

Using the same type variable in nested models allows you to enforce typing relationships at different points in your model:
```
from typing import Generic, TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar('T')


class InnerT(BaseModel, Generic[T]):
    inner: T


class OuterT(BaseModel, Generic[T]):
    outer: T
    nested: InnerT[T]


nested = InnerT[int](inner=1)
print(OuterT[int](outer=1, nested=nested))
#> outer=1 nested=InnerT[int](inner=1)
try:
    print(OuterT[int](outer='a', nested=InnerT(inner='a')))  [](https://docs.pydantic.dev/latest/concepts/models/#__code_26_annotation_1)
except ValidationError as e:
    print(e)
    """
    2 validation errors for OuterT[int]
    outer
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    nested.inner
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    """

```

Warning
While it may not raise an error, we strongly advise against using parametrized generics in
For example, you should not do `isinstance(my_model, MyGenericModel[int])`. However, it is fine to do `isinstance(my_model, MyGenericModel)` (note that, for standard generics, it would raise an error to do a subclass check with a parameterized generic class).
If you need to perform
```
class MyIntModel(MyGenericModel[int]): ...

isinstance(my_model, MyIntModel)

```

Implementation Details
When using nested generic models, Pydantic sometimes performs revalidation in an attempt to produce the most intuitive validation result. Specifically, if you have a field of type `GenericModel[SomeType]` and you validate data like `GenericModel[SomeCompatibleType]` against this field, we will inspect the data, recognize that the input data is sort of a "loose" subclass of `GenericModel`, and revalidate the contained `SomeCompatibleType` data.
This adds some validation overhead, but makes things more intuitive for cases like that shown below.
```
from typing import Any, Generic, TypeVar

from pydantic import BaseModel

T = TypeVar('T')


class GenericModel(BaseModel, Generic[T]):
    a: T


class Model(BaseModel):
    inner: GenericModel[Any]


print(repr(Model.model_validate(Model(inner=GenericModel[int](a=1)))))
#> Model(inner=GenericModel[Any](a=1))

```

Note, validation will still fail if you, for example are validating against `GenericModel[int]` and pass in an instance `GenericModel[str](a='not an int')`.
It's also worth noting that this pattern will re-trigger any custom validation as well, like additional model validators and the like. Validators will be called once on the first pass, validating directly against `GenericModel[Any]`. That validation fails, as `GenericModel[int]` is not a subclass of `GenericModel[Any]`. This relates to the warning above about the complications of using parametrized generics in `isinstance()` and `issubclass()` checks. Then, the validators will be called again on the second pass, during more lax force-revalidation phase, which succeeds. To better understand this consequence, see below:
```
from typing import Any, Generic, Self, TypeVar

from pydantic import BaseModel, model_validator

T = TypeVar('T')


class GenericModel(BaseModel, Generic[T]):
    a: T

    @model_validator(mode='after')
    def validate_after(self: Self) -> Self:
        print('after validator running custom validation...')
        return self


class Model(BaseModel):
    inner: GenericModel[Any]


m = Model.model_validate(Model(inner=GenericModel[int](a=1)))
#> after validator running custom validation...
#> after validator running custom validation...
print(repr(m))
#> Model(inner=GenericModel[Any](a=1))

```

### Validation of unparametrized type variables[¶](https://docs.pydantic.dev/latest/concepts/models/#validation-of-unparametrized-type-variables)
When leaving type variables unparametrized, Pydantic treats generic models similarly to how it treats built-in generic types like
  * If the type variable is
  * If the type variable has a default type (as specified by
  * For unbound or unconstrained type variables, Pydantic will fallback to


```
from typing import Generic

from typing_extensions import TypeVar

from pydantic import BaseModel, ValidationError

T = TypeVar('T')
U = TypeVar('U', bound=int)
V = TypeVar('V', default=str)


class Model(BaseModel, Generic[T, U, V]):
    t: T
    u: U
    v: V


print(Model(t='t', u=1, v='v'))
#> t='t' u=1 v='v'

try:
    Model(t='t', u='u', v=1)
except ValidationError as exc:
    print(exc)
    """
    2 validation errors for Model
    u
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='u', input_type=str]
    v
      Input should be a valid string [type=string_type, input_value=1, input_type=int]
    """

```

Warning
In some cases, validation against an unparametrized generic model can lead to data loss. Specifically, if a subtype of the type variable upper bound, constraints, or default is being used and the model isn't explicitly parametrized, the resulting type **will not be** the one being provided:
```
from typing import Generic, TypeVar

from pydantic import BaseModel

ItemT = TypeVar('ItemT', bound='ItemBase')


class ItemBase(BaseModel): ...


class IntItem(ItemBase):
    value: int


class ItemHolder(BaseModel, Generic[ItemT]):
    item: ItemT


loaded_data = {'item': {'value': 1}}


print(ItemHolder(**loaded_data))  [](https://docs.pydantic.dev/latest/concepts/models/#__code_31_annotation_1)
#> item=ItemBase()

print(ItemHolder[IntItem](**loaded_data))  [](https://docs.pydantic.dev/latest/concepts/models/#__code_31_annotation_2)
#> item=IntItem(value=1)

```

### Serialization of unparametrized type variables[¶](https://docs.pydantic.dev/latest/concepts/models/#serialization-of-unparametrized-type-variables)
The behavior of serialization differs when using type variables with
If a Pydantic model is used in a type variable upper bound and the type variable is never parametrized, then Pydantic will use the upper bound for validation but treat the value as
```
from typing import Generic, TypeVar

from pydantic import BaseModel


class ErrorDetails(BaseModel):
    foo: str


ErrorDataT = TypeVar('ErrorDataT', bound=ErrorDetails)


class Error(BaseModel, Generic[ErrorDataT]):
    message: str
    details: ErrorDataT


class MyErrorDetails(ErrorDetails):
    bar: str


# serialized as Any
error = Error(
    message='We just had an error',
    details=MyErrorDetails(foo='var', bar='var2'),
)
assert error.model_dump() == {
    'message': 'We just had an error',
    'details': {
        'foo': 'var',
        'bar': 'var2',
    },
}

# serialized using the concrete parametrization
# note that `'bar': 'var2'` is missing
error = Error[ErrorDetails](
    message='We just had an error',
    details=ErrorDetails(foo='var'),
)
assert error.model_dump() == {
    'message': 'We just had an error',
    'details': {
        'foo': 'var',
    },
}

```

Here's another example of the above behavior, enumerating all permutations regarding bound specification and generic type parametrization:
```
from typing import Generic, TypeVar

from pydantic import BaseModel

TBound = TypeVar('TBound', bound=BaseModel)
TNoBound = TypeVar('TNoBound')


class IntValue(BaseModel):
    value: int


class ItemBound(BaseModel, Generic[TBound]):
    item: TBound


class ItemNoBound(BaseModel, Generic[TNoBound]):
    item: TNoBound


item_bound_inferred = ItemBound(item=IntValue(value=3))
item_bound_explicit = ItemBound[IntValue](item=IntValue(value=3))
item_no_bound_inferred = ItemNoBound(item=IntValue(value=3))
item_no_bound_explicit = ItemNoBound[IntValue](item=IntValue(value=3))

# calling `print(x.model_dump())` on any of the above instances results in the following:
#> {'item': {'value': 3}}

```

However, if [`SerializeAsAny`](https://docs.pydantic.dev/latest/concepts/serialization/#serializeasany-annotation):
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/models/#__tabbed_4_1)[Python 3.13 and above](https://docs.pydantic.dev/latest/concepts/models/#__tabbed_4_2)
```
from typing import Generic

from typing_extensions import TypeVar

from pydantic import BaseModel, SerializeAsAny


class ErrorDetails(BaseModel):
    foo: str


ErrorDataT = TypeVar('ErrorDataT', default=ErrorDetails)


class Error(BaseModel, Generic[ErrorDataT]):
    message: str
    details: ErrorDataT


class MyErrorDetails(ErrorDetails):
    bar: str


# serialized using the default's serializer
error = Error(
    message='We just had an error',
    details=MyErrorDetails(foo='var', bar='var2'),
)
assert error.model_dump() == {
    'message': 'We just had an error',
    'details': {
        'foo': 'var',
    },
}
# If `ErrorDataT` was using an upper bound, `bar` would be present in `details`.


class SerializeAsAnyError(BaseModel, Generic[ErrorDataT]):
    message: str
    details: SerializeAsAny[ErrorDataT]


# serialized as Any
error = SerializeAsAnyError(
    message='We just had an error',
    details=MyErrorDetails(foo='var', bar='baz'),
)
assert error.model_dump() == {
    'message': 'We just had an error',
    'details': {
        'foo': 'var',
        'bar': 'baz',
    },
}

```

```
from typing import Generic

from typing import TypeVar

from pydantic import BaseModel, SerializeAsAny


class ErrorDetails(BaseModel):
    foo: str


ErrorDataT = TypeVar('ErrorDataT', default=ErrorDetails)


class Error(BaseModel, Generic[ErrorDataT]):
    message: str
    details: ErrorDataT


class MyErrorDetails(ErrorDetails):
    bar: str


# serialized using the default's serializer
error = Error(
    message='We just had an error',
    details=MyErrorDetails(foo='var', bar='var2'),
)
assert error.model_dump() == {
    'message': 'We just had an error',
    'details': {
        'foo': 'var',
    },
}
# If `ErrorDataT` was using an upper bound, `bar` would be present in `details`.


class SerializeAsAnyError(BaseModel, Generic[ErrorDataT]):
    message: str
    details: SerializeAsAny[ErrorDataT]


# serialized as Any
error = SerializeAsAnyError(
    message='We just had an error',
    details=MyErrorDetails(foo='var', bar='baz'),
)
assert error.model_dump() == {
    'message': 'We just had an error',
    'details': {
        'foo': 'var',
        'bar': 'baz',
    },
}

```
