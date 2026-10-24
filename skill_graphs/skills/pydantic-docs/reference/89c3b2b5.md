            core_ref: CoreRef = CoreRef(definition['ref'])  # type: ignore
            self._core_defs_invalid_for_json_schema[self.get_defs_ref((core_ref, self.mode))] = e
            continue
    return self.generate_inner(schema['schema'])

```

---|---
###  definition_ref_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.definition_ref_schema)
```
definition_ref_schema(
    schema: DefinitionReferenceSchema,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a schema that references a definition.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `DefinitionReferenceSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def definition_ref_schema(self, schema: core_schema.DefinitionReferenceSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a schema that references a definition.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    core_ref = CoreRef(schema['schema_ref'])
    _, ref_json_schema = self.get_cache_defs_ref_schema(core_ref)
    return ref_json_schema

```

---|---
###  ser_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.ser_schema)
```
ser_schema(
    schema: (
        SerSchema | IncExSeqSerSchema | IncExDictSerSchema
    ),
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue) | None

```

Generates a JSON schema that matches a schema that defines a serialized object.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `SerSchema | IncExSeqSerSchema | IncExDictSerSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue) | None` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def ser_schema(
    self, schema: core_schema.SerSchema | core_schema.IncExSeqSerSchema | core_schema.IncExDictSerSchema
) -> JsonSchemaValue | None:
    """Generates a JSON schema that matches a schema that defines a serialized object.

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    schema_type = schema['type']
    if schema_type == 'function-plain' or schema_type == 'function-wrap':
        # PlainSerializerFunctionSerSchema or WrapSerializerFunctionSerSchema
        return_schema = schema.get('return_schema')
        if return_schema is not None:
            return self.generate_inner(return_schema)
    elif schema_type == 'format' or schema_type == 'to-string':
        # FormatSerSchema or ToStringSerSchema
        return self.str_schema(core_schema.str_schema())
    elif schema['type'] == 'model':
        # ModelSerSchema
        return self.generate_inner(schema['schema'])
    return None

```

---|---
###  complex_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.complex_schema)
```
complex_schema(schema: ComplexSchema) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema that matches a complex number.
JSON has no standard way to represent complex numbers. Complex number is not a numeric type. Here we represent complex number as strings following the rule defined by Python. For instance, '1+2j' is an accepted complex string. Details can be found in
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `ComplexSchema` |  The core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def complex_schema(self, schema: core_schema.ComplexSchema) -> JsonSchemaValue:
    """Generates a JSON schema that matches a complex number.

    JSON has no standard way to represent complex numbers. Complex number is not a numeric
    type. Here we represent complex number as strings following the rule defined by Python.
    For instance, '1+2j' is an accepted complex string. Details can be found in
    [Python's `complex` documentation][complex].

    Args:
        schema: The core schema.

    Returns:
        The generated JSON schema.
    """
    return {'type': 'string'}

```

---|---
###  get_title_from_name [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_title_from_name)
```
get_title_from_name(name: ) ->

```

Retrieves a title from a name.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name to retrieve a title from. |  _required_
Returns:
Type | Description
---|---
|  The title.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def get_title_from_name(self, name: str) -> str:
    """Retrieves a title from a name.

    Args:
        name: The name to retrieve a title from.

    Returns:
        The title.
    """
    return name.title().replace('_', ' ').strip()

```

---|---
###  field_title_should_be_set [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.field_title_should_be_set)
```
field_title_should_be_set(
    schema: CoreSchemaOrField,
) ->

```

Returns true if a field with the given schema should have a title set based on the field name.
Intuitively, we want this to return true for schemas that wouldn't otherwise provide their own title (e.g., int, float, str), and false for those that would (e.g., BaseModel subclasses).
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchemaOrField` |  The schema to check. |  _required_
Returns:
Type | Description
---|---
|  `True` if the field should have a title set, `False` otherwise.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def field_title_should_be_set(self, schema: CoreSchemaOrField) -> bool:
    """Returns true if a field with the given schema should have a title set based on the field name.

    Intuitively, we want this to return true for schemas that wouldn't otherwise provide their own title
    (e.g., int, float, str), and false for those that would (e.g., BaseModel subclasses).

    Args:
        schema: The schema to check.

    Returns:
        `True` if the field should have a title set, `False` otherwise.
    """
    if _core_utils.is_core_schema_field(schema):
        if schema['type'] == 'computed-field':
            field_schema = schema['return_schema']
        else:
            field_schema = schema['schema']
        return self.field_title_should_be_set(field_schema)

    elif _core_utils.is_core_schema(schema):
        if schema.get('ref'):  # things with refs, such as models and enums, should not have titles set
            return False
        if schema['type'] in {'default', 'nullable', 'definitions'}:
            return self.field_title_should_be_set(schema['schema'])  # type: ignore[typeddict-item]
        if _core_utils.is_function_with_inner_schema(schema):
            return self.field_title_should_be_set(schema['schema'])
        if schema['type'] == 'definition-ref':
            # Referenced schemas should not have titles set for the same reason
            # schemas with refs should not
            return False
        return True  # anything else should have title set

    else:
        raise PydanticInvalidForJsonSchema(f'Unexpected schema type: schema={schema}')  # pragma: no cover

```

---|---
###  normalize_name [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.normalize_name)
```
normalize_name(name: ) ->

```

Normalizes a name to be used as a key in a dictionary.
Parameters:
Name | Type | Description | Default
---|---|---|---
`name` |  |  The name to normalize. |  _required_
Returns:
Type | Description
---|---
|  The normalized name.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def normalize_name(self, name: str) -> str:
    """Normalizes a name to be used as a key in a dictionary.

    Args:
        name: The name to normalize.

    Returns:
        The normalized name.
    """
    return re.sub(r'[^a-zA-Z0-9.\-_]', '_', name).replace('.', '__')

```

---|---
###  get_defs_ref [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_defs_ref)
```
get_defs_ref(core_mode_ref: CoreModeRef) -> DefsRef

```

Override this method to change the way that definitions keys are generated from a core reference.
Parameters:
Name | Type | Description | Default
---|---|---|---
`core_mode_ref` |  `CoreModeRef` |  The core reference. |  _required_
Returns:
Type | Description
---|---
`DefsRef` |  The definitions key.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def get_defs_ref(self, core_mode_ref: CoreModeRef) -> DefsRef:
    """Override this method to change the way that definitions keys are generated from a core reference.

    Args:
        core_mode_ref: The core reference.

    Returns:
        The definitions key.
    """
    # Split the core ref into "components"; generic origins and arguments are each separate components
    core_ref, mode = core_mode_ref
    components = re.split(r'([\][,])', core_ref)
    # Remove IDs from each component
    components = [x.rsplit(':', 1)[0] for x in components]
    core_ref_no_id = ''.join(components)
    # Remove everything before the last period from each "component"
    components = [re.sub(r'(?:[^.[\]]+\.)+((?:[^.[\]]+))', r'\1', x) for x in components]
    short_ref = ''.join(components)

    mode_title = _MODE_TITLE_MAPPING[mode]

    # It is important that the generated defs_ref values be such that at least one choice will not
    # be generated for any other core_ref. Currently, this should be the case because we include
    # the id of the source type in the core_ref
    name = DefsRef(self.normalize_name(short_ref))
    name_mode = DefsRef(self.normalize_name(short_ref) + f'-{mode_title}')
    module_qualname = DefsRef(self.normalize_name(core_ref_no_id))
    module_qualname_mode = DefsRef(f'{module_qualname}-{mode_title}')
    module_qualname_id = DefsRef(self.normalize_name(core_ref))
    occurrence_index = self._collision_index.get(module_qualname_id)
    if occurrence_index is None:
        self._collision_counter[module_qualname] += 1
        occurrence_index = self._collision_index[module_qualname_id] = self._collision_counter[module_qualname]

    module_qualname_occurrence = DefsRef(f'{module_qualname}__{occurrence_index}')
    module_qualname_occurrence_mode = DefsRef(f'{module_qualname_mode}__{occurrence_index}')

    self._prioritized_defsref_choices[module_qualname_occurrence_mode] = [
        name,
        name_mode,
        module_qualname,
        module_qualname_mode,
        module_qualname_occurrence,
        module_qualname_occurrence_mode,
    ]

    return module_qualname_occurrence_mode

```

---|---
###  get_cache_defs_ref_schema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_cache_defs_ref_schema)
```
get_cache_defs_ref_schema(
    core_ref: CoreRef,
) -> [DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]

```

This method wraps the get_defs_ref method with some cache-lookup/population logic, and returns both the produced defs_ref and the JSON schema that will refer to the right definition.
Parameters:
Name | Type | Description | Default
---|---|---|---
`core_ref` |  `CoreRef` |  The core reference to get the definitions reference for. |  _required_
Returns:
Type | Description
---|---
`DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  A tuple of the definitions reference and the JSON schema that will refer to it.
Source code in `pydantic/json_schema.py`
```
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
```
| ```
def get_cache_defs_ref_schema(self, core_ref: CoreRef) -> tuple[DefsRef, JsonSchemaValue]:
    """This method wraps the get_defs_ref method with some cache-lookup/population logic,
    and returns both the produced defs_ref and the JSON schema that will refer to the right definition.

    Args:
        core_ref: The core reference to get the definitions reference for.

    Returns:
        A tuple of the definitions reference and the JSON schema that will refer to it.
    """
    core_mode_ref = (core_ref, self.mode)
    maybe_defs_ref = self.core_to_defs_refs.get(core_mode_ref)
    if maybe_defs_ref is not None:
        json_ref = self.core_to_json_refs[core_mode_ref]
        return maybe_defs_ref, {'$ref': json_ref}

    defs_ref = self.get_defs_ref(core_mode_ref)

    # populate the ref translation mappings
    self.core_to_defs_refs[core_mode_ref] = defs_ref
    self.defs_to_core_refs[defs_ref] = core_mode_ref

    json_ref = JsonRef(self.ref_template.format(model=defs_ref))
    self.core_to_json_refs[core_mode_ref] = json_ref
    self.json_to_defs_refs[json_ref] = defs_ref
    ref_json_schema = {'$ref': json_ref}
    return defs_ref, ref_json_schema

```

---|---
###  handle_ref_overrides [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.handle_ref_overrides)
```
handle_ref_overrides(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Remove any sibling keys that are redundant with the referenced schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`json_schema` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The schema to remove redundant sibling keys from. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The schema with redundant sibling keys removed.
Source code in `pydantic/json_schema.py`
```
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
2292
2293
2294
2295
2296
2297
2298
2299
2300
2301
2302
2303
2304
```
| ```
def handle_ref_overrides(self, json_schema: JsonSchemaValue) -> JsonSchemaValue:
    """Remove any sibling keys that are redundant with the referenced schema.

    Args:
        json_schema: The schema to remove redundant sibling keys from.

    Returns:
        The schema with redundant sibling keys removed.
    """
    if '$ref' in json_schema:
        # prevent modifications to the input; this copy may be safe to drop if there is significant overhead
        json_schema = json_schema.copy()

        referenced_json_schema = self.get_schema_from_definitions(JsonRef(json_schema['$ref']))
        if referenced_json_schema is None:
            # This can happen when building schemas for models with not-yet-defined references.
            # It may be a good idea to do a recursive pass at the end of the generation to remove
            # any redundant override keys.
            return json_schema
        for k, v in list(json_schema.items()):
            if k == '$ref':
                continue
            if k in referenced_json_schema and referenced_json_schema[k] == v:
                del json_schema[k]  # redundant key

    return json_schema

```

---|---
###  encode_default [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.encode_default)
```
encode_default(dft: ) ->

```

Encode a default value to a JSON-serializable value.
This is used to encode default values for fields in the generated JSON schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`dft` |  |  The default value to encode. |  _required_
Returns:
Type | Description
---|---
|  The encoded default value.
Source code in `pydantic/json_schema.py`
```
2317
2318
2319
2320
2321
2322
2323
2324
2325
2326
2327
2328
2329
2330
2331
2332
2333
2334
2335
2336
2337
2338
2339
2340
2341
2342
2343
2344
```
| ```
def encode_default(self, dft: Any) -> Any:
    """Encode a default value to a JSON-serializable value.

    This is used to encode default values for fields in the generated JSON schema.

    Args:
        dft: The default value to encode.

    Returns:
        The encoded default value.
    """
    from .type_adapter import TypeAdapter, _type_has_config

    config = self._config
    try:
        default = (
            dft
            if _type_has_config(type(dft))
            else TypeAdapter(type(dft), config=config.config_dict).dump_python(
                dft, by_alias=self.by_alias, mode='json'
            )
        )
    except PydanticSchemaGenerationError:
        raise pydantic_core.PydanticSerializationError(f'Unable to encode default value {dft}')

    return pydantic_core.to_jsonable_python(
        default, timedelta_mode=config.ser_json_timedelta, bytes_mode=config.ser_json_bytes, by_alias=self.by_alias
    )

```

---|---
###  update_with_validations [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.update_with_validations)
```
update_with_validations(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
    core_schema: CoreSchema,
    mapping: [, ],
) -> None

```

Update the json_schema with the corresponding validations specified in the core_schema, using the provided mapping to translate keys in core_schema to the appropriate keys for a JSON schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`json_schema` |  `JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The JSON schema to update. |  _required_
`core_schema` |  `CoreSchema` |  The core schema to get the validations from. |  _required_
`mapping` |  |  A mapping from core_schema attribute names to the corresponding JSON schema attribute names. |  _required_
Source code in `pydantic/json_schema.py`
```
2346
2347
2348
2349
2350
2351
2352
2353
2354
2355
2356
2357
2358
2359
```
| ```
def update_with_validations(
    self, json_schema: JsonSchemaValue, core_schema: CoreSchema, mapping: dict[str, str]
) -> None:
    """Update the json_schema with the corresponding validations specified in the core_schema,
    using the provided mapping to translate keys in core_schema to the appropriate keys for a JSON schema.

    Args:
        json_schema: The JSON schema to update.
        core_schema: The core schema to get the validations from.
        mapping: A mapping from core_schema attribute names to the corresponding JSON schema attribute names.
    """
    for core_key, json_schema_key in mapping.items():
        if core_key in core_schema:
            json_schema[json_schema_key] = core_schema[core_key]

```

---|---
###  get_json_ref_counts [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.get_json_ref_counts)
```
get_json_ref_counts(
    json_schema: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
) -> [JsonRef, ]

```

Get all values corresponding to the key '$ref' anywhere in the json_schema.
Source code in `pydantic/json_schema.py`
```
2405
2406
2407
2408
2409
2410
2411
2412
2413
2414
2415
2416
2417
2418
2419
2420
2421
2422
2423
2424
2425
2426
2427
2428
2429
2430
2431
2432
2433
2434
2435
2436
2437
2438
2439
```
| ```
def get_json_ref_counts(self, json_schema: JsonSchemaValue) -> dict[JsonRef, int]:
    """Get all values corresponding to the key '$ref' anywhere in the json_schema."""
    json_refs: dict[JsonRef, int] = Counter()

    def _add_json_refs(schema: Any) -> None:
        if isinstance(schema, dict):
            if '$ref' in schema:
                json_ref = JsonRef(schema['$ref'])
                if not isinstance(json_ref, str):
                    return  # in this case, '$ref' might have been the name of a property
                already_visited = json_ref in json_refs
                json_refs[json_ref] += 1
                if already_visited:
                    return  # prevent recursion on a definition that was already visited
                try:
                    defs_ref = self.json_to_defs_refs[json_ref]
                    if defs_ref in self._core_defs_invalid_for_json_schema:
                        raise self._core_defs_invalid_for_json_schema[defs_ref]
                    _add_json_refs(self.definitions[defs_ref])
                except KeyError:
                    if not json_ref.startswith(('http://', 'https://')):
                        raise

            for k, v in schema.items():
                if k == 'examples' and isinstance(v, list):
                    # Skip examples that may contain arbitrary values and references
                    # (see the comment in `_get_all_json_refs` for more details).
                    continue
                _add_json_refs(v)
        elif isinstance(schema, list):
            for v in schema:
                _add_json_refs(v)

    _add_json_refs(json_schema)
    return json_refs

```

---|---
###  emit_warning [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.emit_warning)
```
emit_warning(
    kind: JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind), detail:
) -> None

```

This method simply emits PydanticJsonSchemaWarnings based on handling in the `warning_message` method.
Source code in `pydantic/json_schema.py`
```
2444
2445
2446
2447
2448
```
| ```
def emit_warning(self, kind: JsonSchemaWarningKind, detail: str) -> None:
    """This method simply emits PydanticJsonSchemaWarnings based on handling in the `warning_message` method."""
    message = self.render_warning_message(kind, detail)
    if message is not None:
        warnings.warn(message, PydanticJsonSchemaWarning)

```

---|---
###  render_warning_message [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.render_warning_message)
```
render_warning_message(
    kind: JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind), detail:
) ->  | None

```

This method is responsible for ignoring warnings as desired, and for formatting the warning messages.
You can override the value of `ignored_warning_kinds` in a subclass of GenerateJsonSchema to modify what warnings are generated. If you want more control, you can override this method; just return None in situations where you don't want warnings to be emitted.
Parameters:
Name | Type | Description | Default
---|---|---|---
`kind` |  `JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind)` |  The kind of warning to render. It can be one of the following:
  * 'skipped-choice': A choice field was skipped because it had no valid choices.
  * 'non-serializable-default': A default value was skipped because it was not JSON-serializable.

|  _required_
`detail` |  |  A string with additional details about the warning. |  _required_
Returns:
Type | Description
---|---
|  The formatted warning message, or `None` if no warning should be emitted.
Source code in `pydantic/json_schema.py`
```
2450
2451
2452
2453
2454
2455
2456
2457
2458
2459
2460
2461
2462
2463
2464
2465
2466
2467
2468
2469
```
| ```
def render_warning_message(self, kind: JsonSchemaWarningKind, detail: str) -> str | None:
    """This method is responsible for ignoring warnings as desired, and for formatting the warning messages.

    You can override the value of `ignored_warning_kinds` in a subclass of GenerateJsonSchema
    to modify what warnings are generated. If you want more control, you can override this method;
    just return None in situations where you don't want warnings to be emitted.

    Args:
        kind: The kind of warning to render. It can be one of the following:
