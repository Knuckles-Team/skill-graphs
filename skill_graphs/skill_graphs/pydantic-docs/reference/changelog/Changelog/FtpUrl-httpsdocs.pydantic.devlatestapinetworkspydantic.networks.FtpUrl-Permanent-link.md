##  FtpUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.FtpUrl "Permanent link")
```
FtpUrl(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept ftp URL.
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
##  PostgresDsn [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.PostgresDsn "Permanent link")
```
PostgresDsn(url:  | MultiHostUrl[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.MultiHostUrl "pydantic_core.MultiHostUrl") | _BaseMultiHostUrl)

```

Bases: `_BaseMultiHostUrl`
A type that will accept any Postgres DSN.
  * User info required
  * TLD not required
  * Host required
  * Supports multiple hosts


If further validation is required, these properties can be used by validators to enforce specific behaviour:
```
from pydantic import (
    BaseModel,
    HttpUrl,
    PostgresDsn,
    ValidationError,
    field_validator,
)

class MyModel(BaseModel):
    url: HttpUrl

m = MyModel(url='http://www.example.com')
