## v0.27 (2019-05-30)[¶](https://docs.pydantic.dev/latest/changelog/#v027-2019-05-30)
  * **breaking change** `_pydantic_post_init` to execute dataclass' original `__post_init__` before validation,
  * fix handling of generic types without specified parameters,
  * **breaking change** (maybe): this is the first release compiled with **cython** , see the docs and please submit an issue if you run into problems
