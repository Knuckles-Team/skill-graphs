##  WebsocketUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.WebsocketUrl "Permanent link")
```
WebsocketUrl(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any ws or wss URL.
  * TLD not required
  * Host not required
  * Max length 2083

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
##  FileUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.FileUrl "Permanent link")
```
FileUrl(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any file URL.
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
