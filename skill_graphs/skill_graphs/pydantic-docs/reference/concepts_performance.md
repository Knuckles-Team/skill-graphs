[ Skip to content ](https://docs.pydantic.dev/latest/concepts/performance/#performance-tips)
What's new — we've launched [Pydantic Logfire](https://pydantic.dev/articles/logfire-announcement) ![🔥](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.0.3/assets/svg/1f525.svg) to help you monitor and understand your [FastAPI app.](https://logfire.pydantic.dev/docs/integrations/fastapi/)
[ ![logo](https://docs.pydantic.dev/latest/logo-white.svg) ](https://docs.pydantic.dev/latest/ "Pydantic Validation")
Pydantic Validation
2.12
  * [dev](https://docs.pydantic.dev/dev/)
  * [2.12](https://docs.pydantic.dev/2.12/)
  * [2.11](https://docs.pydantic.dev/2.11/)
  * [2.10](https://docs.pydantic.dev/2.10/)
  * [2.9](https://docs.pydantic.dev/2.9/)
  * [2.8](https://docs.pydantic.dev/2.8/)
  * [2.7](https://docs.pydantic.dev/2.7/)
  * [2.6](https://docs.pydantic.dev/2.6/)
  * [2.5](https://docs.pydantic.dev/2.5/)
  * [2.4](https://docs.pydantic.dev/2.4/)
  * [2.3](https://docs.pydantic.dev/2.3/)
  * [2.2](https://docs.pydantic.dev/2.2/)
  * [2.1](https://docs.pydantic.dev/2.1/)
  * [2.0](https://docs.pydantic.dev/2.0/)
  * [1.10](https://docs.pydantic.dev/1.10/)


Performance
Type to start searching
  * [ Get Started ](https://docs.pydantic.dev/latest/)
  * [ Concepts ](https://docs.pydantic.dev/latest/concepts/models/)
  * [ API Documentation ](https://docs.pydantic.dev/latest/api/base_model/)
  * [ Internals ](https://docs.pydantic.dev/latest/internals/architecture/)
  * [ Examples ](https://docs.pydantic.dev/latest/examples/files/)
  * [ Error Messages ](https://docs.pydantic.dev/latest/errors/errors/)
  * [ Integrations ](https://docs.pydantic.dev/latest/integrations/logfire/)
  * [ Blog ](https://blog.pydantic.dev/)
  * [ Pydantic People ](https://docs.pydantic.dev/latest/pydantic_people/)


[ ![logo](https://docs.pydantic.dev/latest/logo-white.svg) ](https://docs.pydantic.dev/latest/ "Pydantic Validation") Pydantic Validation
  * Get Started
    * [ Welcome to Pydantic  ](https://docs.pydantic.dev/latest/)
    * [ Why use Pydantic  ](https://docs.pydantic.dev/latest/why/)
    * [ Help with Pydantic  ](https://docs.pydantic.dev/latest/help_with_pydantic/)
    * [ Installation  ](https://docs.pydantic.dev/latest/install/)
    * [ Migration Guide  ](https://docs.pydantic.dev/latest/migration/)
    * [ Version Policy  ](https://docs.pydantic.dev/latest/version-policy/)
    * [ Contributing  ](https://docs.pydantic.dev/latest/contributing/)
    * [ Changelog  ](https://docs.pydantic.dev/latest/changelog/)
  * Concepts
    * [ Models  ](https://docs.pydantic.dev/latest/concepts/models/)
    * [ Fields  ](https://docs.pydantic.dev/latest/concepts/fields/)
    * [ JSON Schema  ](https://docs.pydantic.dev/latest/concepts/json_schema/)
    * [ JSON  ](https://docs.pydantic.dev/latest/concepts/json/)
    * [ Types  ](https://docs.pydantic.dev/latest/concepts/types/)
    * [ Unions  ](https://docs.pydantic.dev/latest/concepts/unions/)
    * [ Alias  ](https://docs.pydantic.dev/latest/concepts/alias/)
    * [ Configuration  ](https://docs.pydantic.dev/latest/concepts/config/)
    * [ Serialization  ](https://docs.pydantic.dev/latest/concepts/serialization/)
    * [ Validators  ](https://docs.pydantic.dev/latest/concepts/validators/)
    * [ Dataclasses  ](https://docs.pydantic.dev/latest/concepts/dataclasses/)
    * [ Forward Annotations  ](https://docs.pydantic.dev/latest/concepts/forward_annotations/)
    * [ Strict Mode  ](https://docs.pydantic.dev/latest/concepts/strict_mode/)
    * [ Type Adapter  ](https://docs.pydantic.dev/latest/concepts/type_adapter/)
    * [ Validation Decorator  ](https://docs.pydantic.dev/latest/concepts/validation_decorator/)
    * [ Conversion Table  ](https://docs.pydantic.dev/latest/concepts/conversion_table/)
    * [ Settings Management  ](https://docs.pydantic.dev/latest/concepts/pydantic_settings/)
    * Performance  [ Performance  ](https://docs.pydantic.dev/latest/concepts/performance/)
      * [ In general, use model_validate_json() not model_validate(json.loads(...))  ](https://docs.pydantic.dev/latest/concepts/performance/#in-general-use-model_validate_json-not-model_validatejsonloads)
      * [ TypeAdapter instantiated once  ](https://docs.pydantic.dev/latest/concepts/performance/#typeadapter-instantiated-once)
      * [ Sequence vs list or tuple with Mapping vs dict  ](https://docs.pydantic.dev/latest/concepts/performance/#sequence-vs-list-or-tuple-with-mapping-vs-dict)
      * [ Don't do validation when you don't have to, use Any to keep the value unchanged  ](https://docs.pydantic.dev/latest/concepts/performance/#dont-do-validation-when-you-dont-have-to-use-any-to-keep-the-value-unchanged)
      * [ Avoid extra information via subclasses of primitives  ](https://docs.pydantic.dev/latest/concepts/performance/#avoid-extra-information-via-subclasses-of-primitives)
      * [ Use tagged union, not union  ](https://docs.pydantic.dev/latest/concepts/performance/#use-tagged-union-not-union)
      * [ Use TypedDict over nested models  ](https://docs.pydantic.dev/latest/concepts/performance/#use-typeddict-over-nested-models)
      * [ Avoid wrap validators if you really care about performance  ](https://docs.pydantic.dev/latest/concepts/performance/#avoid-wrap-validators-if-you-really-care-about-performance)
      * [ Failing early with FailFast  ](https://docs.pydantic.dev/latest/concepts/performance/#failing-early-with-failfast)
    * [ Experimental  ](https://docs.pydantic.dev/latest/concepts/experimental/)
  * API Documentation
    * Pydantic
      * [ BaseModel  ](https://docs.pydantic.dev/latest/api/base_model/)
      * [ RootModel  ](https://docs.pydantic.dev/latest/api/root_model/)
      * [ Pydantic Dataclasses  ](https://docs.pydantic.dev/latest/api/dataclasses/)
      * [ TypeAdapter  ](https://docs.pydantic.dev/latest/api/type_adapter/)
      * [ Validate Call  ](https://docs.pydantic.dev/latest/api/validate_call/)
      * [ Fields  ](https://docs.pydantic.dev/latest/api/fields/)
      * [ Aliases  ](https://docs.pydantic.dev/latest/api/aliases/)
      * [ Configuration  ](https://docs.pydantic.dev/latest/api/config/)
      * [ JSON Schema  ](https://docs.pydantic.dev/latest/api/json_schema/)
      * [ Errors  ](https://docs.pydantic.dev/latest/api/errors/)
      * [ Functional Validators  ](https://docs.pydantic.dev/latest/api/functional_validators/)
      * [ Functional Serializers  ](https://docs.pydantic.dev/latest/api/functional_serializers/)
      * [ Standard Library Types  ](https://docs.pydantic.dev/latest/api/standard_library_types/)
      * [ Pydantic Types  ](https://docs.pydantic.dev/latest/api/types/)
      * [ Network Types  ](https://docs.pydantic.dev/latest/api/networks/)
      * [ Version Information  ](https://docs.pydantic.dev/latest/api/version/)
      * [ Annotated Handlers  ](https://docs.pydantic.dev/latest/api/annotated_handlers/)
      * [ Experimental  ](https://docs.pydantic.dev/latest/api/experimental/)
    * Pydantic Core
      * [ pydantic_core  ](https://docs.pydantic.dev/latest/api/pydantic_core/)
      * [ pydantic_core.core_schema  ](https://docs.pydantic.dev/latest/api/pydantic_core_schema/)
    * [ Pydantic Settings  ](https://docs.pydantic.dev/latest/api/pydantic_settings/)
    * Pydantic Extra Types
      * [ Color  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_color/)
      * [ Country  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_country/)
      * [ Payment  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_payment/)
      * [ Phone Numbers  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_phone_numbers/)
      * [ Routing Numbers  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_routing_numbers/)
      * [ Coordinate  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_coordinate/)
      * [ Mac Address  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_mac_address/)
      * [ ISBN  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_isbn/)
      * [ Pendulum  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_pendulum_dt/)
      * [ Currency  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_currency_code/)
      * [ Language  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_language_code/)
      * [ Script Code  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_script_code/)
      * [ Semantic Version  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_semantic_version/)
      * [ Timezone Name  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_timezone_name/)
      * [ ULID  ](https://docs.pydantic.dev/latest/api/pydantic_extra_types_ulid/)
  * Internals
    * [ Architecture  ](https://docs.pydantic.dev/latest/internals/architecture/)
    * [ Resolving Annotations  ](https://docs.pydantic.dev/latest/internals/resolving_annotations/)
  * Examples
    * [ Validating File Data  ](https://docs.pydantic.dev/latest/examples/files/)
    * [ Web and API Requests  ](https://docs.pydantic.dev/latest/examples/requests/)
    * [ Queues  ](https://docs.pydantic.dev/latest/examples/queues/)
    * [ Databases  ](https://docs.pydantic.dev/latest/examples/orms/)
    * [ Custom Validators  ](https://docs.pydantic.dev/latest/examples/custom_validators/)
    * [ Dynamic models  ](https://docs.pydantic.dev/latest/examples/dynamic_models/)
  * Error Messages
    * [ Error Handling  ](https://docs.pydantic.dev/latest/errors/errors/)
    * [ Validation Errors  ](https://docs.pydantic.dev/latest/errors/validation_errors/)
    * [ Usage Errors  ](https://docs.pydantic.dev/latest/errors/usage_errors/)
  * Integrations
    * [ Pydantic Logfire  ](https://docs.pydantic.dev/latest/integrations/logfire/)
    * [ LLMs  ](https://docs.pydantic.dev/latest/integrations/llms/)
    * Dev Tools
      * [ Mypy  ](https://docs.pydantic.dev/latest/integrations/mypy/)
      * [ Pyrefly  ](https://docs.pydantic.dev/latest/integrations/pyrefly/)
      * [ PyCharm  ](https://docs.pydantic.dev/latest/integrations/pycharm/)
      * [ Hypothesis  ](https://docs.pydantic.dev/latest/integrations/hypothesis/)
      * [ Visual Studio Code  ](https://docs.pydantic.dev/latest/integrations/visual_studio_code/)
      * [ datamodel-code-generator  ](https://docs.pydantic.dev/latest/integrations/datamodel_code_generator/)
      * [ devtools  ](https://docs.pydantic.dev/latest/integrations/devtools/)
      * [ Rich  ](https://docs.pydantic.dev/latest/integrations/rich/)
      * [ Linting  ](https://docs.pydantic.dev/latest/integrations/linting/)
      * [ Documentation  ](https://docs.pydantic.dev/latest/integrations/documentation/)
    * Production Tools
      * [ AWS Lambda  ](https://docs.pydantic.dev/latest/integrations/aws_lambda/)
  * [ Blog  ](https://blog.pydantic.dev/)
  * [ Pydantic People  ](https://docs.pydantic.dev/latest/pydantic_people/)


  * [ In general, use model_validate_json() not model_validate(json.loads(...))  ](https://docs.pydantic.dev/latest/concepts/performance/#in-general-use-model_validate_json-not-model_validatejsonloads)
  * [ TypeAdapter instantiated once  ](https://docs.pydantic.dev/latest/concepts/performance/#typeadapter-instantiated-once)
  * [ Sequence vs list or tuple with Mapping vs dict  ](https://docs.pydantic.dev/latest/concepts/performance/#sequence-vs-list-or-tuple-with-mapping-vs-dict)
  * [ Don't do validation when you don't have to, use Any to keep the value unchanged  ](https://docs.pydantic.dev/latest/concepts/performance/#dont-do-validation-when-you-dont-have-to-use-any-to-keep-the-value-unchanged)
  * [ Avoid extra information via subclasses of primitives  ](https://docs.pydantic.dev/latest/concepts/performance/#avoid-extra-information-via-subclasses-of-primitives)
  * [ Use tagged union, not union  ](https://docs.pydantic.dev/latest/concepts/performance/#use-tagged-union-not-union)
  * [ Use TypedDict over nested models  ](https://docs.pydantic.dev/latest/concepts/performance/#use-typeddict-over-nested-models)
  * [ Avoid wrap validators if you really care about performance  ](https://docs.pydantic.dev/latest/concepts/performance/#avoid-wrap-validators-if-you-really-care-about-performance)
  * [ Failing early with FailFast  ](https://docs.pydantic.dev/latest/concepts/performance/#failing-early-with-failfast)


# Performance tips[¶](https://docs.pydantic.dev/latest/concepts/performance/#performance-tips)
In most cases Pydantic won't be your bottle neck, only follow this if you're sure it's necessary.
## In general, use `model_validate_json()` not `model_validate(json.loads(...))`[¶](https://docs.pydantic.dev/latest/concepts/performance/#in-general-use-model_validate_json-not-model_validatejsonloads)
On `model_validate(json.loads(...))`, the JSON is parsed in Python, then converted to a dict, then it's validated internally. On the other hand, `model_validate_json()` already performs the validation internally.
There are a few cases where `model_validate(json.loads(...))` may be faster. Specifically, when using a `'before'` or `'wrap'` validator on a model, validation may be faster with the two step method. You can read more about these special cases in
Many performance improvements are currently in the works for `pydantic-core`, see `model_validate_json()` is always faster than `model_validate(json.loads(...))`.
##  `TypeAdapter` instantiated once[¶](https://docs.pydantic.dev/latest/concepts/performance/#typeadapter-instantiated-once)
The idea here is to avoid constructing validators and serializers more than necessary. Each time a `TypeAdapter` is instantiated, it will construct a new validator and serializer. If you're using a `TypeAdapter` in a function, it will be instantiated each time the function is called. Instead, instantiate it once, and reuse it.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Bad](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Good](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_1_2)
```
from pydantic import TypeAdapter


def my_func():
    adapter = TypeAdapter(list[int])
    # do something with adapter

```

```
from pydantic import TypeAdapter

adapter = TypeAdapter(list[int])

def my_func():
    ...
    # do something with adapter

```

##  `Sequence` vs `list` or `tuple` with `Mapping` vs `dict`[¶](https://docs.pydantic.dev/latest/concepts/performance/#sequence-vs-list-or-tuple-with-mapping-vs-dict)
When using `Sequence`, Pydantic calls `isinstance(value, Sequence)` to check if the value is a sequence. Also, Pydantic will try to validate against different types of sequences, like `list` and `tuple`. If you know the value is a `list` or `tuple`, use `list` or `tuple` instead of `Sequence`.
The same applies to `Mapping` and `dict`. If you know the value is a `dict`, use `dict` instead of `Mapping`.
## Don't do validation when you don't have to, use `Any` to keep the value unchanged[¶](https://docs.pydantic.dev/latest/concepts/performance/#dont-do-validation-when-you-dont-have-to-use-any-to-keep-the-value-unchanged)
If you don't need to validate a value, use `Any` to keep the value unchanged.
```
from typing import Any

from pydantic import BaseModel


class Model(BaseModel):
    a: Any


model = Model(a=1)

```

## Avoid extra information via subclasses of primitives[¶](https://docs.pydantic.dev/latest/concepts/performance/#avoid-extra-information-via-subclasses-of-primitives)
[Don't do this](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_2_1)[Do this](https://docs.pydantic.dev/latest/concepts/performance/#__tabbed_2_2)
```
class CompletedStr(str):
    def __init__(self, s: str):
        self.s = s
        self.done = False

```

```
from pydantic import BaseModel


class CompletedModel(BaseModel):
    s: str
    done: bool = False

```

## Use tagged union, not union[¶](https://docs.pydantic.dev/latest/concepts/performance/#use-tagged-union-not-union)
Tagged union (or discriminated union) is a union with a field that indicates which type it is.
```
from typing import Any, Literal

from pydantic import BaseModel, Field


class DivModel(BaseModel):
    el_type: Literal['div'] = 'div'
    class_name: str | None = None
    children: list[Any] | None = None


class SpanModel(BaseModel):
    el_type: Literal['span'] = 'span'
    class_name: str | None = None
    contents: str | None = None


class ButtonModel(BaseModel):
    el_type: Literal['button'] = 'button'
    class_name: str | None = None
    contents: str | None = None


class InputModel(BaseModel):
    el_type: Literal['input'] = 'input'
    class_name: str | None = None
    value: str | None = None


class Html(BaseModel):
    contents: DivModel | SpanModel | ButtonModel | InputModel = Field(
        discriminator='el_type'
    )

```

See [Discriminated Unions](https://docs.pydantic.dev/latest/concepts/unions/#discriminated-unions) for more details.
## Use `TypedDict` over nested models[¶](https://docs.pydantic.dev/latest/concepts/performance/#use-typeddict-over-nested-models)
Instead of using nested models, use `TypedDict` to define the structure of the data.
Performance comparison
With a simple benchmark, `TypedDict` is about ~2.5x faster than nested models:
```
from timeit import timeit

from typing_extensions import TypedDict

from pydantic import BaseModel, TypeAdapter


class A(TypedDict):
    a: str
    b: int


class TypedModel(TypedDict):
    a: A


class B(BaseModel):
    a: str
    b: int


class Model(BaseModel):
    b: B


ta = TypeAdapter(TypedModel)
result1 = timeit(
    lambda: ta.validate_python({'a': {'a': 'a', 'b': 2}}), number=10000
)
result2 = timeit(
    lambda: Model.model_validate({'b': {'a': 'a', 'b': 2}}), number=10000
)
print(result2 / result1)

```

## Avoid wrap validators if you really care about performance[¶](https://docs.pydantic.dev/latest/concepts/performance/#avoid-wrap-validators-if-you-really-care-about-performance)
Wrap validators are generally slower than other validators. This is because they require that data is materialized in Python during validation. Wrap validators can be incredibly useful for complex validation logic, but if you're looking for the best performance, you should avoid them.
## Failing early with `FailFast`[¶](https://docs.pydantic.dev/latest/concepts/performance/#failing-early-with-failfast)
Starting in v2.8+, you can apply the `FailFast` annotation to sequence types to fail early if any item in the sequence fails validation. If you use this annotation, you won't get validation errors for the rest of the items in the sequence if one fails, so you're effectively trading off visibility for performance.
```
from typing import Annotated

from pydantic import FailFast, TypeAdapter, ValidationError

ta = TypeAdapter(Annotated[list[bool], FailFast()])
try:
    ta.validate_python([True, 'invalid', False, 'also invalid'])
except ValidationError as exc:
    print(exc)
    """
    1 validation error for list[bool]
    1
      Input should be a valid boolean, unable to interpret input [type=bool_parsing, input_value='invalid', input_type=str]
    """

```

Read more about `FailFast` [here](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FailFast).
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
