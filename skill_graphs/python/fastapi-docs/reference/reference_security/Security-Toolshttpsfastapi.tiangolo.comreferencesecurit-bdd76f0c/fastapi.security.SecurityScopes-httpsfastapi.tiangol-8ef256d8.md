##  fastapi.security.SecurityScopes [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.SecurityScopes "Permanent link")
```
SecurityScopes(scopes=None)

```

This is a special class that you can define in a parameter in a dependency to obtain the OAuth2 scopes required by all the dependencies in the same chain.
This way, multiple dependencies can have different scopes, even when used in the same _path operation_. And with this, you can access all the scopes required in all those dependencies in a single place.
Read more about it in the [FastAPI docs for OAuth2 scopes](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/).
PARAMETER | DESCRIPTION
---|---
`scopes` |  This will be filled by FastAPI. **TYPE:** `list[str] | None` **DEFAULT:** `None`
Source code in `fastapi/security/oauth2.py`
```
666
667
668
669
670
671
672
673
674
675
676
677
678
679
680
681
682
683
684
685
686
687
688
689
690
691
692
693
```
| ```
def __init__(
    self,
    scopes: Annotated[
        list[str] | None,
        Doc(
            """
            This will be filled by FastAPI.
            """
        ),
    ] = None,
):
    self.scopes: Annotated[
        list[str],
        Doc(
            """
            The list of all the scopes required by dependencies.
            """
        ),
    ] = scopes or []
    self.scope_str: Annotated[
        str,
        Doc(
            """
            All the scopes required by all the dependencies in a single string
            separated by spaces, as defined in the OAuth2 specification.
            """
        ),
    ] = " ".join(self.scopes)

```

---|---
###  scopes `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.SecurityScopes.scopes "Permanent link")
```
scopes = scopes or []

```

The list of all the scopes required by dependencies.
###  scope_str `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.SecurityScopes.scope_str "Permanent link")
```
scope_str = join(scopes)

```

All the scopes required by all the dependencies in a single string separated by spaces, as defined in the OAuth2 specification.
## OpenID Connect[¶](https://fastapi.tiangolo.com/reference/security/#openid-connect)
##  fastapi.security.OpenIdConnect [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OpenIdConnect "Permanent link")
```
OpenIdConnect(
    *,
    openIdConnectUrl,
    scheme_name=None,
    description=None,
    auto_error=True
)

```

Bases: `SecurityBase`
OpenID Connect authentication class. An instance of it would be used as a dependency.
**Warning** : this is only a stub to connect the components with OpenAPI in FastAPI, but it doesn't implement the full OpenIdConnect scheme, for example, it doesn't use the OpenIDConnect URL. You would need to to subclass it and implement it in your code.
PARAMETER | DESCRIPTION
---|---
`openIdConnectUrl` |  The OpenID Connect URL. **TYPE:** `str`
`scheme_name` |  Security scheme name. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`description` |  Security scheme description. It will be included in the generated OpenAPI (e.g. visible at `/docs`). **TYPE:** `str | None` **DEFAULT:** `None`
`auto_error` |  By default, if no HTTP Authorization header is provided, required for OpenID Connect authentication, it will automatically cancel the request and send the client an error. If `auto_error` is set to `False`, when the HTTP Authorization header is not available, instead of erroring out, the dependency result will be `None`. This is useful when you want to have optional authentication. It is also useful when you want to have authentication that can be provided in one of multiple optional ways (for example, with OpenID Connect or in a cookie). **TYPE:** `bool` **DEFAULT:** `True`
Source code in `fastapi/security/open_id_connect_url.py`
```
22
23
24
25
26
27
28
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
44
45
46
47
48
49
50
51
52
53
54
55
56
57
58
59
60
61
62
63
64
65
66
67
68
69
70
71
72
73
74
75
76
77
78
```
| ```
def __init__(
    self,
    *,
    openIdConnectUrl: Annotated[
        str,
        Doc(
            """
        The OpenID Connect URL.
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
            OpenID Connect authentication, it will automatically cancel the request
            and send the client an error.

            If `auto_error` is set to `False`, when the HTTP Authorization header
            is not available, instead of erroring out, the dependency result will
            be `None`.

            This is useful when you want to have optional authentication.

            It is also useful when you want to have authentication that can be
            provided in one of multiple optional ways (for example, with OpenID
            Connect or in a cookie).
            """
        ),
    ] = True,
):
    self.model = OpenIdConnectModel(
        openIdConnectUrl=openIdConnectUrl, description=description
    )
    self.scheme_name = scheme_name or self.__class__.__name__
    self.auto_error = auto_error

```

---|---
###  model `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OpenIdConnect.model "Permanent link")
```
model = OpenIdConnect[](https://fastapi.tiangolo.com/reference/openapi/models/#fastapi.openapi.models.OpenIdConnect "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">OpenIdConnect</span> \(<code>fastapi.openapi.models.OpenIdConnect</code>\)")(
    openIdConnectUrl=openIdConnectUrl,
    description=description,
)

```

###  scheme_name `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OpenIdConnect.scheme_name "Permanent link")
```
scheme_name = scheme_name or __name__

```

###  auto_error `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OpenIdConnect.auto_error "Permanent link")
```
auto_error = auto_error

```

###  make_not_authenticated_error [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OpenIdConnect.make_not_authenticated_error "Permanent link")
```
make_not_authenticated_error()

```

Source code in `fastapi/security/open_id_connect_url.py`
```
80
81
82
83
84
85
```
| ```
def make_not_authenticated_error(self) -> HTTPException:
    return HTTPException(
        status_code=HTTP_401_UNAUTHORIZED,
        detail="Not authenticated",
        headers={"WWW-Authenticate": "Bearer"},
    )

```

---|---
