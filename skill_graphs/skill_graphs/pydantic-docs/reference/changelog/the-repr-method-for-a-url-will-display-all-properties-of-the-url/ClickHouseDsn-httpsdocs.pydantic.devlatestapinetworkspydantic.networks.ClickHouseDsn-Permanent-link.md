##  ClickHouseDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.ClickHouseDsn "Permanent link")
```
ClickHouseDsn(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any ClickHouse DSN.
  * User info required
  * TLD not required
  * Host not required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def __init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```

---|---
##  SnowflakeDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.SnowflakeDsn "Permanent link")
```
SnowflakeDsn(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any Snowflake DSN.
  * User info required
  * TLD not required
  * Host required

Source code in `pydantic/networks.py`
```
130
131
```
| ```
def __init__(self, url: str | _CoreUrl | _BaseUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```

---|---
###  host `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.SnowflakeDsn.host "Permanent link")
```
host:

```

The required URL host.
