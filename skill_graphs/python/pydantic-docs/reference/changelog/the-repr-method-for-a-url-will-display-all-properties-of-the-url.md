# the repr() method for a url will display all properties of the url
print(repr(m.url))
#> HttpUrl('http://www.example.com/')
print(m.url.scheme)
#> http
print(m.url.host)
#> www.example.com
print(m.url.port)
#> 80

class MyDatabaseModel(BaseModel):
    db: PostgresDsn

    @field_validator('db')
    def check_db_name(cls, v):
        assert v.path and len(v.path) > 1, 'database must be provided'
        return v

m = MyDatabaseModel(db='postgres://user:pass@localhost:5432/foobar')
print(m.db)
#> postgres://user:pass@localhost:5432/foobar

try:
    MyDatabaseModel(db='postgres://user:pass@localhost:5432')
except ValidationError as e:
    print(e)
    '''
    1 validation error for MyDatabaseModel
    db
      Assertion failed, database must be provided
    assert (None)
     +  where None = PostgresDsn('postgres://user:pass@localhost:5432').path [type=assertion_error, input_value='postgres://user:pass@localhost:5432', input_type=str]
    '''

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
###  host `property` [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.PostgresDsn.host "Permanent link")
```
host:

```

The required URL host.
