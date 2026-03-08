# Create an instance
m = ImportThings(obj='math.cos')
print(m)
#> obj=<built-in function cos>
print(m.model_dump_json())
#> {"obj":"math.cos"}

```

Source code in `pydantic/types.py`
```
 913
 914
 915
 916
 917
 918
 919
 920
 921
 922
 923
 924
 925
 926
 927
 928
 929
 930
 931
 932
 933
 934
 935
 936
 937
 938
 939
 940
 941
 942
 943
 944
 945
 946
 947
 948
 949
 950
 951
 952
 953
 954
 955
 956
 957
 958
 959
 960
 961
 962
 963
 964
 965
 966
 967
 968
 969
 970
 971
 972
 973
 974
 975
 976
 977
 978
 979
 980
 981
 982
 983
 984
 985
 986
 987
 988
 989
 990
 991
 992
 993
 994
 995
 996
 997
 998
 999
1000
1001
1002
1003
1004
1005
1006
1007
1008
1009
1010
1011
1012
1013
1014
1015
1016
1017
1018
1019
1020
1021
1022
1023
1024
1025
1026
1027
1028
1029
1030
1031
1032
1033
1034
```
| ```
class ImportString:
    """A type that can be used to import a Python object from a string.

    `ImportString` expects a string and loads the Python object importable at that dotted path.
    Attributes of modules may be separated from the module by `:` or `.`, e.g. if `'math:cos'` is provided,
    the resulting field value would be the function `cos`. If a `.` is used and both an attribute and submodule
    are present at the same path, the module will be preferred.

    On model instantiation, pointers will be evaluated and imported. There is
    some nuance to this behavior, demonstrated in the examples below.

```python
    import math

    from pydantic import BaseModel, Field, ImportString, ValidationError

    class ImportThings(BaseModel):
        obj: ImportString

    # A string value will cause an automatic import
    my_cos = ImportThings(obj='math.cos')

    # You can use the imported function as you would expect
    cos_of_0 = my_cos.obj(0)
    assert cos_of_0 == 1

    # A string whose value cannot be imported will raise an error
    try:
        ImportThings(obj='foo.bar')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for ImportThings
        obj
          Invalid python path: No module named 'foo.bar' [type=import_error, input_value='foo.bar', input_type=str]
        '''

    # Actual python objects can be assigned as well
    my_cos = ImportThings(obj=math.cos)
    my_cos_2 = ImportThings(obj='math.cos')
    my_cos_3 = ImportThings(obj='math:cos')
    assert my_cos == my_cos_2 == my_cos_3

    # You can set default field value either as Python object:
    class ImportThingsDefaultPyObj(BaseModel):
        obj: ImportString = math.cos

    # or as a string value (but only if used with `validate_default=True`)
    class ImportThingsDefaultString(BaseModel):
        obj: ImportString = Field(default='math.cos', validate_default=True)

    my_cos_default1 = ImportThingsDefaultPyObj()
    my_cos_default2 = ImportThingsDefaultString()
    assert my_cos_default1.obj == my_cos_default2.obj == math.cos

    # note: this will not work!
    class ImportThingsMissingValidateDefault(BaseModel):
        obj: ImportString = 'math.cos'

    my_cos_default3 = ImportThingsMissingValidateDefault()
    assert my_cos_default3.obj == 'math.cos'  # just string, not evaluated
```

    Serializing an `ImportString` type to json is also possible.

```python
    from pydantic import BaseModel, ImportString

    class ImportThings(BaseModel):
        obj: ImportString

    # Create an instance
    m = ImportThings(obj='math.cos')
    print(m)
    #> obj=<built-in function cos>
    print(m.model_dump_json())
    #> {"obj":"math.cos"}
```
    """

    @classmethod
    def __class_getitem__(cls, item: AnyType) -> AnyType:
        return Annotated[item, cls()]

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        serializer = core_schema.plain_serializer_function_ser_schema(cls._serialize, when_used='json')
        if cls is source:
            # Treat bare usage of ImportString (`schema is None`) as the same as ImportString[Any]
            return core_schema.no_info_plain_validator_function(
                function=_validators.import_string, serialization=serializer
            )
        else:
            return core_schema.no_info_before_validator_function(
                function=_validators.import_string, schema=handler(source), serialization=serializer
            )

    @classmethod
    def __get_pydantic_json_schema__(cls, cs: CoreSchema, handler: GetJsonSchemaHandler) -> JsonSchemaValue:
        return handler(core_schema.str_schema())

    @staticmethod
    def _serialize(v: Any) -> str:
        if isinstance(v, ModuleType):
            return v.__name__
        elif hasattr(v, '__module__') and hasattr(v, '__name__'):
            return f'{v.__module__}.{v.__name__}'
        # Handle special cases for sys.XXX streams
        # if we see more of these, we should consider a more general solution
        elif hasattr(v, 'name'):
            if v.name == '<stdout>':
                return 'sys.stdout'
            elif v.name == '<stdin>':
                return 'sys.stdin'
            elif v.name == '<stderr>':
                return 'sys.stderr'
        return v

    def __repr__(self) -> str:
        return 'ImportString'

```

---|---
###  UuidVersion `dataclass` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.UuidVersion)
A field metadata class to indicate a
Use this class as an annotation via
Attributes:
Name | Type | Description
---|---|---
`uuid_version` |  |  The version of the UUID. Must be one of 1, 3, 4, 5, 6, 7 or 8.
Example
```
from typing import Annotated
from uuid import UUID

from pydantic.types import UuidVersion

UUID1 = Annotated[UUID, UuidVersion(1)]

```

Source code in `pydantic/types.py`
```
1137
1138
1139
1140
1141
1142
1143
1144
1145
1146
1147
1148
1149
1150
1151
1152
1153
1154
1155
1156
1157
1158
1159
1160
1161
1162
1163
1164
1165
1166
1167
1168
1169
1170
1171
1172
1173
1174
```
| ```
@_dataclasses.dataclass(**_internal_dataclass.slots_true)
class UuidVersion:
    """A field metadata class to indicate a [UUID](https://docs.python.org/3/library/uuid.html) version.

    Use this class as an annotation via [`Annotated`](https://docs.python.org/3/library/typing.html#typing.Annotated), as seen below.

    Attributes:
        uuid_version: The version of the UUID. Must be one of 1, 3, 4, 5, 6, 7 or 8.

    Example:
    ```python
        from typing import Annotated
        from uuid import UUID

        from pydantic.types import UuidVersion

        UUID1 = Annotated[UUID, UuidVersion(1)]
    ```
    """

    uuid_version: Literal[1, 3, 4, 5, 6, 7, 8]

    def __get_pydantic_json_schema__(
        self, core_schema: core_schema.CoreSchema, handler: GetJsonSchemaHandler
    ) -> JsonSchemaValue:
        field_schema = handler(core_schema)
        field_schema.pop('anyOf', None)  # remove the bytes/str union
        field_schema.update(type='string', format=f'uuid{self.uuid_version}')
        return field_schema

    def __get_pydantic_core_schema__(self, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        schema = handler(source)
        _check_annotated_type(schema['type'], 'uuid', self.__class__.__name__)
        schema['version'] = self.uuid_version  # type: ignore
        return schema

    def __hash__(self) -> int:
        return hash(type(self.uuid_version))

```

---|---
###  Json [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Json)
A special type wrapper which loads JSON before parsing.
You can use the `Json` data type to make Pydantic first load a raw JSON string before validating the loaded data into the parametrized type:
```
from typing import Any

from pydantic import BaseModel, Json, ValidationError

class AnyJsonModel(BaseModel):
    json_obj: Json[Any]

class ConstrainedJsonModel(BaseModel):
    json_obj: Json[list[int]]

print(AnyJsonModel(json_obj='{"b": 1}'))
#> json_obj={'b': 1}
print(ConstrainedJsonModel(json_obj='[1, 2, 3]'))
#> json_obj=[1, 2, 3]

try:
    ConstrainedJsonModel(json_obj=12)
except ValidationError as e:
    print(e)
    '''
    1 validation error for ConstrainedJsonModel
    json_obj
      JSON input should be string, bytes or bytearray [type=json_type, input_value=12, input_type=int]
    '''

try:
    ConstrainedJsonModel(json_obj='[a, b]')
except ValidationError as e:
    print(e)
    '''
    1 validation error for ConstrainedJsonModel
    json_obj
      Invalid JSON: expected value at line 1 column 2 [type=json_invalid, input_value='[a, b]', input_type=str]
    '''

try:
    ConstrainedJsonModel(json_obj='["a", "b"]')
except ValidationError as e:
    print(e)
    '''
    2 validation errors for ConstrainedJsonModel
    json_obj.0
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
    json_obj.1
      Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='b', input_type=str]
    '''

```

When you dump the model using `model_dump` or `model_dump_json`, the dumped value will be the result of validation, not the original JSON string. However, you can use the argument `round_trip=True` to get the original JSON string back:
```
from pydantic import BaseModel, Json

class ConstrainedJsonModel(BaseModel):
    json_obj: Json[list[int]]

print(ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json())
#> {"json_obj":[1,2,3]}
print(
    ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json(round_trip=True)
)
#> {"json_obj":"[1,2,3]"}

```

Source code in `pydantic/types.py`
```
1436
1437
1438
1439
1440
1441
1442
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
1454
1455
1456
1457
1458
1459
1460
1461
1462
1463
1464
1465
1466
1467
1468
1469
1470
1471
1472
1473
1474
1475
1476
1477
1478
1479
1480
1481
1482
1483
1484
1485
1486
1487
1488
1489
1490
1491
1492
1493
1494
1495
1496
1497
1498
1499
1500
1501
1502
1503
1504
1505
1506
1507
1508
1509
1510
1511
1512
1513
1514
1515
1516
1517
1518
1519
1520
1521
1522
1523
1524
1525
1526
1527
```
| ```
class Json:
    """A special type wrapper which loads JSON before parsing.

    You can use the `Json` data type to make Pydantic first load a raw JSON string before
    validating the loaded data into the parametrized type:

```python
    from typing import Any

    from pydantic import BaseModel, Json, ValidationError

    class AnyJsonModel(BaseModel):
        json_obj: Json[Any]

    class ConstrainedJsonModel(BaseModel):
        json_obj: Json[list[int]]

    print(AnyJsonModel(json_obj='{"b": 1}'))
    #> json_obj={'b': 1}
    print(ConstrainedJsonModel(json_obj='[1, 2, 3]'))
    #> json_obj=[1, 2, 3]

    try:
        ConstrainedJsonModel(json_obj=12)
    except ValidationError as e:
        print(e)
        '''
        1 validation error for ConstrainedJsonModel
        json_obj
          JSON input should be string, bytes or bytearray [type=json_type, input_value=12, input_type=int]
        '''

    try:
        ConstrainedJsonModel(json_obj='[a, b]')
    except ValidationError as e:
        print(e)
        '''
        1 validation error for ConstrainedJsonModel
        json_obj
          Invalid JSON: expected value at line 1 column 2 [type=json_invalid, input_value='[a, b]', input_type=str]
        '''

    try:
        ConstrainedJsonModel(json_obj='["a", "b"]')
    except ValidationError as e:
        print(e)
        '''
        2 validation errors for ConstrainedJsonModel
        json_obj.0
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='a', input_type=str]
        json_obj.1
          Input should be a valid integer, unable to parse string as an integer [type=int_parsing, input_value='b', input_type=str]
        '''
```

    When you dump the model using `model_dump` or `model_dump_json`, the dumped value will be the result of validation,
    not the original JSON string. However, you can use the argument `round_trip=True` to get the original JSON string back:

```python
    from pydantic import BaseModel, Json

    class ConstrainedJsonModel(BaseModel):
        json_obj: Json[list[int]]

    print(ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json())
    #> {"json_obj":[1,2,3]}
    print(
        ConstrainedJsonModel(json_obj='[1, 2, 3]').model_dump_json(round_trip=True)
    )
    #> {"json_obj":"[1,2,3]"}
```
    """

    @classmethod
    def __class_getitem__(cls, item: AnyType) -> AnyType:
        return Annotated[item, cls()]

    @classmethod
    def __get_pydantic_core_schema__(cls, source: Any, handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        if cls is source:
            return core_schema.json_schema(None)
        else:
            return core_schema.json_schema(handler(source))

    def __repr__(self) -> str:
        return 'Json'

    def __hash__(self) -> int:
        return hash(type(self))

    def __eq__(self, other: Any) -> bool:
        return type(other) is type(self)

```

---|---
###  Secret [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.Secret)
Bases: `_SecretBase[SecretType]`
A generic base class used for defining a field with sensitive information that you do not want to be visible in logging or tracebacks.
You may either directly parametrize `Secret` with a type, or subclass from `Secret` with a parametrized type. The benefit of subclassing is that you can define a custom `_display` method, which will be used for `repr()` and `str()` methods. The examples below demonstrate both ways of using `Secret` to create a new secret type.
  1. Directly parametrizing `Secret` with a type:


```
from pydantic import BaseModel, Secret

SecretBool = Secret[bool]

class Model(BaseModel):
    secret_bool: SecretBool

m = Model(secret_bool=True)
print(m.model_dump())
#> {'secret_bool': Secret('**********')}

print(m.model_dump_json())
#> {"secret_bool":"**********"}

print(m.secret_bool.get_secret_value())
#> True

```

  1. Subclassing from parametrized `Secret`:


```
from datetime import date

from pydantic import BaseModel, Secret

class SecretDate(Secret[date]):
    def _display(self) -> str:
        return '****/**/**'

class Model(BaseModel):
    secret_date: SecretDate

m = Model(secret_date=date(2022, 1, 1))
print(m.model_dump())
#> {'secret_date': SecretDate('****/**/**')}

print(m.model_dump_json())
#> {"secret_date":"****/**/**"}

print(m.secret_date.get_secret_value())
#> 2022-01-01

```

The value returned by the `_display` method will be used for `repr()` and `str()`.
You can enforce constraints on the underlying type through annotations: For example:
```
from typing import Annotated

from pydantic import BaseModel, Field, Secret, ValidationError

SecretPosInt = Secret[Annotated[int, Field(gt=0, strict=True)]]

class Model(BaseModel):
    sensitive_int: SecretPosInt

m = Model(sensitive_int=42)
print(m.model_dump())
#> {'sensitive_int': Secret('**********')}

try:
    m = Model(sensitive_int=-42)  [](https://docs.pydantic.dev/latest/api/types/#__code_73_annotation_1)
except ValidationError as exc_info:
    print(exc_info.errors(include_url=False, include_input=False))
    '''
    [
        {
            'type': 'greater_than',
            'loc': ('sensitive_int',),
            'msg': 'Input should be greater than 0',
            'ctx': {'gt': 0},
        }
    ]
    '''

try:
    m = Model(sensitive_int='42')  [](https://docs.pydantic.dev/latest/api/types/#__code_73_annotation_2)
except ValidationError as exc_info:
    print(exc_info.errors(include_url=False, include_input=False))
    '''
    [
        {
            'type': 'int_type',
            'loc': ('sensitive_int',),
            'msg': 'Input should be a valid integer',
        }
    ]
    '''

```

Source code in `pydantic/types.py`
```
1571
1572
1573
1574
1575
1576
1577
1578
1579
1580
1581
1582
1583
1584
1585
1586
1587
1588
1589
1590
1591
1592
1593
1594
1595
1596
1597
1598
1599
1600
1601
1602
1603
1604
1605
1606
1607
1608
1609
1610
1611
1612
1613
1614
1615
1616
1617
1618
1619
1620
1621
1622
1623
1624
1625
1626
1627
1628
1629
1630
1631
1632
1633
1634
1635
1636
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
```
| ```
class Secret(_SecretBase[SecretType]):
    """A generic base class used for defining a field with sensitive information that you do not want to be visible in logging or tracebacks.

    You may either directly parametrize `Secret` with a type, or subclass from `Secret` with a parametrized type. The benefit of subclassing
    is that you can define a custom `_display` method, which will be used for `repr()` and `str()` methods. The examples below demonstrate both
    ways of using `Secret` to create a new secret type.

    1. Directly parametrizing `Secret` with a type:

```python
    from pydantic import BaseModel, Secret

    SecretBool = Secret[bool]

    class Model(BaseModel):
        secret_bool: SecretBool

    m = Model(secret_bool=True)
    print(m.model_dump())
    #> {'secret_bool': Secret('**********')}

    print(m.model_dump_json())
    #> {"secret_bool":"**********"}

    print(m.secret_bool.get_secret_value())
    #> True
```

    2. Subclassing from parametrized `Secret`:

```python
    from datetime import date

    from pydantic import BaseModel, Secret

    class SecretDate(Secret[date]):
        def _display(self) -> str:
            return '****/**/**'

    class Model(BaseModel):
        secret_date: SecretDate

    m = Model(secret_date=date(2022, 1, 1))
    print(m.model_dump())
    #> {'secret_date': SecretDate('****/**/**')}

    print(m.model_dump_json())
    #> {"secret_date":"****/**/**"}

    print(m.secret_date.get_secret_value())
    #> 2022-01-01
```

    The value returned by the `_display` method will be used for `repr()` and `str()`.

    You can enforce constraints on the underlying type through annotations:
    For example:

```python
    from typing import Annotated

    from pydantic import BaseModel, Field, Secret, ValidationError

    SecretPosInt = Secret[Annotated[int, Field(gt=0, strict=True)]]

    class Model(BaseModel):
        sensitive_int: SecretPosInt

    m = Model(sensitive_int=42)
    print(m.model_dump())
    #> {'sensitive_int': Secret('**********')}

    try:
        m = Model(sensitive_int=-42)  # (1)!
    except ValidationError as exc_info:
        print(exc_info.errors(include_url=False, include_input=False))
        '''
        [
            {
                'type': 'greater_than',
                'loc': ('sensitive_int',),
                'msg': 'Input should be greater than 0',
                'ctx': {'gt': 0},
            }
        ]
        '''

    try:
        m = Model(sensitive_int='42')  # (2)!
    except ValidationError as exc_info:
        print(exc_info.errors(include_url=False, include_input=False))
        '''
        [
            {
                'type': 'int_type',
                'loc': ('sensitive_int',),
                'msg': 'Input should be a valid integer',
            }
        ]
        '''
```

    1. The input value is not greater than 0, so it raises a validation error.
    2. The input value is not an integer, so it raises a validation error because the `SecretPosInt` type has strict mode enabled.
    """

    def _display(self) -> str | bytes:
        return '**********' if self.get_secret_value() else ''

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        inner_type = None
        # if origin_type is Secret, then cls is a GenericAlias, and we can extract the inner type directly
        origin_type = get_origin(source)
        if origin_type is not None:
            inner_type = get_args(source)[0]
        # otherwise, we need to get the inner type from the base class
        else:
            bases = getattr(cls, '__orig_bases__', getattr(cls, '__bases__', []))
            for base in bases:
                if get_origin(base) is Secret:
                    inner_type = get_args(base)[0]
            if bases == [] or inner_type is None:
                raise TypeError(
                    f"Can't get secret type from {cls.__name__}. "
                    'Please use Secret[<type>], or subclass from Secret[<type>] instead.'
                )

        inner_schema = handler.generate_schema(inner_type)  # type: ignore

        def validate_secret_value(value, handler) -> Secret[SecretType]:
            if isinstance(value, Secret):
                value = value.get_secret_value()
            validated_inner = handler(value)
            return cls(validated_inner)

        return core_schema.json_or_python_schema(
            python_schema=core_schema.no_info_wrap_validator_function(
                validate_secret_value,
                inner_schema,
            ),
            json_schema=core_schema.no_info_after_validator_function(lambda x: cls(x), inner_schema),
            serialization=core_schema.plain_serializer_function_ser_schema(
                _serialize_secret,
                info_arg=True,
                when_used='always',
            ),
        )

    __pydantic_serializer__ = SchemaSerializer(
        core_schema.any_schema(
            serialization=core_schema.plain_serializer_function_ser_schema(
                _serialize_secret,
                info_arg=True,
                when_used='always',
            )
        )
    )

```

---|---
###  SecretStr [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr)
Bases: `_SecretField[`
A string used for storing sensitive information that you do not want to be visible in logging or tracebacks.
When the secret value is nonempty, it is displayed as `'**********'` instead of the underlying value in calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `''`.
```
from pydantic import BaseModel, SecretStr

class User(BaseModel):
    username: str
    password: SecretStr

user = User(username='scolvin', password='password1')

print(user)
#> username='scolvin' password=SecretStr('**********')
print(user.password.get_secret_value())
#> password1
print((SecretStr('password'), SecretStr('')))
#> (SecretStr('**********'), SecretStr(''))

```

As seen above, by default, [`SecretStr`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretStr) (and [`SecretBytes`](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretBytes)) will be serialized as `**********` when serializing to json.
You can use the [`field_serializer`](https://docs.pydantic.dev/latest/api/functional_serializers/#pydantic.functional_serializers.field_serializer) to dump the secret as plain-text when serializing to json.
```
from pydantic import BaseModel, SecretBytes, SecretStr, field_serializer

class Model(BaseModel):
    password: SecretStr
    password_bytes: SecretBytes

    @field_serializer('password', 'password_bytes', when_used='json')
    def dump_secret(self, v):
        return v.get_secret_value()

model = Model(password='IAmSensitive', password_bytes=b'IAmSensitiveBytes')
print(model)
#> password=SecretStr('**********') password_bytes=SecretBytes(b'**********')
print(model.password)
#> **********
print(model.model_dump())
'''
{
    'password': SecretStr('**********'),
    'password_bytes': SecretBytes(b'**********'),
}
'''
print(model.model_dump_json())
#> {"password":"IAmSensitive","password_bytes":"IAmSensitiveBytes"}

```

Source code in `pydantic/types.py`
```
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
1835
1836
1837
1838
1839
1840
1841
1842
1843
1844
1845
1846
1847
1848
1849
1850
1851
1852
1853
1854
1855
1856
1857
1858
1859
1860
1861
1862
1863
1864
1865
```
| ```
class SecretStr(_SecretField[str]):
    """A string used for storing sensitive information that you do not want to be visible in logging or tracebacks.

    When the secret value is nonempty, it is displayed as `'**********'` instead of the underlying value in
    calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `''`.

```python
    from pydantic import BaseModel, SecretStr

    class User(BaseModel):
        username: str
        password: SecretStr

    user = User(username='scolvin', password='password1')

    print(user)
    #> username='scolvin' password=SecretStr('**********')
    print(user.password.get_secret_value())
    #> password1
    print((SecretStr('password'), SecretStr('')))
    #> (SecretStr('**********'), SecretStr(''))
```

    As seen above, by default, [`SecretStr`][pydantic.types.SecretStr] (and [`SecretBytes`][pydantic.types.SecretBytes])
    will be serialized as `**********` when serializing to json.

    You can use the [`field_serializer`][pydantic.functional_serializers.field_serializer] to dump the
    secret as plain-text when serializing to json.

```python
    from pydantic import BaseModel, SecretBytes, SecretStr, field_serializer

    class Model(BaseModel):
        password: SecretStr
        password_bytes: SecretBytes

        @field_serializer('password', 'password_bytes', when_used='json')
