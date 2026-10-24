##  fastapi.security.APIKeyQuery [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery "Permanent link")
```
APIKeyQuery(
    *,
    name,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `APIKeyBase`
API key authentication using a query parameter.
This defines the name of the query parameter that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the query parameter automatically and provides it as the dependency result. But it doesn't define how to send that API key to the client.
#### Usage[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery--usage)
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be a string containing the key value.
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery--example)
```
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyQuery

app = FastAPI()

query_scheme = APIKeyQuery(name="api_key")


@app.get("/items/")
async def read_items(api_key: str = Depends(query_scheme)):
    return {"api_key": api_key}

```

PARAMETER | DESCRIPTION
---|---
`name` |  Query parameter name. **TYPE:** `str`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if the query parameter is not provided, `APIKeyQuery` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the query parameter is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in a query parameter or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/api_key.py`
```
 85
 86
 87
 88
 89
 90
 91
 92
 93
 94
 95
 96
 97
 98
 99
100
101
102
103
104
105
106
107
108
109
110
111
112
113
114
115
116
117
118
119
120
121
122
123
124
125
126
127
128
129
130
131
132
133
134
135
136
137
138
```
| ```
def __init__(
    self,
    *,
    name: Annotated[
        str,
        Doc("Query parameter name."),
    ],
    scheme_name: Annotated[
        str | None,
        Doc(
            """
            Security scheme name.

            It will be included in the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Security scheme description.

            It will be included in the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    auto_error: Annotated[
        bool,
        Doc(
            """
            By default, if the query parameter is not provided, `APIKeyQuery` will
            automatically cancel the request and send the client an error.

            If `auto_error` is set to `False`, when the query parameter is not
            available, instead of erroring out, the dependency result will be
            `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, in a query
            parameter or in an HTTP Bearer token).
            """
        ),
    ] = True,
):
    super().__init__(
        location=APIKeyIn.query,
        name=name,
        scheme_name=scheme_name,
        description=description,
        auto_error=auto_error,
    )

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery.model "Permanent link")
```
model = APIKey[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">APIKey</span> \(<code>fastapi.openapi.models.APIKey</code>\)")(
    **{"in": location}, name=name, description=description
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery.make_not_authenticated_error "Permanent link")
```
make_not_authenticated_error()

```

The WWW-Authenticate header is not standardized for API Key authentication but the HTTP specification requires that an error of 401 "Unauthorized" must include a WWW-Authenticate header.
Ref: https://datatracker.ietf.org/doc/html/rfc9110#name-401-unauthorized
For this, this method sends a custom challenge `APIKey`.
Source code in `fastapi/security/api_key.py`
```
29
30
31
32
33
34
35
36
37
38
39
40
41
42
43
```
| ```
def make_not_authenticated_error(self) -> HTTPException:
    """
    The WWW-Authenticate header is not standardized for API Key authentication but
    the HTTP specification requires that an error of 401 "Unauthorized" must
    include a WWW-Authenticate header.

    Ref: https://datatracker.ietf.org/doc/html/rfc9110#name-401-unauthorized

    For this, this method sends a custom challenge `APIKey`.
    """
    return HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "APIKey"},
    )

```

---|---
###  check_api_key [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyQuery.check_api_key "Permanent link")
```
check_api_key(api_key)

```

Source code in `fastapi/security/api_key.py`
```
45
46
47
48
49
50
```
| ```
def check_api_key(self, api_key: str | None) -> str | None:
    if not api_key:
        if self.auto_error:
            raise self.make_not_authenticated_error()
        return None
    return api_key

```

---|---
## HTTP Authentication Schemes[¶](https://fastapi.tiangolo.com/reference/security/#http-authentication-schemes)
##  fastapi.security.HTTPBasic [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic "Permanent link")
```
HTTPBasic(
    *,
    scheme_name=None,
    realm=None,
    description=None,
    auto_error=True
)

```

Bases: `HTTPBase`
HTTP Basic authentication.
Ref: https://datatracker.ietf.org/doc/html/rfc7617
#### Usage[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic--usage)
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be an `HTTPBasicCredentials` object containing the `username` and the `password`.
Read more about it in the [FastAPI docs for HTTP Basic Auth](https://fastapi.tiangolo.com/advanced/security/http-basic-auth/).
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic--example)
```
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI()

security = HTTPBasic()


@app.get("/users/me")
def read_current_user(credentials: Annotated[HTTPBasicCredentials, Depends(security)]):
    return {"username": credentials.username, "password": credentials.password}

```

PARAMETER | DESCRIPTION
---|---
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`realm` |  HTTP Basic authentication realm. **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if the HTTP Basic authentication is not provided (a header), `HTTPBasic` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Basic authentication is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in HTTP Basic authentication or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/http.py`
```
140
141
142
143
144
145
146
147
148
149
150
151
152
153
154
155
156
157
158
159
160
161
162
163
164
165
166
167
168
169
170
171
172
173
174
175
176
177
178
179
180
181
182
183
184
185
186
187
188
189
190
191
192
193
194
195
```
| ```
def __init__(
    self,
    *,
    scheme_name: Annotated[
        str | None,
        Doc(
            """
            Security scheme name.

            It will be included in the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    realm: Annotated[
        str | None,
        Doc(
            """
            HTTP Basic authentication realm.
            """
        ),
    ] = None,
    description: Annotated[
        str | None,
        Doc(
            """
            Security scheme description.

            It will be included in the generated OpenAPI (e.g. visible at `/docs`).
            """
        ),
    ] = None,
    auto_error: Annotated[
        bool,
        Doc(
            """
            By default, if the HTTP Basic authentication is not provided (a
            header), `HTTPBasic` will automatically cancel the request and send the
            client an error.

            If `auto_error` is set to `False`, when the HTTP Basic authentication
            is not available, instead of erroring out, the dependency result will
            be `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, in HTTP Basic
            authentication or in an HTTP Bearer token).
            """
        ),
    ] = True,
):
    self.model = HTTPBaseModel(scheme="basic", description=description)
    self.scheme_name = scheme_name or self.__class__.__name__
    self.realm = realm
    self.auto_error = auto_error

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic.model "Permanent link")
```
model = HTTPBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">HTTPBase</span> \(<code>fastapi.openapi.models.HTTPBase</code>\)")(scheme='basic', description=description)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  realm `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic.realm "Permanent link")
```
realm = realm

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic.make_not_authenticated_error "Permanent link")
```
make_not_authenticated_error()

```

Source code in `fastapi/security/http.py`
```
87
88
89
90
91
92
```
| ```
def make_not_authenticated_error(self) -> HTTPException:
    return HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers=self.make_authenticate_headers(),
    )

```

---|---
###  make_authenticate_headers [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBasic.make_authenticate_headers "Permanent link")
```
make_authenticate_headers()

```

Source code in `fastapi/security/http.py`
```
197
198
199
200
```
| ```
def make_authenticate_headers(self) -> dict[str, str]:
    if self.realm:
        return {"WWW-Authenticate": f'Basic realm="{self.realm}"'}
    return {"WWW-Authenticate": "Basic"}

```

---|---
