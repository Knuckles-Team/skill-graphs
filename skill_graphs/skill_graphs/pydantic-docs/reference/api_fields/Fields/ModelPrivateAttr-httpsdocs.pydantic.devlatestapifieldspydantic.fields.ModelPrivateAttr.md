##  ModelPrivateAttr [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ModelPrivateAttr)
```
ModelPrivateAttr(
    default:  = PydanticUndefined,
    *,
    default_factory: [[], ] | None = None
)

```

Bases: `Representation`
A descriptor for private attributes in class models.
Warning
You generally shouldn't be creating `ModelPrivateAttr` instances directly, instead use `pydantic.fields.PrivateAttr`. (This is similar to `FieldInfo` vs. `Field`.)
Attributes:
Name | Type | Description
---|---|---
`default` |  |  The default value of the attribute if not provided.
`default_factory` |  |  A callable function that generates the default value of the attribute if not provided.
Source code in `pydantic/fields.py`
```
1415
1416
1417
1418
1419
1420
```
| ```
def __init__(self, default: Any = PydanticUndefined, *, default_factory: Callable[[], Any] | None = None) -> None:
    if default is Ellipsis:
        self.default = PydanticUndefined
    else:
        self.default = default
    self.default_factory = default_factory

```

---|---
###  __getattr__ [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ModelPrivateAttr.__getattr__)
```
__getattr__(item: ) ->

```

This function improves compatibility with custom descriptors by ensuring delegation happens as expected when the default value of a private attribute is a descriptor.
Source code in `pydantic/fields.py`
```
1425
1426
1427
1428
1429
1430
1431
1432
```
| ```
def __getattr__(self, item: str) -> Any:
    """This function improves compatibility with custom descriptors by ensuring delegation happens
    as expected when the default value of a private attribute is a descriptor.
    """
    if item in {'__get__', '__set__', '__delete__'}:
        if hasattr(self.default, item):
            return getattr(self.default, item)
    raise AttributeError(f'{type(self).__name__!r} object has no attribute {item!r}')

```

---|---
###  __set_name__ [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ModelPrivateAttr.__set_name__)
```
__set_name__(cls: [], name: ) -> None

```

Preserve `__set_name__` protocol defined in https://peps.python.org/pep-0487.
Source code in `pydantic/fields.py`
```
1434
1435
1436
1437
1438
1439
1440
1441
```
| ```
def __set_name__(self, cls: type[Any], name: str) -> None:
    """Preserve `__set_name__` protocol defined in https://peps.python.org/pep-0487."""
    default = self.default
    if default is PydanticUndefined:
        return
    set_name = getattr(default, '__set_name__', None)
    if callable(set_name):
        set_name(cls, name)

```

---|---
###  get_default [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ModelPrivateAttr.get_default)
```
get_default() ->

```

Retrieve the default value of the object.
If `self.default_factory` is `None`, the method will return a deep copy of the `self.default` object.
If `self.default_factory` is not `None`, it will call `self.default_factory` and return the value returned.
Returns:
Type | Description
---|---
|  The default value of the object.
Source code in `pydantic/fields.py`
```
1443
1444
1445
1446
1447
1448
1449
1450
1451
1452
1453
```
| ```
def get_default(self) -> Any:
    """Retrieve the default value of the object.

    If `self.default_factory` is `None`, the method will return a deep copy of the `self.default` object.

    If `self.default_factory` is not `None`, it will call `self.default_factory` and return the value returned.

    Returns:
        The default value of the object.
    """
    return _utils.smart_deepcopy(self.default) if self.default_factory is None else self.default_factory()

```

---|---
