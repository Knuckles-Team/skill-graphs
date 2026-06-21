## v2.12.0b1 (2025-10-03)[¶](https://docs.pydantic.dev/latest/changelog/#v2120b1-2025-10-03)
This is the first beta release of the upcoming 2.12 release.
### What's Changed[¶](https://docs.pydantic.dev/latest/changelog/#whats-changed_4)
#### Packaging[¶](https://docs.pydantic.dev/latest/changelog/#packaging_1)
  * Bump `pydantic-core` to v2.40.1 by


#### New Features[¶](https://docs.pydantic.dev/latest/changelog/#new-features_1)
  * Add support for `exclude_if` at the field level by
  * Add `ValidateAs` annotation helper by
  * Add configuration options for validation and JSON serialization of temporal types by
  * Add support for PEP 728 by
  * Add field name in serialization error by
  * Add option to preserve empty URL paths by


#### Changes[¶](https://docs.pydantic.dev/latest/changelog/#changes)
  * Raise error if an incompatible `pydantic-core` version is installed by
  * Remove runtime warning for experimental features by
  * Warn if registering virtual subclasses on Pydantic models by


#### Fixes[¶](https://docs.pydantic.dev/latest/changelog/#fixes_3)
  * Fix `__getattr__()` behavior on Pydantic models when a property raised an `AttributeError` and extra values are present by
  * Add test to prevent regression with Pydantic models used as annotated metadata by
  * Allow to use property setters on Pydantic dataclasses with `validate_assignment` set by
  * Fix mypy v2 plugin for upcoming mypy release by
  * Respect custom title in functions JSON Schema by
  * Fix `ImportString` JSON serialization for objects with a `name` attribute by
  * Do not error on fields overridden by methods in the mypy plugin by


### New Contributors[¶](https://docs.pydantic.dev/latest/changelog/#new-contributors_2)
