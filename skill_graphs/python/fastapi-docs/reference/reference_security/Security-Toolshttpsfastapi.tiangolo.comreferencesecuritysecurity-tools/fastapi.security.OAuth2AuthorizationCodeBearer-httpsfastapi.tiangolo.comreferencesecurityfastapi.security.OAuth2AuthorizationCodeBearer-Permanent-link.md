##  fastapi.security.OAuth2AuthorizationCodeBearer [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2AuthorizationCodeBearer "Permanent link")
```
OAuth2AuthorizationCodeBearer(
    authorizationUrl,
    tokenUrl,
    refreshUrl=None,
    scheme_name=None,
    scopes=None,
    description=None,
    auto_error=True,
)

```

Bases: `OAuth2[](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2 "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.security.OAuth2</span> \(<code>fastapi.security.oauth2.OAuth2</code>\)")`
OAuth2 flow for authentication using a bearer token obtained with an OAuth2 code flow. An instance of it would be used as a dependency.
PARAMETER | DESCRIPTION
---|---
`tokenUrl` |  The URL to obtain the OAuth2 token. **TYPE:** `str`
`refreshUrl` |  The URL to refresh the token and obtain a new one. **TYPE:** `str | None` **DEFAULT:** `None`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`scopes` |  The OAuth2 scopes that would be required by the _path operations_ that use this dependency. **TYPE:** `dict[str, str] | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OAuth2 authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OAuth2 or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/oauth2.py`
```
553
554
555
556
557
558
559
560
561
562
563
564
565
566
567
568
569
570
571
572
573
574
575
576
577
578
579
580
581
582
583
584
585
586
587
588
589
590
591
592
593
594
595
596
597
598
599
600
601
602
603
604
605
606
607
608
609
610
611
612
613
614
615
616
617
618
619
620
621
622
623
624
625
626
627
628
629
630
631
632
633
634
635
636
637
638
639
640
```
| ```
def __init__(
    self,
    authorizationUrl: str,
    tokenUrl: Annotated[
        str,
        Doc(
            """
            The URL to obtain the OAuth2 token.
            """
        ),
    ],
    refreshUrl: Annotated[
        str | None,
        Doc(
            """
            The URL to refresh the token and obtain a new one.
            """
        ),
    ] = None,
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
    if not scopes:
        scopes = {}
    flows = OAuthFlowsModel(
        authorizationCode=cast(
            Any,
            {
                "authorizationUrl": authorizationUrl,
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
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2AuthorizationCodeBearer.model "Permanent link")
```
model = OAuth2[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuth2 "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuth2</span> \(<code>fastapi.openapi.models.OAuth2</code>\)")(
    flows=cast(OAuthFlows[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OAuthFlows "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OAuthFlows</span> \(<code>fastapi.openapi.models.OAuthFlows</code>\)"), flows), description=description
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2AuthorizationCodeBearer.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2AuthorizationCodeBearer.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2AuthorizationCodeBearer.make_not_authenticated_error "Permanent link")
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
