##  fastapi.security.APIKeyCookie [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie "Permanent link")
```
APIKeyCookie(
    *,
    name,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `APIKeyBase`
API key authentication using a cookie.
This defines the name of the cookie that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the cookie automatically and provides it as the dependency result. But it doesn't define how to set that cookie.
#### Usage[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie--usage)
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be a string containing the key value.
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie--example)
```
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyCookie

app = FastAPI()

cookie_scheme = APIKeyCookie(name="session")


@app.get("/items/")
async def read_items(session: str = Depends(cookie_scheme)):
    return {"session": session}

```

PARAMETER | DESCRIPTION
---|---
`name` |  Cookie name. **TYPE:** `str`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if the cookie is not provided, `APIKeyCookie` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the cookie is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in a cookie or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/api_key.py`
```
265
266
267
268
269
270
271
272
273
274
275
276
277
278
279
280
281
282
283
284
285
286
287
288
289
290
291
292
293
294
295
296
297
298
299
300
301
302
303
304
305
306
307
308
309
310
311
312
313
314
```
| ```
def __init__(
    self,
    *,
    name: Annotated[str, Doc("Cookie name.")],
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
            By default, if the cookie is not provided, `APIKeyCookie` will
            automatically cancel the request and send the client an error.

            If `auto_error` is set to `False`, when the cookie is not available,
            instead of erroring out, the dependency result will be `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, in a cookie or
            in an HTTP Bearer token).
            """
        ),
    ] = True,
):
    super().__init__(
        location=APIKeyIn.cookie,
        name=name,
        scheme_name=scheme_name,
        description=description,
        auto_error=auto_error,
    )

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie.model "Permanent link")
```
model = APIKey[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">APIKey</span> \(<code>fastapi.openapi.models.APIKey</code>\)")(
    **{"in": location}, name=name, description=description
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie.make_not_authenticated_error "Permanent link")
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
###  check_api_key [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyCookie.check_api_key "Permanent link")
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
##  fastapi.security.APIKeyHeader [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader "Permanent link")
```
APIKeyHeader(
    *,
    name,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `APIKeyBase`
API key authentication using a header.
This defines the name of the header that should be provided in the request with the API key and integrates that into the OpenAPI documentation. It extracts the key value sent in the header automatically and provides it as the dependency result. But it doesn't define how to send that key to the client.
#### Usage[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader--usage)
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be a string containing the key value.
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader--example)
```
from fastapi import Depends, FastAPI
from fastapi.security import APIKeyHeader

app = FastAPI()

header_scheme = APIKeyHeader(name="x-key")


@app.get("/items/")
async def read_items(key: str = Depends(header_scheme)):
    return {"key": key}

```

PARAMETER | DESCRIPTION
---|---
`name` |  Header name. **TYPE:** `str`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if the header is not provided, `APIKeyHeader` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in a header or in an HTTP Bearer token). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/api_key.py`
```
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
196
197
198
199
200
201
202
203
204
205
206
207
208
209
210
211
212
213
214
215
216
217
218
219
220
221
222
223
224
225
226
```
| ```
def __init__(
    self,
    *,
    name: Annotated[str, Doc("Header name.")],
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
            By default, if the header is not provided, `APIKeyHeader` will
            automatically cancel the request and send the client an error.

            If `auto_error` is set to `False`, when the header is not available,
            instead of erroring out, the dependency result will be `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, in a header or
            in an HTTP Bearer token).
            """
        ),
    ] = True,
):
    super().__init__(
        location=APIKeyIn.header,
        name=name,
        scheme_name=scheme_name,
        description=description,
        auto_error=auto_error,
    )

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader.model "Permanent link")
```
model = APIKey[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.APIKey "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">APIKey</span> \(<code>fastapi.openapi.models.APIKey</code>\)")(
    **{"in": location}, name=name, description=description
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader.make_not_authenticated_error "Permanent link")
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
###  check_api_key [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.APIKeyHeader.check_api_key "Permanent link")
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
