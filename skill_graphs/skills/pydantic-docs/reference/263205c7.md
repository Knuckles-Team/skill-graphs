##  GenerateJsonSchema [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema)
```
GenerateJsonSchema(
    by_alias:  = True,
    ref_template:  = DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE),
    union_format: [
        "any_of", "primitive_type_array"
    ] = "any_of",
)

```

Usage Documentation
[Customizing the JSON Schema Generation Process](https://docs.pydantic.dev/latest/concepts/json_schema/#customizing-the-json-schema-generation-process)
A class for generating JSON schemas.
This class generates JSON schemas based on configured parameters. The default schema dialect is `by_alias` to configure how fields with multiple names are handled and `ref_template` to format reference names.
Attributes:
Name | Type | Description
---|---|---
`schema_dialect` |  |  The JSON schema dialect used to generate the schema. See
`ignored_warning_kinds` |  `JsonSchemaWarningKind[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaWarningKind)]` |  Warnings to ignore when generating the schema. `self.render_warning_message` will do nothing if its argument `kind` is in `ignored_warning_kinds`; this value can be modified on subclasses to easily control which warnings are emitted.
`by_alias` |  |  Whether to use field aliases when generating the schema.
`ref_template` |  |  The format string used when generating reference names.
`core_to_json_refs` |  `CoreModeRef, JsonRef]` |  A mapping of core refs to JSON refs.
`core_to_defs_refs` |  `CoreModeRef, DefsRef]` |  A mapping of core refs to definition refs.
`defs_to_core_refs` |  `DefsRef, CoreModeRef]` |  A mapping of definition refs to core refs.
`json_to_defs_refs` |  `JsonRef, DefsRef]` |  A mapping of JSON refs to definition refs.
`definitions` |  `DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]` |  Definitions in the schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`by_alias` |  |  Whether to use field aliases in the generated schemas. |  `True`
`ref_template` |  |  The format string to use when generating reference names. |  `DEFAULT_REF_TEMPLATE[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.DEFAULT_REF_TEMPLATE)`
`union_format` |  |  The format to use when combining schemas from unions together. Can be one of:
  * `'any_of'`: Use the
  * `'primitive_type_array'`: Use the `string`, `boolean`, `null`, `integer` or `number`) or contains constraints/metadata, falls back to `any_of`.

|  `'any_of'`
Raises:
Type | Description
---|---
`JsonSchemaError` |  If the instance of the class is inadvertently reused after generating a schema.
Source code in `pydantic/json_schema.py`
```
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
```
| ```
def __init__(
    self,
    by_alias: bool = True,
    ref_template: str = DEFAULT_REF_TEMPLATE,
    union_format: Literal['any_of', 'primitive_type_array'] = 'any_of',
) -> None:
    self.by_alias = by_alias
    self.ref_template = ref_template
    self.union_format: Literal['any_of', 'primitive_type_array'] = union_format

    self.core_to_json_refs: dict[CoreModeRef, JsonRef] = {}
    self.core_to_defs_refs: dict[CoreModeRef, DefsRef] = {}
    self.defs_to_core_refs: dict[DefsRef, CoreModeRef] = {}
    self.json_to_defs_refs: dict[JsonRef, DefsRef] = {}

    self.definitions: dict[DefsRef, JsonSchemaValue] = {}
    self._config_wrapper_stack = _config.ConfigWrapperStack(_config.ConfigWrapper({}))

    self._mode: JsonSchemaMode = 'validation'

    # The following includes a mapping of a fully-unique defs ref choice to a list of preferred
    # alternatives, which are generally simpler, such as only including the class name.
    # At the end of schema generation, we use these to produce a JSON schema with more human-readable
    # definitions, which would also work better in a generated OpenAPI client, etc.
    self._prioritized_defsref_choices: dict[DefsRef, list[DefsRef]] = {}
    self._collision_counter: dict[str, int] = defaultdict(int)
    self._collision_index: dict[str, int] = {}

    self._schema_type_to_method = self.build_schema_type_to_method()

    # When we encounter definitions we need to try to build them immediately
    # so that they are available schemas that reference them
    # But it's possible that CoreSchema was never going to be used
    # (e.g. because the CoreSchema that references short circuits is JSON schema generation without needing
    #  the reference) so instead of failing altogether if we can't build a definition we
    # store the error raised and re-throw it if we end up needing that def
    self._core_defs_invalid_for_json_schema: dict[DefsRef, PydanticInvalidForJsonSchema] = {}

    # This changes to True after generating a schema, to prevent issues caused by accidental reuse
    # of a single instance of a schema generator
    self._used = False

```

---|---
###  ValidationsMapping [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.ValidationsMapping)
This class just contains mappings from core_schema attribute names to the corresponding JSON schema attribute names. While I suspect it is unlikely to be necessary, you can in principle override this class in a subclass of GenerateJsonSchema (by inheriting from GenerateJsonSchema.ValidationsMapping) to change these mappings.
###  build_schema_type_to_method [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.build_schema_type_to_method)
```
build_schema_type_to_method() -> [
    CoreSchemaOrFieldType[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.CoreSchemaOrFieldType),
    [[CoreSchemaOrField], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)],
]

```

Builds a dictionary mapping fields to methods for generating JSON schemas.
Returns:
Type | Description
---|---
`CoreSchemaOrFieldType[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.CoreSchemaOrFieldType), CoreSchemaOrField], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]]` |  A dictionary containing the mapping of `CoreSchemaOrFieldType` to a handler method.
Raises:
Type | Description
---|---
|  If no method has been defined for generating a JSON schema for a given pydantic core schema type.
Source code in `pydantic/json_schema.py`
```
319
320
321
322
323
324
325
326
327
328
329
330
331
332
333
334
335
336
337
338
339
340
341
342
343
```
| ```
def build_schema_type_to_method(
    self,
) -> dict[CoreSchemaOrFieldType, Callable[[CoreSchemaOrField], JsonSchemaValue]]:
    """Builds a dictionary mapping fields to methods for generating JSON schemas.

    Returns:
        A dictionary containing the mapping of `CoreSchemaOrFieldType` to a handler method.

    Raises:
        TypeError: If no method has been defined for generating a JSON schema for a given pydantic core schema type.
    """
    mapping: dict[CoreSchemaOrFieldType, Callable[[CoreSchemaOrField], JsonSchemaValue]] = {}
    core_schema_types: list[CoreSchemaOrFieldType] = list(get_literal_values(CoreSchemaOrFieldType))
    for key in core_schema_types:
        method_name = f'{key.replace("-", "_")}_schema'
        try:
            mapping[key] = getattr(self, method_name)
        except AttributeError as e:  # pragma: no cover
            if os.getenv('PYDANTIC_PRIVATE_ALLOW_UNHANDLED_SCHEMA_TYPES'):
                continue
            raise TypeError(
                f'No method for generating JsonSchema for core_schema.type={key!r} '
                f'(expected: {type(self).__name__}.{method_name})'
            ) from e
    return mapping

```

---|---
###  generate_definitions [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generate_definitions)
```
generate_definitions(
    inputs: [
        [JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode), CoreSchema]
    ]
) -> [
    [
        [JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)],
        JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue),
    ],
    [DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)],
]

```

Generates JSON schema definitions from a list of core schemas, pairing the generated definitions with a mapping that links the input keys to the definition references.
Parameters:
Name | Type | Description | Default
---|---|---|---
`inputs` |  `JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode), CoreSchema]]` |  A sequence of tuples, where:
  * The first element is a JSON schema key type.
  * The second element is the JSON mode: either 'validation' or 'serialization'.
  * The third element is a core schema.

|  _required_
Returns:
Type | Description
---|---
`JsonSchemaKeyT, JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)], JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)], DefsRef, JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)]]` |  A tuple where:
  * The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have JsonRef references to definitions that are defined in the second returned element.)
  * The second element is a dictionary whose keys are definition references for the JSON schemas from the first returned element, and whose values are the actual JSON schema definitions.


Raises:
Type | Description
---|---
`PydanticUserError[](https://docs.pydantic.dev/latest/api/errors/#pydantic.errors.PydanticUserError)` |  Raised if the JSON schema generator has already been used to generate a JSON schema.
Source code in `pydantic/json_schema.py`
```
345
346
347
348
349
350
351
352
353
354
355
356
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
```
| ```
def generate_definitions(
    self, inputs: Sequence[tuple[JsonSchemaKeyT, JsonSchemaMode, core_schema.CoreSchema]]
) -> tuple[dict[tuple[JsonSchemaKeyT, JsonSchemaMode], JsonSchemaValue], dict[DefsRef, JsonSchemaValue]]:
    """Generates JSON schema definitions from a list of core schemas, pairing the generated definitions with a
    mapping that links the input keys to the definition references.

    Args:
        inputs: A sequence of tuples, where:

            - The first element is a JSON schema key type.
            - The second element is the JSON mode: either 'validation' or 'serialization'.
            - The third element is a core schema.

    Returns:
        A tuple where:

            - The first element is a dictionary whose keys are tuples of JSON schema key type and JSON mode, and
                whose values are the JSON schema corresponding to that pair of inputs. (These schemas may have
                JsonRef references to definitions that are defined in the second returned element.)
            - The second element is a dictionary whose keys are definition references for the JSON schemas
                from the first returned element, and whose values are the actual JSON schema definitions.

    Raises:
        PydanticUserError: Raised if the JSON schema generator has already been used to generate a JSON schema.
    """
    if self._used:
        raise PydanticUserError(
            'This JSON schema generator has already been used to generate a JSON schema. '
            f'You must create a new instance of {type(self).__name__} to generate a new JSON schema.',
            code='json-schema-already-used',
        )

    for _, mode, schema in inputs:
        self._mode = mode
        self.generate_inner(schema)

    definitions_remapping = self._build_definitions_remapping()

    json_schemas_map: dict[tuple[JsonSchemaKeyT, JsonSchemaMode], DefsRef] = {}
    for key, mode, schema in inputs:
        self._mode = mode
        json_schema = self.generate_inner(schema)
        json_schemas_map[(key, mode)] = definitions_remapping.remap_json_schema(json_schema)

    json_schema = {'$defs': self.definitions}
    json_schema = definitions_remapping.remap_json_schema(json_schema)
    self._used = True
    return json_schemas_map, self.sort(json_schema['$defs'])  # type: ignore

```

---|---
###  generate [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generate)
```
generate(
    schema: CoreSchema, mode: JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode) = "validation"
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema for a specified schema in a specified mode.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchema` |  A Pydantic model. |  _required_
`mode` |  `JsonSchemaMode[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaMode)` |  The mode in which to generate the schema. Defaults to 'validation'. |  `'validation'`
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  A JSON schema representing the specified schema.
Raises:
Type | Description
---|---
`PydanticUserError[](https://docs.pydantic.dev/latest/api/errors/#pydantic.errors.PydanticUserError)` |  If the JSON schema generator has already been used to generate a JSON schema.
Source code in `pydantic/json_schema.py`
```
394
395
396
397
398
399
400
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
422
423
424
425
426
427
428
429
430
431
432
433
434
435
436
437
438
439
440
441
```
| ```
def generate(self, schema: CoreSchema, mode: JsonSchemaMode = 'validation') -> JsonSchemaValue:
    """Generates a JSON schema for a specified schema in a specified mode.

    Args:
        schema: A Pydantic model.
        mode: The mode in which to generate the schema. Defaults to 'validation'.

    Returns:
        A JSON schema representing the specified schema.

    Raises:
        PydanticUserError: If the JSON schema generator has already been used to generate a JSON schema.
    """
    self._mode = mode
    if self._used:
        raise PydanticUserError(
            'This JSON schema generator has already been used to generate a JSON schema. '
            f'You must create a new instance of {type(self).__name__} to generate a new JSON schema.',
            code='json-schema-already-used',
        )

    json_schema: JsonSchemaValue = self.generate_inner(schema)
    json_ref_counts = self.get_json_ref_counts(json_schema)

    ref = cast(JsonRef, json_schema.get('$ref'))
    while ref is not None:  # may need to unpack multiple levels
        ref_json_schema = self.get_schema_from_definitions(ref)
        if json_ref_counts[ref] == 1 and ref_json_schema is not None and len(json_schema) == 1:
            # "Unpack" the ref since this is the only reference and there are no sibling keys
            json_schema = ref_json_schema.copy()  # copy to prevent recursive dict reference
            json_ref_counts[ref] -= 1
            ref = cast(JsonRef, json_schema.get('$ref'))
        ref = None

    self._garbage_collect_definitions(json_schema)
    definitions_remapping = self._build_definitions_remapping()

    if self.definitions:
        json_schema['$defs'] = self.definitions

    json_schema = definitions_remapping.remap_json_schema(json_schema)

    # For now, we will not set the $schema key. However, if desired, this can be easily added by overriding
    # this method and adding the following line after a call to super().generate(schema):
    # json_schema['$schema'] = self.schema_dialect

    self._used = True
    return self.sort(json_schema)

```

---|---
###  generate_inner [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.generate_inner)
```
generate_inner(
    schema: CoreSchemaOrField,
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Generates a JSON schema for a given core schema.
Parameters:
Name | Type | Description | Default
---|---|---|---
`schema` |  `CoreSchemaOrField` |  The given core schema. |  _required_
Returns:
Type | Description
---|---
`JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)` |  The generated JSON schema.
TODO: the nested function definitions here seem like bad practice, I'd like to unpack these in a future PR. It'd be great if we could shorten the call stack a bit for JSON schema generation, and I think there's potential for that here.
Source code in `pydantic/json_schema.py`
```
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
535
536
537
538
539
540
541
542
543
544
545
546
547
548
549
550
551
552
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
```
| ```
def generate_inner(self, schema: CoreSchemaOrField) -> JsonSchemaValue:  # noqa: C901
    """Generates a JSON schema for a given core schema.

    Args:
        schema: The given core schema.

    Returns:
        The generated JSON schema.

    TODO: the nested function definitions here seem like bad practice, I'd like to unpack these
    in a future PR. It'd be great if we could shorten the call stack a bit for JSON schema generation,
    and I think there's potential for that here.
    """
    # If a schema with the same CoreRef has been handled, just return a reference to it
    # Note that this assumes that it will _never_ be the case that the same CoreRef is used
    # on types that should have different JSON schemas
    if 'ref' in schema:
        core_ref = CoreRef(schema['ref'])  # type: ignore[typeddict-item]
        core_mode_ref = (core_ref, self.mode)
        if core_mode_ref in self.core_to_defs_refs and self.core_to_defs_refs[core_mode_ref] in self.definitions:
            return {'$ref': self.core_to_json_refs[core_mode_ref]}

    def populate_defs(core_schema: CoreSchema, json_schema: JsonSchemaValue) -> JsonSchemaValue:
        if 'ref' in core_schema:
            core_ref = CoreRef(core_schema['ref'])  # type: ignore[typeddict-item]
            defs_ref, ref_json_schema = self.get_cache_defs_ref_schema(core_ref)
            json_ref = JsonRef(ref_json_schema['$ref'])
            # Replace the schema if it's not a reference to itself
            # What we want to avoid is having the def be just a ref to itself
            # which is what would happen if we blindly assigned any
            if json_schema.get('$ref', None) != json_ref:
                self.definitions[defs_ref] = json_schema
                self._core_defs_invalid_for_json_schema.pop(defs_ref, None)
            json_schema = ref_json_schema
        return json_schema

    def handler_func(schema_or_field: CoreSchemaOrField) -> JsonSchemaValue:
        """Generate a JSON schema based on the input schema.

        Args:
            schema_or_field: The core schema to generate a JSON schema from.

        Returns:
            The generated JSON schema.

        Raises:
            TypeError: If an unexpected schema type is encountered.
        """
        # Generate the core-schema-type-specific bits of the schema generation:
        json_schema: JsonSchemaValue | None = None
        if self.mode == 'serialization' and 'serialization' in schema_or_field:
            # In this case, we skip the JSON Schema generation of the schema
            # and use the `'serialization'` schema instead (canonical example:
            # `Annotated[int, PlainSerializer(str)]`).
            ser_schema = schema_or_field['serialization']  # type: ignore
            json_schema = self.ser_schema(ser_schema)

            # It might be that the 'serialization'` is skipped depending on `when_used`.
            # This is only relevant for `nullable` schemas though, so we special case here.
            if (
                json_schema is not None
                and ser_schema.get('when_used') in ('unless-none', 'json-unless-none')
                and schema_or_field['type'] == 'nullable'
            ):
                json_schema = self.get_union_of_schemas([{'type': 'null'}, json_schema])
        if json_schema is None:
            if _core_utils.is_core_schema(schema_or_field) or _core_utils.is_core_schema_field(schema_or_field):
                generate_for_schema_type = self._schema_type_to_method[schema_or_field['type']]
                json_schema = generate_for_schema_type(schema_or_field)
            else:
                raise TypeError(f'Unexpected schema type: schema={schema_or_field}')
        return json_schema

    current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, handler_func)

    metadata = cast(_core_metadata.CoreMetadata, schema.get('metadata', {}))

    # TODO: I dislike that we have to wrap these basic dict updates in callables, is there any way around this?

    if js_updates := metadata.get('pydantic_js_updates'):

        def js_updates_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
        ) -> JsonSchemaValue:
            json_schema = {**current_handler(schema_or_field), **js_updates}
            return json_schema

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, js_updates_handler_func)

    if js_extra := metadata.get('pydantic_js_extra'):

        def js_extra_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
        ) -> JsonSchemaValue:
            json_schema = current_handler(schema_or_field)
            if isinstance(js_extra, dict):
                json_schema.update(to_jsonable_python(js_extra))
            elif callable(js_extra):
                # similar to typing issue in _update_class_schema when we're working with callable js extra
                js_extra(json_schema)  # type: ignore
            return json_schema

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, js_extra_handler_func)

    for js_modify_function in metadata.get('pydantic_js_functions', ()):

        def new_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
            js_modify_function: GetJsonSchemaFunction = js_modify_function,
        ) -> JsonSchemaValue:
            json_schema = js_modify_function(schema_or_field, current_handler)
            if _core_utils.is_core_schema(schema_or_field):
                json_schema = populate_defs(schema_or_field, json_schema)
            original_schema = current_handler.resolve_ref_schema(json_schema)
            ref = json_schema.pop('$ref', None)
            if ref and json_schema:
                original_schema.update(json_schema)
            return original_schema

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, new_handler_func)

    for js_modify_function in metadata.get('pydantic_js_annotation_functions', ()):

        def new_handler_func(
            schema_or_field: CoreSchemaOrField,
            current_handler: GetJsonSchemaHandler = current_handler,
            js_modify_function: GetJsonSchemaFunction = js_modify_function,
        ) -> JsonSchemaValue:
            return js_modify_function(schema_or_field, current_handler)

        current_handler = _schema_generation_shared.GenerateJsonSchemaHandler(self, new_handler_func)

    json_schema = current_handler(schema)
    if _core_utils.is_core_schema(schema):
        json_schema = populate_defs(schema, json_schema)
    return json_schema

```

---|---
###  sort [¶](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.GenerateJsonSchema.sort)
```
sort(
    value: JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue), parent_key:  | None = None
) -> JsonSchemaValue[](https://docs.pydantic.dev/latest/api/json_schema/#pydantic.json_schema.JsonSchemaValue)

```

Override this method to customize the sorting of the JSON schema (e.g., don't sort at all, sort all keys unconditionally, etc.)
By default, alphabetically sort the keys in the JSON schema, skipping the 'properties' and 'default' keys to preserve field definition order. This sort is recursive, so it will sort all nested dictionaries as well.
