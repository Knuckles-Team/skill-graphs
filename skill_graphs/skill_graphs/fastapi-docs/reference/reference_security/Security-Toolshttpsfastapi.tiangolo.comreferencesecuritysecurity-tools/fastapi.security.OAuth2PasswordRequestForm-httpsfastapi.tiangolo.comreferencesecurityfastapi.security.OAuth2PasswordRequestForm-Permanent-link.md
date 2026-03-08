##  fastapi.security.OAuth2PasswordRequestForm [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm "Permanent link")
```
OAuth2PasswordRequestForm(
    *,
    grant_type=None,
    username,
    password,
    scope="",
    client_id=None,
    client_secret=None
)

```

This is a dependency class to collect the `username` and `password` as form data for an OAuth2 password flow.
The OAuth2 specification dictates that for a password flow the data should be collected using form data (instead of JSON) and that it should have the specific fields `username` and `password`.
All the initialization parameters are extracted from the request.
Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm--example)
```
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()


@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestForm, Depends()]):
    data = {}
    data["scopes"] = []
    for scope in form_data.scopes:
        data["scopes"].append(scope)
    if form_data.client_id:
        data["client_id"] = form_data.client_id
    if form_data.client_secret:
        data["client_secret"] = form_data.client_secret
    return data

```

Note that for OAuth2 the scope `items:read` is a single scope in an opaque string. You could have custom internal logic to separate it by colon characters (`:`) or similar, and get the two parts `items` and `read`. Many applications do that to group and organize permissions, you could do it as well in your application, just know that that it is application specific, it's not part of the specification.
PARAMETER | DESCRIPTION
---|---
`grant_type` |  The OAuth2 spec says it is required and MUST be the fixed string "password". Nevertheless, this dependency class is permissive and allows not passing it. If you want to enforce it, use instead the `OAuth2PasswordRequestFormStrict` dependency. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str | None` **DEFAULT:** `None`
`username` |  `username` string. The OAuth2 spec requires the exact field name `username`. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str`
`password` |  `password` string. The OAuth2 spec requires the exact field name `password`. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str`
`scope` |  A single string with actually several scopes separated by spaces. Each scope is also a string. For example, a single string with: ```python "items:read items:write users:read profile openid" ```` would represent the scopes:
  * `items:read`
  * `items:write`
  * `users:read`
  * `profile`
  * `openid`

Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str` **DEFAULT:** `''`
`client_id` |  If there's a `client_id`, it can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `str | None` **DEFAULT:** `None`
`client_secret` |  If there's a `client_password` (and a `client_id`), they can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `str | None` **DEFAULT:** `None`
Source code in `fastapi/security/oauth2.py`
```
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
 83
 84
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
154
155
156
157
158
159
```
| ```
def __init__(
    self,
    *,
    grant_type: Annotated[
        str | None,
        Form(pattern="^password$"),
        Doc(
            """
            The OAuth2 spec says it is required and MUST be the fixed string
            "password". Nevertheless, this dependency class is permissive and
            allows not passing it. If you want to enforce it, use instead the
            `OAuth2PasswordRequestFormStrict` dependency.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ] = None,
    username: Annotated[
        str,
        Form(),
        Doc(
            """
            `username` string. The OAuth2 spec requires the exact field name
            `username`.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ],
    password: Annotated[
        str,
        Form(json_schema_extra={"format": "password"}),
        Doc(
            """
            `password` string. The OAuth2 spec requires the exact field name
            `password`.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ],
    scope: Annotated[
        str,
        Form(),
        Doc(
            """
            A single string with actually several scopes separated by spaces. Each
            scope is also a string.

            For example, a single string with:

        ```python
            "items:read items:write users:read profile openid"
        ````

            would represent the scopes:

            * `items:read`
            * `items:write`
            * `users:read`
            * `profile`
            * `openid`

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ] = "",
    client_id: Annotated[
        str | None,
        Form(),
        Doc(
            """
            If there's a `client_id`, it can be sent as part of the form fields.
            But the OAuth2 specification recommends sending the `client_id` and
            `client_secret` (if any) using HTTP Basic auth.
            """
        ),
    ] = None,
    client_secret: Annotated[
        str | None,
        Form(json_schema_extra={"format": "password"}),
        Doc(
            """
            If there's a `client_password` (and a `client_id`), they can be sent
            as part of the form fields. But the OAuth2 specification recommends
            sending the `client_id` and `client_secret` (if any) using HTTP Basic
            auth.
            """
        ),
    ] = None,
):
    self.grant_type = grant_type
    self.username = username
    self.password = password
    self.scopes = scope.split()
    self.client_id = client_id
    self.client_secret = client_secret

```

---|---
###  grant_type `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm.grant_type "Permanent link")
```
grant_type = grant_type

```

###  username `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm.username "Permanent link")
```
username = username

```

###  password `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm.password "Permanent link")
```
password = password

```

###  scopes `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm.scopes "Permanent link")
```
scopes = split()

```

###  client_id `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm.client_id "Permanent link")
```
client_id = client_id

```

###  client_secret `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm.client_secret "Permanent link")
```
client_secret = client_secret

```

##  fastapi.security.OAuth2PasswordRequestFormStrict [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict "Permanent link")
```
OAuth2PasswordRequestFormStrict(
    grant_type,
    username,
    password,
    scope="",
    client_id=None,
    client_secret=None,
)

```

Bases: `OAuth2PasswordRequestForm[](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestForm "<code class="doc-symbol doc-symbol-heading doc-symbol-class"></code>            <span class="doc doc-object-name doc-class-name">fastapi.security.OAuth2PasswordRequestForm</span> \(<code>fastapi.security.oauth2.OAuth2PasswordRequestForm</code>\)")`
This is a dependency class to collect the `username` and `password` as form data for an OAuth2 password flow.
The OAuth2 specification dictates that for a password flow the data should be collected using form data (instead of JSON) and that it should have the specific fields `username` and `password`.
All the initialization parameters are extracted from the request.
The only difference between `OAuth2PasswordRequestFormStrict` and `OAuth2PasswordRequestForm` is that `OAuth2PasswordRequestFormStrict` requires the client to send the form field `grant_type` with the value `"password"`, which is required in the OAuth2 specification (it seems that for no particular reason), while for `OAuth2PasswordRequestForm` `grant_type` is optional.
Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
#### Example[¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict--example)
```
from typing import Annotated

from fastapi import Depends, FastAPI
from fastapi.security import OAuth2PasswordRequestForm

app = FastAPI()


@app.post("/login")
def login(form_data: Annotated[OAuth2PasswordRequestFormStrict, Depends()]):
    data = {}
    data["scopes"] = []
    for scope in form_data.scopes:
        data["scopes"].append(scope)
    if form_data.client_id:
        data["client_id"] = form_data.client_id
    if form_data.client_secret:
        data["client_secret"] = form_data.client_secret
    return data

```

Note that for OAuth2 the scope `items:read` is a single scope in an opaque string. You could have custom internal logic to separate it by colon characters (`:`) or similar, and get the two parts `items` and `read`. Many applications do that to group and organize permissions, you could do it as well in your application, just know that that it is application specific, it's not part of the specification.
the OAuth2 spec says it is required and MUST be the fixed string "password".
This dependency is strict about it. If you want to be permissive, use instead the OAuth2PasswordRequestForm dependency class.
username: username string. The OAuth2 spec requires the exact field name "username". password: password string. The OAuth2 spec requires the exact field name "password". scope: Optional string. Several scopes (each one a string) separated by spaces. E.g. "items:read items:write users:read profile openid" client_id: optional string. OAuth2 recommends sending the client_id and client_secret (if any) using HTTP Basic auth, as: client_id:client_secret client_secret: optional string. OAuth2 recommends sending the client_id and client_secret (if any) using HTTP Basic auth, as: client_id:client_secret
PARAMETER | DESCRIPTION
---|---
`grant_type` |  The OAuth2 spec says it is required and MUST be the fixed string "password". This dependency is strict about it. If you want to be permissive, use instead the `OAuth2PasswordRequestForm` dependency class. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str`
`username` |  `username` string. The OAuth2 spec requires the exact field name `username`. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str`
`password` |  `password` string. The OAuth2 spec requires the exact field name `password`. Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str`
`scope` |  A single string with actually several scopes separated by spaces. Each scope is also a string. For example, a single string with: ```python "items:read items:write users:read profile openid" ```` would represent the scopes:
  * `items:read`
  * `items:write`
  * `users:read`
  * `profile`
  * `openid`

Read more about it in the [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/). **TYPE:** `str` **DEFAULT:** `''`
`client_id` |  If there's a `client_id`, it can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `str | None` **DEFAULT:** `None`
`client_secret` |  If there's a `client_password` (and a `client_id`), they can be sent as part of the form fields. But the OAuth2 specification recommends sending the `client_id` and `client_secret` (if any) using HTTP Basic auth. **TYPE:** `str | None` **DEFAULT:** `None`
Source code in `fastapi/security/oauth2.py`
```
226
227
228
229
230
231
232
233
234
235
236
237
238
239
240
241
242
243
244
245
246
247
248
249
250
251
252
253
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
315
316
317
318
319
320
321
322
323
324
325
326
327
```
| ```
def __init__(
    self,
    grant_type: Annotated[
        str,
        Form(pattern="^password$"),
        Doc(
            """
            The OAuth2 spec says it is required and MUST be the fixed string
            "password". This dependency is strict about it. If you want to be
            permissive, use instead the `OAuth2PasswordRequestForm` dependency
            class.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ],
    username: Annotated[
        str,
        Form(),
        Doc(
            """
            `username` string. The OAuth2 spec requires the exact field name
            `username`.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ],
    password: Annotated[
        str,
        Form(),
        Doc(
            """
            `password` string. The OAuth2 spec requires the exact field name
            `password`.

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ],
    scope: Annotated[
        str,
        Form(),
        Doc(
            """
            A single string with actually several scopes separated by spaces. Each
            scope is also a string.

            For example, a single string with:

        ```python
            "items:read items:write users:read profile openid"
        ````

            would represent the scopes:

            * `items:read`
            * `items:write`
            * `users:read`
            * `profile`
            * `openid`

            Read more about it in the
            [FastAPI docs for Simple OAuth2 with Password and Bearer](https://fastapi.tiangolo.com/tutorial/security/simple-oauth2/).
            """
        ),
    ] = "",
    client_id: Annotated[
        str | None,
        Form(),
        Doc(
            """
            If there's a `client_id`, it can be sent as part of the form fields.
            But the OAuth2 specification recommends sending the `client_id` and
            `client_secret` (if any) using HTTP Basic auth.
            """
        ),
    ] = None,
    client_secret: Annotated[
        str | None,
        Form(),
        Doc(
            """
            If there's a `client_password` (and a `client_id`), they can be sent
            as part of the form fields. But the OAuth2 specification recommends
            sending the `client_id` and `client_secret` (if any) using HTTP Basic
            auth.
            """
        ),
    ] = None,
):
    super().__init__(
        grant_type=grant_type,
        username=username,
        password=password,
        scope=scope,
        client_id=client_id,
        client_secret=client_secret,
    )

```

---|---
###  grant_type `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict.grant_type "Permanent link")
```
grant_type = grant_type

```

###  username `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict.username "Permanent link")
```
username = username

```

###  password `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict.password "Permanent link")
```
password = password

```

###  scopes `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict.scopes "Permanent link")
```
scopes = split()

```

###  client_id `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict.client_id "Permanent link")
```
client_id = client_id

```

###  client_secret `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.OAuth2PasswordRequestFormStrict.client_secret "Permanent link")
```
client_secret = client_secret

```
