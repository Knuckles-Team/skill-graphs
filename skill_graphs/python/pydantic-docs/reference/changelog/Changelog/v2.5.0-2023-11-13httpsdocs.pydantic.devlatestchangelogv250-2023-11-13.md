## v2.5.0 (2023-11-13)[¶](https://docs.pydantic.dev/latest/changelog/#v250-2023-11-13)
The code released in v2.5.0 is functionally identical to that of v2.5.0b1.
### What's Changed[¶](https://docs.pydantic.dev/latest/changelog/#whats-changed_44)
#### Packaging[¶](https://docs.pydantic.dev/latest/changelog/#packaging_28)
  * Update pydantic-core from 2.10.1 to 2.14.1, significant changes from these updates are described below, full changelog
  * Update to `pyright==1.1.335` by


#### New Features[¶](https://docs.pydantic.dev/latest/changelog/#new-features_14)
  * Allow plugins to catch non `ValidationError` errors by
  * Support `__doc__` argument in `create_model()` by
  * Expose `regex_engine` flag - meaning you can use with the Rust or Python regex libraries in constraints by
  * Save return type generated from type annotation in `ComputedFieldInfo` by
  * Adopting `ruff` formatter by
  * Added `validation_error_cause` to config by
  * Make path of the item to validate available in plugin by
  * Add `CallableDiscriminator` and `Tag` by
    * `CallableDiscriminator` renamed to `Discriminator` by
  * Make union case tags affect union error messages by
  * Add `examples` and `json_schema_extra` to `@computed_field` by
  * Add `JsonValue` type by
  * Allow `str` as argument to `Discriminator` by
  * Add `SchemaSerializer.__reduce__` method to enable pickle serialization by


#### Changes[¶](https://docs.pydantic.dev/latest/changelog/#changes_11)
  * **Significant Change:** replace `ultra_strict` with new smart union implementation, the way unions are validated has changed significantly to improve performance and correctness, we have worked hard to absolutely minimise the number of cases where behaviour has changed, see the PR for details - by
  * Add support for instance method reassignment when `extra='allow'` by
  * Support JSON schema generation for `Enum` types with no cases by
  * Warn if a class inherits from `Generic` before `BaseModel` by


#### Performance[¶](https://docs.pydantic.dev/latest/changelog/#performance_8)
  * New custom JSON parser, `jiter` by
  * PGO build for MacOS M1 by
  * Use `__getattr__` for all package imports, improve import time by


#### Fixes[¶](https://docs.pydantic.dev/latest/changelog/#fixes_43)
  * Fix `mypy` issue with subclasses of `RootModel` by
  * Properly rebuild the `FieldInfo` when a forward ref gets evaluated by
  * Fix failure to load `SecretStr` from JSON (regression in v2.4) by
  * Fix `defer_build` behavior with `TypeAdapter` by
  * Improve compatibility with legacy `mypy` versions by
  * Fix: update `TypeVar` handling when default is not set by
  * Support specification of `strict` on `Enum` type fields by
  * Wrap `weakref.ref` instead of subclassing to fix `cloudpickle` serialization by
  * Keep values of private attributes set within `model_post_init` in subclasses by
  * Add more specific type for non-callable `json_schema_extra` by
  * Raise an error when deleting frozen (model) fields by
  * Fix schema sorting bug with default values by
  * Use generated alias for aliases that are not specified otherwise by
  * Support `strict` specification for `UUID` types by
  * JSON schema: fix extra parameter handling by
  * Fix: support `pydantic.Field(kw_only=True)` with inherited dataclasses by
  * Support `validate_call` decorator for methods in classes with `__slots__` by
  * Fix pydantic dataclass problem with `dataclasses.field` default by
  * Fix schema generation for generics with union type bounds by
  * Fix version for `importlib_metadata` on python 3.7 by
  * Support `|` operator (Union) in PydanticRecursiveRef by
  * Fix `display_as_type` for `TypeAliasType` in python 3.12 by
  * Add support for `NotRequired` generics in `TypedDict` by
  * Make generic `TypeAliasType` specifications produce different schema definitions by
  * Added fix for signature of inherited dataclass by
  * Make the model name generation more robust in JSON schema by
  * Fix plurals in validation error messages (in tests) by
  * `PrivateAttr` is passed from `Annotated` default position by
  * Don't decode bytes (which may not be UTF8) when displaying SecretBytes by
  * Use `classmethod` instead of `classmethod[Any, Any, Any]` by
  * Clearer error on invalid Plugin by
  * Correct pydantic dataclasses import by
  * Fix misbehavior for models referencing redefined type aliases by
  * Fix `Optional` field with `validate_default` only performing one field validation by
  * Fix `definition-ref` bug with `Dict` keys by
  * Fix bug allowing validation of `bool` types with `coerce_numbers_to_str=True` by
  * Don't accept `NaN` in float and decimal constraints by
  * Add `lax_str` and `lax_int` support for enum values not inherited from str/int by
  * Support subclasses in lists in `Union` of `List` types by
  * Allow validation against `max_digits` and `decimals` to pass if normalized or non-normalized input is valid by
  * Fix: proper pluralization in `ValidationError` messages by
  * Disallow the string `'-'` as `datetime` input by
  * Fix: NaN and Inf float serialization by
  * Restore manylinux-compatible PGO builds by


### New Contributors[¶](https://docs.pydantic.dev/latest/changelog/#new-contributors_17)
####  `pydantic`[¶](https://docs.pydantic.dev/latest/changelog/#pydantic_2)
####  `pydantic-core`[¶](https://docs.pydantic.dev/latest/changelog/#pydantic-core_2)
