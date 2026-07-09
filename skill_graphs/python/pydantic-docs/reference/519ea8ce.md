##  CoreConfig [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.CoreConfig)
Bases:
Base class for schema configuration options.
Attributes:
Name | Type | Description
---|---|---
`title` |  |  The name of the configuration.
`strict` |  |  Whether the configuration should strictly adhere to specified rules.
`extra_fields_behavior` |  `ExtraBehavior` |  The behavior for handling extra fields.
`typed_dict_total` |  |  Whether the TypedDict should be considered total. Default is `True`.
`from_attributes` |  |  Whether to use attributes for models, dataclasses, and tagged union keys.
`loc_by_alias` |  |  Whether to use the used alias (or first alias for "field required" errors) instead of `field_names` to construct error `loc`s. Default is `True`.
`revalidate_instances` |  |  Whether instances of models and dataclasses should re-validate. Default is 'never'.
`validate_default` |  |  Whether to validate default values during validation. Default is `False`.
`str_max_length` |  |  The maximum length for string fields.
`str_min_length` |  |  The minimum length for string fields.
`str_strip_whitespace` |  |  Whether to strip whitespace from string fields.
`str_to_lower` |  |  Whether to convert string fields to lowercase.
`str_to_upper` |  |  Whether to convert string fields to uppercase.
`allow_inf_nan` |  |  Whether to allow infinity and NaN values for float fields. Default is `True`.
`ser_json_timedelta` |  |  The serialization option for `timedelta` values. Default is 'iso8601'. Note that if ser_json_temporal is set, then this param will be ignored.
`ser_json_temporal` |  |  The serialization option for datetime like values. Default is 'iso8601'. The types this covers are datetime, date, time and timedelta. If this is set, it will take precedence over ser_json_timedelta
`ser_json_bytes` |  |  The serialization option for `bytes` values. Default is 'utf8'.
`ser_json_inf_nan` |  |  The serialization option for infinity and NaN values in float fields. Default is 'null'.
`val_json_bytes` |  |  The validation option for `bytes` values, complementing ser_json_bytes. Default is 'utf8'.
`hide_input_in_errors` |  |  Whether to hide input data from `ValidationError` representation.
`validation_error_cause` |  |  Whether to add user-python excs to the **cause** of a ValidationError. Requires exceptiongroup backport pre Python 3.11.
`coerce_numbers_to_str` |  |  Whether to enable coercion of any `Number` type to `str` (not applicable in `strict` mode).
`regex_engine` |  |  The regex engine to use for regex pattern validation. Default is 'rust-regex'. See `StringSchema`.
`cache_strings` |  |  Whether to cache strings. Default is `True`, `True` or `'all'` is required to cache strings during general validation since validators don't know if they're in a key or a value.
`validate_by_alias` |  |  Whether to use the field's alias when validating against the provided input data. Default is `True`.
`validate_by_name` |  |  Whether to use the field's name when validating against the provided input data. Default is `False`. Replacement for `populate_by_name`.
`serialize_by_alias` |  |  Whether to serialize by alias. Default is `False`, expected to change to `True` in V3.
`url_preserve_empty_path` |  |  Whether to preserve empty URL paths when validating values for a URL type. Defaults to `False`.
