## More details about `SecurityScopes`[¶](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/#more-details-about-securityscopes)
You can use `SecurityScopes` at any point, and in multiple places, it doesn't have to be at the "root" dependency.
It will always have the security scopes declared in the current `Security` dependencies and all the dependants for **that specific** _path operation_ and **that specific** dependency tree.
Because the `SecurityScopes` will have all the scopes declared by dependants, you can use it to verify that a token has the required scopes in a central dependency function, and then declare different scope requirements in different _path operations_.
They will be checked independently for each _path operation_.
