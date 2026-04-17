## v0.20.0a1 (2019-02-13)[¶](https://docs.pydantic.dev/latest/changelog/#v0200a1-2019-02-13)
  * **breaking change** (maybe): more sophisticated argument parsing for validators, any subset of `values`, `config` and `field` is now permitted, eg. `(cls, value, field)`, however the variadic key word argument ("`**kwargs`") **must** be called `kwargs`,
  * **breaking change** : Adds `skip_defaults` argument to `BaseModel.dict()` to allow skipping of fields that were not explicitly set, signature of `Model.construct()` changed,
  * add `py.typed` marker file for PEP-561 support,
  * Fix `extra` behaviour for multiple inheritance/mix-ins,
