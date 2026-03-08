##  fastapi.security.OAuth2PasswordBearer [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordBearer "Permanent link")
```
OAuth2PasswordBearer(
    tokenUrl,
    scheme_name=None,
    scopes=None,
    description=None,
    auto_error=True,
    refreshUrl=None,
)

```

Bases: `OAuth2[](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2 "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.security.OAuth2</span> \(<code>fastapi.security.oauth2.OAuth2</code>\)")`
OAuth2 flow for authentication using a bearer token obtained with a password. An instance of it would be used as a dependency.
Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
PARAMETER | DESCRIPTION
---|---
`tokenUrl` |  The URL to obtain the OAuth2 token. This would be the _path operation_ that has `OAuth2PasswordRequestForm` as a dependency. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`scopes` |  The OAuth2 scopes that would be required by the _path operations_ that use this dependency. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `dict[str, str] | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OAuth2 authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OAuth2 or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`
`refreshUrl` |  The URL to refresh the token and obtain a new one. **TYPE:** `str | None` **DEFAULT:** `None`
Source code in `fastapi/security/oauth2.py`
```
442
443
444
445
446
447
448
449
450
451
452
453
454
455
456
457
458
459
460
461
462
463
464
465
466
467
468
469
470
471
472
473
474
475
476
477
478
479
480
481
482
483
484
485
486
487
488
489
490
491
492
493
494
495
496
497
498
499
500
501
502
503
504
505
506
507
508
509
510
511
512
513
514
515
516
517
518
519
520
521
522
523
524
525
526
527
528
529
530
531
532
533
534
```
| ```
def __init__(
    self,
    tokenUrl: Annotated[
        str,
        Doc(
            """
            The URL to obtain the OAuth2 token. This would be the *path operation*
            that has `OAuth2PasswordRequestForm` as a dependency.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
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
    scopes: Annotated[
        dict[str, str] | None,
        Doc(
            """
            The OAuth2 scopes that would be required by the *path operations* that
            use this dependency.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
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
    refreshUrl: Annotated[
        str | None,
        Doc(
            """
            The URL to refresh the token and obtain a new one.
            """
        ),
    ] = None,
):
    if not scopes:
        scopes = {}
    flows = OAuthFlowsModel(
        password=cast(
            Any,
            {
                "tokenUrl": tokenUrl,
                "refreshUrl": refreshUrl,
                "scopes": scopes,
            },
        )
    )
    super().__init__(
        flows=flows,
        scheme_name=scheme_name,
        description=description,
        auto_error=auto_error,
    )

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordBearer.model "Permanent link")
```
model = OAuth2[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2 "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuth2</span> \(<code>fastapi.openapi.models.OAuth2</code>\)")(
    flows=cast(OAuthFlows[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlows</span> \(<code>fastapi.openapi.models.OAuthFlows</code>\)"), flows), description=description
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordBearer.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordBearer.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordBearer.make_not_authenticated_error "Permanent link")
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
