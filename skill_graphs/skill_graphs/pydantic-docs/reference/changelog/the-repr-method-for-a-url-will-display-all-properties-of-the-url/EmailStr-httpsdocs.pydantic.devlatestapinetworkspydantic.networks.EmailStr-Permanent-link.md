##  EmailStr [¶](https://docs.pydantic.dev/latest/api/networks/#pydantic.networks.EmailStr "Permanent link")
Info
To use this type, you need to install the optional
```
pip install email-validator

```

Validate email addresses.
```
from pydantic import BaseModel, EmailStr

class Model(BaseModel):
    email: EmailStr

print(Model(email='[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)'))
#> email='[email protected][](https://docs.pydantic.dev/cdn-cgi/l/email-protection)'

```
