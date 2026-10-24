# and that all values in ``z`` are meant to be either strings or ints
z: Mapping[str, str | int] = {}

```

[`list`](https://docs.python.org/3/library/stdtypes.html#list "list") only accepts one type argument, so a type checker would emit an error on the `y` assignment above. Similarly, [`Mapping`](https://docs.python.org/3/library/collections.abc.html#collections.abc.Mapping "collections.abc.Mapping") only accepts two type arguments: the first indicates the type of the keys, and the second indicates the type of the values.
Unlike most other Python containers, however, it is common in idiomatic Python code for tuples to have elements which are not all of the same type. For this reason, tuples are special-cased in Python’s typing system. [`tuple`](https://docs.python.org/3/library/stdtypes.html#tuple "tuple") accepts _any number_ of type arguments:
Copy```
# OK: ``x`` is assigned to a tuple of length 1 where the sole element is an int
x: tuple[int] = (5,)

# OK: ``y`` is assigned to a tuple of length 2;
# element 1 is an int, element 2 is a str
y: tuple[int, str] = (5, "foo")

# Error: the type annotation indicates a tuple of length 1,
# but ``z`` has been assigned to a tuple of length 3
z: tuple[int] = (1, 2, 3)

```

To denote a tuple which could be of _any_ length, and in which all elements are of the same type `T`, use the literal ellipsis `...`: `tuple[T, ...]`. To denote an empty tuple, use `tuple[()]`. Using plain `tuple` as an annotation is equivalent to using `tuple[Any, ...]`:
Copy```
x: tuple[int, ...] = (1, 2)
