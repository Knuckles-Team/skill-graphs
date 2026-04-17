##  fastapi.responses.JSONResponse [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse "Permanent link")
```
JSONResponse(
    content,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `Response[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.Response</span> \(<code>starlette.responses.Response</code>\)")`
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
###  charset `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.charset "Permanent link")
```
charset = 'utf-8'

```

###  status_code `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.status_code "Permanent link")
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.media_type "Permanent link")
```
media_type = 'application/json'

```

###  body `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.body "Permanent link")
```
body = render(content)

```

###  background `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.background "Permanent link")
```
background = background

```

###  headers `property` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.headers "Permanent link")
```
headers

```

###  render [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.render "Permanent link")
```
render(content)

```

Source code in `starlette/responses.py`
```
191
192
193
194
195
196
197
198
```
| ```
def render(self, content: Any) -> bytes:
    return json.dumps(
        content,
        ensure_ascii=False,
        allow_nan=False,
        indent=None,
        separators=(",", ":"),
    ).encode("utf-8")

```

---|---
###  init_headers [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.init_headers "Permanent link")
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
###  set_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.set_cookie "Permanent link")
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
###  delete_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.JSONResponse.delete_cookie "Permanent link")
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
##  fastapi.responses.PlainTextResponse [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse "Permanent link")
```
PlainTextResponse(
    content=None,
    status_code=200,
    headers=None,
    media_type=None,
    background=None,
)

```

Bases: `Response[](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.Response "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.responses.Response</span> \(<code>starlette.responses.Response</code>\)")`
Source code in `starlette/responses.py`
```
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
```
| ```
def __init__(
    self,
    content: Any = None,
    status_code: int = 200,
    headers: Mapping[str, str] | None = None,
    media_type: str | None = None,
    background: BackgroundTask | None = None,
) -> None:
    self.status_code = status_code
    if media_type is not None:
        self.media_type = media_type
    self.background = background
    self.body = self.render(content)
    self.init_headers(headers)

```

---|---
###  charset `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.charset "Permanent link")
```
charset = 'utf-8'

```

###  status_code `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.status_code "Permanent link")
```
status_code = status_code

```

###  media_type `class-attribute` `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.media_type "Permanent link")
```
media_type = 'text/plain'

```

###  body `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.body "Permanent link")
```
body = render(content)

```

###  background `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.background "Permanent link")
```
background = background

```

###  headers `property` [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.headers "Permanent link")
```
headers

```

###  render [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.render "Permanent link")
```
render(content)

```

Source code in `starlette/responses.py`
```
49
50
51
52
53
54
```
| ```
def render(self, content: Any) -> bytes | memoryview:
    if content is None:
        return b""
    if isinstance(content, bytes | memoryview):
        return content
    return content.encode(self.charset)  # type: ignore

```

---|---
###  init_headers [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.init_headers "Permanent link")
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
###  set_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.set_cookie "Permanent link")
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
###  delete_cookie [¶](https://fastapi.tiangolo.com/reference/responses/#fastapi.responses.PlainTextResponse.delete_cookie "Permanent link")
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
