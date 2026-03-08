# Standard Library Types
This section enumerates the supported built-in and standard library types: the allowed values, the possible constraints, and whether strictness can be configured.
See also the [conversion table](https://docs.pydantic.dev/latest/concepts/conversion_table/) for a summary of the allowed values for each type.
Note
Unless specified otherwise, values are serialized as-is, in both Python and JSON modes.
## Booleans[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#booleans)
Built-in type:
### Validation
  * A valid `True` or `False`.
  * The integers `0` or `1`.
  * A string, which when converted to lowercase is one of `'0'`, `'off'`, `'f'`, `'false'`, `'n'`, `'no'`, `'1'`, `'on'` `'t'`, `'true'`, `'y'`, `'yes'`.


### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only boolean values are valid. Pydantic provides the [`StrictBool`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBool) type as a convenience to [using the `Strict()` metadata class](https://docs.pydantic.dev/latest/concepts/strict_mode/#using-the-strict-metadata-class).
### Example
```
from pydantic import BaseModel, ValidationError


class BooleanModel(BaseModel):
    bool_value: bool


print(BooleanModel(bool_value=False))
#> bool_value=False
print(BooleanModel(bool_value='False'))
#> bool_value=False
print(BooleanModel(bool_value=1))
#> bool_value=True
try:
    BooleanModel(bool_value=[])
except ValidationError as e:
    print(str(e))
    """
    1 validation error for BooleanModel
    bool_value
      Input should be a valid boolean [type=bool_type, input_value=[], input_type=list]
    """

```

## Strings[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#strings)
Built-in type:
### Validation
  * Strings are accepted as-is.
  * If [`coerce_numbers_to_str`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.coerce_numbers_to_str) is set, any number type (


### Constraints
Strings support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`pattern` | A regex pattern that the string must match |  [note](https://docs.pydantic.dev/latest/api/standard_library_types/#pattern-constraint-note) below).
`min_length` | The minimum length of the string |
`max_length` | The maximum length of the string |
`strip_whitespace` | Whether to remove leading and trailing whitespace | N/A
`to_upper` | Whether to convert the string to uppercase | N/A
`to_lower` | Whether to convert the string to lowercase | N/A
These constraints can be provided using the [`StringConstraints`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StringConstraints) metadata type, or using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function (except for `to_upper` and `to_lower`). The `MinLen`, `MaxLen`, `Len`, `LowerCase`, `UpperCase` metadata types from the
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
`pattern` constraint
By default, Pydantic will use the `pattern` constraint. The regex engine can be controlled using the [`regex_engine`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.regex_engine) configuration value. If a compiled `pattern`, the Python engine will automatically be used.
While the JSON Schema specification _not_ enforce it.
### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only string values are valid. Pydantic provides the [`StrictStr`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictStr) type as a convenience to [using the `Strict()` metadata class](https://docs.pydantic.dev/latest/concepts/strict_mode/#using-the-strict-metadata-class).
### Example
```
from typing import Annotated

from pydantic import BaseModel, StringConstraints


class StringModel(BaseModel):
    str_value: str = ""
    constrained_str_value: Annotated[str, StringConstraints(to_lower=True)] = ""


print(StringModel(str_value="test").str_value)
#> test
print(StringModel(constrained_str_value='TEST').constrained_str_value)
#> test

```

## Bytes[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#bytes)
Built-in type:
See also: [`ByteSize`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ByteSize).
### Validation
  * Strings and [`val_json_bytes`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.val_json_bytes) configuration value (despite its name, it applies to both Python and JSON modes).


### Constraints
Strings support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`min_length` | The minimum length of the bytes |
`max_length` | The maximum length of the bytes |
The `MinLen` and `MaxLen` metadata types from the
### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only [`StrictBytes`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBytes) type as a convenience to [using the `Strict()` metadata class](https://docs.pydantic.dev/latest/concepts/strict_mode/#using-the-strict-metadata-class).
In JSON mode, strict mode has no effect.
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Numbers[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#numbers)
Pydantic supports the following numeric types from the Python standard library:
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Integers[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#integers)
Built-in type:
#### Validation
  * Integers are validated as-is.
  * Strings and bytes are attempted to be converted to integers and validated as-is (see the
  * Floats are validated as integers, provided the float input is not infinite or a NaN (not-a-number) and the fractional part is 0.


#### Constraints
Integers support the following constraints (numbers must be coercible to integers):
Constraint | Description | JSON Schema
---|---|---
`le` | The value must be less than or equal to this number |
`ge` | The value must be greater than or equal to this number |
`lt` | The value must be strictly less than this number |
`gt` | The value must be strictly greater than this number |
`multiple_of` | The value must be a multiple of this number |
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `Le`, `Ge`, `Lt`, `Gt` and `MultipleOf` metadata types from the
Pydantic also provides the following types to further constrain the allowed integer values:
  * [`PositiveInt`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PositiveInt): Requires the input to be greater than zero.
  * [`NegativeInt`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NegativeInt): Requires the input to be less than zero.
  * [`NonPositiveInt`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonPositiveInt): Requires the input to be less than or equal to zero.
  * [`NonNegativeInt`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonNegativeInt): Requires the input to be greater than or equal to zero.


#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only integer values are valid. Pydantic provides the [`StrictInt`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictInt) type as a convenience to [using the `Strict()` metadata class](https://docs.pydantic.dev/latest/concepts/strict_mode/#using-the-strict-metadata-class).
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Floats[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#floats)
Built-in type:
#### Validation
  * Floats are validated as-is.
  * String and bytes are attempted to be converted to floats and validated as-is. (see the
  * If the input has a `__float__()` is not defined, it falls back to


#### Constraints
Floats support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`le` | The value must be less than or equal to this number |
`ge` | The value must be greater than or equal to this number |
`lt` | The value must be strictly less than this number |
`gt` | The value must be strictly greater than this number |
`multiple_of` | The value must be a multiple of this number |
`allow_inf_nan` | Whether to allow NaN (not-a-number) and infinite values | N/A
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `Le`, `Ge`, `Lt`, `Gt` and `MultipleOf` metadata types from the [`AllowInfNan`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AllowInfNan) type can also be used.
Pydantic also provides the following types as convenience aliases:
  * [`PositiveFloat`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PositiveFloat): Requires the input to be greater than zero.
  * [`NegativeFloat`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NegativeFloat): Requires the input to be less than zero.
  * [`NonPositiveFloat`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonPositiveFloat): Requires the input to be less than or equal to zero.
  * [`NonNegativeFloat`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonNegativeFloat): Requires the input to be greater than or equal to zero.
  * [`FiniteFloat`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FiniteFloat): Prevents NaN (not-a-number) and infinite values.


#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only float values and inputs having a [`StrictFloat`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictFloat) type as a convenience to [using the `Strict()` metadata class](https://docs.pydantic.dev/latest/concepts/strict_mode/#using-the-strict-metadata-class).
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Integer enums[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#integer-enums)
Standard library type:
#### Validation
  * If the
  * If an


See [Enums](https://docs.pydantic.dev/latest/api/standard_library_types/#enums) for more details.
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Decimals[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#decimals)
Standard library type:
#### Validation
  * Any value accepted by the


#### Constraints
Decimals support the following constraints (numbers must be coercible to decimals):
Constraint | Description | JSON Schema
---|---|---
`le` | The value must be less than or equal to this number |
`ge` | The value must be greater than or equal to this number |
`lt` | The value must be strictly less than this number |
`gt` | The value must be strictly greater than this number |
`multiple_of` | The value must be a multiple of this number |
`allow_inf_nan` | Whether to allow NaN (not-a-number) and infinite values | N/A
`max_digits` | The maximum number of decimal digits allowed. The zero before the decimal point and trailing zeros are not counted. |
`decimal_places` | The maximum number of decimal places allowed. Trailing zeros are not counted. |
Note that the JSON Schema `max_digits` and/or `decimal_places` is specified).
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `Le`, `Ge`, `Lt`, `Gt` and `MultipleOf` metadata types from the [`AllowInfNan`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AllowInfNan) type can also be used.
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only
#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode),
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings. A [serializer](https://docs.pydantic.dev/latest/concepts/serialization/#field-plain-serializer) can be used to override this behavior:
```
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, PlainSerializer


class Model(BaseModel):
    f: Annotated[Decimal, PlainSerializer(float, when_used='json')]


my_model = Model(f=Decimal('2.1'))

print(my_model.model_dump())  [](https://docs.pydantic.dev/latest/api/standard_library_types/#__code_2_annotation_1)
#> {'f': Decimal('2.1')}
print(my_model.model_dump_json())  [](https://docs.pydantic.dev/latest/api/standard_library_types/#__code_2_annotation_2)
#> {"f":2.1}

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Complex numbers[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#complex-numbers)
Built-in type:
#### Validation
  * Strings are validated using the
  * Numbers (integers and floats) are used as the real part.
  * Objects defining _not_ accepted.


#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only
#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode),
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Fractions[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#fractions)
Standard library type:
#### Validation
  * Floats, strings and


#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only
#### Serialization
Fractions are serialized as strings, both in [Python](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode) and [JSON](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode) modes.
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Date and time types[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#date-and-time-types)
Pydantic supports the following
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Datetimes[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#datetimes)
Standard library type:
#### Validation
  * Strings and bytes are validated in two ways:
    * Strings complying to the
    * Unix timestamps, both as seconds or milliseconds sinch the [`val_temporal_unit`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.val_temporal_unit) configuration value for more details.
  * Integers and floats (or types that can be coerced as integers or floats) are validated as unix timestamps, following the same semantics as strings.
  * `0`, and the `None`.


Note
Named timezone support (as specified in
#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode),
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
#### Constraints
Datetimes support the following constraints (constraint values must be coercible to a
Constraint | Description | JSON Schema
---|---|---
`le` | The value must be less than or equal to this datetime | N/A
`ge` | The value must be greater than or equal to this datetime | N/A
`lt` | The value must be strictly less than this datetime | N/A
`gt` | The value must be strictly greater than this datetime | N/A
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `Le`, `Ge`, `Lt` and `Gt` metadata types from the
Pydantic also provides the following types to further constrain the allowed datetime values:
  * [`AwareDatetime`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AwareDatetime): Requires the input to have a timezone.
  * [`NaiveDatetime`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NaiveDatetime): Requires the input to _not_ have a timezone.
  * [`PastDatetime`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PastDatetime): Requires the input to be in the past when validated.
  * [`FutureDatetime`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FutureDatetime): Requires the input to be in the future when validated.


#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _only_ datetime) or as unix timestamps are accepted.
#### Example
```
from datetime import datetime
from typing import Annotated

from pydantic import AwareDatetime, BaseModel, Field


class Event(BaseModel):
    dt: Annotated[AwareDatetime, Field(gt=datetime(2000, 1, 1))]


event = Event(dt='2032-04-23T10:20:30.400+02:30')

print(event.model_dump())
"""
{'dt': datetime.datetime(2032, 4, 23, 10, 20, 30, 400000, tzinfo=TzInfo(9000))}
"""
print(event.model_dump_json())
#> {"dt":"2032-04-23T10:20:30.400000+02:30"}

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Dates[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#dates)
Standard library type:
#### Validation
  * Strings and bytes are validated in two ways:
    * Strings complying to the
    * Unix timestamps, both as seconds or milliseconds sinch the [`val_temporal_unit`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.val_temporal_unit) configuration value for more details.
  * If the validation fails, the input can be [validated as a datetime](https://docs.pydantic.dev/latest/api/standard_library_types/#datetimes) (including as numbers), provided that the time component is 0 and that it is naive.


#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode),
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
#### Constraints
Dates support the following constraints (constraint values must be coercible to a
Constraint | Description | JSON Schema
---|---|---
`le` | The value must be less than or equal to this date | N/A
`ge` | The value must be greater than or equal to this date | N/A
`lt` | The value must be strictly less than this date | N/A
`gt` | The value must be strictly greater than this date | N/A
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `Le`, `Ge`, `Lt` and `Gt` metadata types from the
Pydantic also provides the following types to further constrain the allowed date values:
  * [`PastDate`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PastDate): Requires the input to be in the past when validated.
  * [`FutureDate`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FutureDate): Requires the input to be in the future when validated.


#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _only_ date) or as unix timestamps are accepted.
#### Example
```
from datetime import date

from pydantic import BaseModel


class Birthday(BaseModel):
    d: date


my_birthday = Birthday(d=1679616000.0)

print(my_birthday.model_dump())
#> {'d': datetime.date(2023, 3, 24)}
print(my_birthday.model_dump_json())
#> {"d":"2023-03-24"}

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Time[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#time)
Standard library type:
#### Validation
  * Strings and bytes are validated according to the
  * Integers and floats (or values that can be coerced to such numbers) are validated as seconds. The value should not exceed 86 399.


#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode),
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
Note
Named timezones from the _not_ serialized with time objects. This is consistent with the
#### Constraints
Time support the following constraints (constraint values must be coercible to a
Constraint | Description | JSON Schema
---|---|---
`le` | The value must be less than or equal to this time | N/A
`ge` | The value must be greater than or equal to this time | N/A
`lt` | The value must be strictly less than this time | N/A
`gt` | The value must be strictly greater than this time | N/A
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `Le`, `Ge`, `Lt` and `Gt` metadata types from the
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only
#### Example
```
from datetime import time

from pydantic import BaseModel


class Meeting(BaseModel):
    t: time


m = Meeting(t=time(4, 8, 16))

print(m.model_dump())
#> {'t': datetime.time(4, 8, 16)}
print(m.model_dump_json())
#> {"t":"04:08:16"}

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Timedeltas[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#timedeltas)
Standard library type:
#### Validation
  * Strings and bytes are validated according to the
  * Integers and floats (or values that can be coerced to such numbers) are validated as seconds.


#### Constraints
Timedeltas support the following constraints (constraint values must be coercible to a
Constraint | Description | JSON Schema
---|---|---
`le` | The value must be less than or equal to this timedelta | N/A
`ge` | The value must be greater than or equal to this timedelta | N/A
`lt` | The value must be strictly less than this timedelta | N/A
`gt` | The value must be strictly greater than this timedelta | N/A
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `Le`, `Ge`, `Lt` and `Gt` metadata types from the
#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode),
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only
#### Example
```
from datetime import timedelta

from pydantic import BaseModel


class Model(BaseModel):
    td: timedelta


m = Model(td='P3DT12H30M5S')

print(m.model_dump())
#> {'td': datetime.timedelta(days=3, seconds=45005)}
print(m.model_dump_json())
#> {"td":"P3DT12H30M5S"}

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Enums[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#enums)
Standard library type:
### Validation
  * If the
  * If an


### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), enum instances are serialized as is. The [`use_enum_values`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.use_enum_values) configuration value can be set to use the enum
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), enum instances are serialized using their
### Example
```
from enum import Enum, IntEnum

from pydantic import BaseModel, ValidationError


class FruitEnum(str, Enum):
    PEAR = 'pear'
    BANANA = 'banana'


class ToolEnum(IntEnum):
    SPANNER = 1
    WRENCH = 2


class CookingModel(BaseModel):
    fruit: FruitEnum = FruitEnum.PEAR
    tool: ToolEnum = ToolEnum.SPANNER


print(CookingModel())
#> fruit=<FruitEnum.PEAR: 'pear'> tool=<ToolEnum.SPANNER: 1>
print(CookingModel(tool=2, fruit='banana'))
#> fruit=<FruitEnum.BANANA: 'banana'> tool=<ToolEnum.WRENCH: 2>
try:
    CookingModel(fruit='other')
except ValidationError as e:
    print(e)
    """
    1 validation error for CookingModel
    fruit
      Input should be 'pear' or 'banana' [type=enum, input_value='other', input_type=str]
    """

```

## None types[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#none-types)
Supported types: `Literal[None]` (they are
Allows only `None` as a value.
## Generic collection types[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#generic-collection-types)
Pydantic supports a wide variety of generic collection types, both built-ins (such as
In most cases, it is recommended to make use of the built-in types over the abstract ones. Due to [data coercion](https://docs.pydantic.dev/latest/concepts/models/#data-conversion), using
Strictness on collection types
When applying [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/) on collection types, strictness will _not_ apply to the inner types. This may change in the future, see
### Lists[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#lists)
Built-in type:
#### Validation
  * Allows _not_ a
  * If a generic parameter is provided, the appropriate validation is applied to all items of the list.


#### Constraints
Lists support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`min_length` | The list must have at least this many items |
`max_length` | The list must have at most this many items |
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `MinLen` and `MaxLen` metadata types from the
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _not_ apply to the items of the list. The strict constraint must be applied to the parameter type for this to work.
#### Example
[Python 3.9 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_1_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_1_2)
```
from typing import Optional

from pydantic import BaseModel, Field


class Model(BaseModel):
    simple_list: Optional[list[object]] = None
    list_of_ints: Optional[list[int]] = Field(default=None, strict=True)


print(Model(simple_list=('1', '2', '3')).simple_list)
#> ['1', '2', '3']
print(Model(list_of_ints=['1', 2, 3]).list_of_ints)
#> [1, 2, 3]

```

```
from pydantic import BaseModel, Field


class Model(BaseModel):
    simple_list: list[object] | None = None
    list_of_ints: list[int] | None = Field(default=None, strict=True)


print(Model(simple_list=('1', '2', '3')).simple_list)
#> ['1', '2', '3']
print(Model(list_of_ints=['1', 2, 3]).list_of_ints)
#> [1, 2, 3]

```

### Tuples[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#tuples)
Built-in type:
Note
_not_ yet supported, and can be tracked in
#### Validation
  * Allows _not_ a
  * Appropriate validation is applied to items of the tuple, if


#### Constraints
Lists support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`min_length` | The tuple must have at least this many items |
`max_length` | The tuple must have at most this many items |
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `MinLen` and `MaxLen` metadata types from the
Additionally, the
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _not_ apply to the items of the tuple. The strict constraint must be applied to the parameter types for this to work.
#### Example
[Python 3.9 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_2_2)
```
from typing import Optional

from pydantic import BaseModel


class Model(BaseModel):
    simple_tuple: Optional[tuple] = None
    tuple_of_different_types: Optional[tuple[int, float, bool]] = None


print(Model(simple_tuple=[1, 2, 3, 4]).simple_tuple)
#> (1, 2, 3, 4)
print(Model(tuple_of_different_types=[3, 2, 1]).tuple_of_different_types)
#> (3, 2.0, True)

```

```
from pydantic import BaseModel


class Model(BaseModel):
    simple_tuple: tuple | None = None
    tuple_of_different_types: tuple[int, float, bool] | None = None


print(Model(simple_tuple=[1, 2, 3, 4]).simple_tuple)
#> (1, 2, 3, 4)
print(Model(tuple_of_different_types=[3, 2, 1]).tuple_of_different_types)
#> (3, 2.0, True)

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Named tuples[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#named-tuples)
Standard library type:
#### Validation
  * Allows
  * Allows


#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), named tuples are serialized as tuples. In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as arrays.
#### Example
```
from typing import NamedTuple

from pydantic import BaseModel


class Point(NamedTuple):
    x: int
    y: int


class Model(BaseModel):
    p: Point


model = Model(p=('1', 2))

print(model.model_dump())
#> {'p': (1, 2)}

```

### Sets[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#sets)
Types:
#### Validation
  * Allows _not_ a
  * If a generic parameter is provided, the appropriate validation is applied to all items of the set/frozenset.


#### Constraints
Sets support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`min_length` | The set must have at least this many items |
`max_length` | The set must have at most this many items |
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `MinLen` and `MaxLen` metadata types from the
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _not_ apply to the items of the set. The strict constraint must be applied to the parameter type for this to work.
#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), sets are serialized as is. In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as arrays.
#### Example
[Python 3.9 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_3_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_3_2)
```
from typing import Optional

from pydantic import BaseModel


class Model(BaseModel):
    simple_set: Optional[set] = None
    set_of_ints: Optional[frozenset[int]] = None


print(Model(simple_set=['1', '2', '3']).simple_set)
#> {'1', '2', '3'}
print(Model(set_of_ints=['1', '2', '3']).set_of_ints)
#> frozenset({1, 2, 3})

```

```
from pydantic import BaseModel


class Model(BaseModel):
    simple_set: set | None = None
    set_of_ints: frozenset[int] | None = None


print(Model(simple_set=['1', '2', '3']).simple_set)
#> {'1', '2', '3'}
print(Model(set_of_ints=['1', '2', '3']).set_of_ints)
#> frozenset({1, 2, 3})

```

### Deque[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#deque)
Standard library type:
#### Validation
Values are first validated as a [list](https://docs.pydantic.dev/latest/api/standard_library_types/#lists), and then passed to the
#### Constraints
Deques support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`min_length` | The deque must have at least this many items |
`max_length` | The deque must have at most this many items |
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `MinLen` and `MaxLen` metadata types from the
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _not_ apply to the items of the deque. The strict constraint must be applied to the parameter type for this to work.
#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), deques are serialized as is. In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as arrays.
#### Example
```
from collections import deque

from pydantic import BaseModel


class Model(BaseModel):
    deque: deque[int]


print(Model(deque=[1, 2, 3]).deque)
#> deque([1, 2, 3])

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Sequences[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#sequences)
Standard library type:
In most cases, you will want to use the built-in types (such as [list](https://docs.pydantic.dev/latest/api/standard_library_types/#lists) or [tuple](https://docs.pydantic.dev/latest/api/standard_library_types/#tuples)) as [type coercion](https://docs.pydantic.dev/latest/concepts/models/#data-conversion) will apply. The
#### Validation
Any
Strings aren't treated as sequences
While strings are technically valid sequence instances, this is frequently not intended as is a common source of bugs.
As a result, Pydantic will _not_ accept strings and bytes for the
#### Constraints
Sequences support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`min_length` | The sequence must have at least this many items |
`max_length` | The sequence must have at most this many items |
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `MinLen` and `MaxLen` metadata types from the
#### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), sequences are serialized as is. In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as arrays.
#### Example
```
from collections.abc import Sequence

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    sequence_of_strs: Sequence[str]


print(Model(sequence_of_strs=['a', 'bc']).sequence_of_strs)
#> ['a', 'bc']
print(Model(sequence_of_strs=('a', 'bc')).sequence_of_strs)
#> ('a', 'bc')

try:
    Model(sequence_of_strs='abc')
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    sequence_of_strs
      'str' instances are not allowed as a Sequence value [type=sequence_str, input_value='abc', input_type=str]
    """

```

### Dictionaries[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#dictionaries)
Built-in type:
#### Validation
  * If generic parameters for keys and values are provided, the appropriate validation is applied.


#### Constraints
Dictionaries support the following constraints:
Constraint | Description | JSON Schema
---|---|---
`min_length` | The dictionary must have at least this many items |
`max_length` | The dictionary must have at most this many items |
These constraints can be provided using the [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) function. The `MinLen` and `MaxLen` metadata types from the
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _not_ apply to the keys and values of the dictionaries. The strict constraint must be applied to the parameter types for this to work.
#### Example
```
from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    x: dict[str, int]


m = Model(x={'foo': 1})
print(m.model_dump())
#> {'x': {'foo': 1}}

try:
    Model(x='test')
except ValidationError as e:
    print(e)
    """
    1 validation error for Model
    x
      Input should be a valid dictionary [type=dict_type, input_value='test', input_type=str]
    """

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Typed dictionaries[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#typed-dictionaries)
Standard library type:
Note
Because of runtime limitations, Pydantic will require using the
This type [supports configuration](https://docs.pydantic.dev/latest/concepts/config/#configuration-on-other-supported-types).
#### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only _not_ apply to the values of the typed dictionary. The strict constraint must be applied to the value types for this to work.
#### Example
[Python 3.9 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_4_1)[Python 3.13 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_4_2)
```
from typing_extensions import TypedDict

from pydantic import TypeAdapter, ValidationError


class User(TypedDict):
    name: str
    id: int


ta = TypeAdapter(User)

print(ta.validate_python({'name': 'foo', 'id': 1}))
#> {'name': 'foo', 'id': 1}

try:
    ta.validate_python({'name': 'foo'})
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    id
      Field required [type=missing, input_value={'name': 'foo'}, input_type=dict]
    """

```

```
from typing import TypedDict

from pydantic import TypeAdapter, ValidationError


class User(TypedDict):
    name: str
    id: int


ta = TypeAdapter(User)

print(ta.validate_python({'name': 'foo', 'id': 1}))
#> {'name': 'foo', 'id': 1}

try:
    ta.validate_python({'name': 'foo'})
except ValidationError as e:
    print(e)
    """
    1 validation error for User
    id
      Field required [type=missing, input_value={'name': 'foo'}, input_type=dict]
    """

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
### Iterables[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#iterables)
Standard library type:
#### Validation
Iterables are lazily validated, and wrapped in an internal datastructure that can be iterated over (and will validated the items type while doing so). This means that even if you provide a concrete container such as a list, the validated type will _not_ be of type
It is recommended to use concrete collection types (such as [lists](https://docs.pydantic.dev/latest/api/standard_library_types/#lists)) instead, unless you are using an infinite iterator (in which case eagerly validating the input would result in an infinite loop).
#### Example
```
from collections.abc import Iterable

from pydantic import BaseModel, ValidationError


class Model(BaseModel):
    f: Iterable[str]


m = Model(f=[1, 2])  # Validates fine

try:
    next(m.f)
except ValidationError as e:
    print(e)
    """
    1 validation error for ValidatorIterator
    0
      Input should be a valid string [type=string_type, input_value=1, input_type=int]
    """

```

## Callable[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#callable)
Standard library type:
### Validation
Pydantic only validates that the input is a _not_ validate the number of parameters or their type, nor the type of the return value.
[Python 3.9 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_5_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/api/standard_library_types/#__tabbed_5_2)
```
from typing import Callable

from pydantic import BaseModel


class Foo(BaseModel):
    callback: Callable[[int], int]


m = Foo(callback=lambda x: x)
print(m)
#> callback=<function <lambda> at 0x0123456789ab>

```

```
from collections.abc import Callable

from pydantic import BaseModel


class Foo(BaseModel):
    callback: Callable[[int], int]


m = Foo(callback=lambda x: x)
print(m)
#> callback=<function <lambda> at 0x0123456789ab>

```

### Serialization
Callables are serialized as is. Callables can't be serialized in [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode) (a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) is raised).
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## IP Addresses[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#ip-addresses)
Standard library types:
See also: the [`IPvAnyAddress`](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyAddress), [`IPvAnyInterface`](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyInterface) and [`IPvAnyNetwork`](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyNetwork) Pydantic types.
### Validation
  * Instances are validated as is.
  * Other input values are passed to the constructor of the relevant address type.


### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only the address types are accepted. In JSON mode, strict mode has no effect.
### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), IP addresses are serialized as is. In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
## UUID[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#uuid)
Standard library type:
### Validation
  * Strings and bytes are validated as UUIDs, and casted to a


### Constraints
The `version` constraint. The [`UuidVersion`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion) metadata type can be used.
Pydantic also provides the following types as convenience aliases: [`UUID1`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID1), [`UUID3`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID3), [`UUID4`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID4), [`UUID5`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID5), [`UUID6`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID6), [`UUID7`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID7), [`UUID8`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID8).
### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only
### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), UUIDs are serialized as is. In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
### Example
```
from typing import Annotated
from uuid import UUID

from pydantic import BaseModel
from pydantic.types import UUID7, UuidVersion


class Model(BaseModel):
    u1: UUID7
    u2: Annotated[UUID, UuidVersion(4)]


print(
    Model(
        u1='01999b2c-8353-749b-8dac-859307fae22b',
        u2=UUID('125725f3-e1b4-44e3-90c3-1a20eab12da5'),
    )
)
"""
u1=UUID('01999b2c-8353-749b-8dac-859307fae22b') u2=UUID('125725f3-e1b4-44e3-90c3-1a20eab12da5')
"""

```

## Type[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#type)
Built-in type:
### Validation
Allows any type that is a subclass of the type argument. For instance, with `type[str]`, allows the `type` is used as an annotation), allow any class.
### Serialization
Types are serialized as is. Types can't be serialized in [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode) (a [`PydanticSerializationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticSerializationError) is raised).
```
from pydantic import BaseModel, ValidationError


class Foo:
    pass


class Bar(Foo):
    pass


class Other:
    pass


class SimpleModel(BaseModel):
    just_subclasses: type[Foo]


SimpleModel(just_subclasses=Foo)
SimpleModel(just_subclasses=Bar)
try:
    SimpleModel(just_subclasses=Other)
except ValidationError as e:
    print(e)
    """
    1 validation error for SimpleModel
    just_subclasses
      Input should be a subclass of Foo [type=is_subclass_of, input_value=<class '__main__.Other'>, input_type=type]
    """

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Literals[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#literals)
Typing construct:
Literals can be used to only allow specific literal values.
Note that Pydantic applies [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/) behavior when validating literal values (see
### Example
```
from typing import Literal

from pydantic import BaseModel, ValidationError


class Pie(BaseModel):
    flavor: Literal['apple', 'pumpkin']
    quantity: Literal[1, 2] = 1


Pie(flavor='apple')
Pie(flavor='pumpkin')
try:
    Pie(flavor='cherry')
except ValidationError as e:
    print(str(e))
    """
    1 validation error for Pie
    flavor
      Input should be 'apple' or 'pumpkin' [type=literal_error, input_value='cherry', input_type=str]
    """

try:
    Pie(flavor='apple', quantity='1')
except ValidationError as e:
    print(str(e))
    """
    1 validation error for Pie
    quantity
      Input should be 1 or 2 [type=literal_error, input_value='1', input_type=str]
    """

```

[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Any[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#any)
Types:
Allows any value, including `None`.
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Hashables[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#hashables)
Standard library type:
### Validation
Any value that is hashable (using `isinstance(value, Hashable)`).
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Regex patterns[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#regex-patterns)
Standard library type:
### Validation
  * For
  * If the type parameter is


### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode),
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
[](https://docs.pydantic.dev/latest/api/standard_library_types/)
## Paths[¶](https://docs.pydantic.dev/latest/api/standard_library_types/#paths)
Standard library types:
### Validation
  * Path instances are validated as is.
  * Strings are accepted and passed to the type constructor. If


### Strictness
In [strict mode](https://docs.pydantic.dev/latest/concepts/strict_mode/), only Path instances are accepted. In JSON mode, strict mode has no effect.
### Serialization
In [Python mode](https://docs.pydantic.dev/latest/concepts/serialization/#python-mode), Path instances are serialized as is.
In [JSON mode](https://docs.pydantic.dev/latest/concepts/serialization/#json-mode), they are serialized as strings.
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
