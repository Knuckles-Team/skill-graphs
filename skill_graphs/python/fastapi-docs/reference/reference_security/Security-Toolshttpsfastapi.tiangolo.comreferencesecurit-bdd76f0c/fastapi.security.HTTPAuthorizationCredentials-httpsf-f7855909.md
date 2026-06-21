##  fastapi.security.HTTPAuthorizationCredentials [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPAuthorizationCredentials "Permanent link")
Bases: `BaseModel`
The HTTP authorization credentials in the result of using `HTTPBearer` or `HTTPDigest` in a dependency.
The HTTP authorization header value is split by the first space.
The first part is the `scheme`, the second part is the `credentials`.
For example, in an HTTP Bearer token scheme, the client will send a header like:
```
Authorization: Bearer deadbeef12346

```

In this case:
  * `scheme` will have the value `"Bearer"`
  * `credentials` will have the value `"deadbeef12346"`


###  scheme `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPAuthorizationCredentials.scheme "Permanent link")
```
scheme

```

The HTTP authorization scheme extracted from the header value.
###  credentials `instance-attribute` [¶](https://fastapi.tiangolo.com/reference/security/#fastapi.security.HTTPAuthorizationCredentials.credentials "Permanent link")
```
credentials

```

The HTTP authorization credentials extracted from the header value.
