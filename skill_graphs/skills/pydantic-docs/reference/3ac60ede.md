## v1.10.5 (2023-02-15)[¶](https://docs.pydantic.dev/latest/changelog/#v1105-2023-02-15)
  * Fix broken parametrized bases handling with `GenericModel`s with complex sets of models,
  * Invalidate mypy cache if plugin config changes,
  * Fix `RecursionError` when deep-copying dataclass types wrapped by pydantic,
  * Fix `X | Y` union syntax breaking `GenericModel`,
  * Switch coverage badge to show coverage for this branch/release,
