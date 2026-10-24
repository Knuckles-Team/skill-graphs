# OAuth2 scopes[¶](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/#oauth2-scopes)
You can use OAuth2 scopes directly with **FastAPI** , they are integrated to work seamlessly.
This would allow you to have a more fine-grained permission system, following the OAuth2 standard, integrated into your OpenAPI application (and the API docs).
OAuth2 with scopes is the mechanism used by many big authentication providers, like Facebook, Google, GitHub, Microsoft, X (Twitter), etc. They use it to provide specific permissions to users and applications.
Every time you "log in with" Facebook, Google, GitHub, Microsoft, X (Twitter), that application is using OAuth2 with scopes.
In this section you will see how to manage authentication and authorization with the same OAuth2 with scopes in your **FastAPI** application.
Warning
This is a more or less advanced section. If you are just starting, you can skip it.
You don't necessarily need OAuth2 scopes, and you can handle authentication and authorization however you want.
But OAuth2 with scopes can be nicely integrated into your API (with OpenAPI) and your API docs.
Nevertheless, you still enforce those scopes, or any other security/authorization requirement, however you need, in your code.
In many cases, OAuth2 with scopes can be an overkill.
But if you know you need it, or you are curious, keep reading.
