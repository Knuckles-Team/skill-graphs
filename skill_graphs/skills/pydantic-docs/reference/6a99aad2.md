    min_length: int | None = None,
    max_length: int | None = None,
    pattern: str | Pattern[str] | None = None,
) -> type[str]:
    """
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`StringConstraints`][pydantic.types.StringConstraints] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `constr` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, constr

            class Foo(BaseModel):
                bar: constr(strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$')
        ```

        === ":white_check_mark: Do this"
        ```python
            from typing import Annotated

            from pydantic import BaseModel, StringConstraints

            class Foo(BaseModel):
                bar: Annotated[
                    str,
                    StringConstraints(
                        strip_whitespace=True, to_upper=True, pattern=r'^[A-Z]+$'
                    ),
                ]
        ```

    A wrapper around `str` that allows for additional constraints.

```python
    from pydantic import BaseModel, constr

    class Foo(BaseModel):
        bar: constr(strip_whitespace=True, to_upper=True)

    foo = Foo(bar='  hello  ')
    print(foo)
    #> bar='HELLO'
```

    Args:
        strip_whitespace: Whether to remove leading and trailing whitespace.
        to_upper: Whether to turn all characters to uppercase.
        to_lower: Whether to turn all characters to lowercase.
        strict: Whether to validate the string in strict mode.
        min_length: The minimum length of the string.
        max_length: The maximum length of the string.
        pattern: A regex pattern to validate the string against.

    Returns:
        The wrapped string type.
    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        str,
        StringConstraints(
            strip_whitespace=strip_whitespace,
            to_upper=to_upper,
            to_lower=to_lower,
            strict=strict,
            min_length=min_length,
            max_length=max_length,
            pattern=pattern,
        ),
    ]

```

---|---
###  conset [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conset)
```
conset(
    item_type: [HashableItemType],
    *,
    min_length:  | None = None,
    max_length:  | None = None
) -> [[HashableItemType]]

```

A wrapper around `typing.Set` that allows for additional constraints.
Parameters:
Name | Type | Description | Default
---|---|---|---
`item_type` |  `HashableItemType]` |  The type of the items in the set. |  _required_
`min_length` |  |  The minimum length of the set. |  `None`
`max_length` |  |  The maximum length of the set. |  `None`
Returns:
Type | Description
---|---
`HashableItemType]]` |  The wrapped set type.
Source code in `pydantic/types.py`
```
839
840
841
842
843
844
845
846
847
848
849
850
851
852
```
| ```
def conset(
    item_type: type[HashableItemType], *, min_length: int | None = None, max_length: int | None = None
) -> type[set[HashableItemType]]:
    """A wrapper around `typing.Set` that allows for additional constraints.

    Args:
        item_type: The type of the items in the set.
        min_length: The minimum length of the set.
        max_length: The maximum length of the set.

    Returns:
        The wrapped set type.
    """
    return Annotated[set[item_type], annotated_types.Len(min_length or 0, max_length)]  # pyright: ignore[reportReturnType]

```

---|---
###  confrozenset [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.confrozenset)
```
confrozenset(
    item_type: [HashableItemType],
    *,
    min_length:  | None = None,
    max_length:  | None = None
) -> [[HashableItemType]]

```

A wrapper around `typing.FrozenSet` that allows for additional constraints.
Parameters:
Name | Type | Description | Default
---|---|---|---
`item_type` |  `HashableItemType]` |  The type of the items in the frozenset. |  _required_
`min_length` |  |  The minimum length of the frozenset. |  `None`
`max_length` |  |  The maximum length of the frozenset. |  `None`
Returns:
Type | Description
---|---
`HashableItemType]]` |  The wrapped frozenset type.
Source code in `pydantic/types.py`
```
855
856
857
858
859
860
861
862
863
864
865
866
867
868
```
| ```
def confrozenset(
    item_type: type[HashableItemType], *, min_length: int | None = None, max_length: int | None = None
) -> type[frozenset[HashableItemType]]:
    """A wrapper around `typing.FrozenSet` that allows for additional constraints.

    Args:
        item_type: The type of the items in the frozenset.
        min_length: The minimum length of the frozenset.
        max_length: The maximum length of the frozenset.

    Returns:
        The wrapped frozenset type.
    """
    return Annotated[frozenset[item_type], annotated_types.Len(min_length or 0, max_length)]  # pyright: ignore[reportReturnType]

```

---|---
###  conlist [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.conlist)
```
conlist(
    item_type: [AnyItemType],
    *,
    min_length:  | None = None,
    max_length:  | None = None,
    unique_items:  | None = None
) -> [[AnyItemType]]

```

A wrapper around
Parameters:
Name | Type | Description | Default
---|---|---|---
`item_type` |  `AnyItemType]` |  The type of the items in the list. |  _required_
`min_length` |  |  The minimum length of the list. Defaults to None. |  `None`
`max_length` |  |  The maximum length of the list. Defaults to None. |  `None`
`unique_items` |  |  Whether the items in the list must be unique. Defaults to None. Warning The `unique_items` parameter is deprecated, use `Set` instead. See  |  `None`
Returns:
Type | Description
---|---
`AnyItemType]]` |  The wrapped list type.
Source code in `pydantic/types.py`
```
874
875
876
877
878
879
880
881
882
883
884
885
886
887
888
889
890
891
892
893
894
895
896
897
898
899
900
901
902
903
```
| ```
def conlist(
    item_type: type[AnyItemType],
    *,
    min_length: int | None = None,
    max_length: int | None = None,
    unique_items: bool | None = None,
) -> type[list[AnyItemType]]:
    """A wrapper around [`list`][] that adds validation.

    Args:
        item_type: The type of the items in the list.
        min_length: The minimum length of the list. Defaults to None.
        max_length: The maximum length of the list. Defaults to None.
        unique_items: Whether the items in the list must be unique. Defaults to None.
            !!! warning Deprecated
                The `unique_items` parameter is deprecated, use `Set` instead.
                See [this issue](https://github.com/pydantic/pydantic-core/issues/296) for more details.

    Returns:
        The wrapped list type.
    """
    if unique_items is not None:
        raise PydanticUserError(
            (
                '`unique_items` is removed, use `Set` instead'
                '(this feature is discussed in https://github.com/pydantic/pydantic-core/issues/296)'
            ),
            code='removed-kwargs',
        )
    return Annotated[list[item_type], annotated_types.Len(min_length or 0, max_length)]  # pyright: ignore[reportReturnType]

```

---|---
###  condecimal [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condecimal)
```
condecimal(
    *,
    strict:  | None = None,
    gt:  |  | None = None,
    ge:  |  | None = None,
    lt:  |  | None = None,
    le:  |  | None = None,
    multiple_of:  |  | None = None,
    max_digits:  | None = None,
    decimal_places:  | None = None,
    allow_inf_nan:  | None = None
) -> []

```

Discouraged
This function is **discouraged** in favor of using [`Field`](https://docs.pydantic.dev/latest/api/fields/#pydantic.fields.Field) instead.
This function will be **deprecated** in Pydantic 3.0.
The reason is that `condecimal` returns a type, which doesn't play well with static analysis tools.
[![❌](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/274c.svg) Don't do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condecimal--__tabbed_1_1)[![✅](https://cdn.jsdelivr.net/gh/jdecked/twemoji@15.1.0/assets/svg/2705.svg) Do this](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condecimal--__tabbed_1_2)
```
from pydantic import BaseModel, condecimal

class Foo(BaseModel):
    bar: condecimal(strict=True, allow_inf_nan=True)

```

```
from decimal import Decimal
from typing import Annotated

from pydantic import BaseModel, Field

class Foo(BaseModel):
    bar: Annotated[Decimal, Field(strict=True, allow_inf_nan=True)]

```

A wrapper around Decimal that adds validation.
Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether to validate the value in strict mode. Defaults to `None`. |  `None`
`gt` |  |  The value must be greater than this. Defaults to `None`. |  `None`
`ge` |  |  The value must be greater than or equal to this. Defaults to `None`. |  `None`
`lt` |  |  The value must be less than this. Defaults to `None`. |  `None`
`le` |  |  The value must be less than or equal to this. Defaults to `None`. |  `None`
`multiple_of` |  |  The value must be a multiple of this. Defaults to `None`. |  `None`
`max_digits` |  |  The maximum number of digits. Defaults to `None`. |  `None`
`decimal_places` |  |  The number of decimal places. Defaults to `None`. |  `None`
`allow_inf_nan` |  |  Whether to allow infinity and NaN. Defaults to `None`. |  `None`
```
from decimal import Decimal

from pydantic import BaseModel, ValidationError, condecimal

class ConstrainedExample(BaseModel):
    constrained_decimal: condecimal(gt=Decimal('1.0'))

m = ConstrainedExample(constrained_decimal=Decimal('1.1'))
print(repr(m))
#> ConstrainedExample(constrained_decimal=Decimal('1.1'))

try:
    ConstrainedExample(constrained_decimal=Decimal('0.9'))
except ValidationError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('constrained_decimal',),
            'msg': 'Input should be greater than 1.0',
            'input': Decimal('0.9'),
            'ctx': {'gt': Decimal('1.0')},
            'url': 'https://errors.pydantic.dev/2/v/greater_than',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
1040
1041
1042
1043
1044
1045
1046
1047
1048
1049
1050
1051
1052
1053
1054
1055
1056
1057
1058
1059
1060
1061
1062
1063
1064
1065
1066
1067
1068
1069
1070
1071
1072
1073
1074
1075
1076
1077
1078
1079
1080
1081
1082
1083
1084
1085
1086
1087
1088
1089
1090
1091
1092
1093
1094
1095
1096
1097
1098
1099
1100
1101
1102
1103
1104
1105
1106
1107
1108
1109
1110
1111
1112
1113
1114
1115
1116
1117
1118
1119
1120
1121
1122
1123
1124
1125
1126
1127
1128
1129
1130
1131
```
| ```
def condecimal(
    *,
    strict: bool | None = None,
    gt: int | Decimal | None = None,
    ge: int | Decimal | None = None,
    lt: int | Decimal | None = None,
    le: int | Decimal | None = None,
    multiple_of: int | Decimal | None = None,
    max_digits: int | None = None,
    decimal_places: int | None = None,
    allow_inf_nan: bool | None = None,
) -> type[Decimal]:
    """
    !!! warning "Discouraged"
        This function is **discouraged** in favor of using
        [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated) with
        [`Field`][pydantic.fields.Field] instead.

        This function will be **deprecated** in Pydantic 3.0.

        The reason is that `condecimal` returns a type, which doesn't play well with static analysis tools.

        === ":x: Don't do this"
        ```python
            from pydantic import BaseModel, condecimal

            class Foo(BaseModel):
                bar: condecimal(strict=True, allow_inf_nan=True)
        ```

        === ":white_check_mark: Do this"
        ```python
            from decimal import Decimal
            from typing import Annotated

            from pydantic import BaseModel, Field

            class Foo(BaseModel):
                bar: Annotated[Decimal, Field(strict=True, allow_inf_nan=True)]
        ```

    A wrapper around Decimal that adds validation.

    Args:
        strict: Whether to validate the value in strict mode. Defaults to `None`.
        gt: The value must be greater than this. Defaults to `None`.
        ge: The value must be greater than or equal to this. Defaults to `None`.
        lt: The value must be less than this. Defaults to `None`.
        le: The value must be less than or equal to this. Defaults to `None`.
        multiple_of: The value must be a multiple of this. Defaults to `None`.
        max_digits: The maximum number of digits. Defaults to `None`.
        decimal_places: The number of decimal places. Defaults to `None`.
        allow_inf_nan: Whether to allow infinity and NaN. Defaults to `None`.

```python
    from decimal import Decimal

    from pydantic import BaseModel, ValidationError, condecimal

    class ConstrainedExample(BaseModel):
        constrained_decimal: condecimal(gt=Decimal('1.0'))

    m = ConstrainedExample(constrained_decimal=Decimal('1.1'))
    print(repr(m))
    #> ConstrainedExample(constrained_decimal=Decimal('1.1'))

    try:
        ConstrainedExample(constrained_decimal=Decimal('0.9'))
    except ValidationError as e:
        print(e.errors())
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('constrained_decimal',),
                'msg': 'Input should be greater than 1.0',
                'input': Decimal('0.9'),
                'ctx': {'gt': Decimal('1.0')},
                'url': 'https://errors.pydantic.dev/2/v/greater_than',
            }
        ]
        '''
```
    """  # noqa: D212
    return Annotated[  # pyright: ignore[reportReturnType]
        Decimal,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
        annotated_types.MultipleOf(multiple_of) if multiple_of is not None else None,
        _fields.pydantic_general_metadata(max_digits=max_digits, decimal_places=decimal_places),
        AllowInfNan(allow_inf_nan) if allow_inf_nan is not None else None,
    ]

```

---|---
###  condate [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.condate)
```
condate(
    *,
    strict:  | None = None,
    gt:  | None = None,
    ge:  | None = None,
    lt:  | None = None,
    le:  | None = None
) -> []

```

A wrapper for date that adds constraints.
Parameters:
Name | Type | Description | Default
---|---|---|---
`strict` |  |  Whether to validate the date value in strict mode. Defaults to `None`. |  `None`
`gt` |  |  The value must be greater than this. Defaults to `None`. |  `None`
`ge` |  |  The value must be greater than or equal to this. Defaults to `None`. |  `None`
`lt` |  |  The value must be less than this. Defaults to `None`. |  `None`
`le` |  |  The value must be less than or equal to this. Defaults to `None`. |  `None`
Returns:
Type | Description
---|---
|  A date type with the specified constraints.
Source code in `pydantic/types.py`
```
2237
2238
2239
2240
2241
2242
2243
2244
2245
2246
2247
2248
2249
2250
2251
2252
2253
2254
2255
2256
2257
2258
2259
2260
2261
```
| ```
def condate(
    *,
    strict: bool | None = None,
    gt: date | None = None,
    ge: date | None = None,
    lt: date | None = None,
    le: date | None = None,
) -> type[date]:
    """A wrapper for date that adds constraints.

    Args:
        strict: Whether to validate the date value in strict mode. Defaults to `None`.
        gt: The value must be greater than this. Defaults to `None`.
        ge: The value must be greater than or equal to this. Defaults to `None`.
        lt: The value must be less than this. Defaults to `None`.
        le: The value must be less than or equal to this. Defaults to `None`.

    Returns:
        A date type with the specified constraints.
    """
    return Annotated[  # pyright: ignore[reportReturnType]
        date,
        Strict(strict) if strict is not None else None,
        annotated_types.Interval(gt=gt, ge=ge, lt=lt, le=le),
    ]

```

---|---
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
Made with
