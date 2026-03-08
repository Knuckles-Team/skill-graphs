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
    """

    _inner_schema: ClassVar[CoreSchema] = core_schema.str_schema()
    _error_kind: ClassVar[str] = 'string_type'

    def __len__(self) -> int:
        return len(self._secret_value)

    def _display(self) -> str:
        return _secret_display(self._secret_value)

```

---|---
###  SecretBytes [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.SecretBytes)
Bases: `_SecretField[`
A bytes used for storing sensitive information that you do not want to be visible in logging or tracebacks.
It displays `b'**********'` instead of the string value on `repr()` and `str()` calls. When the secret value is nonempty, it is displayed as `b'**********'` instead of the underlying value in calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `b''`.
```
from pydantic import BaseModel, SecretBytes

class User(BaseModel):
    username: str
    password: SecretBytes

user = User(username='scolvin', password=b'password1')
#> username='scolvin' password=SecretBytes(b'**********')
print(user.password.get_secret_value())
#> b'password1'
print((SecretBytes(b'password'), SecretBytes(b'')))
#> (SecretBytes(b'**********'), SecretBytes(b''))

```

Source code in `pydantic/types.py`
```
1868
1869
1870
1871
1872
1873
1874
1875
1876
1877
1878
1879
1880
1881
1882
1883
1884
1885
1886
1887
1888
1889
1890
1891
1892
1893
1894
1895
1896
1897
1898
```
| ```
class SecretBytes(_SecretField[bytes]):
    """A bytes used for storing sensitive information that you do not want to be visible in logging or tracebacks.

    It displays `b'**********'` instead of the string value on `repr()` and `str()` calls.
    When the secret value is nonempty, it is displayed as `b'**********'` instead of the underlying value in
    calls to `repr()` and `str()`. If the value _is_ empty, it is displayed as `b''`.

```python
    from pydantic import BaseModel, SecretBytes

    class User(BaseModel):
        username: str
        password: SecretBytes

    user = User(username='scolvin', password=b'password1')
    #> username='scolvin' password=SecretBytes(b'**********')
    print(user.password.get_secret_value())
    #> b'password1'
    print((SecretBytes(b'password'), SecretBytes(b'')))
    #> (SecretBytes(b'**********'), SecretBytes(b''))
```
    """

    _inner_schema: ClassVar[CoreSchema] = core_schema.bytes_schema()
    _error_kind: ClassVar[str] = 'bytes_type'

    def __len__(self) -> int:
        return len(self._secret_value)

    def _display(self) -> bytes:
        return _secret_display(self._secret_value).encode()

```

---|---
###  PaymentCardNumber [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber)
Bases:
Based on: https://en.wikipedia.org/wiki/Payment_card_number.
Source code in `pydantic/types.py`
```
1914
1915
1916
1917
1918
1919
1920
1921
1922
1923
1924
1925
1926
1927
1928
1929
1930
1931
1932
1933
1934
1935
1936
1937
1938
1939
1940
1941
1942
1943
1944
1945
1946
1947
1948
1949
1950
1951
1952
1953
1954
1955
1956
1957
1958
1959
1960
1961
1962
1963
1964
1965
1966
1967
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
1985
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
```
| ```
@deprecated(
    'The `PaymentCardNumber` class is deprecated, use `pydantic_extra_types` instead. '
    'See https://docs.pydantic.dev/latest/api/pydantic_extra_types_payment/#pydantic_extra_types.payment.PaymentCardNumber.',
    category=PydanticDeprecatedSince20,
)
class PaymentCardNumber(str):
    """Based on: https://en.wikipedia.org/wiki/Payment_card_number."""

    strip_whitespace: ClassVar[bool] = True
    min_length: ClassVar[int] = 12
    max_length: ClassVar[int] = 19
    bin: str
    last4: str
    brand: PaymentCardBrand

    def __init__(self, card_number: str):
        self.validate_digits(card_number)

        card_number = self.validate_luhn_check_digit(card_number)

        self.bin = card_number[:6]
        self.last4 = card_number[-4:]
        self.brand = self.validate_brand(card_number)

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.with_info_after_validator_function(
            cls.validate,
            core_schema.str_schema(
                min_length=cls.min_length, max_length=cls.max_length, strip_whitespace=cls.strip_whitespace
            ),
        )

    @classmethod
    def validate(cls, input_value: str, /, _: core_schema.ValidationInfo) -> PaymentCardNumber:
        """Validate the card number and return a `PaymentCardNumber` instance."""
        return cls(input_value)

    @property
    def masked(self) -> str:
        """Mask all but the last 4 digits of the card number.

        Returns:
            A masked card number string.
        """
        num_masked = len(self) - 10  # len(bin) + len(last4) == 10
        return f'{self.bin}{"*" * num_masked}{self.last4}'

    @classmethod
    def validate_digits(cls, card_number: str) -> None:
        """Validate that the card number is all digits."""
        if not card_number.isdigit():
            raise PydanticCustomError('payment_card_number_digits', 'Card number is not all digits')

    @classmethod
    def validate_luhn_check_digit(cls, card_number: str) -> str:
        """Based on: https://en.wikipedia.org/wiki/Luhn_algorithm."""
        sum_ = int(card_number[-1])
        length = len(card_number)
        parity = length % 2
        for i in range(length - 1):
            digit = int(card_number[i])
            if i % 2 == parity:
                digit *= 2
            if digit > 9:
                digit -= 9
            sum_ += digit
        valid = sum_ % 10 == 0
        if not valid:
            raise PydanticCustomError('payment_card_number_luhn', 'Card number is not luhn valid')
        return card_number

    @staticmethod
    def validate_brand(card_number: str) -> PaymentCardBrand:
        """Validate length based on BIN for major brands:
        https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN).
        """
        if card_number[0] == '4':
            brand = PaymentCardBrand.visa
        elif 51 <= int(card_number[:2]) <= 55:
            brand = PaymentCardBrand.mastercard
        elif card_number[:2] in {'34', '37'}:
            brand = PaymentCardBrand.amex
        else:
            brand = PaymentCardBrand.other

        required_length: None | int | str = None
        if brand in PaymentCardBrand.mastercard:
            required_length = 16
            valid = len(card_number) == required_length
        elif brand == PaymentCardBrand.visa:
            required_length = '13, 16 or 19'
            valid = len(card_number) in {13, 16, 19}
        elif brand == PaymentCardBrand.amex:
            required_length = 15
            valid = len(card_number) == required_length
        else:
            valid = True

        if not valid:
            raise PydanticCustomError(
                'payment_card_number_brand',
                'Length for a {brand} card must be {required_length}',
                {'brand': brand, 'required_length': required_length},
            )
        return brand

```

---|---
####  masked `property` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.masked)
```
masked:

```

Mask all but the last 4 digits of the card number.
Returns:
Type | Description
---|---
|  A masked card number string.
####  validate `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate)
```
validate(
    input_value: , /, _: ValidationInfo[](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.ValidationInfo)
) -> PaymentCardNumber[](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber)

```

Validate the card number and return a `PaymentCardNumber` instance.
Source code in `pydantic/types.py`
```
1947
1948
1949
1950
```
| ```
@classmethod
def validate(cls, input_value: str, /, _: core_schema.ValidationInfo) -> PaymentCardNumber:
    """Validate the card number and return a `PaymentCardNumber` instance."""
    return cls(input_value)

```

---|---
####  validate_digits `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate_digits)
```
validate_digits(card_number: ) -> None

```

Validate that the card number is all digits.
Source code in `pydantic/types.py`
```
1962
1963
1964
1965
1966
```
| ```
@classmethod
def validate_digits(cls, card_number: str) -> None:
    """Validate that the card number is all digits."""
    if not card_number.isdigit():
        raise PydanticCustomError('payment_card_number_digits', 'Card number is not all digits')

```

---|---
####  validate_luhn_check_digit `classmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate_luhn_check_digit)
```
validate_luhn_check_digit(card_number: ) ->

```

Based on: https://en.wikipedia.org/wiki/Luhn_algorithm.
Source code in `pydantic/types.py`
```
1968
1969
1970
1971
1972
1973
1974
1975
1976
1977
1978
1979
1980
1981
1982
1983
1984
```
| ```
@classmethod
def validate_luhn_check_digit(cls, card_number: str) -> str:
    """Based on: https://en.wikipedia.org/wiki/Luhn_algorithm."""
    sum_ = int(card_number[-1])
    length = len(card_number)
    parity = length % 2
    for i in range(length - 1):
        digit = int(card_number[i])
        if i % 2 == parity:
            digit *= 2
        if digit > 9:
            digit -= 9
        sum_ += digit
    valid = sum_ % 10 == 0
    if not valid:
        raise PydanticCustomError('payment_card_number_luhn', 'Card number is not luhn valid')
    return card_number

```

---|---
####  validate_brand `staticmethod` [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PaymentCardNumber.validate_brand)
```
validate_brand(card_number: ) -> PaymentCardBrand

```

Validate length based on BIN for major brands: https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN).
Source code in `pydantic/types.py`
```
1986
1987
1988
1989
1990
1991
1992
1993
1994
1995
1996
1997
1998
1999
2000
2001
2002
2003
2004
2005
2006
2007
2008
2009
2010
2011
2012
2013
2014
2015
2016
2017
2018
2019
```
| ```
@staticmethod
def validate_brand(card_number: str) -> PaymentCardBrand:
    """Validate length based on BIN for major brands:
    https://en.wikipedia.org/wiki/Payment_card_number#Issuer_identification_number_(IIN).
    """
    if card_number[0] == '4':
        brand = PaymentCardBrand.visa
    elif 51 <= int(card_number[:2]) <= 55:
        brand = PaymentCardBrand.mastercard
    elif card_number[:2] in {'34', '37'}:
        brand = PaymentCardBrand.amex
    else:
        brand = PaymentCardBrand.other

    required_length: None | int | str = None
    if brand in PaymentCardBrand.mastercard:
        required_length = 16
        valid = len(card_number) == required_length
    elif brand == PaymentCardBrand.visa:
        required_length = '13, 16 or 19'
        valid = len(card_number) in {13, 16, 19}
    elif brand == PaymentCardBrand.amex:
        required_length = 15
        valid = len(card_number) == required_length
    else:
        valid = True

    if not valid:
        raise PydanticCustomError(
            'payment_card_number_brand',
            'Length for a {brand} card must be {required_length}',
            {'brand': brand, 'required_length': required_length},
        )
    return brand

```

---|---
###  ByteSize [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ByteSize)
Bases:
Converts a string representing a number of bytes with units (such as `'1KB'` or `'11.5MiB'`) into an integer.
You can use the `ByteSize` data type to (case-insensitively) convert a string representation of a number of bytes into an integer, and also to print out human-readable strings representing a number of bytes.
In conformance with `'1KB'` to mean 1000 bytes, and `'1KiB'` to mean 1024 bytes. In general, including a middle `'i'` will cause the unit to be interpreted as a power of 2, rather than a power of 10 (so, for example, `'1 MB'` is treated as `1_000_000` bytes, whereas `'1 MiB'` is treated as `1_048_576` bytes).
Info
Note that `1b` will be parsed as "1 byte" and not "1 bit".
```
from pydantic import BaseModel, ByteSize

class MyModel(BaseModel):
    size: ByteSize

print(MyModel(size=52000).size)
#> 52000
print(MyModel(size='3000 KiB').size)
#> 3072000

m = MyModel(size='50 PB')
print(m.size.human_readable())
#> 44.4PiB
print(m.size.human_readable(decimal=True))
#> 50.0PB
print(m.size.human_readable(separator=' '))
#> 44.4 PiB

print(m.size.to('TiB'))
#> 45474.73508864641

```

Source code in `pydantic/types.py`
```
2025
2026
2027
2028
2029
2030
2031
2032
2033
2034
2035
2036
2037
2038
2039
2040
2041
2042
2043
2044
2045
2046
2047
2048
2049
2050
2051
2052
2053
2054
2055
2056
2057
2058
2059
2060
2061
2062
2063
2064
2065
2066
2067
2068
2069
2070
2071
2072
2073
2074
2075
2076
2077
2078
2079
2080
2081
2082
2083
2084
2085
2086
2087
2088
2089
2090
2091
2092
2093
2094
2095
2096
2097
2098
2099
2100
2101
2102
2103
2104
2105
2106
2107
2108
2109
2110
2111
2112
2113
2114
2115
2116
2117
2118
2119
2120
2121
2122
2123
2124
2125
2126
2127
2128
2129
2130
2131
2132
2133
2134
2135
2136
2137
2138
2139
2140
2141
2142
2143
2144
2145
2146
2147
2148
2149
2150
2151
2152
2153
2154
2155
2156
2157
2158
2159
2160
2161
2162
2163
2164
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
```
| ```
class ByteSize(int):
    """Converts a string representing a number of bytes with units (such as `'1KB'` or `'11.5MiB'`) into an integer.

    You can use the `ByteSize` data type to (case-insensitively) convert a string representation of a number of bytes into
    an integer, and also to print out human-readable strings representing a number of bytes.

    In conformance with [IEC 80000-13 Standard](https://en.wikipedia.org/wiki/ISO/IEC_80000) we interpret `'1KB'` to mean 1000 bytes,
    and `'1KiB'` to mean 1024 bytes. In general, including a middle `'i'` will cause the unit to be interpreted as a power of 2,
    rather than a power of 10 (so, for example, `'1 MB'` is treated as `1_000_000` bytes, whereas `'1 MiB'` is treated as `1_048_576` bytes).

    !!! info
        Note that `1b` will be parsed as "1 byte" and not "1 bit".

```python
    from pydantic import BaseModel, ByteSize

    class MyModel(BaseModel):
        size: ByteSize

    print(MyModel(size=52000).size)
    #> 52000
    print(MyModel(size='3000 KiB').size)
    #> 3072000

    m = MyModel(size='50 PB')
    print(m.size.human_readable())
    #> 44.4PiB
    print(m.size.human_readable(decimal=True))
    #> 50.0PB
    print(m.size.human_readable(separator=' '))
    #> 44.4 PiB

    print(m.size.to('TiB'))
    #> 45474.73508864641
```
    """

    byte_sizes = {
        'b': 1,
        'kb': 10**3,
        'mb': 10**6,
        'gb': 10**9,
        'tb': 10**12,
        'pb': 10**15,
        'eb': 10**18,
        'kib': 2**10,
        'mib': 2**20,
        'gib': 2**30,
        'tib': 2**40,
        'pib': 2**50,
        'eib': 2**60,
        'bit': 1 / 8,
        'kbit': 10**3 / 8,
        'mbit': 10**6 / 8,
        'gbit': 10**9 / 8,
        'tbit': 10**12 / 8,
        'pbit': 10**15 / 8,
        'ebit': 10**18 / 8,
        'kibit': 2**10 / 8,
        'mibit': 2**20 / 8,
        'gibit': 2**30 / 8,
        'tibit': 2**40 / 8,
        'pibit': 2**50 / 8,
        'eibit': 2**60 / 8,
    }
    byte_sizes.update({k.lower()[0]: v for k, v in byte_sizes.items() if 'i' not in k})

    byte_string_pattern = r'^\s*(\d*\.?\d+)\s*(\w+)?'
    byte_string_re = re.compile(byte_string_pattern, re.IGNORECASE)

    @classmethod
    def __get_pydantic_core_schema__(cls, source: type[Any], handler: GetCoreSchemaHandler) -> core_schema.CoreSchema:
        return core_schema.with_info_after_validator_function(
            function=cls._validate,
            schema=core_schema.union_schema(
                [
                    core_schema.str_schema(pattern=cls.byte_string_pattern),
                    core_schema.int_schema(ge=0),
                ],
                custom_error_type='byte_size',
                custom_error_message='could not parse value and unit from byte string',
            ),
            serialization=core_schema.plain_serializer_function_ser_schema(
                int, return_schema=core_schema.int_schema(ge=0)
            ),
        )

    @classmethod
    def _validate(cls, input_value: Any, /, _: core_schema.ValidationInfo) -> ByteSize:
        try:
            return cls(int(input_value))
        except ValueError:
            pass

        str_match = cls.byte_string_re.match(str(input_value))
        if str_match is None:
            raise PydanticCustomError('byte_size', 'could not parse value and unit from byte string')

        scalar, unit = str_match.groups()
        if unit is None:
            unit = 'b'

        try:
            unit_mult = cls.byte_sizes[unit.lower()]
        except KeyError:
            raise PydanticCustomError('byte_size_unit', 'could not interpret byte unit: {unit}', {'unit': unit})

        return cls(int(float(scalar) * unit_mult))

    def human_readable(self, decimal: bool = False, separator: str = '') -> str:
        """Converts a byte size to a human readable string.

        Args:
            decimal: If True, use decimal units (e.g. 1000 bytes per KB). If False, use binary units
                (e.g. 1024 bytes per KiB).
            separator: A string used to split the value and unit. Defaults to an empty string ('').

        Returns:
            A human readable string representation of the byte size.
        """
        if decimal:
            divisor = 1000
            units = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
            final_unit = 'EB'
        else:
            divisor = 1024
            units = 'B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB'
            final_unit = 'EiB'

        num = float(self)
        for unit in units:
            if abs(num) < divisor:
                if unit == 'B':
                    return f'{num:0.0f}{separator}{unit}'
                else:
                    return f'{num:0.1f}{separator}{unit}'
            num /= divisor

        return f'{num:0.1f}{separator}{final_unit}'

    def to(self, unit: str) -> float:
        """Converts a byte size to another unit, including both byte and bit units.

        Args:
            unit: The unit to convert to. Must be one of the following: B, KB, MB, GB, TB, PB, EB,
                KiB, MiB, GiB, TiB, PiB, EiB (byte units) and
                bit, kbit, mbit, gbit, tbit, pbit, ebit,
                kibit, mibit, gibit, tibit, pibit, eibit (bit units).

        Returns:
            The byte size in the new unit.
        """
        try:
            unit_div = self.byte_sizes[unit.lower()]
        except KeyError:
            raise PydanticCustomError('byte_size_unit', 'Could not interpret byte unit: {unit}', {'unit': unit})

        return self / unit_div

```

---|---
####  human_readable [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ByteSize.human_readable)
```
human_readable(
    decimal:  = False, separator:  = ""
) ->

```

Converts a byte size to a human readable string.
Parameters:
Name | Type | Description | Default
---|---|---|---
`decimal` |  |  If True, use decimal units (e.g. 1000 bytes per KB). If False, use binary units (e.g. 1024 bytes per KiB). |  `False`
`separator` |  |  A string used to split the value and unit. Defaults to an empty string (''). |  `''`
Returns:
Type | Description
---|---
|  A human readable string representation of the byte size.
Source code in `pydantic/types.py`
```
2134
2135
2136
2137
2138
2139
2140
2141
2142
2143
2144
2145
2146
2147
2148
2149
2150
2151
2152
2153
2154
2155
2156
2157
2158
2159
2160
2161
2162
2163
```
| ```
def human_readable(self, decimal: bool = False, separator: str = '') -> str:
    """Converts a byte size to a human readable string.

    Args:
        decimal: If True, use decimal units (e.g. 1000 bytes per KB). If False, use binary units
            (e.g. 1024 bytes per KiB).
        separator: A string used to split the value and unit. Defaults to an empty string ('').

    Returns:
        A human readable string representation of the byte size.
    """
    if decimal:
        divisor = 1000
        units = 'B', 'KB', 'MB', 'GB', 'TB', 'PB'
        final_unit = 'EB'
    else:
        divisor = 1024
        units = 'B', 'KiB', 'MiB', 'GiB', 'TiB', 'PiB'
        final_unit = 'EiB'

    num = float(self)
    for unit in units:
        if abs(num) < divisor:
            if unit == 'B':
                return f'{num:0.0f}{separator}{unit}'
            else:
                return f'{num:0.1f}{separator}{unit}'
        num /= divisor

    return f'{num:0.1f}{separator}{final_unit}'

```

---|---
####  to [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.ByteSize.to)
```
to(unit: ) ->

```

Converts a byte size to another unit, including both byte and bit units.
Parameters:
Name | Type | Description | Default
---|---|---|---
`unit` |  |  The unit to convert to. Must be one of the following: B, KB, MB, GB, TB, PB, EB, KiB, MiB, GiB, TiB, PiB, EiB (byte units) and bit, kbit, mbit, gbit, tbit, pbit, ebit, kibit, mibit, gibit, tibit, pibit, eibit (bit units). |  _required_
Returns:
Type | Description
---|---
|  The byte size in the new unit.
Source code in `pydantic/types.py`
```
2165
2166
2167
2168
2169
2170
2171
2172
2173
2174
2175
2176
2177
2178
2179
2180
2181
2182
```
| ```
def to(self, unit: str) -> float:
    """Converts a byte size to another unit, including both byte and bit units.

    Args:
        unit: The unit to convert to. Must be one of the following: B, KB, MB, GB, TB, PB, EB,
            KiB, MiB, GiB, TiB, PiB, EiB (byte units) and
            bit, kbit, mbit, gbit, tbit, pbit, ebit,
            kibit, mibit, gibit, tibit, pibit, eibit (bit units).

    Returns:
        The byte size in the new unit.
    """
    try:
        unit_div = self.byte_sizes[unit.lower()]
    except KeyError:
        raise PydanticCustomError('byte_size_unit', 'Could not interpret byte unit: {unit}', {'unit': unit})

    return self / unit_div

```

---|---
###  PastDate [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.PastDate)
A date in the past.
Source code in `pydantic/types.py`
```
2198
2199
2200
2201
2202
2203
2204
2205
2206
2207
2208
2209
2210
2211
2212
2213
2214
2215
```
| ```
class PastDate:
    """A date in the past."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.date_schema(now_op='past')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'date', cls.__name__)
            schema['now_op'] = 'past'
            return schema

    def __repr__(self) -> str:
        return 'PastDate'

```

---|---
###  FutureDate [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.FutureDate)
A date in the future.
Source code in `pydantic/types.py`
```
2217
2218
2219
2220
2221
2222
2223
2224
2225
2226
2227
2228
2229
2230
2231
2232
2233
2234
```
| ```
class FutureDate:
    """A date in the future."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.date_schema(now_op='future')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'date', cls.__name__)
            schema['now_op'] = 'future'
            return schema

    def __repr__(self) -> str:
        return 'FutureDate'

```

---|---
###  AwareDatetime [¶](https://docs.pydantic.dev/latest/api/types/#pydantic.types.AwareDatetime)
A datetime that requires timezone info.
Source code in `pydantic/types.py`
```
2274
2275
2276
2277
2278
2279
2280
2281
2282
2283
2284
2285
2286
2287
2288
2289
2290
2291
```
| ```
class AwareDatetime:
    """A datetime that requires timezone info."""

    @classmethod
    def __get_pydantic_core_schema__(
        cls, source: type[Any], handler: GetCoreSchemaHandler
    ) -> core_schema.CoreSchema:
        if cls is source:
            # used directly as a type
            return core_schema.datetime_schema(tz_constraint='aware')
        else:
            schema = handler(source)
            _check_annotated_type(schema['type'], 'datetime', cls.__name__)
            schema['tz_constraint'] = 'aware'
