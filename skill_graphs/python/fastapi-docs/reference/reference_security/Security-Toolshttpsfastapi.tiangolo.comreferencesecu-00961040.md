# Security Tools[¶](https://fastapi.tiangolo.com/reference/security/#security-tools)
When you need to declare dependencies with OAuth2 scopes you use `Security()`.
But you still need to define what is the dependable, the callable that you pass as a parameter to `Depends()` or `Security()`.
There are multiple tools that you can use to create those dependables, and they get integrated into OpenAPI so they are shown in the automatic docs UI, they can be used by automatically generated clients and SDKs, etc.
You can import them from `fastapi.security`:
```
from fastapi.security import (
    APIKeyCookie,
    APIKeyHeader,
    APIKeyQuery,
    HTTPAuthorizationCredentials,
    HTTPBasic,
    HTTPBasicCredentials,
    HTTPBearer,
    HTTPDigest,
    OAuth2,
    OAuth2AuthorizationCodeBearer,
    OAuth2PasswordBearer,
    OAuth2PasswordRequestForm,
    OAuth2PasswordRequestFormStrict,
    OpenIdConnect,
    SecurityScopes,
)

```

Read more about them in the [FastAPI docs about Security](https://fastapi.tiangolo.com/tutorial/security/).
