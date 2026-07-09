##  HttpUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.HttpUrl "Permanent link")
```
HttpUrl(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any http or https URL.
  * TLD not required
  * Host not required
  * Max length 2083


```
from pydantic import BaseModel, HttpUrl, ValidationError

class MyModel(BaseModel):
    url: HttpUrl

m = MyModel(url='http://www.example.com')  # (1)!
print(m.url)
#> http://www.example.com/

try:
    MyModel(url='ftp://invalid.url')
except ValidationError as e:
    print(e)
    '''
    1 validation error for MyModel
    url
      URL scheme should be 'http' or 'https' [type=url_scheme, input_value='ftp://invalid.url', input_type=str]
    '''

try:
    MyModel(url='not a url')
except ValidationError as e:
    print(e)
    '''
    1 validation error for MyModel
    url
      Input should be a valid URL, relative URL without a base [type=url_parsing, input_value='not a url', input_type=str]
    '''

```

  1. Note: mypy would prefer `m = MyModel(url=HttpUrl('http://www.example.com'))`, but Pydantic will convert the string to an HttpUrl instance anyway.


"International domains" (e.g. a URL where the host or TLD includes non-ascii characters) will be encoded via
```
from pydantic import BaseModel, HttpUrl

class MyModel(BaseModel):
    url: HttpUrl

m1 = MyModel(url='http://puny£code.com')
print(m1.url)
#> http://xn--punycode-eja.com/
m2 = MyModel(url='https://www.аррӏе.com/')
print(m2.url)
#> https://www.xn--80ak6aa92e.com/
m3 = MyModel(url='https://www.example.珠宝/')
print(m3.url)
#> https://www.example.xn--pbt977c/

```

Underscores in Hostnames
In Pydantic, underscores are allowed in all parts of a domain except the TLD. Technically this might be wrong - in theory the hostname cannot have underscores, but subdomains can.
To explain this; consider the following two cases:
  * `exam_ple.co.uk`: the hostname is `exam_ple`, which should not be allowed since it contains an underscore.
  * `foo_bar.example.com` the hostname is `example`, which should be allowed since the underscore is in the subdomain.


Without having an exhaustive list of TLDs, it would be impossible to differentiate between these two. Therefore underscores are allowed, but you can always do further validation in a validator if desired.
Also, Chrome, Firefox, and Safari all currently accept `http://exam_ple.com` as a URL, so we're in good (or at least big) company.
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
##  AnyWebsocketUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyWebsocketUrl "Permanent link")
```
AnyWebsocketUrl(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any ws or wss URL.
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
