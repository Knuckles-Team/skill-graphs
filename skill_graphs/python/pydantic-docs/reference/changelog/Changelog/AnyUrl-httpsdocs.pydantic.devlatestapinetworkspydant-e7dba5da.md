##  AnyUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "Permanent link")
```
AnyUrl(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `_BaseUrl`
Base type for all URLs.
  * Any scheme allowed
  * Top-level domain (TLD) not required
  * Host not required


Assuming an input URL of `http://samuel:[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection):8000/the/path/?query=here#fragment=is;this=bit`, the types export the following properties:
  * `scheme`: the URL scheme (`http`), always set.
  * `host`: the URL host (`example.com`).
  * `username`: optional username if included (`samuel`).
  * `password`: optional password if included (`pass`).
  * `port`: optional port (`8000`).
  * `path`: optional path (`/the/path/`).
  * `query`: optional URL query (for example, `GET` arguments or "search string", such as `query=here`).
  * `fragment`: optional fragment (`fragment=is;this=bit`).

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
##  AnyHttpUrl [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyHttpUrl "Permanent link")
```
AnyHttpUrl(url:  | Url[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.Url "pydantic_core.Url") | _BaseUrl)

```

Bases: `AnyUrl[](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.AnyUrl "pydantic.networks.AnyUrl")`
A type that will accept any http or https URL.
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
