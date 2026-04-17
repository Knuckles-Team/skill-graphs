##  fastapi.responses.UJSONResponse [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse "Permanent link")
```
UJSONResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")`
JSON response using the ujson library to serialize data to JSON.
**Deprecated** : `UJSONResponse` is deprecated. FastAPI now serializes data directly to JSON bytes via Pydantic when a return type or response model is set, which is faster and doesn't need a custom response class.
Read more in the [FastAPI docs for Custom Response](https://fastapi.tiangolo.com/advanced/custom-response/#orjson-or-response-model) and the [FastAPI docs for Response Model](https://fastapi.tiangolo.com/tutorial/response-model/).
**Note** : `ujson` is not included with FastAPI and must be installed separately, e.g. `pip install ujson`.
Source code in `starlette/responses.py`
```
181
182
183
184
185
186
187
188
189
```
| ```
def __init__(
    self,
    content: Any,
    status_code: int = 200,
    headers: Mapping[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> None:
    super().__init__(content, status_code, headers, media_type, background)

```

---|---
###  charset `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.charset "Permanent link")
```
charset = 'utf-8'

```

###  status_code `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.status_code "Permanent link")
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.media_type "Permanent link")
```
media_type = 'application/json'

```

###  body `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.body "Permanent link")
```
body = render(content)

```

###  background `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.background "Permanent link")
```
background = background

```

###  headers `property` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.headers "Permanent link")
```
headers

```

###  render [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.render "Permanent link")
```
render(content)

```

Source code in `fastapi/responses.py`
```
51
52
53
```
| ```
def render(self, content: Any) -> bytes:
    assert ujson is not None, "ujson must be installed to use UJSONResponse"
    return ujson.dumps(content, ensure_ascii=False).encode("utf-8")

```

---|---
###  init_headers [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.init_headers "Permanent link")
```
init_headers(headers=None)

```

Source code in `starlette/responses.py`
```
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
79
80
81
82
```
| ```
def init_headers(self, headers: Mapping[str, str] | None = None) -> None:
    if headers is None:
        raw_headers: list[tuple[bytes, bytes]] = []
        populate_content_length = True
        populate_content_type = True
    else:
        raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
        keys = [h[0] for h in raw_headers]
        populate_content_length = b"content-length" not in keys
        populate_content_type = b"content-type" not in keys

    body = getattr(self, "body", None)
    if (
        body is not None
        and populate_content_length
        and not (self.status_code < 200 or self.status_code in (204, 304))
    ):
        content_length = str(len(body))
        raw_headers.append((b"content-length", content_length.encode("latin-1")))

    content_type = self.media_type
    if content_type is not None and populate_content_type:
        if content_type.startswith("text/") and "charset=" not in content_type.lower():
            content_type += "; charset=" + self.charset
        raw_headers.append((b"content-type", content_type.encode("latin-1")))

    self.raw_headers = raw_headers

```

---|---
###  set_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.set_cookie "Permanent link")
```
set_cookie(
    key,
    value="",
    max_age=None,
    expires=None,
    path="/",
    domain=None,
    secure=False,
    httponly=False,
    samesite="lax",
    partitioned=False,
)

```

Source code in `starlette/responses.py`
```
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
```
| ```
def set_cookie(
    self,
    key: str,
    value: str = "",
    max_age: int | None = None,
    expires: datetime | str | int | None = None,
    path: str | None = "/",
    domain: str | None = None,
    secure: bool = False,
    httponly: bool = False,
    samesite: Literal["lax", "strict", "none"] | None = "lax",
    partitioned: bool = False,
) -> None:
    cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
    cookie[key] = value
    if max_age is not None:
        cookie[key]["max-age"] = max_age
    if expires is not None:
        if isinstance(expires, datetime):
            cookie[key]["expires"] = format_datetime(expires, usegmt=True)
        else:
            cookie[key]["expires"] = expires
    if path is not None:
        cookie[key]["path"] = path
    if domain is not None:
        cookie[key]["domain"] = domain
    if secure:
        cookie[key]["secure"] = True
    if httponly:
        cookie[key]["httponly"] = True
    if samesite is not None:
        assert samesite.lower() in [
            "strict",
            "lax",
            "none",
        ], "samesite must be either 'strict', 'lax' or 'none'"
        cookie[key]["samesite"] = samesite
    if partitioned:
        if sys.version_info < (3, 14):
            raise ValueError("Partitioned cookies are only supported in Python 3.14 and above.")  # pragma: no cover
        cookie[key]["partitioned"] = True  # pragma: no cover

    cookie_val = cookie.output(header="").strip()
    self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```

---|---
###  delete_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.UJSONResponse.delete_cookie "Permanent link")
```
delete_cookie(
    key,
    path="/",
    domain=None,
    secure=False,
    httponly=False,
    samesite="lax",
)

```

Source code in `starlette/responses.py`
```
135
136
137
138
139
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
```
| ```
def delete_cookie(
    self,
    key: str,
    path: str = "/",
    domain: str | None = None,
    secure: bool = False,
    httponly: bool = False,
    samesite: Literal["lax", "strict", "none"] | None = "lax",
) -> None:
    self.set_cookie(
        key,
        max_age=0,
        expires=0,
        path=path,
        domain=domain,
        secure=secure,
        httponly=httponly,
        samesite=samesite,
    )

```

---|---
##  fastapi.responses.ORJSONResponse [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse "Permanent link")
```
ORJSONResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `JSONResponse[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.JSONResponse</span> \(<code>starlette.responses.JSONResponse</code>\)")`
JSON response using the orjson library to serialize data to JSON.
**Deprecated** : `ORJSONResponse` is deprecated. FastAPI now serializes data directly to JSON bytes via Pydantic when a return type or response model is set, which is faster and doesn't need a custom response class.
Read more in the [FastAPI docs for Custom Response](https://fastapi.tiangolo.com/advanced/custom-response/#orjson-or-response-model) and the [FastAPI docs for Response Model](https://fastapi.tiangolo.com/tutorial/response-model/).
**Note** : `orjson` is not included with FastAPI and must be installed separately, e.g. `pip install orjson`.
Source code in `starlette/responses.py`
```
181
182
183
184
185
186
187
188
189
```
| ```
def __init__(
    self,
    content: Any,
    status_code: int = 200,
    headers: Mapping[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> None:
    super().__init__(content, status_code, headers, media_type, background)

```

---|---
###  charset `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.charset "Permanent link")
```
charset = 'utf-8'

```

###  status_code `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.status_code "Permanent link")
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.media_type "Permanent link")
```
media_type = 'application/json'

```

###  body `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.body "Permanent link")
```
body = render(content)

```

###  background `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.background "Permanent link")
```
background = background

```

###  headers `property` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.headers "Permanent link")
```
headers

```

###  render [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.render "Permanent link")
```
render(content)

```

Source code in `fastapi/responses.py`
```
81
82
83
84
85
```
| ```
def render(self, content: Any) -> bytes:
    assert orjson is not None, "orjson must be installed to use ORJSONResponse"
    return orjson.dumps(
        content, option=orjson.OPT_NON_STR_KEYS | orjson.OPT_SERIALIZE_NUMPY
    )

```

---|---
###  init_headers [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.init_headers "Permanent link")
```
init_headers(headers=None)

```

Source code in `starlette/responses.py`
```
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
79
80
81
82
```
| ```
def init_headers(self, headers: Mapping[str, str] | None = None) -> None:
    if headers is None:
        raw_headers: list[tuple[bytes, bytes]] = []
        populate_content_length = True
        populate_content_type = True
    else:
        raw_headers = [(k.lower().encode("latin-1"), v.encode("latin-1")) for k, v in headers.items()]
        keys = [h[0] for h in raw_headers]
        populate_content_length = b"content-length" not in keys
        populate_content_type = b"content-type" not in keys

    body = getattr(self, "body", None)
    if (
        body is not None
        and populate_content_length
        and not (self.status_code < 200 or self.status_code in (204, 304))
    ):
        content_length = str(len(body))
        raw_headers.append((b"content-length", content_length.encode("latin-1")))

    content_type = self.media_type
    if content_type is not None and populate_content_type:
        if content_type.startswith("text/") and "charset=" not in content_type.lower():
            content_type += "; charset=" + self.charset
        raw_headers.append((b"content-type", content_type.encode("latin-1")))

    self.raw_headers = raw_headers

```

---|---
###  set_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.set_cookie "Permanent link")
```
set_cookie(
    key,
    value="",
    max_age=None,
    expires=None,
    path="/",
    domain=None,
    secure=False,
    httponly=False,
    samesite="lax",
    partitioned=False,
)

```

Source code in `starlette/responses.py`
```
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
```
| ```
def set_cookie(
    self,
    key: str,
    value: str = "",
    max_age: int | None = None,
    expires: datetime | str | int | None = None,
    path: str | None = "/",
    domain: str | None = None,
    secure: bool = False,
    httponly: bool = False,
    samesite: Literal["lax", "strict", "none"] | None = "lax",
    partitioned: bool = False,
) -> None:
    cookie: http.cookies.BaseCookie[str] = http.cookies.SimpleCookie()
    cookie[key] = value
    if max_age is not None:
        cookie[key]["max-age"] = max_age
    if expires is not None:
        if isinstance(expires, datetime):
            cookie[key]["expires"] = format_datetime(expires, usegmt=True)
        else:
            cookie[key]["expires"] = expires
    if path is not None:
        cookie[key]["path"] = path
    if domain is not None:
        cookie[key]["domain"] = domain
    if secure:
        cookie[key]["secure"] = True
    if httponly:
        cookie[key]["httponly"] = True
    if samesite is not None:
        assert samesite.lower() in [
            "strict",
            "lax",
            "none",
        ], "samesite must be either 'strict', 'lax' or 'none'"
        cookie[key]["samesite"] = samesite
    if partitioned:
        if sys.version_info < (3, 14):
            raise ValueError("Partitioned cookies are only supported in Python 3.14 and above.")  # pragma: no cover
        cookie[key]["partitioned"] = True  # pragma: no cover

    cookie_val = cookie.output(header="").strip()
    self.raw_headers.append((b"set-cookie", cookie_val.encode("latin-1")))

```

---|---
###  delete_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.ORJSONResponse.delete_cookie "Permanent link")
```
delete_cookie(
    key,
    path="/",
    domain=None,
    secure=False,
    httponly=False,
    samesite="lax",
)

```

Source code in `starlette/responses.py`
```
135
136
137
138
139
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
```
| ```
def delete_cookie(
    self,
    key: str,
    path: str = "/",
    domain: str | None = None,
    secure: bool = False,
    httponly: bool = False,
    samesite: Literal["lax", "strict", "none"] | None = "lax",
) -> None:
    self.set_cookie(
        key,
        max_age=0,
        expires=0,
        path=path,
        domain=domain,
        secure=secure,
        httponly=httponly,
        samesite=samesite,
    )

```

---|---
