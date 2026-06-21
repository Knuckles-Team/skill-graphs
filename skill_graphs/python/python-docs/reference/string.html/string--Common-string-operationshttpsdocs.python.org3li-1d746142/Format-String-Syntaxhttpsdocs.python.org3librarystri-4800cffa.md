## Format String Syntax[¶](https://docs.python.org/3/library/string.html#format-string-syntax "Link to this heading")
The [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") method and the [`Formatter`](https://docs.python.org/3/library/string.html#string.Formatter "string.Formatter") class share the same syntax for format strings (although in the case of `Formatter`, subclasses can define their own format string syntax). The syntax is related to that of [formatted string literals](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) and [template string literals](https://docs.python.org/3/reference/lexical_analysis.html#t-strings), but it is less sophisticated and, in particular, does not support arbitrary expressions in interpolations.
Format strings contain “replacement fields” surrounded by curly braces `{}`. Anything that is not contained in braces is considered literal text, which is copied unchanged to the output. If you need to include a brace character in the literal text, it can be escaped by doubling: `{{` and `}}`.
The grammar for a replacement field is as follows:
```
**replacement_field**: "{" [[field_name](https://docs.python.org/3/library/string.html#grammar-token-format-string-field_name)] ["!" [conversion](https://docs.python.org/3/library/string.html#grammar-token-format-string-conversion)] [":" [format_spec](https://docs.python.org/3/library/string.html#grammar-token-format-string-format_spec)] "}"
**field_name**:        [arg_name](https://docs.python.org/3/library/string.html#grammar-token-format-string-arg_name) ("." [attribute_name](https://docs.python.org/3/library/string.html#grammar-token-format-string-attribute_name) | "[" [element_index](https://docs.python.org/3/library/string.html#grammar-token-format-string-element_index) "]")*
**arg_name**:          [[identifier](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier) | [digit](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-digit)+]
**attribute_name**:    [identifier](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-identifier)
**element_index**:     [digit](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-digit)+ | [index_string](https://docs.python.org/3/library/string.html#grammar-token-format-string-index_string)
**index_string**:      <any source character except "]"> +
**conversion**:        "r" | "s" | "a"
**format_spec**:       [format-spec:format_spec](https://docs.python.org/3/library/string.html#grammar-token-format-spec-format_spec)

```

In less formal terms, the replacement field can start with a _field_name_ that specifies the object whose value is to be formatted and inserted into the output instead of the replacement field. The _field_name_ is optionally followed by a _conversion_ field, which is preceded by an exclamation point `'!'`, and a _format_spec_ , which is preceded by a colon `':'`. These specify a non-default format for the replacement value.
See also the [Format Specification Mini-Language](https://docs.python.org/3/library/string.html#formatspec) section.
The _field_name_ itself begins with an _arg_name_ that is either a number or a keyword. If it’s a number, it refers to a positional argument, and if it’s a keyword, it refers to a named keyword argument. An _arg_name_ is treated as a number if a call to [`str.isdecimal()`](https://docs.python.org/3/library/stdtypes.html#str.isdecimal "str.isdecimal") on the string would return true. If the numerical arg_names in a format string are 0, 1, 2, … in sequence, they can all be omitted (not just some) and the numbers 0, 1, 2, … will be automatically inserted in that order. Because _arg_name_ is not quote-delimited, it is not possible to specify arbitrary dictionary keys (e.g., the strings `'10'` or `':-]'`) within a format string. The _arg_name_ can be followed by any number of index or attribute expressions. An expression of the form `'.name'` selects the named attribute using [`getattr()`](https://docs.python.org/3/library/functions.html#getattr "getattr"), while an expression of the form `'[index]'` does an index lookup using [`__getitem__()`](https://docs.python.org/3/reference/datamodel.html#object.__getitem__ "object.__getitem__").
Changed in version 3.1: The positional argument specifiers can be omitted for [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format"), so `'{} {}'.format(a, b)` is equivalent to `'{0} {1}'.format(a, b)`.
Changed in version 3.4: The positional argument specifiers can be omitted for [`Formatter`](https://docs.python.org/3/library/string.html#string.Formatter "string.Formatter").
Some simple format string examples:
Copy```
"First, thou shalt count to {0}"  # References first positional argument
"Bring me a {}"                   # Implicitly references the first positional argument
"From {} to {}"                   # Same as "From {0} to {1}"
"My quest is {name}"              # References keyword argument 'name'
"Weight in tons {0.weight}"       # 'weight' attribute of first positional arg
"Units destroyed: {players[0]}"   # First element of keyword argument 'players'.

```

The _conversion_ field causes a type coercion before formatting. Normally, the job of formatting a value is done by the [`__format__()`](https://docs.python.org/3/reference/datamodel.html#object.__format__ "object.__format__") method of the value itself. However, in some cases it is desirable to force a type to be formatted as a string, overriding its own definition of formatting. By converting the value to a string before calling `__format__()`, the normal formatting logic is bypassed.
Three conversion flags are currently supported: `'!s'` which calls [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") on the value, `'!r'` which calls [`repr()`](https://docs.python.org/3/library/functions.html#repr "repr") and `'!a'` which calls [`ascii()`](https://docs.python.org/3/library/functions.html#ascii "ascii").
Some examples:
Copy```
"Harold's a clever {0!s}"        # Calls str() on the argument first
"Bring out the holy {name!r}"    # Calls repr() on the argument first
"More {!a}"                      # Calls ascii() on the argument first

```

The _format_spec_ field contains a specification of how the value should be presented, including such details as field width, alignment, padding, decimal precision and so on. Each value type can define its own “formatting mini-language” or interpretation of the _format_spec_.
Most built-in types support a common formatting mini-language, which is described in the next section.
A _format_spec_ field can also include nested replacement fields within it. These nested replacement fields may contain a field name, conversion flag and format specification, but deeper nesting is not allowed. The replacement fields within the format_spec are substituted before the _format_spec_ string is interpreted. This allows the formatting of a value to be dynamically specified.
See the [Format examples](https://docs.python.org/3/library/string.html#formatexamples) section for some examples.
### Format Specification Mini-Language[¶](https://docs.python.org/3/library/string.html#format-specification-mini-language "Link to this heading")
“Format specifications” are used within replacement fields contained within a format string to define how individual values are presented (see [Format String Syntax](https://docs.python.org/3/library/string.html#formatstrings), [f-strings](https://docs.python.org/3/reference/lexical_analysis.html#f-strings), and [t-strings](https://docs.python.org/3/reference/lexical_analysis.html#t-strings)). They can also be passed directly to the built-in [`format()`](https://docs.python.org/3/library/functions.html#format "format") function. Each formattable type may define how the format specification is to be interpreted.
Most built-in types implement the following options for format specifications, although some of the formatting options are only supported by the numeric types.
A general convention is that an empty format specification produces the same result as if you had called [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") on the value. A non-empty format specification typically modifies the result.
The general form of a _standard format specifier_ is:
```
**format_spec**:             [[options](https://docs.python.org/3/library/string.html#grammar-token-format-spec-options)][[width_and_precision](https://docs.python.org/3/library/string.html#grammar-token-format-spec-width_and_precision)][[type](https://docs.python.org/3/library/string.html#grammar-token-format-spec-type)]
**options**:                 [[[fill](https://docs.python.org/3/library/string.html#grammar-token-format-spec-fill)][align](https://docs.python.org/3/library/string.html#grammar-token-format-spec-align)][[sign](https://docs.python.org/3/library/string.html#grammar-token-format-spec-sign)]["z"]["#"]["0"]
**fill**:                    <any character>
**align**:                   "<" | ">" | "=" | "^"
**sign**:                    "+" | "-" | " "
**width_and_precision**:     [[width_with_grouping](https://docs.python.org/3/library/string.html#grammar-token-format-spec-width_with_grouping)][[precision_with_grouping](https://docs.python.org/3/library/string.html#grammar-token-format-spec-precision_with_grouping)]
**width_with_grouping**:     [[width](https://docs.python.org/3/library/string.html#grammar-token-format-spec-width)][[grouping](https://docs.python.org/3/library/string.html#grammar-token-format-spec-grouping)]
**precision_with_grouping**: "." [[precision](https://docs.python.org/3/library/string.html#grammar-token-format-spec-precision)][[grouping](https://docs.python.org/3/library/string.html#grammar-token-format-spec-grouping)] | "." [grouping](https://docs.python.org/3/library/string.html#grammar-token-format-spec-grouping)
**width**:                   [digit](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-digit)+
**precision**:               [digit](https://docs.python.org/3/reference/lexical_analysis.html#grammar-token-python-grammar-digit)+
**grouping**:                "," | "_"
**type**:                    "b" | "c" | "d" | "e" | "E" | "f" | "F" | "g"
                         | "G" | "n" | "o" | "s" | "x" | "X" | "%"

```

If a valid _align_ value is specified, it can be preceded by a _fill_ character that can be any character and defaults to a space if omitted. It is not possible to use a literal curly brace (”`{`” or “`}`”) as the _fill_ character in a [formatted string literal](https://docs.python.org/3/reference/lexical_analysis.html#f-strings) or when using the [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") method. However, it is possible to insert a curly brace with a nested replacement field. This limitation doesn’t affect the [`format()`](https://docs.python.org/3/library/functions.html#format "format") function.
The meaning of the various alignment options is as follows:
Option | Meaning
---|---
`'<'` | Forces the field to be left-aligned within the available space (this is the default for most objects).
`'>'` | Forces the field to be right-aligned within the available space (this is the default for numbers).
`'='` | Forces the padding to be placed after the sign (if any) but before the digits. This is used for printing fields in the form ‘+000000120’. This alignment option is only valid for numeric types, excluding [`complex`](https://docs.python.org/3/library/functions.html#complex "complex"). It becomes the default for numbers when ‘0’ immediately precedes the field width.
`'^'` | Forces the field to be centered within the available space.
Note that unless a minimum field width is defined, the field width will always be the same size as the data to fill it, so that the alignment option has no meaning in this case.
The _sign_ option is only valid for number types, and can be one of the following:
Option | Meaning
---|---
`'+'` | Indicates that a sign should be used for both positive as well as negative numbers.
`'-'` | Indicates that a sign should be used only for negative numbers (this is the default behavior).
space | Indicates that a leading space should be used on positive numbers, and a minus sign on negative numbers.
The `'z'` option coerces negative zero floating-point values to positive zero after rounding to the format precision. This option is only valid for floating-point presentation types.
Changed in version 3.11: Added the `'z'` option (see also [**PEP 682**](https://peps.python.org/pep-0682/)).
The `'#'` option causes the “alternate form” to be used for the conversion. The alternate form is defined differently for different types. This option is only valid for integer, float and complex types. For integers, when binary, octal, or hexadecimal output is used, this option adds the respective prefix `'0b'`, `'0o'`, `'0x'`, or `'0X'` to the output value. For float and complex the alternate form causes the result of the conversion to always contain a decimal-point character, even if no digits follow it. Normally, a decimal-point character appears in the result of these conversions only if a digit follows it. In addition, for `'g'` and `'G'` conversions, trailing zeros are not removed from the result.
The _width_ is a decimal integer defining the minimum total field width, including any prefixes, separators, and other formatting characters. If not specified, then the field width will be determined by the content.
When no explicit alignment is given, preceding the _width_ field by a zero (`'0'`) character enables sign-aware zero-padding for numeric types, excluding [`complex`](https://docs.python.org/3/library/functions.html#complex "complex"). This is equivalent to a _fill_ character of `'0'` with an _alignment_ type of `'='`.
Changed in version 3.10: Preceding the _width_ field by `'0'` no longer affects the default alignment for strings.
The _precision_ is a decimal integer indicating how many digits should be displayed after the decimal point for presentation types `'f'` and `'F'`, or before and after the decimal point for presentation types `'g'` or `'G'`. For string presentation types the field indicates the maximum field size - in other words, how many characters will be used from the field content. The _precision_ is not allowed for integer presentation types.
The _grouping_ option after _width_ and _precision_ fields specifies a digit group separator for the integral and fractional parts of a number respectively. It can be one of the following:
Option | Meaning
---|---
`','` | Inserts a comma every 3 digits for integer presentation type `'d'` and floating-point presentation types, excluding `'n'`. For other presentation types, this option is not supported.
`'_'` | Inserts an underscore every 3 digits for integer presentation type `'d'` and floating-point presentation types, excluding `'n'`. For integer presentation types `'b'`, `'o'`, `'x'`, and `'X'`, underscores are inserted every 4 digits. For other presentation types, this option is not supported.
For a locale aware separator, use the `'n'` presentation type instead.
Changed in version 3.1: Added the `','` option (see also [**PEP 378**](https://peps.python.org/pep-0378/)).
Changed in version 3.6: Added the `'_'` option (see also [**PEP 515**](https://peps.python.org/pep-0515/)).
Changed in version 3.14: Support the _grouping_ option for the fractional part.
Finally, the _type_ determines how the data should be presented.
The available string presentation types are:
> Type | Meaning
> ---|---
> `'s'` | String format. This is the default type for strings and may be omitted.
> None | The same as `'s'`.
The available integer presentation types are:
> Type | Meaning
> ---|---
> `'b'` | Binary format. Outputs the number in base 2.
> `'c'` | Character. Converts the integer to the corresponding unicode character before printing.
> `'d'` | Decimal Integer. Outputs the number in base 10.
> `'o'` | Octal format. Outputs the number in base 8.
> `'x'` | Hex format. Outputs the number in base 16, using lower-case letters for the digits above 9.
> `'X'` | Hex format. Outputs the number in base 16, using upper-case letters for the digits above 9. In case `'#'` is specified, the prefix `'0x'` will be upper-cased to `'0X'` as well.
> `'n'` | Number. This is the same as `'d'`, except that it uses the current locale setting to insert the appropriate digit group separators.
> None | The same as `'d'`.
In addition to the above presentation types, integers can be formatted with the floating-point presentation types listed below (except `'n'` and `None`). When doing so, [`float()`](https://docs.python.org/3/library/functions.html#float "float") is used to convert the integer to a floating-point number before formatting.
The available presentation types for [`float`](https://docs.python.org/3/library/functions.html#float "float") and [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal") values are:
> Type | Meaning
> ---|---
> `'e'` |  Scientific notation. For a given precision `p`, formats the number in scientific notation with the letter ‘e’ separating the coefficient from the exponent. The coefficient has one digit before and `p` digits after the decimal point, for a total of `p + 1` significant digits. With no precision given, uses a precision of `6` digits after the decimal point for [`float`](https://docs.python.org/3/library/functions.html#float "float"), and shows all coefficient digits for [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"). If `p=0`, the decimal point is omitted unless the `#` option is used. For [`float`](https://docs.python.org/3/library/functions.html#float "float"), the exponent always contains at least two digits, and is zero if the value is zero.
> `'E'` | Scientific notation. Same as `'e'` except it uses an upper case ‘E’ as the separator character.
> `'f'` | Fixed-point notation. For a given precision `p`, formats the number as a decimal number with exactly `p` digits following the decimal point. With no precision given, uses a precision of `6` digits after the decimal point for [`float`](https://docs.python.org/3/library/functions.html#float "float"), and uses a precision large enough to show all coefficient digits for [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"). If `p=0`, the decimal point is omitted unless the `#` option is used.
> `'F'` | Fixed-point notation. Same as `'f'`, but converts `nan` to `NAN` and `inf` to `INF`.
> `'g'` |  General format. For a given precision `p >= 1`, this rounds the number to `p` significant digits and then formats the result in either fixed-point format or in scientific notation, depending on its magnitude. A precision of `0` is treated as equivalent to a precision of `1`. The precise rules are as follows: suppose that the result formatted with presentation type `'e'` and precision `p-1` would have exponent `exp`. Then, if `m <= exp < p`, where `m` is -4 for floats and -6 for [`Decimals`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"), the number is formatted with presentation type `'f'` and precision `p-1-exp`. Otherwise, the number is formatted with presentation type `'e'` and precision `p-1`. In both cases insignificant trailing zeros are removed from the significand, and the decimal point is also removed if there are no remaining digits following it, unless the `'#'` option is used. With no precision given, uses a precision of `6` significant digits for [`float`](https://docs.python.org/3/library/functions.html#float "float"). For [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"), the coefficient of the result is formed from the coefficient digits of the value; scientific notation is used for values smaller than `1e-6` in absolute value and values where the place value of the least significant digit is larger than 1, and fixed-point notation is used otherwise. Positive and negative infinity, positive and negative zero, and nans, are formatted as `inf`, `-inf`, `0`, `-0` and `nan` respectively, regardless of the precision.
> `'G'` | General format. Same as `'g'` except switches to `'E'` if the number gets too large. The representations of infinity and NaN are uppercased, too.
> `'n'` | Number. This is the same as `'g'`, except that it uses the current locale setting to insert the appropriate digit group separators for the integral part of a number.
> `'%'` | Percentage. Multiplies the number by 100 and displays in fixed (`'f'`) format, followed by a percent sign.
> None |  For [`float`](https://docs.python.org/3/library/functions.html#float "float") this is like the `'g'` type, except that when fixed-point notation is used to format the result, it always includes at least one digit past the decimal point, and switches to the scientific notation when `exp >= p - 1`. When the precision is not specified, the latter will be as large as needed to represent the given value faithfully. For [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"), this is the same as either `'g'` or `'G'` depending on the value of `context.capitals` for the current decimal context. The overall effect is to match the output of [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") as altered by the other format modifiers.
The result should be correctly rounded to a given precision `p` of digits after the decimal point. The rounding mode for [`float`](https://docs.python.org/3/library/functions.html#float "float") matches that of the [`round()`](https://docs.python.org/3/library/functions.html#round "round") builtin. For [`Decimal`](https://docs.python.org/3/library/decimal.html#decimal.Decimal "decimal.Decimal"), the rounding mode of the current [context](https://docs.python.org/3/library/decimal.html#decimal-context) will be used.
The available presentation types for [`complex`](https://docs.python.org/3/library/functions.html#complex "complex") are the same as those for [`float`](https://docs.python.org/3/library/functions.html#float "float") (`'%'` is not allowed). Both the real and imaginary components of a complex number are formatted as floating-point numbers, according to the specified presentation type. They are separated by the mandatory sign of the imaginary part, the latter being terminated by a `j` suffix. If the presentation type is missing, the result will match the output of [`str()`](https://docs.python.org/3/library/stdtypes.html#str "str") (complex numbers with a non-zero real part are also surrounded by parentheses), possibly altered by other format modifiers.
### Format examples[¶](https://docs.python.org/3/library/string.html#format-examples "Link to this heading")
This section contains examples of the [`str.format()`](https://docs.python.org/3/library/stdtypes.html#str.format "str.format") syntax and comparison with the old `%`-formatting.
In most of the cases the syntax is similar to the old `%`-formatting, with the addition of the `{}` and with `:` used instead of `%`. For example, `'%03.2f'` can be translated to `'{:03.2f}'`.
The new format syntax also supports new and different options, shown in the following examples.
Accessing arguments by position:
Copy```
>>> '{0}, {1}, {2}'.format('a', 'b', 'c')
'a, b, c'
>>> '{}, {}, {}'.format('a', 'b', 'c')  # 3.1+ only
'a, b, c'
>>> '{2}, {1}, {0}'.format('a', 'b', 'c')
'c, b, a'
>>> '{2}, {1}, {0}'.format(*'abc')      # unpacking argument sequence
'c, b, a'
>>> '{0}{1}{0}'.format('abra', 'cad')   # arguments' indices can be repeated
'abracadabra'

```

Accessing arguments by name:
Copy```
>>> 'Coordinates: {latitude}, {longitude}'.format(latitude='37.24N', longitude='-115.81W')
'Coordinates: 37.24N, -115.81W'
>>> coord = {'latitude': '37.24N', 'longitude': '-115.81W'}
>>> 'Coordinates: {latitude}, {longitude}'.format(**coord)
'Coordinates: 37.24N, -115.81W'

```

Accessing arguments’ attributes:
Copy```
>>> c = 3-5j
>>> ('The complex number {0} is formed from the real part {0.real} '
...  'and the imaginary part {0.imag}.').format(c)
'The complex number (3-5j) is formed from the real part 3.0 and the imaginary part -5.0.'
>>> class Point:
...     def __init__(self, x, y):
...         self.x, self.y = x, y
...     def __str__(self):
...         return 'Point({self.x}, {self.y})'.format(self=self)
...
>>> str(Point(4, 2))
'Point(4, 2)'

```

Accessing arguments’ items:
Copy```
>>> coord = (3, 5)
>>> 'X: {0[0]};  Y: {0[1]}'.format(coord)
'X: 3;  Y: 5'

```

Replacing `%s` and `%r`:
Copy```
>>> "repr() shows quotes: {!r}; str() doesn't: {!s}".format('test1', 'test2')
"repr() shows quotes: 'test1'; str() doesn't: test2"

```

Aligning the text and specifying a width:
Copy```
>>> '{:<30}'.format('left aligned')
'left aligned                  '
>>> '{:>30}'.format('right aligned')
'                 right aligned'
>>> '{:^30}'.format('centered')
'           centered           '
>>> '{:*^30}'.format('centered')  # use '*' as a fill char
'***********centered***********'

```

Replacing `%+f`, `%-f`, and `% f` and specifying a sign:
Copy```
>>> '{:+f}; {:+f}'.format(3.14, -3.14)  # show it always
'+3.140000; -3.140000'
>>> '{: f}; {: f}'.format(3.14, -3.14)  # show a space for positive numbers
' 3.140000; -3.140000'
>>> '{:-f}; {:-f}'.format(3.14, -3.14)  # show only the minus -- same as '{:f}; {:f}'
'3.140000; -3.140000'

```

Replacing `%x` and `%o` and converting the value to different bases:
Copy```
>>> # format also supports binary numbers
>>> "int: {0:d};  hex: {0:x};  oct: {0:o};  bin: {0:b}".format(42)
'int: 42;  hex: 2a;  oct: 52;  bin: 101010'
>>> # with 0x, 0o, or 0b as prefix:
>>> "int: {0:d};  hex: {0:#x};  oct: {0:#o};  bin: {0:#b}".format(42)
'int: 42;  hex: 0x2a;  oct: 0o52;  bin: 0b101010'

```

Using the comma or the underscore as a digit group separator:
Copy```
>>> '{:,}'.format(1234567890)
'1,234,567,890'
>>> '{:_}'.format(1234567890)
'1_234_567_890'
>>> '{:_b}'.format(1234567890)
'100_1001_1001_0110_0000_0010_1101_0010'
>>> '{:_x}'.format(1234567890)
'4996_02d2'
>>> '{:_}'.format(123456789.123456789)
'123_456_789.12345679'
>>> '{:.,}'.format(123456789.123456789)
'123456789.123,456,79'
>>> '{:,._}'.format(123456789.123456789)
'123,456,789.123_456_79'

```

Expressing a percentage:
Copy```
>>> points = 19
>>> total = 22
>>> 'Correct answers: {:.2%}'.format(points/total)
'Correct answers: 86.36%'

```

Using type-specific formatting:
Copy```
>>> import datetime
>>> d = datetime.datetime(2010, 7, 4, 12, 15, 58)
>>> '{:%Y-%m-%d %H:%M:%S}'.format(d)
'2010-07-04 12:15:58'

```

Nesting arguments and more complex examples:
Copy```
>>> for align, text in zip('<^>', ['left', 'center', 'right']):
...     '{0:{fill}{align}16}'.format(text, fill=align, align=align)
...
'left<<<<<<<<<<<<'
'^^^^^center^^^^^'
'>>>>>>>>>>>right'
>>>
>>> octets = [192, 168, 0, 1]
>>> '{:02X}{:02X}{:02X}{:02X}'.format(*octets)
'C0A80001'
>>> int(_, 16)
3232235521
>>>
>>> width = 5
>>> for num in range(5,12):
...     for base in 'dXob':
...         print('{0:{width}{base}}'.format(num, base=base, width=width), end=' ')
...     print()
...
    5     5     5   101
    6     6     6   110
    7     7     7   111
    8     8    10  1000
    9     9    11  1001
   10     A    12  1010
   11     B    13  1011

```
