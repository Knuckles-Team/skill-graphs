##  computed_field [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.computed_field)
```
computed_field(func: PropertyT) -> PropertyT

```

```
computed_field(
    *,
    alias:  | None = None,
    alias_priority:  | None = None,
    title:  | None = None,
    field_title_generator: (
        [[, ComputedFieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo)], ] | None
    ) = None,
    description:  | None = None,
    deprecated: Deprecated |  |  | None = None,
    examples: [] | None = None,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = None,
    repr:  = True,
    return_type:  = PydanticUndefined
) -> [[PropertyT], PropertyT]

```

```
computed_field(
    func: PropertyT | None = None,
    /,
    *,
    alias:  | None = None,
    alias_priority:  | None = None,
    title:  | None = None,
    field_title_generator: (
        [[, ComputedFieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo)], ] | None
    ) = None,
    description:  | None = None,
    deprecated: Deprecated |  |  | None = None,
    examples: [] | None = None,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ) = None,
    repr:  | None = None,
    return_type:  = PydanticUndefined,
) -> PropertyT | [[PropertyT], PropertyT]

```

Usage Documentation
[The `computed_field` decorator](https://docs.pydantic.dev/latest/concepts/fields/#the-computed_field-decorator)
Decorator to include `property` and `cached_property` when serializing models or dataclasses.
This is useful for fields that are computed from other fields, or for fields that are expensive to compute and should be cached.
```
from pydantic import BaseModel, computed_field

class Rectangle(BaseModel):
    width: int
    length: int

    @computed_field
    @property
    def area(self) -> int:
        return self.width * self.length

print(Rectangle(width=3, length=2).model_dump())
#> {'width': 3, 'length': 2, 'area': 6}

```

If applied to functions not yet decorated with `@property` or `@cached_property`, the function is automatically wrapped with `property`. Although this is more concise, you will lose IntelliSense in your IDE, and confuse static type checkers, thus explicit use of `@property` is recommended.
Mypy Warning
Even with the `@property` or `@cached_property` applied to your function before `@computed_field`, mypy may throw a `Decorated property not supported` error. See `# type: ignore[prop-decorator]` to the `@computed_field` line.
`@computed_field` without error.
```
import random

from pydantic import BaseModel, computed_field

class Square(BaseModel):
    width: float

    @computed_field
    def area(self) -> float:  # converted to a `property` by `computed_field`
        return round(self.width**2, 2)

    @area.setter
    def area(self, new_area: float) -> None:
        self.width = new_area**0.5

    @computed_field(alias='the magic number', repr=False)
    def random_number(self) -> int:
        return random.randint(0, 1_000)

square = Square(width=1.3)

# `random_number` does not appear in representation
print(repr(square))
#> Square(width=1.3, area=1.69)

print(square.random_number)
#> 3

square.area = 4

print(square.model_dump_json(by_alias=True))
#> {"width":2.0,"area":4.0,"the magic number":3}

```

Overriding with `computed_field`
You can't override a field from a parent class with a `computed_field` in the child class. `mypy` complains about this behavior if allowed, and `dataclasses` doesn't allow this pattern either. See the example below:
```
from pydantic import BaseModel, computed_field

class Parent(BaseModel):
    a: str

try:

    class Child(Parent):
        @computed_field
        @property
        def a(self) -> str:
            return 'new a'

except TypeError as e:
    print(e)
    '''
    Field 'a' of class 'Child' overrides symbol of same name in a parent class. This override with a computed_field is incompatible.
    '''

```

Private properties decorated with `@computed_field` have `repr=False` by default.
```
from functools import cached_property

from pydantic import BaseModel, computed_field

class Model(BaseModel):
    foo: int

    @computed_field
    @cached_property
    def _private_cached_property(self) -> int:
        return -self.foo

    @computed_field
    @property
    def _private_property(self) -> int:
        return -self.foo

m = Model(foo=1)
print(repr(m))
#> Model(foo=1)

```

Parameters:
Name | Type | Description | Default
---|---|---|---
`func` |  `PropertyT | None` |  the function to wrap. |  `None`
`alias` |  |  alias to use when serializing this computed field, only used when `by_alias=True` |  `None`
`alias_priority` |  |  priority of the alias. This affects whether an alias generator is used |  `None`
`title` |  |  Title to use when including this computed field in JSON Schema |  `None`
`field_title_generator` |  `ComputedFieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo)], ` |  A callable that takes a field name and returns title for it. |  `None`
`description` |  |  Description to use when including this computed field in JSON Schema, defaults to the function's docstring |  `None`
`deprecated` |  `Deprecated | ` |  A deprecation message (or an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport). to be emitted when accessing the field. Or a boolean. This will automatically be set if the property is decorated with the `deprecated` decorator. |  `None`
`examples` |  |  Example values to use when including this computed field in JSON Schema |  `None`
`json_schema_extra` |  `JsonDict | JsonDict], None] | None` |  A dict or callable to provide extra JSON schema properties. |  `None`
`repr` |  |  whether to include this computed field in model repr. Default is `False` for private properties and `True` for public properties. |  `None`
`return_type` |  |  optional return for serialization logic to expect when serializing to JSON, if included this must be correct, otherwise a `TypeError` is raised. If you don't include a return type Any is used, which does runtime introspection to handle arbitrary objects. |  `PydanticUndefined`
Returns:
Type | Description
---|---
`PropertyT | PropertyT], PropertyT]` |  A proxy wrapper for the property.
Source code in `pydantic/fields.py`
```
1637
1638
1639
1640
1641
1642
1643
1644
1645
1646
1647
1648
1649
1650
1651
1652
1653
1654
1655
1656
1657
1658
1659
1660
1661
1662
1663
1664
1665
1666
1667
1668
1669
1670
1671
1672
1673
1674
1675
1676
1677
1678
1679
1680
1681
1682
1683
1684
1685
1686
1687
1688
1689
1690
1691
1692
1693
1694
1695
1696
1697
1698
1699
1700
1701
1702
1703
1704
1705
1706
1707
1708
1709
1710
1711
1712
1713
1714
1715
1716
1717
1718
1719
1720
1721
1722
1723
1724
1725
1726
1727
1728
1729
1730
1731
1732
1733
1734
1735
1736
1737
1738
1739
1740
1741
1742
1743
1744
1745
1746
1747
1748
1749
1750
1751
1752
1753
1754
1755
1756
1757
1758
1759
1760
1761
1762
1763
1764
1765
1766
1767
1768
1769
1770
1771
1772
1773
1774
1775
1776
1777
1778
1779
1780
1781
1782
1783
1784
1785
1786
1787
1788
1789
1790
1791
1792
1793
1794
1795
1796
1797
1798
1799
1800
1801
1802
1803
1804
1805
1806
1807
1808
1809
1810
1811
1812
1813
1814
1815
1816
1817
1818
1819
1820
1821
1822
1823
1824
1825
1826
1827
1828
1829
1830
1831
1832
1833
1834
```
| ```
def computed_field(
    func: PropertyT | None = None,
    /,
    *,
    alias: str | None = None,
    alias_priority: int | None = None,
    title: str | None = None,
    field_title_generator: Callable[[str, ComputedFieldInfo], str] | None = None,
    description: str | None = None,
    deprecated: Deprecated | str | bool | None = None,
    examples: list[Any] | None = None,
    json_schema_extra: JsonDict | Callable[[JsonDict], None] | None = None,
    repr: bool | None = None,
    return_type: Any = PydanticUndefined,
) -> PropertyT | Callable[[PropertyT], PropertyT]:
    """!!! abstract "Usage Documentation"
        [The `computed_field` decorator](../concepts/fields.md#the-computed_field-decorator)

    Decorator to include `property` and `cached_property` when serializing models or dataclasses.

    This is useful for fields that are computed from other fields, or for fields that are expensive to compute and should be cached.

```python
    from pydantic import BaseModel, computed_field

    class Rectangle(BaseModel):
        width: int
        length: int

        @computed_field
        @property
        def area(self) -> int:
            return self.width * self.length

    print(Rectangle(width=3, length=2).model_dump())
    #> {'width': 3, 'length': 2, 'area': 6}
```

    If applied to functions not yet decorated with `@property` or `@cached_property`, the function is
    automatically wrapped with `property`. Although this is more concise, you will lose IntelliSense in your IDE,
    and confuse static type checkers, thus explicit use of `@property` is recommended.

    !!! warning "Mypy Warning"
        Even with the `@property` or `@cached_property` applied to your function before `@computed_field`,
        mypy may throw a `Decorated property not supported` error.
        See [mypy issue #1362](https://github.com/python/mypy/issues/1362), for more information.
        To avoid this error message, add `# type: ignore[prop-decorator]` to the `@computed_field` line.

        [pyright](https://github.com/microsoft/pyright) supports `@computed_field` without error.

```python
    import random

    from pydantic import BaseModel, computed_field

    class Square(BaseModel):
        width: float

        @computed_field
        def area(self) -> float:  # converted to a `property` by `computed_field`
            return round(self.width**2, 2)

        @area.setter
        def area(self, new_area: float) -> None:
            self.width = new_area**0.5

        @computed_field(alias='the magic number', repr=False)
        def random_number(self) -> int:
            return random.randint(0, 1_000)

    square = Square(width=1.3)

    # `random_number` does not appear in representation
    print(repr(square))
    #> Square(width=1.3, area=1.69)

    print(square.random_number)
    #> 3

    square.area = 4

    print(square.model_dump_json(by_alias=True))
    #> {"width":2.0,"area":4.0,"the magic number":3}
```

    !!! warning "Overriding with `computed_field`"
        You can't override a field from a parent class with a `computed_field` in the child class.
        `mypy` complains about this behavior if allowed, and `dataclasses` doesn't allow this pattern either.
        See the example below:

```python
    from pydantic import BaseModel, computed_field

    class Parent(BaseModel):
        a: str

    try:

        class Child(Parent):
            @computed_field
            @property
            def a(self) -> str:
                return 'new a'

    except TypeError as e:
        print(e)
        '''
        Field 'a' of class 'Child' overrides symbol of same name in a parent class. This override with a computed_field is incompatible.
        '''
```

    Private properties decorated with `@computed_field` have `repr=False` by default.

```python
    from functools import cached_property

    from pydantic import BaseModel, computed_field

    class Model(BaseModel):
        foo: int

        @computed_field
        @cached_property
        def _private_cached_property(self) -> int:
            return -self.foo

        @computed_field
        @property
        def _private_property(self) -> int:
            return -self.foo

    m = Model(foo=1)
    print(repr(m))
    #> Model(foo=1)
```

    Args:
        func: the function to wrap.
        alias: alias to use when serializing this computed field, only used when `by_alias=True`
        alias_priority: priority of the alias. This affects whether an alias generator is used
        title: Title to use when including this computed field in JSON Schema
        field_title_generator: A callable that takes a field name and returns title for it.
        description: Description to use when including this computed field in JSON Schema, defaults to the function's
            docstring
        deprecated: A deprecation message (or an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport).
            to be emitted when accessing the field. Or a boolean. This will automatically be set if the property is decorated with the
            `deprecated` decorator.
        examples: Example values to use when including this computed field in JSON Schema
        json_schema_extra: A dict or callable to provide extra JSON schema properties.
        repr: whether to include this computed field in model repr.
            Default is `False` for private properties and `True` for public properties.
        return_type: optional return for serialization logic to expect when serializing to JSON, if included
            this must be correct, otherwise a `TypeError` is raised.
            If you don't include a return type Any is used, which does runtime introspection to handle arbitrary
            objects.

    Returns:
        A proxy wrapper for the property.
    """

    def dec(f: Any) -> Any:
        nonlocal description, deprecated, return_type, alias_priority
        unwrapped = _decorators.unwrap_wrapped_function(f)

        if description is None and unwrapped.__doc__:
            description = inspect.cleandoc(unwrapped.__doc__)

        if deprecated is None and hasattr(unwrapped, '__deprecated__'):
            deprecated = unwrapped.__deprecated__

        # if the function isn't already decorated with `@property` (or another descriptor), then we wrap it now
        f = _decorators.ensure_property(f)
        alias_priority = (alias_priority or 2) if alias is not None else None

        if repr is None:
            repr_: bool = not _wrapped_property_is_private(property_=f)
        else:
            repr_ = repr

        dec_info = ComputedFieldInfo(
            f,
            return_type,
            alias,
            alias_priority,
            title,
            field_title_generator,
            description,
            deprecated,
            examples,
            json_schema_extra,
            repr_,
        )
        return _decorators.PydanticDescriptorProxy(f, dec_info)

    if func is None:
        return dec
    else:
        return dec(func)

```

---|---
##  ComputedFieldInfo `dataclass` [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo)
```
ComputedFieldInfo(
    wrapped_property: ,
    return_type: ,
    alias:  | None,
    alias_priority:  | None,
    title:  | None,
    field_title_generator: (
        [[, ComputedFieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo)], ] | None
    ),
    description:  | None,
    deprecated: Deprecated |  |  | None,
    examples: [] | None,
    json_schema_extra: (
        JsonDict | [[JsonDict], None] | None
    ),
    repr: ,
)

```

A container for data from `@computed_field` so that we can access it while building the pydantic-core schema.
Attributes:
Name | Type | Description
---|---|---
`decorator_repr` |  |  A class variable representing the decorator string, '@computed_field'.
`wrapped_property` |  |  The wrapped computed field property.
`return_type` |  |  The type of the computed field property's return value.
`alias` |  |  The alias of the property to be used during serialization.
`alias_priority` |  |  The priority of the alias. This affects whether an alias generator is used.
`title` |  |  Title of the computed field to include in the serialization JSON schema.
`field_title_generator` |  `ComputedFieldInfo[](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo)], ` |  A callable that takes a field name and returns title for it.
`description` |  |  Description of the computed field to include in the serialization JSON schema.
`deprecated` |  `Deprecated | ` |  A deprecation message, an instance of `warnings.deprecated` or the `typing_extensions.deprecated` backport, or a boolean. If `True`, a default deprecation message will be emitted when accessing the field.
`examples` |  |  Example values of the computed field to include in the serialization JSON schema.
`json_schema_extra` |  `JsonDict | JsonDict], None] | None` |  A dict or callable to provide extra JSON schema properties.
`repr` |  |  A boolean indicating whether to include the field in the **repr** output.
###  deprecation_message `property` [¶](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.ComputedFieldInfo.deprecation_message)
```
deprecation_message:  | None

```

The deprecation message to be emitted, or `None` if not set.
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
