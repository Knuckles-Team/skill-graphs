#  `typing` — Support for type hints[¶](https://docs.python.org/3/library/typing.html#typing-support-for-type-hints "Link to this heading")
Added in version 3.5.
**Source code:**
Note
The Python runtime does not enforce function and variable type annotations. They can be used by third party tools such as [type checkers](https://docs.python.org/3/glossary.html#term-static-type-checker), IDEs, linters, etc.
* * *
This module provides runtime support for type hints.
Consider the function below:
Copy```
def surface_area_of_cube(edge_length: float) -> str:
    return f"The surface area of the cube is {6 * edge_length ** 2}."

```

The function `surface_area_of_cube` takes an argument expected to be an instance of [`float`](https://docs.python.org/3/library/functions.html#float "float"), as indicated by the [type hint](https://docs.python.org/3/glossary.html#term-type-hint) `edge_length: float`. The function is expected to return an instance of [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), as indicated by the `-> str` hint.
While type hints can be simple classes like [`float`](https://docs.python.org/3/library/functions.html#float "float") or [`str`](https://docs.python.org/3/library/stdtypes.html#str "str"), they can also be more complex. The [`typing`](https://docs.python.org/3/library/typing.html#module-typing "typing: Support for type hints \(see :pep:`484`\).") module provides a vocabulary of more advanced type hints.
New features are frequently added to the `typing` module. The
See also
A quick overview of type hints (hosted at the mypy docs)

Type System Reference section of

The Python typing system is standardised via PEPs, so this reference should broadly apply to most Python type checkers. (Some parts may still be specific to mypy.)

[Static Typing with Python](https://typing.python.org/en/latest/)

Type-checker-agnostic documentation written by the community detailing type system features, useful typing related tools and typing best practices.
## Specification for the Python Type System[¶](https://docs.python.org/3/library/typing.html#specification-for-the-python-type-system "Link to this heading")
The canonical, up-to-date specification of the Python type system can be found at [Specification for the Python type system](https://typing.python.org/en/latest/spec/index.html).
## Type aliases[¶](https://docs.python.org/3/library/typing.html#type-aliases "Link to this heading")
A type alias is defined using the [`type`](https://docs.python.org/3/reference/simple_stmts.html#type) statement, which creates an instance of [`TypeAliasType`](https://docs.python.org/3/library/typing.html#typing.TypeAliasType "typing.TypeAliasType"). In this example, `Vector` and `list[float]` will be treated equivalently by static type checkers:
Copy```
type Vector = list[float]

def scale(scalar: float, vector: Vector) -> Vector:
    return [scalar * num for num in vector]

# passes type checking; a list of floats qualifies as a Vector.
new_vector = scale(2.0, [1.0, -4.2, 5.4])

```

Type aliases are useful for simplifying complex type signatures. For example:
Copy```
from collections.abc import Sequence

type ConnectionOptions = dict[str, str]
type Address = tuple[str, int]
type Server = tuple[Address, ConnectionOptions]

def broadcast_message(message: str, servers: Sequence[Server]) -> None:
    ...
