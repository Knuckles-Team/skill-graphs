##  UrlConstraints `dataclass` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.UrlConstraints "Permanent link")
```
UrlConstraints(
    max_length:  | None = None,
    allowed_schemes: [] | None = None,
    host_required:  | None = None,
    default_host:  | None = None,
    default_port:  | None = None,
    default_path:  | None = None,
    preserve_empty_path:  | None = None,
)

```

Url constraints.
Attributes:
Name | Type | Description
---|---|---
`max_length` |  |  The maximum length of the url. Defaults to `None`.
`allowed_schemes` |  |  The allowed schemes. Defaults to `None`.
`host_required` |  |  Whether the host is required. Defaults to `None`.
`default_host` |  |  The default host. Defaults to `None`.
`default_port` |  |  The default port. Defaults to `None`.
`default_path` |  |  The default path. Defaults to `None`.
`preserve_empty_path` |  |  Whether to preserve empty URL paths. Defaults to `None`.
###  defined_constraints `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.UrlConstraints.defined_constraints "Permanent link")
```
defined_constraints: [, ]

```

Fetch a key / value mapping of constraints to values that are not None. Used for core schema updates.
