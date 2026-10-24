##  WhenUsed `module-attribute` [¶](https://docs.pydantic.dev/latest/api/pydantic_core_schema/#pydantic_core.core_schema.WhenUsed)
```
WhenUsed = [
    "always", "unless-none", "json", "json-unless-none"
]

```

Values have the following meanings:
  * `'always'` means always use
  * `'unless-none'` means use unless the value is `None`
  * `'json'` means use when serializing to JSON
  * `'json-unless-none'` means use when serializing to JSON and the value is not `None`
