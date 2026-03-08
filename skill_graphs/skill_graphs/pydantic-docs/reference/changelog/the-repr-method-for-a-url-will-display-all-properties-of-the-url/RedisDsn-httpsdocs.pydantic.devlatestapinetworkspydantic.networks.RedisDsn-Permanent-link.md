##  RedisDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.RedisDsn "Permanent link")
```
RedisDsn(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any Redis DSN.
  * User info required
  * TLD not required
  * Host required (e.g., `rediss://:pass@localhost`)

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
###  host `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.RedisDsn.host "Permanent link")
```
host:

```

The required URL host.
##  MongoDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.MongoDsn "Permanent link")
```
MongoDsn(url:  | MultiHostUrl[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl "pydantic_core.MultiHostUrl") | _BaseMultiHostUrl)

```

Bases: `_BaseMultiHostUrl`
A type that will accept any MongoDB DSN.
  * User info not required
  * Database name not required
  * Port not required
  * User info may be passed without user part (e.g., `mongodb://mongodb0.example.com:27017`).


Warning
If a port isn't specified, the default MongoDB port `27017` will be used. If this behavior is undesirable, you can use the following:
```
from typing import Annotated

from pydantic import UrlConstraints
from pydantic_core import MultiHostUrl

MongoDsnNoDefaultPort = Annotated[
    MultiHostUrl,
    UrlConstraints(allowed_schemes=['mongodb', 'mongodb+srv']),
]

```

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
