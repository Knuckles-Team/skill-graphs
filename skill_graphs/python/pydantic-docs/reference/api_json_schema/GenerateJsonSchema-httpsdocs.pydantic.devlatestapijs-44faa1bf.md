Parameters:
Name | Type | Description | Default
---|---|---|---
`field` |  `ModelField | DataclassField | TypedDictField` |  The schema for the field itself. |  _required_
`total` |  |  Only applies to `TypedDictField`s. Indicates if the `TypedDict` this field belongs to is total, in which case any fields that don't explicitly specify `required=False` are required. |  _required_
Returns:
Type | Description
---|---
|  `True` if the field should be marked as required in the generated JSON schema, `False` otherwise.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def field_is_required(
    self,
    field: core_schema.ModelField | core_schema.DataclassField | core_schema.TypedDictField,
    total: bool,
) -> bool:
    """Whether the field should be marked as required in the generated JSON schema.
    (Note that this is irrelevant if the field is not present in the JSON schema.).

    Args:
        field: The schema for the field itself.
        total: Only applies to `TypedDictField`s.
            Indicates if the `TypedDict` this field belongs to is total, in which case any fields that don't
            explicitly specify `required=False` are required.

    Returns:
        `True` if the field should be marked as required in the generated JSON schema, `False` otherwise.
    """
    if field['type'] == 'typed-dict-field':
        required = field.get('required', total)
    else:
        required = field['schema']['type'] != 'default'

    if self.mode == 'serialization':
        has_exclude_if = field.get('serialization_exclude_if') is not None
        if self._config.json_schema_serialization_defaults_required:
            return not has_exclude_if
        else:
            return required and not has_exclude_if
    else:
        return required

```

---|---
###  dataclass_args_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dataclass_args_schema)
```
dataclass_args_schema(
    schema: DataclassArgsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a dataclass's constructor arguments.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DataclassArgsSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def dataclass_args_schema(self, schema: core_schema.DataclassArgsSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a dataclass's constructor arguments.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    named_required_fields: list[tuple[str, bool, CoreSchemaField]] = [
        (field['name'], self.field_is_required(field, total=True), field)
        for field in schema['fields']
        if self.field_is_present(field)
    ]
    if self.mode == 'serialization':
        named_required_fields.extend(self._name_required_computed_fields(schema.get('computed_fields', [])))
    return self._named_required_fields_schema(named_required_fields)

```

---|---
###  dataclass_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.dataclass_schema)
```
dataclass_schema(
    schema: DataclassSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a dataclass.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DataclassSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def dataclass_schema(self, schema: core_schema.DataclassSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a dataclass.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    from ._internal._dataclasses import is_stdlib_dataclass

    cls = schema['cls']
    config: ConfigDict = getattr(cls, '__pydantic_config__', cast('ConfigDict', {}))

    with self._config_wrapper_stack.push(config):
        json_schema = self.generate_inner(schema['schema']).copy()

    self._update_class_schema(json_schema, cls, config)

    # Dataclass-specific handling of description
    if is_stdlib_dataclass(cls):
        # vanilla dataclass; don't use cls.__doc__ as it will contain the class signature by default
        description = None
    else:
        description = None if cls.__doc__ is None else inspect.cleandoc(cls.__doc__)
    if description:
        json_schema['description'] = description

    return json_schema

```

---|---
###  arguments_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.arguments_schema)
```
arguments_schema(
    schema: ArgumentsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's arguments.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ArgumentsSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def arguments_schema(self, schema: core_schema.ArgumentsSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a function's arguments.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    prefer_positional = schema.get('metadata', {}).get('pydantic_js_prefer_positional_arguments')

    arguments = schema['arguments_schema']
    kw_only_arguments = [a for a in arguments if a.get('mode') == 'keyword_only']
    kw_or_p_arguments = [a for a in arguments if a.get('mode') in {'positional_or_keyword', None}]
    p_only_arguments = [a for a in arguments if a.get('mode') == 'positional_only']
    var_args_schema = schema.get('var_args_schema')
    var_kwargs_schema = schema.get('var_kwargs_schema')

    if prefer_positional:
        positional_possible = not kw_only_arguments and not var_kwargs_schema
        if positional_possible:
            return self.p_arguments_schema(p_only_arguments + kw_or_p_arguments, var_args_schema)

    keyword_possible = not p_only_arguments and not var_args_schema
    if keyword_possible:
        return self.kw_arguments_schema(kw_or_p_arguments + kw_only_arguments, var_kwargs_schema)

    if not prefer_positional:
        positional_possible = not kw_only_arguments and not var_kwargs_schema
        if positional_possible:
            return self.p_arguments_schema(p_only_arguments + kw_or_p_arguments, var_args_schema)

    raise PydanticInvalidForJsonSchema(
        'Unable to generate JSON schema for arguments validator with positional-only and keyword-only arguments'
    )

```

---|---
###  kw_arguments_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.kw_arguments_schema)
```
kw_arguments_schema(
    arguments: [ArgumentsParameter],
    var_kwargs_schema: CoreSchema | None,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's keyword arguments.
Parameters:
Name | Type | Description | Default
---|---|---|---
`arguments` |  `ArgumentsParameter]` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1857
1858
1859
1860
1861
1862
1863
1864
1865
1866
1867
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
```
| ```
def kw_arguments_schema(
    self, arguments: list[core_schema.ArgumentsParameter], var_kwargs_schema: CoreSchema | None
) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a function's keyword arguments.

    Args:
        arguments: The core schema.

    Returns:
        The generated JSON schema.
    """
    properties: dict[str, JsonSchemaValue] = {}
    required: list[str] = []
    for argument in arguments:
        name = self.get_argument_name(argument)
        argument_schema = self.generate_inner(argument['schema']).copy()
        if 'title' not in argument_schema and self.field_title_should_be_set(argument['schema']):
            argument_schema['title'] = self.get_title_from_name(name)
        properties[name] = argument_schema

        if argument['schema']['type'] != 'default':
            # This assumes that if the argument has a default value,
            # the inner schema must be of type WithDefaultSchema.
            # I believe this is true, but I am not 100% sure
            required.append(name)

    json_schema: JsonSchemaValue = {'type': 'object', 'properties': properties}
    if required:
        json_schema['required'] = required

    if var_kwargs_schema:
        additional_properties_schema = self.generate_inner(var_kwargs_schema)
        if additional_properties_schema:
            json_schema['additionalProperties'] = additional_properties_schema
    else:
        json_schema['additionalProperties'] = False
    return json_schema

```

---|---
###  p_arguments_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.p_arguments_schema)
```
p_arguments_schema(
    arguments: [ArgumentsParameter],
    var_args_schema: CoreSchema | None,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's positional arguments.
Parameters:
Name | Type | Description | Default
---|---|---|---
`arguments` |  `ArgumentsParameter]` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
1895
1896
1897
1898
1899
1900
1901
1902
1903
1904
1905
1906
1907
1908
1909
1910
1911
1912
1913
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
```
| ```
def p_arguments_schema(
    self, arguments: list[core_schema.ArgumentsParameter], var_args_schema: CoreSchema | None
) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a function's positional arguments.

    Args:
        arguments: The core schema.

    Returns:
        The generated JSON schema.
    """
    prefix_items: list[JsonSchemaValue] = []
    min_items = 0

    for argument in arguments:
        name = self.get_argument_name(argument)

        argument_schema = self.generate_inner(argument['schema']).copy()
        if 'title' not in argument_schema and self.field_title_should_be_set(argument['schema']):
            argument_schema['title'] = self.get_title_from_name(name)
        prefix_items.append(argument_schema)

        if argument['schema']['type'] != 'default':
            # This assumes that if the argument has a default value,
            # the inner schema must be of type WithDefaultSchema.
            # I believe this is true, but I am not 100% sure
            min_items += 1

    json_schema: JsonSchemaValue = {'type': 'array'}
    if prefix_items:
        json_schema['prefixItems'] = prefix_items
    if min_items:
        json_schema['minItems'] = min_items

    if var_args_schema:
        items_schema = self.generate_inner(var_args_schema)
        if items_schema:
            json_schema['items'] = items_schema
    else:
        json_schema['maxItems'] = len(prefix_items)

    return json_schema

```

---|---
###  get_argument_name [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_argument_name)
```
get_argument_name(
    argument: ArgumentsParameter | ArgumentsV3Parameter,
) ->

```

Retrieves the name of an argument.
Parameters:
Name | Type | Description | Default
---|---|---|---
`argument` |  `ArgumentsParameter | ArgumentsV3Parameter` |  The core schema. |  _required_
Returns:
Type | Description
---|---
|  The name of the argument.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def get_argument_name(self, argument: core_schema.ArgumentsParameter | core_schema.ArgumentsV3Parameter) -> str:
    """Retrieves the name of an argument.

    Args:
        argument: The core schema.

    Returns:
        The name of the argument.
    """
    name = argument['name']
    if self.by_alias:
        alias = argument.get('alias')
        if isinstance(alias, str):
            name = alias
        else:
            pass  # might want to do something else?
    return name

```

---|---
###  arguments_v3_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.arguments_v3_schema)
```
arguments_v3_schema(
    schema: ArgumentsV3Schema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function's arguments.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ArgumentsV3Schema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def arguments_v3_schema(self, schema: core_schema.ArgumentsV3Schema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a function's arguments.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    arguments = schema['arguments_schema']
    properties: dict[str, JsonSchemaValue] = {}
    required: list[str] = []
    for argument in arguments:
        mode = argument.get('mode', 'positional_or_keyword')
        name = self.get_argument_name(argument)
        argument_schema = self.generate_inner(argument['schema']).copy()
        if mode == 'var_args':
            argument_schema = {'type': 'array', 'items': argument_schema}
        elif mode == 'var_kwargs_uniform':
            argument_schema = {'type': 'object', 'additionalProperties': argument_schema}

        argument_schema.setdefault('title', self.get_title_from_name(name))
        properties[name] = argument_schema

        if (
            (mode == 'var_kwargs_unpacked_typed_dict' and 'required' in argument_schema)
            or mode not in {'var_args', 'var_kwargs_uniform', 'var_kwargs_unpacked_typed_dict'}
            and argument['schema']['type'] != 'default'
        ):
            # This assumes that if the argument has a default value,
            # the inner schema must be of type WithDefaultSchema.
            # I believe this is true, but I am not 100% sure
            required.append(name)

    json_schema: JsonSchemaValue = {'type': 'object', 'properties': properties}
    if required:
        json_schema['required'] = required
    return json_schema

```

---|---
###  call_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.call_schema)
```
call_schema(schema: CallSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a function call.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CallSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def call_schema(self, schema: core_schema.CallSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a function call.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['arguments_schema'])

```

---|---
###  custom_error_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.custom_error_schema)
```
custom_error_schema(
    schema: CustomErrorSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a custom error.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CustomErrorSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def custom_error_schema(self, schema: core_schema.CustomErrorSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a custom error.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return self.generate_inner(schema['schema'])

```

---|---
###  json_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.json_schema)
```
json_schema(schema: JsonSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a JSON object.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `JsonSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def json_schema(self, schema: core_schema.JsonSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a JSON object.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    content_core_schema = schema.get('schema') or core_schema.any_schema()
    content_json_schema = self.generate_inner(content_core_schema)
    if self.mode == 'validation':
        return {'type': 'string', 'contentMediaType': 'application/json', 'contentSchema': content_json_schema}
    else:
        # self.mode == 'serialization'
        return content_json_schema

```

---|---
###  url_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.url_schema)
```
url_schema(schema: UrlSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a URL.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `UrlSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def url_schema(self, schema: core_schema.UrlSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a URL.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    json_schema = {'type': 'string', 'format': 'uri', 'minLength': 1}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.string)
    return json_schema

```

---|---
###  multi_host_url_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.multi_host_url_schema)
```
multi_host_url_schema(
    schema: MultiHostUrlSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a URL that can be used with multiple hosts.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `MultiHostUrlSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def multi_host_url_schema(self, schema: core_schema.MultiHostUrlSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a URL that can be used with multiple hosts.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    # Note: 'multi-host-uri' is a custom/pydantic-specific format, not part of the JSON Schema spec
    json_schema = {'type': 'string', 'format': 'multi-host-uri', 'minLength': 1}
    self.update_with_validations(json_schema, schema, self.ValidationsMapping.string)
    return json_schema

```

---|---
###  uuid_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.uuid_schema)
```
uuid_schema(schema: UuidSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a UUID.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `UuidSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def uuid_schema(self, schema: core_schema.UuidSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a UUID.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string', 'format': 'uuid'}

```

---|---
###  definitions_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.definitions_schema)
```
definitions_schema(
    schema: DefinitionsSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that defines a JSON object with definitions.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DefinitionsSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def definitions_schema(self, schema: core_schema.DefinitionsSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that defines a JSON object with definitions.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    for definition in schema['definitions']:
        try:
            self.generate_inner(definition)
        except PydanticInvalidForJsonSchema as e:  # noqa: PERF203
