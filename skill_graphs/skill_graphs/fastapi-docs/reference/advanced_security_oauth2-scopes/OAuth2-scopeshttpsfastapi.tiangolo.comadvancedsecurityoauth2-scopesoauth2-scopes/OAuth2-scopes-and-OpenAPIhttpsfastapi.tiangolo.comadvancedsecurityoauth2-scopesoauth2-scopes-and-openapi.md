## OAuth2 scopes and OpenAPI[¶](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/#oauth2-scopes-and-openapi)
The OAuth2 specification defines "scopes" as a list of strings separated by spaces.
The content of each of these strings can have any format, but should not contain spaces.
These scopes represent "permissions".
In OpenAPI (e.g. the API docs), you can define "security schemes".
When one of these security schemes uses OAuth2, you can also declare and use scopes.
Each "scope" is just a string (without spaces).
They are normally used to declare specific security permissions, for example:
  * `users:read` or `users:write` are common examples.
  * `instagram_basic` is used by Facebook / Instagram.
  * `https://www.googleapis.com/auth/drive` is used by Google.


Info
In OAuth2 a "scope" is just a string that declares a specific permission required.
It doesn't matter if it has other characters like `:` or if it is a URL.
Those details are implementation specific.
For OAuth2 they are just strings.
