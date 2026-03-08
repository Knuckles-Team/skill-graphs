[ Skip to content ](https://docs.pydantic.dev/latest/concepts/experimental/#experimental-features)
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


Experimental
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
    * [ Performance  ](https://docs.pydantic.dev/latest/concepts/performance/)
    * Experimental  [ Experimental  ](https://docs.pydantic.dev/latest/concepts/experimental/)
      * [ Feedback  ](https://docs.pydantic.dev/latest/concepts/experimental/#feedback)
      * [ Pipeline API  ](https://docs.pydantic.dev/latest/concepts/experimental/#pipeline-api)
        * [ Mapping from BeforeValidator, AfterValidator and WrapValidator  ](https://docs.pydantic.dev/latest/concepts/experimental/#mapping-from-beforevalidator-aftervalidator-and-wrapvalidator)
        * [ Alternative patterns  ](https://docs.pydantic.dev/latest/concepts/experimental/#alternative-patterns)
      * [ Partial Validation  ](https://docs.pydantic.dev/latest/concepts/experimental/#partial-validation)
        * [ How Partial Validation Works  ](https://docs.pydantic.dev/latest/concepts/experimental/#how-partial-validation-works)
          * [ 1. Partial JSON parsing  ](https://docs.pydantic.dev/latest/concepts/experimental/#1-partial-json-parsing)
          * [ 2. Ignore errors in the last element of the input  ](https://docs.pydantic.dev/latest/concepts/experimental/#2-ignore-errors-in-last)
        * [ Limitations of Partial Validation  ](https://docs.pydantic.dev/latest/concepts/experimental/#limitations-of-partial-validation)
          * [ TypeAdapter only  ](https://docs.pydantic.dev/latest/concepts/experimental/#typeadapter-only)
          * [ Types supported  ](https://docs.pydantic.dev/latest/concepts/experimental/#types-supported)
          * [ Some invalid but complete JSON will be accepted  ](https://docs.pydantic.dev/latest/concepts/experimental/#some-invalid-but-complete-json-will-be-accepted)
          * [ Any error in the last field of the input will be ignored  ](https://docs.pydantic.dev/latest/concepts/experimental/#any-error-in-the-last-field-of-the-input-will-be-ignored)
      * [ Validation of a callable's arguments  ](https://docs.pydantic.dev/latest/concepts/experimental/#validation-of-a-callables-arguments)
      * [ MISSING sentinel  ](https://docs.pydantic.dev/latest/concepts/experimental/#missing-sentinel)
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


  * [ Feedback  ](https://docs.pydantic.dev/latest/concepts/experimental/#feedback)
  * [ Pipeline API  ](https://docs.pydantic.dev/latest/concepts/experimental/#pipeline-api)
    * [ Mapping from BeforeValidator, AfterValidator and WrapValidator  ](https://docs.pydantic.dev/latest/concepts/experimental/#mapping-from-beforevalidator-aftervalidator-and-wrapvalidator)
    * [ Alternative patterns  ](https://docs.pydantic.dev/latest/concepts/experimental/#alternative-patterns)
  * [ Partial Validation  ](https://docs.pydantic.dev/latest/concepts/experimental/#partial-validation)
    * [ How Partial Validation Works  ](https://docs.pydantic.dev/latest/concepts/experimental/#how-partial-validation-works)
      * [ 1. Partial JSON parsing  ](https://docs.pydantic.dev/latest/concepts/experimental/#1-partial-json-parsing)
      * [ 2. Ignore errors in the last element of the input  ](https://docs.pydantic.dev/latest/concepts/experimental/#2-ignore-errors-in-last)
    * [ Limitations of Partial Validation  ](https://docs.pydantic.dev/latest/concepts/experimental/#limitations-of-partial-validation)
      * [ TypeAdapter only  ](https://docs.pydantic.dev/latest/concepts/experimental/#typeadapter-only)
      * [ Types supported  ](https://docs.pydantic.dev/latest/concepts/experimental/#types-supported)
      * [ Some invalid but complete JSON will be accepted  ](https://docs.pydantic.dev/latest/concepts/experimental/#some-invalid-but-complete-json-will-be-accepted)
      * [ Any error in the last field of the input will be ignored  ](https://docs.pydantic.dev/latest/concepts/experimental/#any-error-in-the-last-field-of-the-input-will-be-ignored)
  * [ Validation of a callable's arguments  ](https://docs.pydantic.dev/latest/concepts/experimental/#validation-of-a-callables-arguments)
  * [ MISSING sentinel  ](https://docs.pydantic.dev/latest/concepts/experimental/#missing-sentinel)


# Experimental Features[¶](https://docs.pydantic.dev/latest/concepts/experimental/#experimental-features)
In this section you will find documentation for new, experimental features in Pydantic. These features are subject to change or removal, and we are looking for feedback and suggestions before making them a permanent part of Pydantic.
See our [Version Policy](https://docs.pydantic.dev/latest/version-policy/#experimental-features) for more information on experimental features.
## Feedback[¶](https://docs.pydantic.dev/latest/concepts/experimental/#feedback)
We welcome feedback on experimental features! Please open an issue on the
We also encourage you to read through existing feedback and add your thoughts to existing issues.
## Pipeline API[¶](https://docs.pydantic.dev/latest/concepts/experimental/#pipeline-api)
Pydantic v2.8.0 introduced an experimental "pipeline" API that allows composing of parsing (validation), constraints and transformations in a more type-safe manner than existing APIs. This API is subject to change or removal, we are looking for feedback and suggestions before making it a permanent part of Pydantic.
API Documentation
[`pydantic.experimental.pipeline`](https://docs.pydantic.dev/latest/api/experimental/#pydantic.experimental.pipeline)

Generally, the pipeline API is used to define a sequence of steps to apply to incoming data during validation. The pipeline API is designed to be more type-safe and composable than the existing Pydantic API.
Each step in the pipeline can be:
  * A validation step that runs pydantic validation on the provided type
  * A transformation step that modifies the data
  * A constraint step that checks the data against a condition
  * A predicate step that checks the data against a condition and raises an error if it returns `False`


Note that the following example attempts to be exhaustive at the cost of complexity: if you find yourself writing this many transformations in type annotations you may want to consider having a `UserIn` and `UserOut` model (example below) or similar where you make the transformations via idiomatic plain Python code. These APIs are meant for situations where the code savings are significant and the added complexity is relatively small.
```
from __future__ import annotations

from datetime import datetime
from typing import Annotated

from pydantic import BaseModel
from pydantic.experimental.pipeline import validate_as


class User(BaseModel):
    name: Annotated[str, validate_as(str).str_lower()]  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_0_annotation_1)
    age: Annotated[int, validate_as(int).gt(0)]  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_0_annotation_2)
    username: Annotated[str, validate_as(str).str_pattern(r'[a-z]+')]  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_0_annotation_3)
    password: Annotated[
        str,
        validate_as(str)
        .transform(str.lower)
        .predicate(lambda x: x != 'password'),  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_0_annotation_4)
    ]
    favorite_number: Annotated[  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_0_annotation_5)
        int,
        (validate_as(int) | validate_as(str).str_strip().validate_as(int)).gt(
            0
        ),
    ]
    friends: Annotated[list[User], validate_as(...).len(0, 100)]  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_0_annotation_6)
    bio: Annotated[
        datetime,
        validate_as(int)
        .transform(lambda x: x / 1_000_000)
        .validate_as(...),  (8)
    ]

```

  1. You can call `validate_as()` before or after other steps to do pre or post processing.


### Mapping from `BeforeValidator`, `AfterValidator` and `WrapValidator`[¶](https://docs.pydantic.dev/latest/concepts/experimental/#mapping-from-beforevalidator-aftervalidator-and-wrapvalidator)
The `validate_as` method is a more type-safe way to define `BeforeValidator`, `AfterValidator` and `WrapValidator`:
```
from typing import Annotated

from pydantic.experimental.pipeline import transform, validate_as

# BeforeValidator
Annotated[int, validate_as(str).str_strip().validate_as(...)]  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_1_annotation_1)
# AfterValidator
Annotated[int, transform(lambda x: x * 2)]  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_1_annotation_2)
# WrapValidator
Annotated[
    int,
    validate_as(str)
    .str_strip()
    .validate_as(...)
    .transform(lambda x: x * 2),  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_1_annotation_3)
]

```

### Alternative patterns[¶](https://docs.pydantic.dev/latest/concepts/experimental/#alternative-patterns)
There are many alternative patterns to use depending on the scenario. Just as an example, consider the `UserIn` and `UserOut` pattern mentioned above:
```
from __future__ import annotations

from pydantic import BaseModel


class UserIn(BaseModel):
    favorite_number: int | str


class UserOut(BaseModel):
    favorite_number: int


def my_api(user: UserIn) -> UserOut:
    favorite_number = user.favorite_number
    if isinstance(favorite_number, str):
        favorite_number = int(user.favorite_number.strip())

    return UserOut(favorite_number=favorite_number)


assert my_api(UserIn(favorite_number=' 1 ')).favorite_number == 1

```

This example uses plain idiomatic Python code that may be easier to understand, type-check, etc. than the examples above. The approach you choose should really depend on your use case. You will have to compare verbosity, performance, ease of returning meaningful errors to your users, etc. to choose the right pattern. Just be mindful of abusing advanced patterns like the pipeline API just because you can.
## Partial Validation[¶](https://docs.pydantic.dev/latest/concepts/experimental/#partial-validation)
Pydantic v2.10.0 introduces experimental support for "partial validation".
This allows you to validate an incomplete JSON string, or a Python object representing incomplete input data.
Partial validation is particularly helpful when processing the output of an LLM, where the model streams structured responses, and you may wish to begin validating the stream while you're still receiving data (e.g. to show partial data to users).
Warning
Partial validation is an experimental feature and may change in future versions of Pydantic. The current implementation should be considered a proof of concept at this time and has a number of [limitations](https://docs.pydantic.dev/latest/concepts/experimental/#limitations-of-partial-validation).
Partial validation can be enabled when using the three validation methods on `TypeAdapter`: [`TypeAdapter.validate_json()`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_json), [`TypeAdapter.validate_python()`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_python), and [`TypeAdapter.validate_strings()`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter.validate_strings). This allows you to parse and validation incomplete JSON, but also to validate Python objects created by parsing incomplete data of any format.
The `experimental_allow_partial` flag can be passed to these methods to enable partial validation. It can take the following values (and is `False`, by default):
  * `False` or `'off'` - disable partial validation
  * `True` or `'on'` - enable partial validation, but don't support trailing strings
  * `'trailing-strings'` - enable partial validation and support trailing strings


`'trailing-strings'` mode
`'trailing-strings'` mode allows for trailing incomplete strings at the end of partial JSON to be included in the output. For example, if you're validating against the following model:
```
from typing import TypedDict


class Model(TypedDict):
    a: str
    b: str

```

Then the following JSON input would be considered valid, despite the incomplete string at the end:
```
'{"a": "hello", "b": "wor'

```

And would be validated as:
```
{'a': 'hello', 'b': 'wor'}

```

`experiment_allow_partial` in action:
```
from typing import Annotated

from annotated_types import MinLen
from typing_extensions import NotRequired, TypedDict

from pydantic import TypeAdapter


class Foobar(TypedDict):  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_6_annotation_1)
    a: int
    b: NotRequired[float]
    c: NotRequired[Annotated[str, MinLen(5)]]


ta = TypeAdapter(list[Foobar])

v = ta.validate_json('[{"a": 1, "b"', experimental_allow_partial=True)  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_6_annotation_2)
print(v)
#> [{'a': 1}]

v = ta.validate_json(
    '[{"a": 1, "b": 1.0, "c": "abcd', experimental_allow_partial=True  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_6_annotation_3)
)
print(v)
#> [{'a': 1, 'b': 1.0}]

v = ta.validate_json(
    '[{"b": 1.0, "c": "abcde"', experimental_allow_partial=True  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_6_annotation_4)
)
print(v)
#> []

v = ta.validate_json(
    '[{"a": 1, "b": 1.0, "c": "abcde"},{"a": ', experimental_allow_partial=True
)
print(v)
#> [{'a': 1, 'b': 1.0, 'c': 'abcde'}]

v = ta.validate_python([{'a': 1}], experimental_allow_partial=True)  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_6_annotation_5)
print(v)
#> [{'a': 1}]

v = ta.validate_python(
    [{'a': 1, 'b': 1.0, 'c': 'abcd'}], experimental_allow_partial=True  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_6_annotation_6)
)
print(v)
#> [{'a': 1, 'b': 1.0}]

v = ta.validate_json(
    '[{"a": 1, "b": 1.0, "c": "abcdefg',
    experimental_allow_partial='trailing-strings',  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_6_annotation_7)
)
print(v)
#> [{'a': 1, 'b': 1.0, 'c': 'abcdefg'}]

```

### How Partial Validation Works[¶](https://docs.pydantic.dev/latest/concepts/experimental/#how-partial-validation-works)
Partial validation follows the zen of Pydantic — it makes no guarantees about what the input data might have been, but it does guarantee to return a valid instance of the type you required, or raise a validation error.
To do this, the `experimental_allow_partial` flag enables two pieces of behavior:
#### 1. Partial JSON parsing[¶](https://docs.pydantic.dev/latest/concepts/experimental/#1-partial-json-parsing)
The `experimental_allow_partial` is simply passed to jiter via the `allow_partial` argument.
Note
If you just want pure JSON parsing with support for partial JSON, you can use the `allow_partial` argument when calling [`pydantic_core.from_json`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.from_json).
#### 2. Ignore errors in the last element of the input[¶](https://docs.pydantic.dev/latest/concepts/experimental/#2-ignore-errors-in-last)
Only having access to part of the input data means errors can commonly occur in the last element of the input data.
For example:
  * if a string has a constraint `MinLen(5)`, when you only see part of the input, validation might fail because part of the string is missing (e.g. `{"name": "Sam` instead of `{"name": "Samuel"}`)
  * if an `int` field has a constraint `Ge(10)`, when you only see part of the input, validation might fail because the number is too small (e.g. `1` instead of `10`)
  * if a `TypedDict` field has 3 required fields, but the partial input only has two of the fields, validation would fail because some field are missing
  * etc. etc. — there are lost more cases like this


The point is that if you only see part of some valid input data, validation errors can often occur in the last element of a sequence or last value of mapping.
To avoid these errors breaking partial validation, Pydantic will ignore ALL errors in the last element of the input data.
Errors in last element ignored```
from typing import Annotated

from annotated_types import MinLen

from pydantic import BaseModel, TypeAdapter


class MyModel(BaseModel):
    a: int
    b: Annotated[str, MinLen(5)]


ta = TypeAdapter(list[MyModel])
v = ta.validate_json(
    '[{"a": 1, "b": "12345"}, {"a": 1,',
    experimental_allow_partial=True,
)
print(v)
#> [MyModel(a=1, b='12345')]

```

### Limitations of Partial Validation[¶](https://docs.pydantic.dev/latest/concepts/experimental/#limitations-of-partial-validation)
#### TypeAdapter only[¶](https://docs.pydantic.dev/latest/concepts/experimental/#typeadapter-only)
You can only pass `experiment_allow_partial` to [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) methods, it's not yet supported via other Pydantic entry points like [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel).
#### Types supported[¶](https://docs.pydantic.dev/latest/concepts/experimental/#types-supported)
Right now only a subset of collection validators know how to handle partial validation:
  * `list`
  * `set`
  * `frozenset`
  * `dict` (as in `dict[X, Y]`)
  * `TypedDict` — only non-required fields may be missing, e.g. via


While you can use `experimental_allow_partial` while validating against types that include other collection validators, those types will be validated "all or nothing", and partial validation will not work on more nested types.
E.g. in the [above](https://docs.pydantic.dev/latest/concepts/experimental/#2-ignore-errors-in-last) example partial validation works although the second item in the list is dropped completely since `BaseModel` doesn't (yet) support partial validation.
But partial validation won't work at all in the follow example because `BaseModel` doesn't support partial validation so it doesn't forward the `allow_partial` instruction down to the list validator in `b`:
```
from typing import Annotated

from annotated_types import MinLen

from pydantic import BaseModel, TypeAdapter, ValidationError


class MyModel(BaseModel):
    a: int = 1
    b: list[Annotated[str, MinLen(5)]] = []  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_8_annotation_1)


ta = TypeAdapter(MyModel)
try:
    v = ta.validate_json(
        '{"a": 1, "b": ["12345", "12', experimental_allow_partial=True
    )
except ValidationError as e:
    print(e)
    """
    1 validation error for MyModel
    b.1
      String should have at least 5 characters [type=string_too_short, input_value='12', input_type=str]
    """

```

#### Some invalid but complete JSON will be accepted[¶](https://docs.pydantic.dev/latest/concepts/experimental/#some-invalid-but-complete-json-will-be-accepted)
The way `{"a": 1, "b": "12"}` and incomplete JSON like `{"a": 1, "b": "12`.
This means that some invalid JSON will be accepted by Pydantic when using `experimental_allow_partial`, e.g.:
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/experimental/#__tabbed_1_1)[Python 3.13 and above](https://docs.pydantic.dev/latest/concepts/experimental/#__tabbed_1_2)
```
from typing import Annotated

from annotated_types import MinLen
from typing_extensions import TypedDict

from pydantic import TypeAdapter


class Foobar(TypedDict, total=False):
    a: int
    b: Annotated[str, MinLen(5)]


ta = TypeAdapter(Foobar)

v = ta.validate_json(
    '{"a": 1, "b": "12', experimental_allow_partial=True  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_9_annotation_1)
)
print(v)
#> {'a': 1}

v = ta.validate_json(
    '{"a": 1, "b": "12"}', experimental_allow_partial=True  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_9_annotation_2)
)
print(v)
#> {'a': 1}

```

```
from typing import Annotated

from annotated_types import MinLen
from typing import TypedDict

from pydantic import TypeAdapter


class Foobar(TypedDict, total=False):
    a: int
    b: Annotated[str, MinLen(5)]


ta = TypeAdapter(Foobar)

v = ta.validate_json(
    '{"a": 1, "b": "12', experimental_allow_partial=True

[](https://docs.pydantic.dev/latest/concepts/experimental/#__code_10_annotation_1)
)
print(v)
#> {'a': 1}

v = ta.validate_json(
    '{"a": 1, "b": "12"}', experimental_allow_partial=True

[](https://docs.pydantic.dev/latest/concepts/experimental/#__code_10_annotation_2)
)
print(v)
#> {'a': 1}

```

  1. This will pass validation as expected although the last field will be omitted as it failed validation.
  2. This will also pass validation since the binary representation of the JSON data passed to pydantic-core is indistinguishable from the previous case.


#### Any error in the last field of the input will be ignored[¶](https://docs.pydantic.dev/latest/concepts/experimental/#any-error-in-the-last-field-of-the-input-will-be-ignored)
As described [above](https://docs.pydantic.dev/latest/concepts/experimental/#2-ignore-errors-in-last), many errors can result from truncating the input. Rather than trying to specifically ignore errors that could result from truncation, Pydantic ignores all errors in the last element of the input in partial validation mode.
This means clearly invalid data will pass validation if the error is in the last field of the input:
```
from typing import Annotated

from annotated_types import Ge

from pydantic import TypeAdapter

ta = TypeAdapter(list[Annotated[int, Ge(10)]])
v = ta.validate_python([20, 30, 4], experimental_allow_partial=True)  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_11_annotation_1)
print(v)
#> [20, 30]

ta = TypeAdapter(list[int])

v = ta.validate_python([1, 2, 'wrong'], experimental_allow_partial=True)  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_11_annotation_2)
print(v)
#> [1, 2]

```

## Validation of a callable's arguments[¶](https://docs.pydantic.dev/latest/concepts/experimental/#validation-of-a-callables-arguments)
Pydantic provides the [`@validate_call`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call) decorator to perform validation on the provided arguments (and additionally return type) of a callable. However, it only allows arguments to be provided by actually calling the decorated callable. In some situations, you may want to just _validate_ the arguments, such as when loading from other data sources such as JSON data.
For this reason, the experimental [`generate_arguments_schema()`](https://docs.pydantic.dev/latest/api/experimental/#pydantic.experimental.arguments_schema.generate_arguments_schema) function can be used to construct a core schema, which can later be used with a [`SchemaValidator`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.SchemaValidator).
```
from pydantic_core import SchemaValidator

from pydantic.experimental.arguments_schema import generate_arguments_schema


def func(p: bool, *args: str, **kwargs: int) -> None: ...


arguments_schema = generate_arguments_schema(func=func)

val = SchemaValidator(arguments_schema, config={'coerce_numbers_to_str': True})

args, kwargs = val.validate_json(
    '{"p": true, "args": ["arg1", 1], "kwargs": {"extra": 1}}'
)
print(args, kwargs)  [](https://docs.pydantic.dev/latest/concepts/experimental/#__code_12_annotation_1)
#> (True, 'arg1', '1') {'extra': 1}

```

Note
Unlike [`@validate_call`](https://docs.pydantic.dev/latest/api/validate_call/#pydantic.validate_call_decorator.validate_call), this core schema will only validate the provided arguments; the underlying callable will _not_ be called.
Additionally, you can ignore specific parameters by providing a callback, which is called for every parameter:
```
from typing import Any

from pydantic_core import SchemaValidator

from pydantic.experimental.arguments_schema import generate_arguments_schema


def func(p: bool, *args: str, **kwargs: int) -> None: ...


def skip_first_parameter(index: int, name: str, annotation: Any) -> Any:
    if index == 0:
        return 'skip'


arguments_schema = generate_arguments_schema(
    func=func,
    parameters_callback=skip_first_parameter,
)

val = SchemaValidator(arguments_schema)

args, kwargs = val.validate_json('{"args": ["arg1"], "kwargs": {"extra": 1}}')
print(args, kwargs)
#> ('arg1',) {'extra': 1}

```

##  `MISSING` sentinel[¶](https://docs.pydantic.dev/latest/concepts/experimental/#missing-sentinel)
The `MISSING` sentinel is a singleton indicating a field value was not provided during validation.
This singleton can be used as a default value, as an alternative to `None` when it has an explicit meaning. During serialization, any field with `MISSING` as a value is excluded from the output.
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/experimental/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/experimental/#__tabbed_2_2)
```
from typing import Union

from pydantic import BaseModel
from pydantic.experimental.missing_sentinel import MISSING


class Configuration(BaseModel):
    timeout: Union[int, None, MISSING] = MISSING


# configuration defaults, stored somewhere else:
defaults = {'timeout': 200}

conf = Configuration()

# `timeout` is excluded from the serialization output:
conf.model_dump()
# {}

# The `MISSING` value doesn't appear in the JSON Schema:
Configuration.model_json_schema()['properties']['timeout']
#> {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Timeout'}}


# `is` can be used to discriminate between the sentinel and other values:
timeout = conf.timeout if conf.timeout is not MISSING else defaults['timeout']

```

```
from pydantic import BaseModel
from pydantic.experimental.missing_sentinel import MISSING


class Configuration(BaseModel):
    timeout: int | None | MISSING = MISSING


# configuration defaults, stored somewhere else:
defaults = {'timeout': 200}

conf = Configuration()

# `timeout` is excluded from the serialization output:
conf.model_dump()
# {}

# The `MISSING` value doesn't appear in the JSON Schema:
Configuration.model_json_schema()['properties']['timeout']
#> {'anyOf': [{'type': 'integer'}, {'type': 'null'}], 'title': 'Timeout'}}


# `is` can be used to discriminate between the sentinel and other values:
timeout = conf.timeout if conf.timeout is not MISSING else defaults['timeout']

```

This feature is marked as experimental because it relies on the draft
As such, the following limitations currently apply:
  * Static type checking of sentinels is only supported with Pyright `enableExperimentalFeatures` type evaluation setting should be enabled.
  * Pickling of models containing `MISSING` as a value is not supported.

Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
