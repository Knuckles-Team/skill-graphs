##  fastapi.security.HTTPBearer [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer "Permanent link")
```
HTTPBearer(
    *,
    bearerFormat=None,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `HTTPBase`
HTTP Bearer token authentication.
#### Usage[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer--usage)
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be an `HTTPAuthorizationCredentials` object containing the `scheme` and the `credentials`.
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer--example)
```
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPAuthorizationCredentials, HTTPBearer

app = FastAPI()

security = HTTPBearer()


@app.get("/users/me")
def read_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
    return {"scheme": credentials.scheme, "credentials": credentials.credentials}

```

PARAMETER | DESCRIPTION
---|---
`bearerFormat` |  Bearer token format. **TYPE:** `str | None` **DEFAULT:** `None`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if the HTTP Bearer token is not provided (in an `Authorization` header), `HTTPBearer` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Bearer token is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in an HTTP Bearer token or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/http.py`
```
254
255
256
257
258
259
260
261
262
263
264
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
```
| ```
def __init__(
    self,
    *,
    bearerFormat: Annotated[str | None, Doc("Bearer token format.")] = None,
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
            By default, if the HTTP Bearer token is not provided (in an
            `Authorization` header), `HTTPBearer` will automatically cancel the
            request and send the client an error.

            If `auto_error` is set to `False`, when the HTTP Bearer token
            is not available, instead of erroring out, the dependency result will
            be `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, in an HTTP
            Bearer token or in a cookie).
            """
        ),
    ] = True,
):
    self.model = HTTPBearerModel(bearerFormat=bearerFormat, description=description)
    self.scheme_name = scheme_name or self.__class__.__name__
    self.auto_error = auto_error

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer.model "Permanent link")
```
model = HTTPBearer[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBearer "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">HTTPBearer</span> \(<code>fastapi.openapi.models.HTTPBearer</code>\)")(
    bearerFormat=bearerFormat, description=description
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_authenticate_headers [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer.make_authenticate_headers "Permanent link")
```
make_authenticate_headers()

```

Source code in `fastapi/security/http.py`
```
84
85
```
| ```
def make_authenticate_headers(self) -> dict[str, str]:
    return {"WWW-Authenticate": f"{self.model.scheme.title()}"}

```

---|---
###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPBearer.make_not_authenticated_error "Permanent link")
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
##  fastapi.security.HTTPDigest [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest "Permanent link")
```
HTTPDigest(
    *, scheme_name=None, description=None, auto_error=True
)

```

Bases: `HTTPBase`
HTTP Digest authentication.
**Warning** : this is only a stub to connect the components with OpenAPI in FastAPI, but it doesn't implement the full Digest scheme, you would need to to subclass it and implement it in your code.
Ref: https://datatracker.ietf.org/doc/html/rfc7616
#### Usage[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest--usage)
Create an instance object and use that object as the dependency in `Depends()`.
The dependency result will be an `HTTPAuthorizationCredentials` object containing the `scheme` and the `credentials`.
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest--example)
```
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import HTTPAuthorizationCredentials, HTTPDigest

app = FastAPI()

security = HTTPDigest()


@app.get("/users/me")
def read_current_user(
    credentials: Annotated[HTTPAuthorizationCredentials, Depends(security)]
):
    return {"scheme": credentials.scheme, "credentials": credentials.credentials}

```

PARAMETER | DESCRIPTION
---|---
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if the HTTP Digest is not provided, `HTTPDigest` will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Digest is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, in HTTP Digest or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/http.py`
```
357
358
359
360
361
362
363
364
365
366
367
368
369
370
371
372
373
374
375
376
377
378
379
380
381
382
383
384
385
386
387
388
389
390
391
392
393
394
395
396
397
398
399
400
401
402
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
            By default, if the HTTP Digest is not provided, `HTTPDigest` will
            automatically cancel the request and send the client an error.

            If `auto_error` is set to `False`, when the HTTP Digest is not
            available, instead of erroring out, the dependency result will
            be `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, in HTTP
            Digest or in a cookie).
            """
        ),
    ] = True,
):
    self.model = HTTPBaseModel(scheme="digest", description=description)
    self.scheme_name = scheme_name or self.__class__.__name__
    self.auto_error = auto_error

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest.model "Permanent link")
```
model = HTTPBase[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.HTTPBase "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">HTTPBase</span> \(<code>fastapi.openapi.models.HTTPBase</code>\)")(scheme='digest', description=description)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_authenticate_headers [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest.make_authenticate_headers "Permanent link")
```
make_authenticate_headers()

```

Source code in `fastapi/security/http.py`
```
84
85
```
| ```
def make_authenticate_headers(self) -> dict[str, str]:
    return {"WWW-Authenticate": f"{self.model.scheme.title()}"}

```

---|---
###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPDigest.make_not_authenticated_error "Permanent link")
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
