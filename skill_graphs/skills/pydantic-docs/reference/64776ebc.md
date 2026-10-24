##  pydantic.types [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types)
The types module contains custom types used by pydantic.
###  StrictBool `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBool)
```
StrictBool = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

A boolean that must be either `True` or `False`.
###  PositiveInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PositiveInt)
```
PositiveInt = [, Gt(0)]

```

An integer that must be greater than zero.
```
from pydantic import BaseModel, PositiveInt, ValidationError

class Model(BaseModel):
    positive_int: PositiveInt

m = Model(positive_int=1)
print(repr(m))
#> Model(positive_int=1)

try:
    Model(positive_int=-1)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('positive_int',),
            'msg': 'Input should be greater than 0',
            'input': -1,
            'ctx': {'gt': 0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

###  NegativeInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NegativeInt)
```
NegativeInt = [, Lt(0)]

```

An integer that must be less than zero.
```
from pydantic import BaseModel, NegativeInt, ValidationError

class Model(BaseModel):
    negative_int: NegativeInt

m = Model(negative_int=-1)
print(repr(m))
#> Model(negative_int=-1)

try:
    Model(negative_int=1)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'less_than',
            'loc': ('negative_int',),
            'msg': 'Input should be less than 0',
            'input': 1,
            'ctx': {'lt': 0},
            'url': 'https://errors.pydantic.dev/2/v/less_than',
        }
    ]
    '''

```

###  NonPositiveInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonPositiveInt)
```
NonPositiveInt = [, Le(0)]

```

An integer that must be less than or equal to zero.
```
from pydantic import BaseModel, NonPositiveInt, ValidationError

class Model(BaseModel):
    non_positive_int: NonPositiveInt

m = Model(non_positive_int=0)
print(repr(m))
#> Model(non_positive_int=0)

try:
    Model(non_positive_int=1)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'less_than_equal',
            'loc': ('non_positive_int',),
            'msg': 'Input should be less than or equal to 0',
            'input': 1,
            'ctx': {'le': 0},
            'url': 'https://errors.pydantic.dev/2/v/less_than_equal',
        }
    ]
    '''

```

###  NonNegativeInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonNegativeInt)
```
NonNegativeInt = [, Ge(0)]

```

An integer that must be greater than or equal to zero.
```
from pydantic import BaseModel, NonNegativeInt, ValidationError

class Model(BaseModel):
    non_negative_int: NonNegativeInt

m = Model(non_negative_int=0)
print(repr(m))
#> Model(non_negative_int=0)

try:
    Model(non_negative_int=-1)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than_equal',
            'loc': ('non_negative_int',),
            'msg': 'Input should be greater than or equal to 0',
            'input': -1,
            'ctx': {'ge': 0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than_equal',
        }
    ]
    '''

```

###  StrictInt `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictInt)
```
StrictInt = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

An integer that must be validated in strict mode.
```
from pydantic import BaseModel, StrictInt, ValidationError

class StrictIntModel(BaseModel):
    strict_int: StrictInt

try:
    StrictIntModel(strict_int=3.14159)
except ValidationError as e:
    print(e)
    '''
    1 validation error for StrictIntModel
    strict_int
      Input should be a valid integer [type=int_type, input_value=3.14159, input_type=float]
    '''

```

###  PositiveFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PositiveFloat)
```
PositiveFloat = [, Gt(0)]

```

A float that must be greater than zero.
```
from pydantic import BaseModel, PositiveFloat, ValidationError

class Model(BaseModel):
    positive_float: PositiveFloat

m = Model(positive_float=1.0)
print(repr(m))
#> Model(positive_float=1.0)

try:
    Model(positive_float=-1.0)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('positive_float',),
            'msg': 'Input should be greater than 0',
            'input': -1.0,
            'ctx': {'gt': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

###  NegativeFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NegativeFloat)
```
NegativeFloat = [, Lt(0)]

```

A float that must be less than zero.
```
from pydantic import BaseModel, NegativeFloat, ValidationError

class Model(BaseModel):
    negative_float: NegativeFloat

m = Model(negative_float=-1.0)
print(repr(m))
#> Model(negative_float=-1.0)

try:
    Model(negative_float=1.0)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'less_than',
            'loc': ('negative_float',),
            'msg': 'Input should be less than 0',
            'input': 1.0,
            'ctx': {'lt': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/less_than',
        }
    ]
    '''

```

###  NonPositiveFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonPositiveFloat)
```
NonPositiveFloat = [, Le(0)]

```

A float that must be less than or equal to zero.
```
from pydantic import BaseModel, NonPositiveFloat, ValidationError

class Model(BaseModel):
    non_positive_float: NonPositiveFloat

m = Model(non_positive_float=0.0)
print(repr(m))
#> Model(non_positive_float=0.0)

try:
    Model(non_positive_float=1.0)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'less_than_equal',
            'loc': ('non_positive_float',),
            'msg': 'Input should be less than or equal to 0',
            'input': 1.0,
            'ctx': {'le': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/less_than_equal',
        }
    ]
    '''

```

###  NonNegativeFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NonNegativeFloat)
```
NonNegativeFloat = [, Ge(0)]

```

A float that must be greater than or equal to zero.
```
from pydantic import BaseModel, NonNegativeFloat, ValidationError

class Model(BaseModel):
    non_negative_float: NonNegativeFloat

m = Model(non_negative_float=0.0)
print(repr(m))
#> Model(non_negative_float=0.0)

try:
    Model(non_negative_float=-1.0)
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than_equal',
            'loc': ('non_negative_float',),
            'msg': 'Input should be greater than or equal to 0',
            'input': -1.0,
            'ctx': {'ge': 0.0},
            'url': 'https://errors.pydantic.dev/2/v/greater_than_equal',
        }
    ]
    '''

```

###  StrictFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictFloat)
```
StrictFloat = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)(True)]

```

A float that must be validated in strict mode.
```
from pydantic import BaseModel, StrictFloat, ValidationError

class StrictFloatModel(BaseModel):
    strict_float: StrictFloat

try:
    StrictFloatModel(strict_float='1.0')
except ValidationError as e:
    print(e)
    '''
    1 validation error for StrictFloatModel
    strict_float
      Input should be a valid number [type=float_type, input_value='1.0', input_type=str]
    '''

```

###  FiniteFloat `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FiniteFloat)
```
FiniteFloat = [, AllowInfNan[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AllowInfNan)(False)]

```

A float that must be finite (not `-inf`, `inf`, or `nan`).
```
from pydantic import BaseModel, FiniteFloat

class Model(BaseModel):
    finite: FiniteFloat

m = Model(finite=1.0)
print(m)
#> finite=1.0

```

###  StrictBytes `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictBytes)
```
StrictBytes = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

A bytes that must be validated in strict mode.
###  StrictStr `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StrictStr)
```
StrictStr = [, Strict[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)()]

```

A string that must be validated in strict mode.
###  UUID1 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID1)
```
UUID1 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(1)]

```

A
```
import uuid

from pydantic import UUID1, BaseModel

class Model(BaseModel):
    uuid1: UUID1

Model(uuid1=uuid.uuid1())

```

###  UUID3 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID3)
```
UUID3 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(3)]

```

A
```
import uuid

from pydantic import UUID3, BaseModel

class Model(BaseModel):
    uuid3: UUID3

Model(uuid3=uuid.uuid3(uuid.NAMESPACE_DNS, 'pydantic.org'))

```

###  UUID4 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID4)
```
UUID4 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(4)]

```

A
```
import uuid

from pydantic import UUID4, BaseModel

class Model(BaseModel):
    uuid4: UUID4

Model(uuid4=uuid.uuid4())

```

###  UUID5 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID5)
```
UUID5 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(5)]

```

A
```
import uuid

from pydantic import UUID5, BaseModel

class Model(BaseModel):
    uuid5: UUID5

Model(uuid5=uuid.uuid5(uuid.NAMESPACE_DNS, 'pydantic.org'))

```

###  UUID6 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID6)
```
UUID6 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(6)]

```

A
```
import uuid

from pydantic import UUID6, BaseModel

class Model(BaseModel):
    uuid6: UUID6

Model(uuid6=uuid.UUID('1efea953-c2d6-6790-aa0a-69db8c87df97'))

```

###  UUID7 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID7)
```
UUID7 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(7)]

```

A
```
import uuid

from pydantic import UUID7, BaseModel

class Model(BaseModel):
    uuid7: UUID7

Model(uuid7=uuid.UUID('0194fdcb-1c47-7a09-b52c-561154de0b4a'))

```

###  UUID8 `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UUID8)
```
UUID8 = [, UuidVersion[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)(8)]

```

A
```
import uuid

from pydantic import UUID8, BaseModel

class Model(BaseModel):
    uuid8: UUID8

Model(uuid8=uuid.UUID('81a0b92e-6078-8551-9c81-8ccb666bdab8'))

```

###  FilePath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FilePath)
```
FilePath = [, PathType('file')]

```

A path that must point to a file.
```
from pathlib import Path

from pydantic import BaseModel, FilePath, ValidationError

class Model(BaseModel):
    f: FilePath

path = Path('text.txt')
path.touch()
m = Model(f='text.txt')
print(m.model_dump())
#> {'f': PosixPath('text.txt')}
path.unlink()

path = Path('directory')
path.mkdir(exist_ok=True)
try:
    Model(f='directory')  # directory
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a file [type=path_not_file, input_value='directory', input_type=str]
    '''
path.rmdir()

try:
    Model(f='not-exists-file')
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a file [type=path_not_file, input_value='not-exists-file', input_type=str]
    '''

```

###  DirectoryPath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.DirectoryPath)
```
DirectoryPath = [, PathType('dir')]

```

A path that must point to a directory.
```
from pathlib import Path

from pydantic import BaseModel, DirectoryPath, ValidationError

class Model(BaseModel):
    f: DirectoryPath

path = Path('directory/')
path.mkdir()
m = Model(f='directory/')
print(m.model_dump())
#> {'f': PosixPath('directory')}
path.rmdir()

path = Path('file.txt')
path.touch()
try:
    Model(f='file.txt')  # file
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a directory [type=path_not_directory, input_value='file.txt', input_type=str]
    '''
path.unlink()

try:
    Model(f='not-exists-directory')
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    f
      Path does not point to a directory [type=path_not_directory, input_value='not-exists-directory', input_type=str]
    '''

```

###  NewPath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.NewPath)
```
NewPath = [, PathType('new')]

```

A path for a new file or directory that must not already exist. The parent directory must already exist.
###  SocketPath `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SocketPath)
```
SocketPath = [, PathType('socket')]

```

A path to an existing socket file
###  Base64Bytes `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Bytes)
```
Base64Bytes = [
    , EncodedBytes[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes)(encoder=Base64Encoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder))
]

```

A bytes type that is encoded and decoded using the standard (non-URL-safe) base64 encoder.
Note
Under the hood, `Base64Bytes` uses the standard library `base64.b64encode` and `base64.b64decode` functions.
As a result, attempting to decode url-safe base64 data using the `Base64Bytes` type may fail or produce an incorrect decoding.
Warning
In versions of Pydantic prior to v2.10, `Base64Bytes` used
If you'd still like to use these legacy encoders / decoders, you can achieve this by creating a custom annotated type, like follows:
```
import base64
from typing import Annotated, Literal

from pydantic_core import PydanticCustomError

from pydantic import EncodedBytes, EncoderProtocol

class LegacyBase64Encoder(EncoderProtocol):
    @classmethod
    def decode(cls, data: bytes) -> bytes:
        try:
            return base64.decodebytes(data)
        except ValueError as e:
            raise PydanticCustomError(
                'base64_decode',
                "Base64 decoding error: '{error}'",
                {'error': str(e)},
            )

    @classmethod
    def encode(cls, value: bytes) -> bytes:
        return base64.encodebytes(value)

    @classmethod
    def get_json_format(cls) -> Literal['base64']:
        return 'base64'

LegacyBase64Bytes = Annotated[bytes, EncodedBytes(encoder=LegacyBase64Encoder)]

```

```
from pydantic import Base64Bytes, BaseModel, ValidationError

class Model(BaseModel):
    base64_bytes: Base64Bytes

# Initialize the model with base64 data
m = Model(base64_bytes=b'VGhpcyBpcyB0aGUgd2F5')

# Access decoded value
print(m.base64_bytes)
#> b'This is the way'

# Serialize into the base64 form
print(m.model_dump())
#> {'base64_bytes': b'VGhpcyBpcyB0aGUgd2F5'}

# Validate base64 data
try:
    print(Model(base64_bytes=b'undecodable').base64_bytes)
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    base64_bytes
      Base64 decoding error: 'Incorrect padding' [type=base64_decode, input_value=b'undecodable', input_type=bytes]
    '''

```

###  Base64Str `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Str)
```
Base64Str = [
    , EncodedStr[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr)(encoder=Base64Encoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Encoder))
]

```

A str type that is encoded and decoded using the standard (non-URL-safe) base64 encoder.
Note
Under the hood, `Base64Str` uses the standard library `base64.b64encode` and `base64.b64decode` functions.
As a result, attempting to decode url-safe base64 data using the `Base64Str` type may fail or produce an incorrect decoding.
Warning
In versions of Pydantic prior to v2.10, `Base64Str` used
See the [`Base64Bytes`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64Bytes) type for more information on how to replicate the old behavior with the legacy encoders / decoders.
```
from pydantic import Base64Str, BaseModel, ValidationError

class Model(BaseModel):
    base64_str: Base64Str

# Initialize the model with base64 data
m = Model(base64_str='VGhlc2UgYXJlbid0IHRoZSBkcm9pZHMgeW91J3JlIGxvb2tpbmcgZm9y')

# Access decoded value
print(m.base64_str)
#> These aren't the droids you're looking for

# Serialize into the base64 form
print(m.model_dump())
#> {'base64_str': 'VGhlc2UgYXJlbid0IHRoZSBkcm9pZHMgeW91J3JlIGxvb2tpbmcgZm9y'}

# Validate base64 data
try:
    print(Model(base64_str='undecodable').base64_str)
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    base64_str
      Base64 decoding error: 'Incorrect padding' [type=base64_decode, input_value='undecodable', input_type=str]
    '''

```

###  Base64UrlBytes `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlBytes)
```
Base64UrlBytes = [
    , EncodedBytes[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedBytes)(encoder=Base64UrlEncoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder))
]

```

A bytes type that is encoded and decoded using the URL-safe base64 encoder.
Note
Under the hood, `Base64UrlBytes` use standard library `base64.urlsafe_b64encode` and `base64.urlsafe_b64decode` functions.
As a result, the `Base64UrlBytes` type can be used to faithfully decode "vanilla" base64 data (using `'+'` and `'/'`).
```
from pydantic import Base64UrlBytes, BaseModel

class Model(BaseModel):
    base64url_bytes: Base64UrlBytes

# Initialize the model with base64 data
m = Model(base64url_bytes=b'SHc_dHc-TXc==')
print(m)
#> base64url_bytes=b'Hw?tw>Mw'

```

###  Base64UrlStr `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlStr)
```
Base64UrlStr = [
    , EncodedStr[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.EncodedStr)(encoder=Base64UrlEncoder[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Base64UrlEncoder))
]

```

A str type that is encoded and decoded using the URL-safe base64 encoder.
Note
Under the hood, `Base64UrlStr` use standard library `base64.urlsafe_b64encode` and `base64.urlsafe_b64decode` functions.
As a result, the `Base64UrlStr` type can be used to faithfully decode "vanilla" base64 data (using `'+'` and `'/'`).
```
from pydantic import Base64UrlStr, BaseModel

class Model(BaseModel):
    base64url_str: Base64UrlStr

# Initialize the model with base64 data
m = Model(base64url_str='SHc_dHc-TXc==')
print(m)
#> base64url_str='Hw?tw>Mw'

```

###  JsonValue `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.JsonValue)
```
JsonValue:  = [
    ["JsonValue"],
    [, "JsonValue"],
    ,
    ,
    ,
    ,
    None,
]

```

A `JsonValue` is used to represent a value that can be serialized to JSON.
It may be one of:
  * `list['JsonValue']`
  * `dict[str, 'JsonValue']`
  * `str`
  * `bool`
  * `int`
  * `float`
  * `None`


The following example demonstrates how to use `JsonValue` to validate JSON data, and what kind of errors to expect when input data is not json serializable.
```
import json

from pydantic import BaseModel, JsonValue, ValidationError

class Model(BaseModel):
    j: JsonValue

valid_json_data = {'j': {'a': {'b': {'c': 1, 'd': [2, None]}}}}
invalid_json_data = {'j': {'a': {'b': ...}}}

print(repr(Model.model_validate(valid_json_data)))
#> Model(j={'a': {'b': {'c': 1, 'd': [2, None]}}})
print(repr(Model.model_validate_json(json.dumps(valid_json_data))))
#> Model(j={'a': {'b': {'c': 1, 'd': [2, None]}}})

try:
    Model.model_validate(invalid_json_data)
except ValidationError as e:
    print(e)
    '''
    1 validation error for Model
    j.dict.a.dict.b
      input was not a valid JSON value [type=invalid-json-value, input_value=Ellipsis, input_type=ellipsis]
    '''

```

###  OnErrorOmit `module-attribute` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.OnErrorOmit)
```
OnErrorOmit = [T, _OnErrorOmit]

```

When used as an item in a list, the key type in a dict, optional values of a TypedDict, etc. this annotation omits the item from the iteration if there is any error validating it. That is, instead of a [`ValidationError`](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.ValidationError) being propagated up and the entire iterable being discarded any invalid items are discarded and the valid ones are returned.
###  Strict `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Strict)
Bases: `PydanticMetadata`, `BaseMetadata`
Usage Documentation
[Strict Mode with `Annotated` `Strict`](https://docs.pydantic.dev/latest/concepts/strict_mode/#strict-mode-with-annotated-strict)
A field metadata class to indicate that a field should be validated in strict mode. Use this class as an annotation via
Attributes:
Name | Type | Description
---|---|---
`strict` |  |  Whether to validate the field in strict mode.
Example
```
from typing import Annotated

from pydantic.types import Strict

StrictBool = Annotated[bool, Strict()]

```

Source code in `pydantic/types.py`
```
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
139
140
```
| ```
@_dataclasses.dataclass
class Strict(_fields.PydanticMetadata, BaseMetadata):
    """!!! abstract "Usage Documentation"
        [Strict Mode with `Annotated` `Strict`](../concepts/strict_mode.md#strict-mode-with-annotated-strict)

    A field metadata class to indicate that a field should be validated in strict mode.
    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        strict: Whether to validate the field in strict mode.

    Example:
    ```python
        from typing import Annotated

        from pydantic.types import Strict

        StrictBool = Annotated[bool, Strict()]
    ```
    """

    strict: bool = True

    def __hash__(self) -> int:
        return hash(self.strict)

```

---|---
###  AllowInfNan `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AllowInfNan)
Bases: `PydanticMetadata`
A field metadata class to indicate that a field should allow `-inf`, `inf`, and `nan`.
Use this class as an annotation via
Attributes:
Name | Type | Description
---|---|---
`allow_inf_nan` |  |  Whether to allow `-inf`, `inf`, and `nan`. Defaults to `True`.
Example
```
from typing import Annotated

from pydantic.types import AllowInfNan

LaxFloat = Annotated[float, AllowInfNan()]

```

Source code in `pydantic/types.py`
```
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
```
| ```
@_dataclasses.dataclass
class AllowInfNan(_fields.PydanticMetadata):
    """A field metadata class to indicate that a field should allow `-inf`, `inf`, and `nan`.

    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        allow_inf_nan: Whether to allow `-inf`, `inf`, and `nan`. Defaults to `True`.

    Example:
    ```python
        from typing import Annotated

        from pydantic.types import AllowInfNan

        LaxFloat = Annotated[float, AllowInfNan()]
    ```
    """

    allow_inf_nan: bool = True

    def __hash__(self) -> int:
        return hash(self.allow_inf_nan)

```

---|---
###  StringConstraints `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.StringConstraints)
Bases: `GroupedMetadata`
Usage Documentation
[String types](https://docs.pydantic.dev/latest/api/standard_library_types/#strings)
A field metadata class to apply constraints to `str` types. Use this class as an annotation via
Attributes:
Name | Type | Description
---|---|---
`strip_whitespace` |  |  Whether to remove leading and trailing whitespace.
`to_upper` |  |  Whether to convert the string to uppercase.
`to_lower` |  |  Whether to convert the string to lowercase.
`strict` |  |  Whether to validate the string in strict mode.
`min_length` |  |  The minimum length of the string.
`max_length` |  |  The maximum length of the string.
`pattern` |  |  A regex pattern that the string must match.
Example
```
from typing import Annotated

from pydantic.types import StringConstraints

ConstrainedStr = Annotated[str, StringConstraints(min_length=1, max_length=10)]

```

Source code in `pydantic/types.py`
```
693
694
695
696
697
698
699
700
701
702
703
704
705
706
707
708
709
710
711
712
713
714
715
716
717
718
719
720
721
722
723
724
725
726
727
728
729
730
731
732
733
734
735
736
737
738
739
740
741
742
743
744
745
746
```
| ```
@_dataclasses.dataclass(frozen=True)
class StringConstraints(annotated_types.GroupedMetadata):
    """!!! abstract "Usage Documentation"
        [String types](./standard_library_types.md#strings)

    A field metadata class to apply constraints to `str` types.
    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        strip_whitespace: Whether to remove leading and trailing whitespace.
        to_upper: Whether to convert the string to uppercase.
        to_lower: Whether to convert the string to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern that the string must match.

    Example:
    ```python
        from typing import Annotated

        from pydantic.types import StringConstraints

        ConstrainedStr = Annotated[str, StringConstraints(min_length=1, max_length=10)]
    ```
    """

    strip_whitespace: bool | None = None
    to_upper: bool | None = None
    to_lower: bool | None = None
    strict: bool | None = None
    min_length: int | None = None
    max_length: int | None = None
    pattern: str | Pattern[str] | None = None

    def __iter__(self) -> Iterator[BaseMetadata]:
        if self.min_length is not None:
            yield MinLen(self.min_length)
        if self.max_length is not None:
            yield MaxLen(self.max_length)
        if self.strict is not None:
            yield Strict(self.strict)
        if (
            self.strip_whitespace is not None
            or self.pattern is not None
            or self.to_lower is not None
            or self.to_upper is not None
        ):
            yield _fields.pydantic_general_metadata(
                strip_whitespace=self.strip_whitespace,
                to_upper=self.to_upper,
                to_lower=self.to_lower,
                pattern=self.pattern,
            )

```

---|---
###  ImportString [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ImportString)
A type that can be used to import a Python object from a string.
`ImportString` expects a string and loads the Python object importable at that dotted path. Attributes of modules may be separated from the module by `:` or `.`, e.g. if `'math:cos'` is provided, the resulting field value would be the function `cos`. If a `.` is used and both an attribute and submodule are present at the same path, the module will be preferred.
On model instantiation, pointers will be evaluated and imported. There is some nuance to this behavior, demonstrated in the examples below.
```
import math

from pydantic import BaseModel, Field, ImportString, ValidationError

class ImportThings(BaseModel):
    obj: ImportString
