## About third party integrations[¶](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/#about-third-party-integrations)
In this example we are using the OAuth2 "password" flow.
This is appropriate when we are logging in to our own application, probably with our own frontend.
Because we can trust it to receive the `username` and `password`, as we control it.
But if you are building an OAuth2 application that others would connect to (i.e., if you are building an authentication provider equivalent to Facebook, Google, GitHub, etc.) you should use one of the other flows.
The most common is the implicit flow.
The most secure is the code flow, but it's more complex to implement as it requires more steps. As it is more complex, many providers end up suggesting the implicit flow.
Note
It's common that each authentication provider names their flows in a different way, to make it part of their brand.
But in the end, they are implementing the same OAuth2 standard.
**FastAPI** includes utilities for all these OAuth2 authentication flows in `fastapi.security.oauth2`.
