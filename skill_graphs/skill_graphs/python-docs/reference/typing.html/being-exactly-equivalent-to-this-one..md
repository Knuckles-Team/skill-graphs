# being exactly equivalent to this one.
def broadcast_message(
    message: str,
    servers: Sequence[tuple[tuple[str, int], dict[str, str]]]
) -> None:
    ...

```

The [`type`](https://docs.python.org/3/reference/simple_stmts.html#type) statement is new in Python 3.12. For backwards compatibility, type aliases can also be created through simple assignment:
Copy```
Vector = list[float]

```

Or marked with [`TypeAlias`](https://docs.python.org/3/library/typing.html#typing.TypeAlias "typing.TypeAlias") to make it explicit that this is a type alias, not a normal variable assignment:
Copy```
from typing import TypeAlias

Vector: TypeAlias = list[float]

```

## NewType[¶](https://docs.python.org/3/library/typing.html#newtype "Link to this heading")
Use the [`NewType`](https://docs.python.org/3/library/typing.html#typing.NewType "typing.NewType") helper to create distinct types:
Copy```
from typing import NewType

UserId = NewType('UserId', int)
some_id = UserId(524313)

```

The static type checker will treat the new type as if it were a subclass of the original type. This is useful in helping catch logical errors:
Copy```
def get_user_name(user_id: UserId) -> str:
    ...
