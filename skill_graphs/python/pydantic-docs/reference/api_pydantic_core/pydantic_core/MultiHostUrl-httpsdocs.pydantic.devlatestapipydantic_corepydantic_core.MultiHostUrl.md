##  MultiHostUrl [¶](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl)
```
MultiHostUrl(url: )

```

Bases: `SupportsAllComparisons`
A URL type with support for multiple hosts, as used by some databases for DSNs, e.g. `https://foo.com,bar.com/path`.
Internal URL logic uses the
