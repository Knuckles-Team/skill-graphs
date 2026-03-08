## v1.8.1 (2021-03-03)[¶](https://docs.pydantic.dev/latest/changelog/#v181-2021-03-03)
Bug fixes for regressions and new features from `v1.8`
  * allow elements of `Config.field` to update elements of a `Field`,
  * fix validation with a `BaseModel` field and a custom root type,
  * expose `Pattern` encoder to `fastapi`,
  * enable the Hypothesis plugin to generate a constrained float when the `multiple_of` argument is specified,
  * Avoid `RecursionError` when using some types like `Enum` or `Literal` with generic models,
  * do not overwrite declared `__hash__` in subclasses of a model,
  * fix `mypy` complaints on `Path` and `UUID` related custom types,
  * Support properly variable length tuples of compound types,
