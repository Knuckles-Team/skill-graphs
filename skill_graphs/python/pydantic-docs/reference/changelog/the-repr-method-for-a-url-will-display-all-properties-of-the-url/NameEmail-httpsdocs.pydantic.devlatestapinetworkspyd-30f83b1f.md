##  NameEmail [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.NameEmail "Permanent link")
```
NameEmail(name: , email: )

```

Bases: `Representation`
Info
To use this type, you need to install the optional
```
pip install email-validator

```

Validate a name and email address combination, as specified by
The `NameEmail` has two properties: `name` and `email`. In case the `name` is not provided, it's inferred from the email address.
```
from pydantic import BaseModel, NameEmail

class User(BaseModel):
    email: NameEmail

user = User(email='Fred Bloggs <[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)>')
print(user.email)
#> Fred Bloggs <[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)>
print(user.email.name)
#> Fred Bloggs

user = User(email='[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)')
print(user.email)
#> fred.bloggs <[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)>
print(user.email.name)
#> fred.bloggs

```

Source code in `pydantic/networks.py`
```
1059
1060
1061
```
| ```
def __init__(self, name: str, email: str):
    self.name = name
    self.email = email

```

---|---
##  IPvAnyAddress [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyAddress "Permanent link")
Validate an IPv4 or IPv6 address.
```
from pydantic import BaseModel
from pydantic.networks import IPvAnyAddress

class IpModel(BaseModel):
    ip: IPvAnyAddress

print(IpModel(ip='127.0.0.1'))
#> ip=IPv4Address('127.0.0.1')

try:
    IpModel(ip='http://www.example.com')
except ValueError as e:
    print(e.errors())
    '''
    [
        {
            'type': 'ip_any_address',
            'loc': ('ip',),
            'msg': 'value is not a valid IPv4 or IPv6 address',
            'input': 'http://www.example.com',
        }
    ]
    '''

```

##  IPvAnyInterface [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyInterface "Permanent link")
Validate an IPv4 or IPv6 interface.
##  IPvAnyNetwork [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.IPvAnyNetwork "Permanent link")
Validate an IPv4 or IPv6 network.
##  validate_email [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.validate_email "Permanent link")
```
validate_email(value: ) -> [, ]

```

Email address validation using
Returns:
Type | Description
---|---
|  A tuple containing the local part of the email (or the name for "pretty" email addresses) and the normalized email.
Raises:
Type | Description
---|---
`PydanticCustomError[](https://docs.pydantic.dev/latest/api/pydantic_core/#pydantic_core.PydanticCustomError "pydantic_core.PydanticCustomError")` |  If the email is invalid.
Note
Note that:
  * Raw IP address (literal) domain parts are not allowed.
  * `"John Doe <[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)>"` style "pretty" email addresses are processed.
  * Spaces are striped from the beginning and end of addresses, but no error is raised.

Source code in `pydantic/networks.py`
```
1283
1284
1285
1286
1287
1288
1289
1290
1291
1292
1293
1294
1295
1296
1297
1298
1299
1300
1301
1302
1303
1304
1305
1306
1307
1308
1309
1310
1311
1312
1313
1314
1315
1316
1317
1318
1319
1320
1321
1322
1323
1324
1325
1326
1327
1328
```
| ```
def validate_email(value: str) -> tuple[str, str]:
    """Email address validation using [email-validator](https://pypi.org/project/email-validator/).

    Returns:
        A tuple containing the local part of the email (or the name for "pretty" email addresses)
            and the normalized email.

    Raises:
        PydanticCustomError: If the email is invalid.

    Note:
        Note that:

        * Raw IP address (literal) domain parts are not allowed.
        * `"John Doe <[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)>"` style "pretty" email addresses are processed.
        * Spaces are striped from the beginning and end of addresses, but no error is raised.
    """
    if email_validator is None:
        import_email_validator()

    if len(value) > MAX_EMAIL_LENGTH:
        raise PydanticCustomError(
            'value_error',
            'value is not a valid email address: {reason}',
            {'reason': f'Length must not exceed {MAX_EMAIL_LENGTH} characters'},
        )

    m = pretty_email_regex.fullmatch(value)
    name: str | None = None
    if m:
        unquoted_name, quoted_name, value = m.groups()
        name = unquoted_name or quoted_name

    email = value.strip()

    try:
        parts = email_validator.validate_email(email, check_deliverability=False)
    except email_validator.EmailNotValidError as e:
        raise PydanticCustomError(
            'value_error', 'value is not a valid email address: {reason}', {'reason': str(e.args[0])}
        ) from e

    email = parts.normalized
    assert email is not None
    name = name or parts.local_part
    return name, email

```

---|---
Was this page helpful?
Thanks for your feedback!
Thanks for your feedback!
