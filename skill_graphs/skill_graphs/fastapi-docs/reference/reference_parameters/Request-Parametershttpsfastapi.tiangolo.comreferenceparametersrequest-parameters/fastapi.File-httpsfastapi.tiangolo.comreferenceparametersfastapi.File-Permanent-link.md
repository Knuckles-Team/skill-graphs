##  fastapi.File [¶](https://fastapi.tiangolo.com/reference/parameters/#fastapi.File "Permanent link")
```
File(
    default=Undefined,
    *,
    default_factory=_Unset,
    media_type="multipart/form-data",
    alias=None,
    alias_priority=_Unset,
    validation_alias=None,
    serialization_alias=None,
    title=None,
    description=None,
    gt=None,
    ge=None,
    lt=None,
    le=None,
    min_length=None,
    max_length=None,
    pattern=None,
    regex=None,
    discriminator=None,
    strict=_Unset,
    multiple_of=_Unset,
    allow_inf_nan=_Unset,
    max_digits=_Unset,
    decimal_places=_Unset,
    examples=None,
    example=_Unset,
    openapi_examples=None,
    deprecated=None,
    include_in_schema=True,
    json_schema_extra=None,
    **extra
)

```

PARAMETER | DESCRIPTION
---|---
`default` |  Default value if the parameter field is not set. **TYPE:** `Any` **DEFAULT:** `Undefined`
`default_factory` |  A callable to generate the default value. This doesn't affect `Path` parameters as the value is always required. The parameter is available only for compatibility. **TYPE:** `Callable[[], Any] | None` **DEFAULT:** `_Unset`
`media_type` |  The media type of this parameter field. Changing it would affect the generated OpenAPI, but currently it doesn't affect the parsing of the data. **TYPE:** `str` **DEFAULT:** `'multipart/form-data'`
`alias` |  An alternative name for the parameter field. This will be used to extract the data and for the generated OpenAPI. It is particularly useful when you can't use the name you want because it is a Python reserved keyword or similar. **TYPE:** `str | None` **DEFAULT:** `None`
`alias_priority` |  Priority of the alias. This affects whether an alias generator is used. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`validation_alias` |  'Whitelist' validation step. The parameter field will be the single one allowed by the alias or set of aliases defined. **TYPE:** `str | AliasPath | AliasChoices | None` **DEFAULT:** `None`
`serialization_alias` |  'Blacklist' validation step. The vanilla parameter field will be the single one of the alias' or set of aliases' fields and all the other fields will be ignored at serialization time. **TYPE:** `str | None` **DEFAULT:** `None`
`title` |  Human-readable title. **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Human-readable description. **TYPE:** `str | None` **DEFAULT:** `None`
`gt` |  Greater than. If set, value must be greater than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`ge` |  Greater than or equal. If set, value must be greater than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`lt` |  Less than. If set, value must be less than this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`le` |  Less than or equal. If set, value must be less than or equal to this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `None`
`min_length` |  Minimum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`max_length` |  Maximum length for strings. **TYPE:** `int | None` **DEFAULT:** `None`
`pattern` |  RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`regex` |  Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead. RegEx pattern for strings. **TYPE:** `str | None` **DEFAULT:** `None`
`discriminator` |  Parameter field name for discriminating the type in a tagged union. **TYPE:** `str | None` **DEFAULT:** `None`
`strict` |  If `True`, strict validation is applied to the field. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`multiple_of` |  Value must be a multiple of this. Only applicable to numbers. **TYPE:** `float | None` **DEFAULT:** `_Unset`
`allow_inf_nan` |  Allow `inf`, `-inf`, `nan`. Only applicable to numbers. **TYPE:** `bool | None` **DEFAULT:** `_Unset`
`max_digits` |  Maximum number of digits allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`decimal_places` |  Maximum number of decimal places allowed for decimal values. **TYPE:** `int | None` **DEFAULT:** `_Unset`
`examples` |  Example values for this field. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/) **TYPE:** `list[Any] | None` **DEFAULT:** `None`
`example` |  Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, although still supported. Use examples instead.  **TYPE:** `Any | None` **DEFAULT:** `_Unset`
`openapi_examples` |  OpenAPI-specific examples. It will be added to the generated OpenAPI (e.g. visible at `/docs`). Swagger UI (that provides the `/docs` interface) has better support for the OpenAPI-specific examples than the JSON Schema `examples`, that's the main use case for this. Read more about it in the [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter). **TYPE:** `dict[str, Example[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.Example "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">Example</span> \(<code>fastapi.openapi.models.Example</code>\)")] | None` **DEFAULT:** `None`
`deprecated` |  Mark this parameter field as deprecated. It will affect the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `deprecated | str | bool | None` **DEFAULT:** `None`
`include_in_schema` |  To include (or not) this parameter field in the generated OpenAPI. You probably don't need it, but it's available. This affects the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `bool` **DEFAULT:** `True`
`json_schema_extra` |  Any additional JSON schema data. **TYPE:** `dict[str, Any] | None` **DEFAULT:** `None`
`**extra` |  The `extra` kwargs is deprecated. Use `json_schema_extra` instead. Include extra fields used by the JSON Schema. **TYPE:** `Any` **DEFAULT:** `{}`
Source code in `fastapi/param_functions.py`
```
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
2020
2021
2022
2023
2024
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
2183
2184
2185
2186
2187
2188
2189
2190
2191
2192
2193
2194
2195
2196
2197
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
2216
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
2235
2236
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
2262
2263
2264
2265
2266
2267
2268
2269
2270
2271
2272
2273
2274
2275
2276
2277
2278
2279
2280
2281
```
| ```
def File(  # noqa: N802
    default: Annotated[
        Any,
        Doc(
            """
            Default value if the parameter field is not set.
            """
        ),
    ] = Undefined,
    *,
    default_factory: Annotated[
        Callable[[], Any] | None,
        Doc(
            """
            A callable to generate the default value.

            This doesn't affect `Path` parameters as the value is always required.
            The parameter is available only for compatibility.
            """
        ),
    ] = _Unset,
    media_type: Annotated[
        str,
        Doc(
            """
            The media type of this parameter field. Changing it would affect the
            generated OpenAPI, but currently it doesn't affect the parsing of the data.
            """
        ),
    ] = "multipart/form-data",
    alias: Annotated[
        str | None,
        Doc(
            """
            An alternative name for the parameter field.

            This will be used to extract the data and for the generated OpenAPI.
            It is particularly useful when you can't use the name you want because it
            is a Python reserved keyword or similar.
            """
        ),
    ] = None,
    alias_priority: Annotated[
        int | None,
        Doc(
            """
            Priority of the alias. This affects whether an alias generator is used.
            """
        ),
    ] = _Unset,
    validation_alias: Annotated[
        str | AliasPath | AliasChoices | None,
        Doc(
            """
            'Whitelist' validation step. The parameter field will be the single one
            allowed by the alias or set of aliases defined.
            """
        ),
    ] = None,
    serialization_alias: Annotated[
        str | None,
        Doc(
            """
            'Blacklist' validation step. The vanilla parameter field will be the
            single one of the alias' or set of aliases' fields and all the other
            fields will be ignored at serialization time.
            """
        ),
    ] = None,
    title: Annotated[
        str | None,
        Doc(
            """
            Human-readable title.
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Human-readable description.
            """
        ),
    ] = None,
    gt: Annotated[
        float | None,
        Doc(
            """
            Greater than. If set, value must be greater than this. Only applicable to
            numbers.
            """
        ),
    ] = None,
    ge: Annotated[
        float | None,
        Doc(
            """
            Greater than or equal. If set, value must be greater than or equal to
            this. Only applicable to numbers.
            """
        ),
    ] = None,
    lt: Annotated[
        float | None,
        Doc(
            """
            Less than. If set, value must be less than this. Only applicable to numbers.
            """
        ),
    ] = None,
    le: Annotated[
        float | None,
        Doc(
            """
            Less than or equal. If set, value must be less than or equal to this.
            Only applicable to numbers.
            """
        ),
    ] = None,
    min_length: Annotated[
        int | None,
        Doc(
            """
            Minimum length for strings.
            """
        ),
    ] = None,
    max_length: Annotated[
        int | None,
        Doc(
            """
            Maximum length for strings.
            """
        ),
    ] = None,
    pattern: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
    ] = None,
    regex: Annotated[
        str | None,
        Doc(
            """
            RegEx pattern for strings.
            """
        ),
        deprecated(
            "Deprecated in FastAPI 0.100.0 and Pydantic v2, use `pattern` instead."
        ),
    ] = None,
    discriminator: Annotated[
        str | None,
        Doc(
            """
            Parameter field name for discriminating the type in a tagged union.
            """
        ),
    ] = None,
    strict: Annotated[
        bool | None,
        Doc(
            """
            If `True`, strict validation is applied to the field.
            """
        ),
    ] = _Unset,
    multiple_of: Annotated[
        float | None,
        Doc(
            """
            Value must be a multiple of this. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    allow_inf_nan: Annotated[
        bool | None,
        Doc(
            """
            Allow `inf`, `-inf`, `nan`. Only applicable to numbers.
            """
        ),
    ] = _Unset,
    max_digits: Annotated[
        int | None,
        Doc(
            """
            Maximum number of digits allowed for decimal values.
            """
        ),
    ] = _Unset,
    decimal_places: Annotated[
        int | None,
        Doc(
            """
            Maximum number of decimal places allowed for decimal values.
            """
        ),
    ] = _Unset,
    examples: Annotated[
        list[Any] | None,
        Doc(
            """
            Example values for this field.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/)
            """
        ),
    ] = None,
    example: Annotated[
        Any | None,
        deprecated(
            "Deprecated in OpenAPI 3.1.0 that now uses JSON Schema 2020-12, "
            "although still supported. Use examples instead."
        ),
    ] = _Unset,
    openapi_examples: Annotated[
        dict[str, Example] | None,
        Doc(
            """
            OpenAPI-specific examples.

            It will be added to the generated OpenAPI (e.g. visible at `/docs`).

            Swagger UI (that provides the `/docs` interface) has better support for the
            OpenAPI-specific examples than the JSON Schema `examples`, that's the main
            use case for this.

            Read more about it in the
            [FastAPI docs for Declare Request Example Data](https://fastapi.tiangolo.com/tutorial/schema-extra-example/#using-the-openapi_examples-parameter).
            """
        ),
    ] = None,
    deprecated: Annotated[
        deprecated | str | bool | None,
        Doc(
            """
            Mark this parameter field as deprecated.

            It will affect the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    include_in_schema: Annotated[
        bool,
        Doc(
            """
            To include (or not) this parameter field in the generated OpenAPI.
            You probably don't need it, but it's available.

            This affects the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = True,
    json_schema_extra: Annotated[
        dict[str, Any] | None,
        Doc(
            """
            Any additional JSON schema data.
            """
        ),
    ] = None,
    **extra: Annotated[
        Any,
        Doc(
            """
            Include extra fields used by the JSON Schema.
            """
        ),
        deprecated(
            """
            The `extra` kwargs is deprecated. Use `json_schema_extra` instead.
            """
        ),
    ],
) -> Any:
    return params.File(
        default=default,
        default_factory=default_factory,
        media_type=media_type,
        alias=alias,
        alias_priority=alias_priority,
        validation_alias=validation_alias,
        serialization_alias=serialization_alias,
        title=title,
        description=description,
        gt=gt,
        ge=ge,
        lt=lt,
        le=le,
        min_length=min_length,
        max_length=max_length,
        pattern=pattern,
        regex=regex,
        discriminator=discriminator,
        strict=strict,
        multiple_of=multiple_of,
        allow_inf_nan=allow_inf_nan,
        max_digits=max_digits,
        decimal_places=decimal_places,
        example=example,
        examples=examples,
        openapi_examples=openapi_examples,
        deprecated=deprecated,
        include_in_schema=include_in_schema,
        json_schema_extra=json_schema_extra,
        **extra,
    )

```

---|---
