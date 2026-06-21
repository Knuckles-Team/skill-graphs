## Dependency tree and scopes[¶](https://fastapi.tiangolo.com/advanced/security/oauth2-scopes/#dependency-tree-and-scopes)
Let's review again this dependency tree and the scopes.
As the `get_current_active_user` dependency has as a sub-dependency on `get_current_user`, the scope `"me"` declared at `get_current_active_user` will be included in the list of required scopes in the `security_scopes.scopes` passed to `get_current_user`.
The _path operation_ itself also declares a scope, `"items"`, so this will also be in the list of `security_scopes.scopes` passed to `get_current_user`.
Here's how the hierarchy of dependencies and scopes looks like:
  * The _path operation_ `read_own_items` has:
    * Required scopes `["items"]` with the dependency:
    * `get_current_active_user`:
      * The dependency function `get_current_active_user` has:
        * Required scopes `["me"]` with the dependency:
        * `get_current_user`:
          * The dependency function `get_current_user` has:
            * No scopes required by itself.
            * A dependency using `oauth2_scheme`.
            * A `security_scopes` parameter of type `SecurityScopes`:
              * This `security_scopes` parameter has a property `scopes` with a `list` containing all these scopes declared above, so:
                * `security_scopes.scopes` will contain `["me", "items"]` for the _path operation_ `read_own_items`.
                * `security_scopes.scopes` will contain `["me"]` for the _path operation_ `read_users_me`, because it is declared in the dependency `get_current_active_user`.
                * `security_scopes.scopes` will contain `[]` (nothing) for the _path operation_ `read_system_status`, because it didn't declare any `Security` with `scopes`, and its dependency, `get_current_user`, doesn't declare any `scopes` either.


Tip
The important and "magic" thing here is that `get_current_user` will have a different list of `scopes` to check for each _path operation_.
All depending on the `scopes` declared in each _path operation_ and each dependency in the dependency tree for that specific _path operation_.
