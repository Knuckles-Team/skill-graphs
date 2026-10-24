##  KafkaDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.KafkaDsn "Permanent link")
```
KafkaDsn(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any Kafka DSN.
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
##  NatsDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.NatsDsn "Permanent link")
```
NatsDsn(url:  | MultiHostUrl[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl "pydantic_core.MultiHostUrl") | _BaseMultiHostUrl)

```

Bases: `_BaseMultiHostUrl`
A type that will accept any NATS DSN.
NATS is a connective technology built for the ever increasingly hyper-connected world. It is a single technology that enables applications to securely communicate across any combination of cloud vendors, on-premise, edge, web and mobile, and devices. More: https://nats.io
Source code in `pydantic/networks.py`
```
350
351
```
| ```
def __init__(self, url: str | _CoreMultiHostUrl | _BaseMultiHostUrl) -> None:
    self._url = _build_type_adapter(self.__class__).validate_python(url)._url

```

---|---
