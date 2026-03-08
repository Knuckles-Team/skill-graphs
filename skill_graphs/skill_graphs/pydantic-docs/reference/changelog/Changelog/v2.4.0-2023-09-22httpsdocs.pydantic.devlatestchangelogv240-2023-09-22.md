## v2.4.0 (2023-09-22)[¶](https://docs.pydantic.dev/latest/changelog/#v240-2023-09-22)
### What's Changed[¶](https://docs.pydantic.dev/latest/changelog/#whats-changed_47)
#### Packaging[¶](https://docs.pydantic.dev/latest/changelog/#packaging_30)
  * Update pydantic-core to 2.10.0 by


#### New Features[¶](https://docs.pydantic.dev/latest/changelog/#new-features_15)
  * Add `Base64Url` types by
  * Implement optional `number` to `str` coercion by
  * Allow access to `field_name` and `data` in all validators if there is data and a field name by
  * Add `BaseModel.model_validate_strings` and `TypeAdapter.validate_strings` by
  * Add Pydantic `plugins` experimental implementation by


#### Changes[¶](https://docs.pydantic.dev/latest/changelog/#changes_12)
  * Do not override `model_post_init` in subclass with private attrs by
  * Make fields with defaults not required in the serialization schema by default by
  * Mark `Extra` as deprecated by
  * Make `EncodedStr` a dataclass by
  * Move `annotated_handlers` to be public by


#### Performance[¶](https://docs.pydantic.dev/latest/changelog/#performance_9)
  * Simplify flattening and inlining of `CoreSchema` by
  * Remove unused copies in `CoreSchema` walking by
  * Add caches for collecting definitions and invalid schemas from a CoreSchema by
  * Eagerly resolve discriminated unions and cache cases where we can't by
  * Replace `dict.get` and `dict.setdefault` with more verbose versions in `CoreSchema` building hot paths by
  * Cache invalid `CoreSchema` discovery by
  * Allow disabling `CoreSchema` validation for faster startup times by


#### Fixes[¶](https://docs.pydantic.dev/latest/changelog/#fixes_46)
  * Fix config detection for `TypedDict` from grandparent classes by
  * Fix hash function generation for frozen models with unusual MRO by
  * Make `strict` config overridable in field for Path by
  * Use `ser_json_<timedelta|bytes>` on default in `GenerateJsonSchema` by
  * Adding a check that alias is validated as an identifier for Python by
  * Raise an error when computed field overrides field by
  * Fix applying `SkipValidation` to referenced schemas by
  * Enforce behavior of private attributes having double leading underscore by
  * Standardize `__get_pydantic_core_schema__` signature by
  * Fix generic dataclass fields mutation bug (when using `TypeAdapter`) by
  * Fix `TypeError` on `model_validator` in `wrap` mode by
  * Improve enum error message by
  * Make `repr` work for instances that failed initialization when handling `ValidationError`s by
  * Fixed a regular expression denial of service issue by limiting whitespaces by
  * Fix handling of `UUID` values having `UUID.version=None` by
  * Fix `__iter__` returning private `cached_property` info by
  * Improvements to version info message by


### New Contributors[¶](https://docs.pydantic.dev/latest/changelog/#new-contributors_19)
