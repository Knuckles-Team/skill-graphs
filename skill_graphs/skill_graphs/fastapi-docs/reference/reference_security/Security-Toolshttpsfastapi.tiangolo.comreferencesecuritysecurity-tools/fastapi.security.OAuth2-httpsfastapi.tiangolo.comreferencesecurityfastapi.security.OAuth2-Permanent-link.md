##  fastapi.security.OAuth2 [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2 "Permanent link")
```
OAuth2(
    *,
    flows=OAuthFlows[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlows</span> \(<code>fastapi.openapi.models.OAuthFlows</code>\)")(),
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `SecurityBase`
This is the base class for OAuth2 authentication, an instance of it would be used as a dependency. All other OAuth2 classes inherit from it and customize it for each OAuth2 flow.
You normally would not create a new class inheriting from it but use one of the existing subclasses, and maybe compose them if you want to support multiple flows.
Read more about it in the [FastAPI docs for Security](https://fastapi.tiangolo.com/tutorial/security/).
PARAMETER | DESCRIPTION
---|---
`flows` |  The dictionary of OAuth2 flows. **TYPE:** `OAuthFlows[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlows</span> \(<code>fastapi.openapi.models.OAuthFlows</code>\)") | dict[str, dict[str, Any]]` **DEFAULT:** `OAuthFlows[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlows</span> \(<code>fastapi.openapi.models.OAuthFlows</code>\)")()`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OAuth2 authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OAuth2 or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/oauth2.py`
```
343
344
345
346
347
348
349
350
351
352
353
354
355
356
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
```
| ```
def __init__(
    self,
    *,
    flows: Annotated[
        OAuthFlowsModel | dict[str, dict[str, Any]],
        Doc(
            """
            The dictionary of OAuth2 flows.
            """
        ),
    ] = OAuthFlowsModel(),
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
            By default, if no HTTP Authorization header is provided, required for
            OAuth2 authentication, it will automatically cancel the request and
            send the client an error.

            If `auto_error` is set to `False`, when the HTTP Authorization header
            is not available, instead of erroring out, the dependency result will
            be `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, with OAuth2
            or in a cookie).
            """
        ),
    ] = True,
):
    self.model = OAuth2Model(
        flows=cast(OAuthFlowsModel, flows), description=description
    )
    self.scheme_name = scheme_name or self.__class__.__name__
    self.auto_error = auto_error

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2.model "Permanent link")
```
model = OAuth2[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2 "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuth2</span> \(<code>fastapi.openapi.models.OAuth2</code>\)")(
    flows=cast(OAuthFlows[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlows</span> \(<code>fastapi.openapi.models.OAuthFlows</code>\)"), flows), description=description
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2.make_not_authenticated_error "Permanent link")
```
make_not_authenticated_error()

```

The OAuth 2 specification doesn't define the challenge that should be used, because a `Bearer` token is not really the only option to authenticate.
But declaring any other authentication challenge would be application-specific as it's not defined in the specification.
For practical reasons, this method uses the `Bearer` challenge by default, as it's probably the most common one.
If you are implementing an OAuth2 authentication scheme other than the provided ones in FastAPI (based on bearer tokens), you might want to override this.
Ref: https://datatracker.ietf.org/doc/html/rfc6749
Source code in `fastapi/security/oauth2.py`
```
401
402
403
404
405
406
407
408
409
410
411
412
413
414
415
416
417
418
419
420
421
```
| ```
def make_not_authenticated_error(self) -> HTTPException:
    """
    The OAuth 2 specification doesn't define the challenge that should be used,
    because a `Bearer` token is not really the only option to authenticate.

    But declaring any other authentication challenge would be application-specific
    as it's not defined in the specification.

    For practical reasons, this method uses the `Bearer` challenge by default, as
    it's probably the most common one.

    If you are implementing an OAuth2 authentication scheme other than the provided
    ones in FastAPI (based on bearer tokens), you might want to override this.

    Ref: https://datatracker.ietf.org/doc/html/rfc6749
    """
    return HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )

```

---|---
