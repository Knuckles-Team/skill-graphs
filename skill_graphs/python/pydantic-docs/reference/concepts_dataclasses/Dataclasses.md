# Dataclasses
API Documentation
[`@pydantic.dataclasses.dataclass`](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.dataclass)

If you don't want to use Pydantic's [`BaseModel`](https://docs.pydantic.dev/latest/api/base_model/#pydantic.BaseModel) you can instead get the same data validation on standard
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_1_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_1_2)
```
from datetime import datetime
from typing import Optional

from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: Optional[datetime] = None


user = User(id='42', signup_ts='2032-06-21T12:00')
print(user)
"""
User(id=42, name='John Doe', signup_ts=datetime.datetime(2032, 6, 21, 12, 0))
"""

```

```
from datetime import datetime

from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    signup_ts: datetime | None = None


user = User(id='42', signup_ts='2032-06-21T12:00')
print(user)
"""
User(id=42, name='John Doe', signup_ts=datetime.datetime(2032, 6, 21, 12, 0))
"""

```

Note
Keep in mind that Pydantic dataclasses are **not** a replacement for [Pydantic models](https://docs.pydantic.dev/latest/concepts/models/). They provide a similar functionality to stdlib dataclasses with the addition of Pydantic validation.
There are cases where subclassing using Pydantic models is the better choice.
For more information and discussion see
Similarities between Pydantic dataclasses and models include support for:
  * [Configuration](https://docs.pydantic.dev/latest/concepts/dataclasses/#dataclass-config) support
  * [Nested](https://docs.pydantic.dev/latest/concepts/models/#nested-models) classes
  * [Generics](https://docs.pydantic.dev/latest/concepts/models/#generic-models)


Some differences between Pydantic dataclasses and models include:
  * [validators](https://docs.pydantic.dev/latest/concepts/dataclasses/#validators-and-initialization-hooks)
  * The behavior with the [`extra`](https://docs.pydantic.dev/latest/api/config/#pydantic.config.ConfigDict.extra) configuration value


Similarly to Pydantic models, arguments used to instantiate the dataclass are [copied](https://docs.pydantic.dev/latest/concepts/models/#attribute-copies).
To make use of the [various methods](https://docs.pydantic.dev/latest/concepts/models/#model-methods-and-properties) to validate, dump and generate a JSON Schema, you can wrap the dataclass with a [`TypeAdapter`](https://docs.pydantic.dev/latest/api/type_adapter/#pydantic.type_adapter.TypeAdapter) and make use of its methods.
You can use both the Pydantic's [`Field()`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) and the stdlib's
[Python 3.9 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_2_1)[Python 3.10 and above](https://docs.pydantic.dev/latest/concepts/dataclasses/#__tabbed_2_2)
```
import dataclasses
from typing import Optional

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    friends: list[int] = dataclasses.field(default_factory=lambda: [0])
    age: Optional[int] = dataclasses.field(
        default=None,
        metadata={'title': 'The age of the user', 'description': 'do not lie!'},
    )
    height: Optional[int] = Field(
        default=None, title='The height in cm', ge=50, le=300
    )


user = User(id='42', height='250')
print(user)
#> User(id=42, name='John Doe', friends=[0], age=None, height=250)

```

```
import dataclasses

from pydantic import Field
from pydantic.dataclasses import dataclass


@dataclass
class User:
    id: int
    name: str = 'John Doe'
    friends: list[int] = dataclasses.field(default_factory=lambda: [0])
    age: int | None = dataclasses.field(
        default=None,
        metadata={'title': 'The age of the user', 'description': 'do not lie!'},
    )
    height: int | None = Field(
        default=None, title='The height in cm', ge=50, le=300
    )


user = User(id='42', height='250')
print(user)
#> User(id=42, name='John Doe', friends=[0], age=None, height=250)

```

The Pydantic [`@dataclass`](https://docs.pydantic.dev/latest/api/dataclasses/#pydantic.dataclasses.dataclass) decorator accepts the same arguments as the standard decorator, with the addition of a `config` parameter.
