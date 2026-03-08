## v1.7.1 (2020-10-28)[¶](https://docs.pydantic.dev/latest/changelog/#v171-2020-10-28)
Thank you to pydantic's sponsors:
  * fix annotation of `validate_arguments` when passing configuration as argument,
  * Fix mypy assignment error when using `PrivateAttr`,
  * fix `underscore_attrs_are_private` causing `TypeError` when overriding `__init__`,
  * Fixed regression introduced in v1.7 involving exception handling in field validators when `validate_assignment=True`,
  * fix: _pydantic_ `dataclass` can inherit from stdlib `dataclass` and `Config.arbitrary_types_allowed` is supported,
